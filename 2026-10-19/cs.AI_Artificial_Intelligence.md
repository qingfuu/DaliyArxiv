# cs.AI | Artificial Intelligence | 2026-10-19

#arxiv #ComputerScience

**论文数**: 31

### [[20_Research/Papers/机器人/Self-Building_Labs|Self-Building Labs]]

![[assets/2610.23826_figure.png|800]]

- **arXiv**: [2610.23826](https://arxiv.org/abs/2610.23826)
- **PDF**: https://arxiv.org/pdf/2610.23826
- **详细分析**: [[20_Research/Papers/机器人/Self-Building_Labs|Self-Building Labs]]
- **作者**: Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, Varinia Bernales, Alán Aspuru-Guzik
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Self-Building Labs》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, which makes laboratory flexibility the bottleneck for scaling discovery. We introduce the self-building laboratory (SBL), which designs, configures, and operates its own laboratory setup given a high-level scientific goal. SBL starts from whatever already exists, from an empty room to a working SDL, and builds the missing capabilities: the lab layout, its digital twin, robot skills, and experimental workflows. We demonstrate the system working across different robots and setups, scaling from a single workstation to laboratories with several robots working together. We validate SBL's end-to-end capabilities through a real-world quantum-dot synthesis experiment. By shifting the role of human researchers from manually configuring and programming device automation to specifying scientific objectives, SBL makes scientific automation more accessible, flexible, and scalable. Project website: https://self-building-labs.github.io/

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Large_Language_Models_A_Mental_World_Model_Framework_for_Mental_Modeling,_Simulation,_Evolution,_and_Interpretability|Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability]]

![[assets/2610.23722_first_page.png|800]]

- **arXiv**: [2610.23722](https://arxiv.org/abs/2610.23722)
- **PDF**: https://arxiv.org/pdf/2610.23722
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Large_Language_Models_A_Mental_World_Model_Framework_for_Mental_Modeling,_Simulation,_Evolution,_and_Interpretability|Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability]]
- **作者**: Qingshi Wang
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states from linguistic information, lacking unified mechanisms for subjective world construction, cognitive-psychological interactions, dynamic evolution, and historical dependencies. This paper introduces the Mental World Model (MWM) and its implementation, the Multi-Branch Mental Evolution Architecture (MMEA), which explicitly constructs subjective worlds, models interactions between cognition and mental states, and simulates continuous mental evolution shaped by historical experiences. On DynToM and RecToM, MMEA achieves 96.48% and 94.00% accuracy, respectively, outperforming leading LLMs and specialized ToM methods. Additional experiments demonstrate improvements of 28.7, 39.3, and 16.6 percentage points in mental state and behavior prediction, long-sequence prediction, and implicit mental state inference, respectively. The results demonstrate that MMEA provides an interpretable framework for continuous mental modeling, enabling AI to move beyond surface-level semantic representations to infer individuals' underlying mental states from linguistic information and dynamically simulate their internal cognitive processes and evolution over time. MWM also provides a promising foundation for causal reasoning, personalized AI, sustained human-AI interaction, and future advances toward artificial general intelligence (AGI).

</details>

---

### [[20_Research/Papers/大模型/On_the_possibilities_and_limitations_of_LLM-based_multi-agent_systems_for_multi-criteria_decision-making_in_healthcare_operations_management|On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management]]

![[assets/2610.23673_figure.png|800]]

- **arXiv**: [2610.23673](https://arxiv.org/abs/2610.23673)
- **PDF**: https://arxiv.org/pdf/2610.23673
- **详细分析**: [[20_Research/Papers/大模型/On_the_possibilities_and_limitations_of_LLM-based_multi-agent_systems_for_multi-criteria_decision-making_in_healthcare_operations_management|On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management]]
- **作者**: Marco Boresta, Tommaso Giovannelli, Sepehr Namirad, Giulia Riccardi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-criteria models for healthcare operations need weights that express how stakeholders trade off patient waiting time, provider workload, and operating cost, but these weights are difficult to quantify. Teams of large language model (LLM) agents, each prompted to represent a stakeholder, have been used to supply them. We propose a framework for assessing the reliability of LLM-generated preferences as inputs to multi-objective optimization and quantifying how their uncertainty affects decisions. We study explicit preferences by asking agents to rate the importance of the criteria in an outpatient appointment scheduling problem, and implicit preferences by inferring trade-offs from the agents' pairwise choices between emergency department configurations. The computational experiments show that the explicit preferences respond to the clinic's operating conditions and differ across roles, but deliberation among the agents can erase these differences, whereas simple averaging preserves them. The pairwise choices used to reveal the agents' implicit preferences depend largely on which option is presented first, and we find limited evidence that a statistical model using contextual information alongside presentation order predicts the agents' choices on new comparison pairs better than a model using presentation order alone. We then formulate robust weighted-sum optimization models to account for preference uncertainty. In most cases, these models select different schedules or configurations from those obtained using average preference weights. These results indicate that LLM-generated preferences need an audit of this kind before they are used as optimization weights in healthcare decision support.

</details>

---

### [[20_Research/Papers/大模型/From_Trajectories_to_Differentiated_Skills_Cognitive_Differentiation_for_Self-Improving_Agents|From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents]]

![[assets/2610.23599_figure.png|800]]

- **arXiv**: [2610.23599](https://arxiv.org/abs/2610.23599)
- **PDF**: https://arxiv.org/pdf/2610.23599
- **详细分析**: [[20_Research/Papers/大模型/From_Trajectories_to_Differentiated_Skills_Cognitive_Differentiation_for_Self-Improving_Agents|From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents]]
- **作者**: Yewei Zhao, Derong Xu, Wei Chen, Yin Xu, Peilun Zhou, Xiaohan Wang, Guojun Yin, Wei Lin, Mingjun Xiao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutomationBench, LiveMathBench, OfficeQA, SealQA, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents tackle complex tasks through reasoning and interaction with external environments. Agent skills provide persistent, transferable capabilities that guide task planning, inform contextual decisions, support tool use, and enable executable procedures. Yet existing skill-evolution methods largely organize knowledge around skill artifacts, overlooking the functional heterogeneity within individual skills and its implications for knowledge maintenance and use. Inspired by cognitive science, we propose Cognitive Differentiation in Skill Evolution (CDSE), which evolves a unified skill through four functionally distinct yet coordinated components: Meta, Experience, Tool, and Script. CDSE extracts evidence-grounded semantic gradients from successful and failed trajectories, consolidates them by functional role, and applies component-specific updates and validation with cross-component coordination and adaptive invocation. An analysis of 500 top-ranked skill packages shows that 96.8% contain knowledge spanning at least two functional roles. Across six benchmarks, three agent models, and two execution harnesses, CDSE achieves the highest scores in all 36 settings, improving over the Base agent by 7.6 percentage points and the strongest competing method in each setting by 2.6 points on average. Ablation studies further support the importance of functional differentiation and adaptive invocation.

</details>

---

### [[20_Research/Papers/大模型/Darwin-Claw_Environment-Adaptive_Experience_Consolidation_for_Recursively_Self-Evolving_Agents|Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents]]

![[assets/2610.23574_figure.png|800]]

- **arXiv**: [2610.23574](https://arxiv.org/abs/2610.23574)
- **PDF**: https://arxiv.org/pdf/2610.23574
- **详细分析**: [[20_Research/Papers/大模型/Darwin-Claw_Environment-Adaptive_Experience_Consolidation_for_Recursively_Self-Evolving_Agents|Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents]]
- **作者**: Mingze Yin, Xiaohan Wang, Dian Li, Longfei Luo, Jiahong Yan, Yiheng Zhu, Chang-Yu Hsieh
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GPQA, RSIBench, Terminal-Bench, WildClawBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Model (LLM) agents have demonstrated remarkable capabilities across complex tasks, they predominantly operate in isolated sessions, lacking the ability to continually learn from historical interactions or adapt to user-specific environments. Existing self-evolution paradigms often indiscriminately inject raw interaction trajectories into memory or skill modules, leading to obscured behavioral patterns and compromised update controllability. Furthermore, as foundational LLM reasoning improves, the bottleneck for agentic evolution shifts from accumulating generic knowledge to effectively managing situational experience. To address this, we propose Darwin-Claw, an environment-adaptive self-evolving framework that systematically distills episodic experiences to drive the comprehensive evolution of operational skills and durable memory. Theoretically grounded in an iterative agent-actor and evolver-critic co-adaptation, Darwin-Claw introduces a Hierarchical Experience Consolidation System that extracts fine-grained error attributions and generalizes them into dynamically updated prototype vectors. This structured situational experience serves as interaction patches for context-sensitive perception and explicit optimization signals for skill refinement. Practically, Darwin-Claw is a readily deployable, automated framework compatible with mainstream agent systems without requiring manual curation. Extensive experiments on WildClawBench demonstrate that Darwin-Claw yields substantial performance improvements, establishing a controllable and stable pathway for the continual, user-centric adaptation of autonomous agents in real-world ecosystems.

</details>

---

### [[20_Research/Papers/大模型/SkillBrowser_Selective_Skill_Exposure_for_Scalable_Skill-Using_Agents|SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents]]

![[assets/2610.23554_figure.png|800]]

- **arXiv**: [2610.23554](https://arxiv.org/abs/2610.23554)
- **PDF**: https://arxiv.org/pdf/2610.23554
- **详细分析**: [[20_Research/Papers/大模型/SkillBrowser_Selective_Skill_Exposure_for_Scalable_Skill-Using_Agents|SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents]]
- **作者**: Jin Ye, Yifan Jiang, Lan-zhe Guo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BigCodeBench, LogicBench, MedCalcBench, SRA-Bench, TheoremQA, ToolQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents increasingly rely on skills to extend their capabilities in complex tasks. However, scalable skill use requires Selective Skill Exposure (SSE): providing relevant procedural content when needed while avoiding unnecessary exposure that may disrupt reasoning. Existing paradigms fall short in complementary ways. Progressive disclosure exposes metadata for a growing skill library, introducing context pollution; retrieval limits catalog exposure, but static retrieval from the initial task query may be misaligned with capability needs that emerge during reasoning and may still inject unnecessary skills. We propose SkillBrowser, a Meta-Skill-managed framework that enables an agent to identify current capability needs, formulate targeted queries, and selectively load skills on demand. Across six SRA-Bench subsets and five LLMs, SkillBrowser improves aggregate accuracy over static retrieval and LLM-based selection, including multi-step tool use, and mitigates accuracy degradation on already-solvable instances. Benefits remain model- and task-dependent, with under-invocation of useful skills and additional latency as key limitations. These results demonstrate the viability of Meta-Skill-managed SSE for scalable skill repositories.

</details>

---

### [[20_Research/Papers/强化学习/Reason-guided_Human_Reward_Modeling_for_Preference-based_Reinforcement_Learning|Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning]]

![[assets/2610.23550_figure.png|800]]

- **arXiv**: [2610.23550](https://arxiv.org/abs/2610.23550)
- **PDF**: https://arxiv.org/pdf/2610.23550
- **详细分析**: [[20_Research/Papers/强化学习/Reason-guided_Human_Reward_Modeling_for_Preference-based_Reinforcement_Learning|Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning]]
- **作者**: Anshul Nayak, Shahil Shaik, Jonathan Smereka, Yue Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.1，强化学习 1.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reason-guided Human Reward Modeling for Preference-based Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) policies optimized for task rewards may produce behaviors that are efficient but misaligned with human expectations, safety preferences, or intent. This paper presents a reason-guided preference-based reinforcement learning (PbRL) framework that learns a human reward model from trajectory-level feedback. In addition to preference labels, the framework incorporates reason tags explaining why a behavior is preferred, enabling the learned reward to capture both human choices and their underlying rationale. Compared with preference-only reward learning, the reason-guided formulation provides additional supervision for learning human-aligned rewards and improves the interpretability of the resulting policy. The learned human reward is combined with the environment reward during policy optimization, allowing the agent to improve task performance while producing more interpretable, human- aligned, and preference-sensitive behavior

</details>

---

### [[20_Research/Papers/强化学习/RECREG_Recovery-based_Shielding_for_Regular_Safety_Properties_in_Reinforcement_Learning|RECREG: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning]]

![[assets/2610.23445_figure.png|800]]

- **arXiv**: [2610.23445](https://arxiv.org/abs/2610.23445)
- **PDF**: https://arxiv.org/pdf/2610.23445
- **详细分析**: [[20_Research/Papers/强化学习/RECREG_Recovery-based_Shielding_for_Regular_Safety_Properties_in_Reinforcement_Learning|RECREG: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning]]
- **作者**: Alexander W. Goodall, Francesco Belardinelli
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RECREG: Recovery-based Shielding for Regular Safety Properties in Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MASA-Safe-RL, SafetyGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In many real-world scenarios we need to consider formal requirements, such as safety and constraint compliance, to deploy Reinforcement Learning (RL) agents. In this paper we introduce RecReg, a safe RL framework capable of enforcing non-Markovian regular safety properties via recovery-based shielding. RecReg is a unified approach that supports different levels of a priori knowledge and safety guarantees. The paper primarily focuses on building the theoretical foundations for RecReg in the tabular setting, providing rigorous safety and convergence guarantees that are not present in related work. We provide an extensive set of empirical results using the MASA-Safe-RL library, and we outline an extension of RecReg to deep RL domains using SOTA model-based RL. Our empirical results demonstrate that RecReg achieves efficient learning and matches the theory in this paper.

</details>

---

### [[20_Research/Papers/具身智能/AWAM_Active_Trajectory-Conditioned_View_Imagination_for_Robust_Robot_Manipulation|AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation]]

![[assets/2610.23396_figure.png|800]]

- **arXiv**: [2610.23396](https://arxiv.org/abs/2610.23396)
- **PDF**: https://arxiv.org/pdf/2610.23396
- **详细分析**: [[20_Research/Papers/具身智能/AWAM_Active_Trajectory-Conditioned_View_Imagination_for_Robust_Robot_Manipulation|AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation]]
- **作者**: Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yanwei Fu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.8（加权：具身智能 1.5，世界模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rapid progress in embodied intelligence has enabled increasingly capable robots to follow language instructions and manipulate diverse objects. However, strong results in structured environments do not automatically transfer to open-world conditions, where clutter, occlusion, and changing viewpoints can obscure the spatial relationships required for action. To address this perceptual gap, a virtual active-perception paradigm is introduced. AWAM, an Active World-Action Model actively plans where to observe and imagines what will be seen along the planned trajectory before acting. Task-related virtual camera motion is predicted and used as a structured query into a geometry-conditioned world model, producing a reusable spatial prior for manipulation, which is later compressed into a fixed memory and fused with live observations through cross-attention for diffusion-based action prediction. AWAM achieves competitive success rates with 75.9% on LIBERO-Occ, 62.4% on LIBERO-Plus, 76.5% on RLBench-OG Occlusion1, and 94.4% in real-robot trials. These results support improved robustness to the evaluated occlusions and distribution shifts, addressing part of the gap between structured manipulation and less controlled environments.

</details>

---

### [[20_Research/Papers/大模型/Language_Models_Learn_to_Improve_Language_Models|Language Models Learn to Improve Language Models]]

![[assets/2610.23344_figure.png|800]]

- **arXiv**: [2610.23344](https://arxiv.org/abs/2610.23344)
- **PDF**: https://arxiv.org/pdf/2610.23344
- **详细分析**: [[20_Research/Papers/大模型/Language_Models_Learn_to_Improve_Language_Models|Language Models Learn to Improve Language Models]]
- **作者**: Minhua Lin, Zijun Wang, Zewen Liu, Zhaotian Weng, Bing He, Zhan Shi, Benoit Dumoulin, Xiang Zhang, Suhang Wang, Hanqing Lu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.6，世界模型 0.2）
- **关联关键词**: LLM, RL, WorldModel

#### 研究背景与动机

《Language Models Learn to Improve Language Models》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used to automate AI research, including language-model (LM) development, offering a potential path toward recursive self-improvement. However, turning experimental feedback into a learned ability to propose effective improvements across models faces two challenges. First, training such an ability with real feedback is expensive: reinforcement learning (RL) requires evaluating tens of thousands of proposals, each potentially requiring a full model-training run. Even at ten GPU-hours per run, reward collection alone would consume hundreds of thousands of GPU-hours, motivating a cheaper surrogate. Second, surrogate feedback can become unreliable as policy optimization favors overestimated proposals when the proposal distribution shifts. To address these challenges, we propose LM2LM, which trains LLMs with RL to generate effective LM improvement proposals. To provide scalable feedback, we use a research world model (RWM), a frozen LLM that predicts proposal gains from real experimental records provided in context, as the reward model for RL. To maintain feedback reliability, we periodically execute current-policy proposals ranked highly by the RWM and add their measured outcomes to its context. Across eight autoregressive and diffusion LM development environments, real-execution evaluations on held-out tasks show that LM2LM enables Qwen3.8-27B to outperform GPT-6-sol, even when GPT-6-sol is given 300 real experimental records in context, while requiring 33% lower data-generation cost. LM2LM also generalizes to a model family unseen during training.

</details>

---

### [[20_Research/Papers/大模型/Robust_Function_Calling_for_LLM_Agents_Under_Interface_Drift|Robust Function Calling for LLM Agents Under Interface Drift]]

![[assets/2610.23342_first_page.png|800]]

- **arXiv**: [2610.23342](https://arxiv.org/abs/2610.23342)
- **PDF**: https://arxiv.org/pdf/2610.23342
- **详细分析**: [[20_Research/Papers/大模型/Robust_Function_Calling_for_LLM_Agents_Under_Interface_Drift|Robust Function Calling for LLM Agents Under Interface Drift]]
- **作者**: Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Robust Function Calling for LLM Agents Under Interface Drift》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Candidate-Set, ComplexFuncBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-augmented language-model agents rely on interface text: tool descriptions, argument schemas, and the candidate tool list shown at inference time. These interfaces often change after deployment even when the underlying tool semantics remain fixed, creating a practical reliability problem for function-calling systems. We study this failure mode as interface drift and evaluate whether a lightweight, training-free repair layer can recover robustness without retraining the base model. Our method, SchemaShield-Lite, combines schema validation, candidate-set retry for missing tool names, and one-shot constrained repair. On Qwen3.5-9B, it raises DICE-300 accuracy from 0.717 to 0.813 and BFCL-200 accuracy from 0.580 to 0.805, recovering 19/22 and 33/45 drift-induced failures with no observed repair harms. Naive retry does not explain the gains. Ablations show that candidate-set drift, especially distractor tools, accounts for most observed damage, while description and schema edits alone are less harmful. The results position validation-and-repair as a practical robustness layer for deployed LLM-agent tool use.

</details>

---

### [[20_Research/Papers/大模型/AgentOnto_Ontology-Guided_LLM_Agents_for_Enterprise_Data_Analytics|AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics]]

![[assets/2610.23317_figure.png|800]]

- **arXiv**: [2610.23317](https://arxiv.org/abs/2610.23317)
- **PDF**: https://arxiv.org/pdf/2610.23317
- **详细分析**: [[20_Research/Papers/大模型/AgentOnto_Ontology-Guided_LLM_Agents_for_Enterprise_Data_Analytics|AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics]]
- **作者**: Dayan Pan, Bincheng Zuo, Xiaojian Wang, Daogang Zhang, Jingyuan Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AgentOnto: Ontology-Guided LLM Agents for Enterprise Data Analytics》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise data analysis requires agents to connect analytical requests with knowledge distributed across databases, business documents, and existing example tasks. Without an explicit representation of this knowledge, an agent may produce incorrect analytical results and cannot reliably incorporate feedback. We present AgentOnto, an ontology-guided LLM agent for enterprise data analytics. AgentOnto organizes heterogeneous enterprise knowledge into an ontology that directly guides analysis and incorporates confirmed feedback. Iterative Ontology Preparation further improves the ontology through self-generated analysis tasks. We evaluate AgentOnto on two public data sources. AgentOnto substantially outperforms representative methods, while module-level evaluations confirm the effectiveness of ontology construction, analysis, and updating. A real-world deployment further demonstrates its practical value in enterprise analytics. These results demonstrate that explicitly constructing, using, and updating enterprise knowledge supports reliable and adaptable data analysis.

</details>

---

### [[20_Research/Papers/大模型/MobileInject_Evaluating_Reasoning-to-Action_Security_of_MLLM-Based_Mobile_Agents_under_Cross-Modal_Consistency_Injection|MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection]]

![[assets/2610.23307_figure.png|800]]

- **arXiv**: [2610.23307](https://arxiv.org/abs/2610.23307)
- **PDF**: https://arxiv.org/pdf/2610.23307
- **详细分析**: [[20_Research/Papers/大模型/MobileInject_Evaluating_Reasoning-to-Action_Security_of_MLLM-Based_Mobile_Agents_under_Cross-Modal_Consistency_Injection|MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection]]
- **作者**: Songping Wang, Peiyang Li, Yi Huang, Fengting Li, Xuhao Ran, Yueming Lyu, Chao Feng, Caifeng Shan
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, AndroidWorld, DigiRL, GhostEI-Bench, MobileSafetyBench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language model (MLLM)-based mobile agents are rapidly evolving from conversational assistants into autonomous systems that perceive, reason over, and act on smartphone environments. This capability also exposes a new security risk: adversaries can embed malicious objectives in cross-application mobile content and steer agent behavior through indirect multimodal injection. Although prompt injection has been studied in desktop and web settings, its cross-modal properties in mobile ecosystems remain poorly understood, and existing security analyses are still limited. To close this gap, we introduce MobileInject, the first benchmark for evaluating mobile agents against multimodal injection attacks and reasoning-to-action security risks. MobileInject provides a high-fidelity interactive mobile evaluation framework covering 11 scenarios, 9 security-risk categories, and 108 executable risk instances. It further introduces Cross-Modal Consistency Injection to exploit corroboration across modalities, two enhanced attack methods, Multi-Role Collaborative Deception and Reasoning-Camouflage Injection, to intensify trust manipulation and reasoning hijacking, and a Reasoning Security Diagnosis Framework for fine-grained failure analysis. Systematic experiments show that mobile agents are broadly vulnerable to multimodal injection, and that many failures stem from reasoning hijacking at early stages. These findings establish MobileInject as a systematic cross-modal benchmark for studying and improving the security of mobile agents. Code release details are provided in the Appendix Open Science section.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Marginal_Influence_Interaction-Aware_Memory_Selection_for_LLM_Agents|Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents]]

![[assets/2610.23266_figure.png|800]]

- **arXiv**: [2610.23266](https://arxiv.org/abs/2610.23266)
- **PDF**: https://arxiv.org/pdf/2610.23266
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Marginal_Influence_Interaction-Aware_Memory_Selection_for_LLM_Agents|Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents]]
- **作者**: BHVSP Subrahmanyam, Neeraj Choudhary
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Beyond Marginal Influence: Interaction-Aware Memory Selection for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：JointCoreBench, LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-agent memory selection often uses retrieval rankings based on record relevance or individual influence. Such rankings cannot identify sufficient subsets under redundant or jointly necessary evidence. We study per-decision memory sufficiency: selecting a small subset that preserves full-memory behavior. To separate search error from model error, we introduce JointCoreBench, a benchmark with nine interaction families, six workflow domains, natural-language decisions, and exact sufficient-set oracles, and JointCore, a relevance cost-ordered group-deletion baseline that tests blocks before individual records. On 6,912 exact conditions, cost-ordered JointCore recovers a minimum-cost sufficient set in 100.0% of cases, reduces subset evaluations from 30.00 to 11.13 (62.9%), and achieves 87.8% active-memory savings. Across four 12B-70B model families and 432 tasks per model, its unweighted mean is 10.28 versus 16.00 model queries and 50.6% versus 43.1% minimum-cost recovery relative to cost aware singleton deletion. Both methods preserve full-memory behavior under the deterministic primary interface. Tests with physical deletion, UNKNOWN masks, PENDING sentinels, counterfactual values, and alternative labels identify interface dependent behavior. JointCore is an efficient benchmark baseline; the study does not establish deployment-ready memory compression.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Reward_Scoring_Online_Multi-Agent_Preference_Learning_for_Multimodal_Response_Generation|Beyond Reward Scoring: Online Multi-Agent Preference Learning for Multimodal Response Generation]]

![[assets/2610.23256_figure.png|800]]

- **arXiv**: [2610.23256](https://arxiv.org/abs/2610.23256)
- **PDF**: https://arxiv.org/pdf/2610.23256
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Reward_Scoring_Online_Multi-Agent_Preference_Learning_for_Multimodal_Response_Generation|Beyond Reward Scoring: Online Multi-Agent Preference Learning for Multimodal Response Generation]]
- **作者**: Ziyun Zou, Jiwoo Hong, Yifan Lu, Shao Tang, Weiyi Wu, Aman Gupta, Jin Tian, Imran Razzak
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.3（加权：大模型 0.9，强化学习 0.4）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Beyond Reward Scoring: Online Multi-Agent Preference Learning for Multimodal Response Generation》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MAPoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal preference alignment often follows a score-based RLHF pipeline: a reward model is first trained to learn human preferences, then used to score on-policy responses and optimize the response model's generation. This turns preference supervision into a scalar signal for generation: a model may learn to produce answers with higher preference scores, but is rarely trained explicitly to learn the reasons underlying human preferences. We therefore ask whether making preference understanding an internal capability of the response model can improve its generation. To investigate this question, we propose \textbf{PrefMind}, an online dual-agent reinforcement learning framework with two trainable agents: a response Generator and a preference Critic. Given a pair of candidate responses, the agents analyze and discuss which response better aligns with human preference. Human labels supervise their judgments and corrections. For pairs on which both the Generator and revised Critic correctly identify the human-preferred response, the Generator produces an improved answer, and the Critic compares it against the original preferred response to provide a generation reward. Both agents are jointly updated from interactions sampled with their current policies. Through this process, \textbf{PrefMind} trains the Generator to understand human preferences via explicit judgment and correction, and to translate this understanding into better responses. Experiments across three model scales show improvements in both standalone preference judgment and downstream response generation.

</details>

---

### [[20_Research/Papers/强化学习/Tree-Aware_Posterior_Distillation_for_Long-Horizon_Agentic_Reinforcement_Learning|Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning]]

![[assets/2610.23181_figure.png|800]]

- **arXiv**: [2610.23181](https://arxiv.org/abs/2610.23181)
- **PDF**: https://arxiv.org/pdf/2610.23181
- **详细分析**: [[20_Research/Papers/强化学习/Tree-Aware_Posterior_Distillation_for_Long-Horizon_Agentic_Reinforcement_Learning|Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning]]
- **作者**: Heming Zou, Qi Wang, Yixiu Mao, Yun Qu, Yuyi Guo, Zeyuan Liu, Chenglin Li, Weijie Liu, Saiyong Yang, Xiangyang Ji
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Tree-Aware Posterior Distillation for Long-Horizon Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards has become a scalable post-training paradigm for large language models. However, training agents over long-horizon interactions presents two challenges: using only terminal rewards makes turn-level credit assignment sparse and high-variance, while sequential mini-batch updates on a fixed rollout batch introduce policy staleness as the current policy drifts from the behavior policy. Existing approaches obtain denser credit via learned critics, process reward models, or on-policy distillation, but they rely on a value network, step-level annotations, or a stronger external teacher that increase training complexity. Meanwhile, importance sampling and clipping mitigate policy drift, but they do not specify a finite target that stops sequential updates from overshooting. In this work, we introduce TreeOPSD, a critic-free, tree-aware posterior self-distillation framework for long-horizon agentic reinforcement learning. Treating each interaction turn as a tree node, TreeOPSD branches alternative continuations from shared prefixes and recursively backs up terminal rewards into implicit turn-level credit. It then maps each credit to a closed-form, bounded teacher distribution parameterized by the likelihood ratio relative to the frozen behavior policy. Minimizing the divergence between this teacher and the student policy recovers the policy-gradient direction as the tangent at the behavior policy while bounding updates toward a finite target across sequential mini-batches. Empirically, TreeOPSD improves agentic capabilities across several competitive benchmarks and model scales, especially for long-horizon tasks, e.g., raising the average accuracy of Qwen3-30B-A3B-Thinking-2507 by 4.97 points over GRPO on the Deep Research setting.

</details>

---

### [[20_Research/Papers/强化学习/WebCoder_Scaling_General_Frontend_Development_with_Artifact-Grounded_Agentic_Reinforcement_Learning|WebCoder: Scaling General Frontend Development with Artifact-Grounded Agentic Reinforcement Learning]]

![[assets/2610.23104_figure.png|800]]

- **arXiv**: [2610.23104](https://arxiv.org/abs/2610.23104)
- **PDF**: https://arxiv.org/pdf/2610.23104
- **详细分析**: [[20_Research/Papers/强化学习/WebCoder_Scaling_General_Frontend_Development_with_Artifact-Grounded_Agentic_Reinforcement_Learning|WebCoder: Scaling General Frontend Development with Artifact-Grounded Agentic Reinforcement Learning]]
- **作者**: Zijun Dou, Zhen Yang, Xijun Liu, Dongzhuoran Zhou, Aohan Zeng, Jie Tang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《WebCoder: Scaling General Frontend Development with Artifact-Grounded Agentic Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Webdev-Bench, Webdev-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world frontend development requires agents to compose reproduction, generation, modification, and repair over an evolving application state. Learning a general policy for this process requires translating heterogeneous execution feedback into task-aligned rewards and effective credit assignment across long sequences of interdependent actions. We introduce WebCoder, a general frontend development agent trained with artifact-grounded agentic reinforcement learning. Our key idea is to assess diverse development activities through their effects on a shared executable artifact and its satisfaction of task requirements. We build Webdev-World, an executable environment that integrates code editing, application execution, browser inspection, and on-demand skills while preserving project state across interactions. An independent verifier evaluates the final application against task requirements to provide terminal rewards, while changes in intermediate artifact progress redistribute the resulting rollout advantage across development segments. Context compaction and message-tree sample construction support training on trajectories beyond a single context window while avoiding repeated loss computation on shared generated history. We further introduce Webdev-Bench to evaluate composed development requirements within a single project. On Webdev-Bench, WebCoder-27B raises requirement satisfaction from 64.8 for its Qwen3.8-27B base model to 72.8, exceeding Claude-Opus-4.8 (65.1) and GPT-5.4 (59.6); on Vision2Web, it improves the average visual and functional score from 41.1 to 62.4, on par with Claude-Opus-4.8. Ablation studies confirm the contributions of artifact-grounded credit assignment and long-horizon training.

</details>

---

### [[20_Research/Papers/具身智能/Unifying_Embodied_Foundation_Models_via_a_Model-to-Policy_Formulation|Unifying Embodied Foundation Models via a Model-to-Policy Formulation]]

![[assets/2610.23053_first_page.png|800]]

- **arXiv**: [2610.23053](https://arxiv.org/abs/2610.23053)
- **PDF**: https://arxiv.org/pdf/2610.23053
- **详细分析**: [[20_Research/Papers/具身智能/Unifying_Embodied_Foundation_Models_via_a_Model-to-Policy_Formulation|Unifying Embodied Foundation Models via a Model-to-Policy Formulation]]
- **作者**: Xinyi Hong, Mingyang Ren
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Unifying Embodied Foundation Models via a Model-to-Policy Formulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, VQ-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models and world-action models (WAMs) have emerged as promising approaches to robot learning and control. These models integrate multimodal perception and action generation, but differ in their architectures, output representations, and learning objectives. In this paper, we present a unified, architecture-agnostic probabilistic formulation for embodied foundation models based on stochastic kernels. Our formulation has two key components: (i) we characterize embodied foundation models through conditional output distributions and action-realization kernels, which together induce task-conditioned robot policies; and (ii) we connect pretraining and post-training to policy deployment, accommodating model-specific pretraining objectives and offline or online post-training strategies. We instantiate the formulation for OpenVLA and DreamZero, covering autoregressive action-token prediction and joint video-action generation.

</details>

---

### [[20_Research/Papers/大模型/Aligning_Language_Models_Towards_Counterfactual_Invariance|Aligning Language Models Towards Counterfactual Invariance]]

![[assets/2610.22942_figure.png|800]]

- **arXiv**: [2610.22942](https://arxiv.org/abs/2610.22942)
- **PDF**: https://arxiv.org/pdf/2610.22942
- **详细分析**: [[20_Research/Papers/大模型/Aligning_Language_Models_Towards_Counterfactual_Invariance|Aligning Language Models Towards Counterfactual Invariance]]
- **作者**: Basar Demir, Emily Shen, Ksheeraj Sai Vepuri, Sourabh Kulkarni, Harihar Subramanyam, Ankit Jain, Nan Jiang, Chirag Nagpal
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.35，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Aligning Language Models Towards Counterfactual Invariance》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DiscrimEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small variations in prompt characteristics can meaningfully alter the semantics, tone, and contextual assumptions of large language model outputs. Such characteristics can involve group variables such as demographics or other sensitive latent attributes. Sensitivity to such input variables is undesirable when demographic information is causally irrelevant to the task, but might still be relevant for generation of semantically coherent responses. This makes the task of enforcing counterfactual invariance while preserving model utility difficult. To study this problem, we first show that standard model alignment recipes (such as reinforcement learning) increase differences in response quality across demographics, while improving overall response quality, ultimately amplifying what is known as counterfactual bias. To address this, we develop a policy gradient technique involving a group-level reward function that operates on matched pairs of counterfactual prompts. For completeness, we build a dataset of controlled counterfactual prompt pairs and design an evaluation that separately measures cases where demographic information is causally relevant to the answer. Finally, we validate our findings on several fairness benchmarks. We demonstrate that our methods reduce counterfactual differences while preserving overall response quality and that the models continue to adapt appropriately when such sensitive information is relevant.

</details>

---

### [[20_Research/Papers/大模型/Cooperation_Without_Adaptation_LLM_Agents_in_a_Collective-Risk_Dilemma|Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma]]

![[assets/2610.22882_figure.png|800]]

- **arXiv**: [2610.22882](https://arxiv.org/abs/2610.22882)
- **PDF**: https://arxiv.org/pdf/2610.22882
- **详细分析**: [[20_Research/Papers/大模型/Cooperation_Without_Adaptation_LLM_Agents_in_a_Collective-Risk_Dilemma|Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma]]
- **作者**: Trung-Kiet Huynh, Dao-Sy Duy-Minh, Chi-Nguyen Tran, Phu-Hoa Pham, Phu-Quy Nguyen-Lam, Le Hong Trang, The Anh Han
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Cooperation Without Adaptation: LLM Agents in a Collective-Risk Dilemma》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-model agents are increasingly deployed to act on behalf of people in settings where individual decisions shape shared outcomes. We examine whether five production models adapt their contributions to changing risks and partner behaviour, or instead follow a relatively fixed strategy. In a collective-risk dilemma game (CRG), six players contribute to a shared pool over ten rounds; if the pool falls short of its target, a catastrophe may destroy their remaining resources. Four models contributed approximately an equal share at every positive risk level, and four of the five also contributed when risk was zero, even though contributing could not improve their payoff. Explicitly stating that only the agent's own payoff mattered reduced zero-risk contributions for most models, while a more neutral prompt did not. Several models correctly identified which action offered the higher expected payoff at different risk levels, yet their contributions changed little. Against fixed partners, no model consistently chose the payoff-maximising response, and in mixed-model groups, a single agent's shortfall in the final round could cause an otherwise successful group to fail. Payoff-based selection also depended on population composition: in a single six-agent group, it favoured the model that contributed least and reduced group success, whereas in larger, randomly mixed populations, it favoured an exact fair-share model at moderate and high risk. These findings show that cooperative self-play alone is not evidence of strategic adaptability. Consistent with a machine-behaviour approach, evaluations of agents in multi-agent systems should test how they respond to incentives, partner actions, and population composition.

</details>

---

### [[20_Research/Papers/强化学习/Sample-Efficient_Reinforcement_Learning_for_Policy_Improvement_via_Flow-Reversed_Action_Anchors|Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors]]

![[assets/2610.22852_figure.png|800]]

- **arXiv**: [2610.22852](https://arxiv.org/abs/2610.22852)
- **PDF**: https://arxiv.org/pdf/2610.22852
- **详细分析**: [[20_Research/Papers/强化学习/Sample-Efficient_Reinforcement_Learning_for_Policy_Improvement_via_Flow-Reversed_Action_Anchors|Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors]]
- **作者**: Carl Qi, Weijun Dong, Xiaojie Wang, Peiyi Chen, Rahul Sajnani, Mingyuan Zhang, Amy Zhang, Jose Barreiros, Manikatan Nambi, Lillian J. Ratliff, Dylan Randle
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Sample-Efficient Reinforcement Learning for Policy Improvement via Flow-Reversed Action Anchors》归入 强化学习、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies offer strong behavioral priors, but achieving deployment-level reliability and throughput remains difficult. Reinforcement learning (RL) can improve these policies, yet its effectiveness is constrained by the cost of online interaction. Existing methods adapt frozen flow-matching policies by treating noise space as a continuous action space. We show that this behaviorally unstructured space makes exploration inefficient, often preventing these methods from extracting meaningful learning signals on challenging tasks. We introduce AnchorQ, which enables coarse-to-fine policy improvement through a structured, refinable latent action representation. At each decision step, AnchorQ uses flow reversal to map reference behaviors to state-conditioned latent anchors, samples local particles around those anchors, and applies value-guided sampling to explore promising refinements. Our analysis shows that anchors reduce identification complexity at the cost of support bias; particle refinement trades this bias against action-class complexity; and critic accuracy determines the reliability of KL-regularized, value-guided selection. Across simulated and real-world manipulation tasks, AnchorQ outperforms state-of-the-art post-training baselines in sample efficiency, delivering a 37% improvement in real-world success rate and 97% higher simulated task throughput under the same interaction budget. Additional visualizations are available on our website https://anchorq-rl.com/.

</details>

---

### [[20_Research/Papers/大模型/Self-Evolving_Coding_Agents_via_Harness-Policy_Optimization|Self-Evolving Coding Agents via Harness-Policy Optimization]]

![[assets/2610.22791_figure.png|800]]

- **arXiv**: [2610.22791](https://arxiv.org/abs/2610.22791)
- **PDF**: https://arxiv.org/pdf/2610.22791
- **详细分析**: [[20_Research/Papers/大模型/Self-Evolving_Coding_Agents_via_Harness-Policy_Optimization|Self-Evolving Coding Agents via Harness-Policy Optimization]]
- **作者**: Zhepei Wei, Wenlin Yao, Baolin Peng, Danqing Wang, Qianhui Wu, Hao Cheng, Yu Meng, Jianfeng Gao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.95（加权：大模型 0.95，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Self-Evolving Coding Agents via Harness-Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have shown promising potential in coding tasks, and their performance is jointly determined by the policy model and the harness that mediates their interaction with the environment. Indeed, harness and policy are mutually reinforcing and evolving only one component is suboptimal---a harness tuned for one checkpoint may not target the failure modes of an updated policy, while policy learning remains limited to the trajectories elicited by a fixed harness. In light of this, we propose Self-HPO, a recursive self-improving framework for coding agents that alternates harness and policy optimization, using the evolving policy as its own harness proposer. Specifically, in each round, the current policy first analyzes its own failures and proposes new harness candidates (H-step). The policy is then updated through reinforcement learning (RL) under the selected harness (P-step), and hard tasks identified during training form the next harness search set, keeping harness optimization targeted to the policy's evolving failure modes. Across three coding benchmarks, Self-HPO consistently outperforms harness-only and policy-only baselines, improving Qwen3.5-35B-A3B's average resolve rate from 57.8% to 64.8%, with gains generalizing to out-of-distribution settings. Further analysis shows that both optimized components retain gains even when paired with their base counterparts, while their joint gain exceeds the sum of their individual gains. Self-HPO also improves reliability (Pass@1) and expands the capability frontier (Pass@k) over the base agent. Additionally, we show that with a stronger external model (e.g., Opus 4.8) as the harness proposer, the same framework yields a further performance boost.

</details>

---

### [[20_Research/Papers/大模型/GlobeBench_Evaluating_Text-Based_World_Model_Capabilities_for_Scalable_Environment_Simulations|GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations]]

![[assets/2610.22708_first_page.png|800]]

- **arXiv**: [2610.22708](https://arxiv.org/abs/2610.22708)
- **PDF**: https://arxiv.org/pdf/2610.22708
- **详细分析**: [[20_Research/Papers/大模型/GlobeBench_Evaluating_Text-Based_World_Model_Capabilities_for_Scalable_Environment_Simulations|GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations]]
- **作者**: Nicholas Saban, Charvi Bannur, Mariya Vasileva, Darshan Deshpande
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.35（加权：大模型 0.35，世界模型 1）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GlobeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-based world models have recently shown potential to simulate complex RL environment state transitions for a diverse set of use cases. However, no standardized benchmark exists to compare, study and improve these models. Through this paper, we attempt to solve this problem by building GlobeBench, a novel benchmark with 1,632 tasks across five separate domains and nineteen simulation skills. The tasks check whether models can predict the environment's response to a specific action given the full agent trajectory by understanding earlier state changes, following environment rules, and predicting the effects of actions on both related and unrelated objects. We compare the predicted environment response with an execution-derived reference, using a hybrid architecture with both deterministic gates and a semantic judge. Among 20 general-purpose LLMs and specialized text world models, GPT-6 Astra achieves the highest task success rate at 49.57%. We find that model accuracy decreases as actions affect a larger portion of the environment. Specifically, when the agent's changes must propagate to dependent objects, task success drops to an average of 5.1% across all 20 models. Although model strengths differ across tasks, 631 tasks remain unsolved by any model, suggesting a significant gap in general LLM capabilities as a world model.

</details>

---

### [[20_Research/Papers/大模型/AlphaBet_Reinforcement_Learning_for_LLM_Event_Forecasting_Agents|AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents]]

![[assets/2610.22684_first_page.png|800]]

- **arXiv**: [2610.22684](https://arxiv.org/abs/2610.22684)
- **PDF**: https://arxiv.org/pdf/2610.22684
- **详细分析**: [[20_Research/Papers/大模型/AlphaBet_Reinforcement_Learning_for_LLM_Event_Forecasting_Agents|AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents]]
- **作者**: Liqin Ye, Rongzhi Zhang, Xin Liu, Zheng Li, Yuan He, Qingyu Yin, Priyanka Nigam, Chao Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.22（加权：大模型 0.9，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AlphaBet: Reinforcement Learning for LLM Event Forecasting Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forecasting an unresolved event requires finding relevant evidence and deciding how strongly it supports each outcome. Yet outcome-based training of Large Language Model (LLM) forecasters often begins with preassembled evidence at a single prediction date, leaving evidence acquisition outside the learning loop. We introduce AlphaBet, an agentic reinforcement learning (RL) framework that trains a single LLM policy to search, reason, and report probabilities across multiple pre-resolution dates. Each dated forecast is scored by a proper scoring rule against the eventual outcome, allowing one resolved event to supervise decisions under different information states. We decompose forecasting regret into an evidence-acquisition gap and a probability-reporting gap, and show that Group Relative Policy Optimization (GRPO)'s standard-deviation normalization can distort the reporting target under multi-class proper scores. On GLM-4.5-Air, AlphaBet reduces the Brier score from 0.731 to 0.626 on Forecast-Dojo and from 0.612 to 0.528 on FutureX. Controlled ablations attribute these gains to multi-date training and show that they come from improvements in both information acquisition and probability reporting. Our empirical results validate that GRPO's std normalization degrades proper-scoring-rule performance while leaving top-outcome accuracy largely unchanged.

</details>

---

### [[20_Research/Papers/大模型/Testing_the_Planning_Claims_of_LLM-Based_Agents_against_Formal_Semantics|Testing the Planning Claims of LLM-Based Agents against Formal Semantics]]

![[assets/2610.22469_figure.png|800]]

- **arXiv**: [2610.22469](https://arxiv.org/abs/2610.22469)
- **PDF**: https://arxiv.org/pdf/2610.22469
- **详细分析**: [[20_Research/Papers/大模型/Testing_the_Planning_Claims_of_LLM-Based_Agents_against_Formal_Semantics|Testing the Planning Claims of LLM-Based Agents against Formal Semantics]]
- **作者**: Oriol Miro-Lopez-Feliu, Oscar Miró López-Feliu, Victor Gimenez-Abalos, Javier Vazquez-Salceda, Victor Carballo Araruna, Sergio Alvarez-Napagao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Testing the Planning Claims of LLM-Based Agents against Formal Semantics》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ACPBench, AutoPlanBench, PlanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents are increasingly credited with the competences of practical reasoning: planning, monitoring, and correcting their own actions. Their success is attributed to the prompting strategies and agent architectures built around the model, such as chain-of-thought, search-based prompting, self-refinement, reflection, critics and tool-using loops. Yet these claims are usually supported by end-to-end success rates, which show only whether a task was completed, or by LLM judges, which are not verifiers. We test LLM planning against formal semantics. Tasks are posed in natural language, but each is grounded in a hidden PDDL model that decides whether every action is applicable, whether the goal is reached, and whether a plan exists at all. Across five domains (two of them new, all released with the paper), four models, six prompting strategies and three agent architectures, the best configuration solves 78% of the solvable tasks offline but only 40% online, where agents mostly act without inspecting the state. Unsolvable tasks are recognised in under 10% of episodes, and heavier prompting strategies use 5 to 22 times as many tokens as direct prompting with no clear gain. In our experiments, planning performance varied more across models than across prompting strategies or agent architectures. Claims that agents can plan require evidence from validated action traces.

</details>

---

### [[20_Research/Papers/大模型/PRIME_Towards_Verifiable_Evidence-Grounded_Reasoning_in_LLM_Agents|PRIME: Towards Verifiable Evidence-Grounded Reasoning in LLM Agents]]

![[assets/2610.22426_first_page.png|800]]

- **arXiv**: [2610.22426](https://arxiv.org/abs/2610.22426)
- **PDF**: https://arxiv.org/pdf/2610.22426
- **详细分析**: [[20_Research/Papers/大模型/PRIME_Towards_Verifiable_Evidence-Grounded_Reasoning_in_LLM_Agents|PRIME: Towards Verifiable Evidence-Grounded Reasoning in LLM Agents]]
- **作者**: Hamed Khosravi, Xiaoming Huo
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PRIME: Towards Verifiable Evidence-Grounded Reasoning in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are used to check records against an organization's requirements, for example whether a vulnerability report is ready for investigation. Requirements often allow several ways to be met, such as a severity rating with a curator-reviewed advisory or a published advisory link. Agents fail by accepting a report after a required check has failed, or by settling for a weaker conclusion without trying another way that could still succeed. We introduce PRIME (Precommitted Rules for Inference from Minimal Evidence). Before checking, it fixes evidence routes specifying how each conclusion may be justified. A separate program records each check result and refuses any conclusion the results do not justify. It also points the agent to checks that could justify a stronger conclusion, or runs them itself. PRIME reports only conclusions authorized by its rules and ledger. With correct requirements, exact checks at known locations, and sufficient budget at stopping, completion reaches the strongest supported conclusion. On 480 public-record tasks, an agent shown the requirements reported unjustified conclusions on 26.7% of tasks, while PRIME reported none. Its directions and added checks raised the average score for justified conclusions from 30.1, with refusal alone, to the maximum of 59.2 out of 100.

</details>

---

### [[20_Research/Papers/大模型/When_is_a_large_language_model_a_good_calibration_agent_Physics-labeled_prompting_for_budgeted_engineering_simulator_calibration|When is a large language model a good calibration agent? Physics-labeled prompting for budgeted engineering simulator calibration]]

![[assets/2610.22379_figure.png|800]]

- **arXiv**: [2610.22379](https://arxiv.org/abs/2610.22379)
- **PDF**: https://arxiv.org/pdf/2610.22379
- **详细分析**: [[20_Research/Papers/大模型/When_is_a_large_language_model_a_good_calibration_agent_Physics-labeled_prompting_for_budgeted_engineering_simulator_calibration|When is a large language model a good calibration agent? Physics-labeled prompting for budgeted engineering simulator calibration]]
- **作者**: Ruo-Qian Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When is a large language model a good calibration agent? Physics-labeled prompting for budgeted engineering simulator calibration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Calibrating expensive engineering simulators requires tuning model parameters to match reference data, a process heavily constrained by computational costs. This study investigates whether Large Language Models (LLMs), conditioned on physical diagnostic descriptions of simulation errors, can propose informative parameter updates more efficiently than conventional derivative-free optimizers. We test this on a cylinder-wake Large-Eddy Simulation and a damped-oscillator inverse problem. Physics-labeled prompts are evaluated against four text ablations (removed, anonymized, padded, misdirected) and standard optimizers (Nelder-Mead, Bayesian optimization, CMA-ES, and random search). Results demonstrate a strong early semantic advantage: the first physics-informed LLM proposal improves the initial design in 23 of 25 trials. After five evaluations, the median calibration error is 21.9 times lower than physics-free controls. However, this advantage is transient - disappearing by fifteen evaluations - and inherent LLM decoder variability yields a 9.8-fold performance spread. To address this, we introduce a hybrid workflow that uses the LLM as a warm-start, passing accumulated evaluations to a conventional optimizer. This two-stage numerical continuation policy reaches target accuracy in just 9 simulator runs, outperforming the LLM alone (12 runs), Nelder-Mead (17 runs), and Bayesian optimization (&gt;60 runs). Supported by sensitivity analysis validating the test cases, this hybrid physics-labeled LLM scheme proves highly effective as a calibration agent under strict evaluation budgets.

</details>

---

### [[20_Research/Papers/大模型/Structured_Authority_Injection_Persistent_Human_Control_for_LLM_Agents_via_Typed_MCP_Overrides|Structured Authority Injection: Persistent Human Control for LLM Agents via Typed MCP Overrides]]

![[assets/2610.22373_figure.png|800]]

- **arXiv**: [2610.22373](https://arxiv.org/abs/2610.22373)
- **PDF**: https://arxiv.org/pdf/2610.22373
- **详细分析**: [[20_Research/Papers/大模型/Structured_Authority_Injection_Persistent_Human_Control_for_LLM_Agents_via_Typed_MCP_Overrides|Structured Authority Injection: Persistent Human Control for LLM Agents via Typed MCP Overrides]]
- **作者**: Ryan Tran, YueMing Zhang, Lingfeng Tao, Nan Yang, Shengjie Xu, Yu Yin, Shuai Xu, Wenlu Zhang, Hailu Xu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Structured Authority Injection: Persistent Human Control for LLM Agents via Typed MCP Overrides》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents are increasingly used as autonomous orchestrators in distributed and multi-agent systems, yet a control gap remains: no protocol-level mechanism allows human operators to inject binding directives that persist across planning cycles. Free-text overrides suffer from ambiguous interpretation due to lack of schema validation and from authority erosion as operator instructions lose influence within accumulating context. We propose Structured Authority Injection (SAI), a protocol that addresses these issues by routing operator corrections through typed, schema-validated Model Context Protocol (MCP) tool calls and maintaining a ranked authority context prepended to each LLM prompt. SAI defines three override classes (Constraint, Priority, and Strategy) with distinct persistence semantics and an explicit precedence order enforced via a directed authority channel inaccessible to the planning process. The method requires no model fine-tuning or access to model weights and applies to instruction-tuned LLMs supporting MCP tool use. Evaluation across nine LLMs and eight scenarios targeting agent failure modes shows reduced ambiguous directive interpretation and mitigated authority decay across planning iterations, with lower prompt overhead in the strongest models (up to 38% depending on model and scenario), though benefit varies substantially across models. SAI provides a general design pattern for agent systems requiring explicit and persistent human control.

</details>

---

### [[20_Research/Papers/大模型/CausalEvo_Causal_Skill_Self-Evolution_for_Health_LLM_Agents|CausalEvo: Causal Skill Self-Evolution for Health LLM Agents]]

![[assets/2610.21016_figure.png|800]]

- **arXiv**: [2610.21016](https://arxiv.org/abs/2610.21016)
- **PDF**: https://arxiv.org/pdf/2610.21016
- **详细分析**: [[20_Research/Papers/大模型/CausalEvo_Causal_Skill_Self-Evolution_for_Health_LLM_Agents|CausalEvo: Causal Skill Self-Evolution for Health LLM Agents]]
- **作者**: Yuchen Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《CausalEvo: Causal Skill Self-Evolution for Health LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MedAgentBench, MedCalc-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents for health can accumulate reusable textual skills from task feedback, such as calculation criteria, measurement time points, and formula units. Deciding which skills to retain is consequential: useful rules improve later answers, while faulty generalizations propagate errors. We propose CausalEvo, a method for causal skill self-evolution that estimates the relative effects of deliberately changed skill sets while holding the model weights, feedback cases, and rule count fixed. At each evolution step, a frozen LLM proposes candidate rules, which are pooled with the incumbent skills so that the current skill set remains a feasible choice. Paired skill replacements against shared background rules are scored on the same feedback cases; least squares converts the score differences into relative skill values, and the top-ranked rules are retained, favoring incumbents on ties. A decision-loss bound separates candidate support, approximation, and estimation errors. On six MedCalc-Bench-Verified tasks with 120 held-out cases, CausalEvo achieves 60.00% accuracy, compared with 55.83% for SkillOpt and 51.67% without skills. Across the recorded training configurations, which use different optimization budgets, it consumes 55.6% fewer training tokens than SkillOpt. Gains concentrate in particular calculations alongside regressions on others, and paired accuracy intervals include zero. CausalEvo turns task feedback into controlled decisions about skill retention and replacement. Project repository: https://github.com/txbrook/CausalEvo

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedMidtrain_Bridging_the_Gap_between_Vision-Language_Models_and_Vision-Language-Action_Models_via_Mid-training|EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training]]

![[assets/2604.20012_figure.png|800]]

- **arXiv**: [2604.20012](https://arxiv.org/abs/2604.20012)
- **PDF**: https://arxiv.org/pdf/2604.20012
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedMidtrain_Bridging_the_Gap_between_Vision-Language_Models_and_Vision-Language-Action_Models_via_Mid-training|EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training]]
- **作者**: Yiyang Du, Zhanqiu Guo, Haochen Zhang, Annabella Macaluso, Xin Ye, Liu Ren, Yonatan Bisk, Chenyan Xiong
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.15（加权：具身智能 2.4，大模型 0.25，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《EmbodiedMidtrain: Bridging the Gap between Vision-Language Models and Vision-Language-Action Models via Mid-training》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, VLM-VLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action Models (VLAs) inherit their visual and linguistic capabilities from Vision-Language Models (VLMs), yet most VLAs are built from off-the-shelf VLMs that are not adapted to the embodied domain, limiting their downstream performance. In this work, we propose EmbodiedMidtrain to bridge the gap between VLMs and VLAs. We first characterize the data distribution gap between them, showing that VLA data occupy compact regions that are largely separated from the broader VLM distribution, while the degree of alignment varies substantially both across and within VLM data sources. Then, we build a mid-training data engine that leverages a lightweight learnable proximity estimator to select the most VLA-aligned candidates from a large VLM pool, and produce EmbodiedMidtrain-1M, a VLM dataset that we further use to mid-train the VLM before downstream VLA fine-tuning. Experiments on both simulated robot manipulation benchmarks and real-world tasks show consistent VLA performance gains over off-the-shelf checkpoints across VLM backbones and VLA action heads. These gains extend to downstream tasks not used to guide data selection. Further analysis reveals that mid-training provides a stronger initialization for VLA fine-tuning, with gains emerging from the earliest steps and widening throughout training. Moreover, the data engine captures both dataset-level and sample-level alignment signals, favoring spatial reasoning over text-centric tasks while preserving the diversity of the VLM data. We will release all code, data and models for future research.

</details>

---

### [[20_Research/Papers/世界模型/Copilot4D_Learning_Unsupervised_World_Models_for_Autonomous_Driving_via_Discrete_Diffusion|Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion]]

![[assets/2311.01017_figure.png|800]]

- **arXiv**: [2311.01017](https://arxiv.org/abs/2311.01017)
- **PDF**: https://arxiv.org/pdf/2311.01017
- **详细分析**: [[20_Research/Papers/世界模型/Copilot4D_Learning_Unsupervised_World_Models_for_Autonomous_Driving_via_Discrete_Diffusion|Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion]]
- **作者**: Lunjun Zhang, Yuwen Xiong, Ze Yang, Sergio Casas, Rui Hu, Raquel Urtasun
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.1，强化学习 0.16，世界模型 0.96，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet, VoxelNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning world models can teach an agent how the world works in an unsupervised manner. Even though it can be viewed as a special case of sequence modeling, progress for scaling world models on robotic applications such as autonomous driving has been somewhat less rapid than scaling language models with Generative Pre-trained Transformers (GPT). We identify two reasons as major bottlenecks: dealing with complex and unstructured observation space, and having a scalable generative model. Consequently, we propose Copilot4D, a novel world modeling approach that first tokenizes sensor observations with VQVAE, then predicts the future via discrete diffusion. To efficiently decode and denoise tokens in parallel, we recast Masked Generative Image Transformer as discrete diffusion and enhance it with a few simple changes, resulting in notable improvement. When applied to learning world models on point cloud observations, Copilot4D reduces prior SOTA Chamfer distance by more than 65% for 1s prediction, and more than 50% for 3s prediction, across NuScenes, KITTI Odometry, and Argoverse2 datasets. Our results demonstrate that discrete diffusion on tokenized agent experience can unlock the power of GPT-like unsupervised learning for robotics.

</details>

---
