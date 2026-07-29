# cs.AI | Artificial Intelligence | 2026-07-27

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/强化学习/Explainable_Reinforcement_Learning_for_assisting_Air_Traffic_Controllers|Explainable Reinforcement Learning for assisting Air Traffic Controllers]]

![[assets/2607.22525_first_page.png|800]]

- **arXiv**: [2607.22525](https://arxiv.org/abs/2607.22525)
- **PDF**: https://arxiv.org/pdf/2607.22525
- **详细分析**: [[20_Research/Papers/强化学习/Explainable_Reinforcement_Learning_for_assisting_Air_Traffic_Controllers|Explainable Reinforcement Learning for assisting Air Traffic Controllers]]
- **作者**: Anduel Mehmeti, Gabriella Gigante, Salvatore Venticinque
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Explainable Reinforcement Learning for assisting Air Traffic Controllers》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To effectively integrate AI into high-stakes, critical environments such as healthcare, autonomous driving, and aviation--and to advance toward higher levels of automation and seamless human-AI collaboration--building trust in AI-driven solutions is essential. Trust, in turn, is closely linked to the explainability of AI systems. The rapid advancements in AI across various domains have underscored the challenges of establishing trust, raising increasing interest in AI explainability even more when applied to deep learning. In this context, the present work aims to explore the application of explainability techniques to Reinforcement Learning (RL) algorithms, specifically within the safety-critical domain of Air Traffic Control (ATC). Using a simplified ATC environment as an initial testbed, an intelligent agent is trained with a reinforcement learning algorithm to make decisions on alternative flight routes that avoid no-fly zones. As a preliminary explainability approach, a saliency map is employed, providing insights into the input features that most significantly influence the agent's decision-making process.

</details>

---

### [[20_Research/Papers/大模型/The_Regression_Tax_Decomposing_Why_Skills_Help_and_Hurt_LLM_Agents|The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents]]

![[assets/2607.22520_figure.png|800]]

- **arXiv**: [2607.22520](https://arxiv.org/abs/2607.22520)
- **PDF**: https://arxiv.org/pdf/2607.22520
- **详细分析**: [[20_Research/Papers/大模型/The_Regression_Tax_Decomposing_Why_Skills_Help_and_Hurt_LLM_Agents|The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents]]
- **作者**: Darshan Tank, Baran Nama
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OfficeQA, SEAGym, SpreadsheetBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adding procedural skills to an LLM agent is typically evaluated by average improvement in task success. However, this metric hides an important cost: skills can also make agents worse. We measure both sides by comparing agents with and without skills across nearly 6,000 runs spanning two office automation benchmarks and three model harness stacks. This allows us to distinguish two outcomes. A regression is a task solved without skills but failed after skills are added. A residual failure is a task that fails both with and without skills. We find that regressions are substantial enough that the best performing skills outperform others primarily by regressing less, not by gaining more. We identify three causes of regression: (i) skill description osmosis, a skill changes an agent's behavior simply by being present in context, even when it is never invoked; (ii) grounding displacement, a skill's prescribed procedure overrides how the agent interprets its inputs; and (iii) verification displacement, where the procedure suppresses checks the agent would otherwise perform on its outputs. Analysing persistent failures reveals the same underlying pattern. Existing skills overemphasize procedural guidance the stage least often responsible for failure while under supporting grounding and verification, the dominant sources of remaining errors. After correcting evaluation artifacts and studying traces, we find many regressions and persistent failures recoverable through better grounding and verification. Procedural skills should be evaluated by decomposing their net effect into gains and regressions, not by aggregate improvement alone. We identify three regression modes skills should avoid, and find that reliability depends more on grounding and verification than on procedural skill choice.

</details>

---

### [[20_Research/Papers/大模型/Opaque_Epistemic_Mediation_How_LLM_Deployment_Configurations_Shape_the_Validation_of_Pseudo-Science|Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation of Pseudo-Science]]

![[assets/2607.22513_first_page.png|800]]

- **arXiv**: [2607.22513](https://arxiv.org/abs/2607.22513)
- **PDF**: https://arxiv.org/pdf/2607.22513
- **详细分析**: [[20_Research/Papers/大模型/Opaque_Epistemic_Mediation_How_LLM_Deployment_Configurations_Shape_the_Validation_of_Pseudo-Science|Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation of Pseudo-Science]]
- **作者**: Davide Scarso, Hugo Noronha de Almeida, Joaquim Pina
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation of Pseudo-Science》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Commercial large language models are increasingly used as knowledge references, yet their stance on contested scientific claims is neither stable nor transparent. We tested how four major LLM families (Claude, Grok, GPT, Gemini) evaluate ethnonationalist pseudo-science derived from Frank Salter's biosocial framework across four temporal snapshots (October 2025-February 2026), via both API and web interfaces. Grok's Fast versions (which power the default user experience on X) consistently assigned credibility scores of 70-75, two to five times higher than all other models (which scored 15-40). This pattern was absent from control prompts testing basic evolutionary consensus and refuted Lamarckian claims, where all models performed comparably. Three additional findings emerged: (1) a silent patch reversed Grok's behaviour from chaotic to stably high validation overnight, without any public documentation; (2) the same Grok model identifier produced radically divergent outputs via API (75) and web (5.5) three months later; (3) refusal to rate the pseudo-scientific claim, the most defensible response observed, appeared in two model families through different interfaces (Claude Opus 4.1 categorically via web, GPT-5.1 Chat intermittently via API) and eroded in the successor version of each. These results indicate that the epistemic stance of a commercial LLM is not a stable property of the model but a contingent effect of deployment configuration: system prompts, safety layers, interface routing, and silent updates. This remains opaque to users and researchers alike. We argue this constitutes a matter of public concern requiring new forms of epistemic accountability.

</details>

---

### [[20_Research/Papers/大模型/Dynamic_Capability_Scoping_for_Enterprise_AI_Agents_A_Synthetic_Dataset_and_Three-Source_Permission_Architecture|Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture]]

![[assets/2607.22445_figure.png|800]]

- **arXiv**: [2607.22445](https://arxiv.org/abs/2607.22445)
- **PDF**: https://arxiv.org/pdf/2607.22445
- **详细分析**: [[20_Research/Papers/大模型/Dynamic_Capability_Scoping_for_Enterprise_AI_Agents_A_Synthetic_Dataset_and_Three-Source_Permission_Architecture|Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture]]
- **作者**: Halil Burak Noyan
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform. This persistent over-privilege expands the attack surface. We argue that capability scoping must follow a dynamic least-privilege principle and be treated as a prevention mechanism before a detection one. A credential that does not exist in an agent's context cannot be misused regardless of the agent's reasoning or evasion sophistication. We outline a three-source architecture instantiating this principle: role-based ceilings, a task-context classifier, and policy-derived combination prohibitions creating a layered proactive defense against LLM agent misalignment and misuse cases. The architecture supports both enforcing and observe-only deployment; the latter records agent permission requests inconsistent with task context, producing a behavioral signal usable in misalignment research. As a first step toward evaluating this architecture, we contribute a synthetic dataset of 600 enterprise task prompts grounded in a multi-department company policy, labeled with minimum required permissions across a 15-permission tool-based taxonomy that maps directly to deployable credentials or enforceable guardrails. The dataset is constructed via a two-pass pipeline that separates prompt generation from permission labeling to avoid circularity, and is validated against a 60-record/688 decisions human-reviewed sample (Cohen's $κ= 0.917$ pre-review and $κ= 0.967$ post-review). Iterating between dataset and policy reduced ceiling violations from 46 to 3, a 93% reduction. This shows that synthetic prompt generation can drive policy refinement when the two are developed together. The dataset, environment specification, and generation pipeline are released to support evaluation of dynamic scoping mechanisms.

</details>

---

### [[20_Research/Papers/机器人/Robot_Learning_to_Communicate_through_Projected_Visual_Abstractions|Robot Learning to Communicate through Projected Visual Abstractions]]

![[assets/2607.22434_figure.png|800]]

- **arXiv**: [2607.22434](https://arxiv.org/abs/2607.22434)
- **PDF**: https://arxiv.org/pdf/2607.22434
- **详细分析**: [[20_Research/Papers/机器人/Robot_Learning_to_Communicate_through_Projected_Visual_Abstractions|Robot Learning to Communicate through Projected Visual Abstractions]]
- **作者**: Danyang Yan, Boyuan Wang, Jiaxun Liu, Boyuan Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Robot Learning to Communicate through Projected Visual Abstractions》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans routinely communicate through abstractions of their bodies, including shadows, silhouettes, and reflections. Yet robots remain largely confined to expressing themselves through their physical morphology. Enabling robots to communicate through such projected visual abstractions requires reasoning not only about bodily motion but also about how that motion is transformed into an external representation perceived by an observer. Among these abstractions, shadows provide a particularly compelling example because they emerge directly from the robot's embodiment while remaining visually distinct from the body itself. Here, we present a robotic system capable of dynamic shadow expression using a 21-degree-of-freedom dexterous hand with compliant soft skin and a learned shadow self-model. The soft-skinned embodiment reduces light leakage to produce visually continuous silhouettes, while the differentiable self-model learns the mapping between hand configurations and projected shadow appearance through task-agnostic self-exploration. Given a target shadow image or video, the robot optimizes its hand configurations through gradient-based search over 1 the learned self-model and refines the solution through collision-aware simulation to obtain physically feasible motions. For dynamic shadow performance, we further introduce expressive-region objectives, temporal smoothness regularization, and keyframe-based optimization to preserve visually important motion cues while reducing optimization complexity. We demonstrate robotic shadow expression across sign-language gestures, hand-shadow puppetry, and animal motion imitation in both simulation and physical experiments. These results establish a framework for enabling robots to manipulate projected visual abstractions of themselves for communication and visual storytelling.

</details>

---

### [[20_Research/Papers/大模型/SceneActBench_Can_Agents_Act_on_the_3D_Scenes_They_See|SceneActBench: Can Agents Act on the 3D Scenes They See?]]

![[assets/2607.22393_figure.png|800]]

- **arXiv**: [2607.22393](https://arxiv.org/abs/2607.22393)
- **PDF**: https://arxiv.org/pdf/2607.22393
- **详细分析**: [[20_Research/Papers/大模型/SceneActBench_Can_Agents_Act_on_the_3D_Scenes_They_See|SceneActBench: Can Agents Act on the 3D Scenes They See?]]
- **作者**: Yifei Zhao, Xiangxin Zhou, Wenhao Yang, Jiaqi Tang, Pu Jian, Huanjin Yao, Jiarui Yao, Haowei Lin, Chunchao Guo, Zhuo Chen, Wenkai Lyu, Jianzhu Ma...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《SceneActBench: Can Agents Act on the 3D Scenes They See?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BlenderGym, EmbodiedBench, GameDevBench, ScanQA, SceneActBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language model (VLM) agents increasingly use tools to act on 3D scenes rather than only describe them. Existing 3D benchmarks score textual responses or single-object operations, leaving agent action on complete multi-object 3D scenes under evaluated. We present SceneActBench, a benchmark for visually conditioned action across five 3D tasks under a unified agent-environment loop. Given PNG images or sampled video frames and, where applicable, supplied 3D assets, an agent acts on a 3D environment. We evaluate each final output against hidden ground truth with task-specific geometric metrics. SceneActBench comprises five tasks built from 210 source instances, yielding 520 task cases including paired input conditions. Every task runs through one fixed agent loop to keep the comparison fair. Across eleven proprietary VLM configurations, Overall scores span 38.6-50.2, and none performs consistently well across tasks. We further analyse where and how failures manifest.

</details>

---

### [[20_Research/Papers/强化学习/Do_Agent_Benchmarks_Measure_Capability_Protocol_Validity_in_the_Age_of_Agentic_AI|Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI]]

![[assets/2607.22368_figure.png|800]]

- **arXiv**: [2607.22368](https://arxiv.org/abs/2607.22368)
- **PDF**: https://arxiv.org/pdf/2607.22368
- **详细分析**: [[20_Research/Papers/强化学习/Do_Agent_Benchmarks_Measure_Capability_Protocol_Validity_in_the_Age_of_Agentic_AI|Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI]]
- **作者**: Jiaqi Shao, Hanck Chen, Wei Zhang, Maxm Pan, Bing Luo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EdgeBench, LiveBench, LiveCodeBench, MLS-Bench, SEAGym, SpecBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent benchmarks increasingly evaluate repository editing, web research, terminal use, and long-horizon interaction. Their scores support capability claims only when the evaluation protocol keeps the intended capability necessary for success. Recent reward-hacking benchmarks and system reports show that agents can instead recover public solutions, read evaluation artifacts, infer generator structure, manipulate feedback, or benefit from invalid scoring paths; existing responses do not provide a common procedure for attributing these shortcuts and quantifying their effect across benchmarks. We formulate protocol validity and introduce HackDetect, a post-hoc audit that identifies an exposure, determines how the agent used it, and assesses whether the resulting score is misleading. We quantify score inflation with the Mislead gap, defined as the exploit score minus the intended score. We audit 2,385 traces across 15 agent benchmarks and find evidence of exposures and reward hacking in 67.0% of Frontier Science traces and 66.7% of AutoLab tasks. Across paired comparisons, we measure score inflation of 0.45-1.00, showing that benchmark reports should provide evidence that scores reflect the intended capability.

</details>

---

### [[20_Research/Papers/具身智能/SiPhy_Single-Image_Physical_Property_Reasoning|SiPhy: Single-Image Physical Property Reasoning]]

![[assets/2607.22355_figure.png|800]]

- **arXiv**: [2607.22355](https://arxiv.org/abs/2607.22355)
- **PDF**: https://arxiv.org/pdf/2607.22355
- **详细分析**: [[20_Research/Papers/具身智能/SiPhy_Single-Image_Physical_Property_Reasoning|SiPhy: Single-Image Physical Property Reasoning]]
- **作者**: Hoang Le, Joonwoo Kwon, Elkhan Ismayilzada, Yufei Zhang, Zijun Cui
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.7（加权：具身智能 0.6，大模型 0.1）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《SiPhy: Single-Image Physical Property Reasoning》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MVImgNet, PhysXNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inferring physical properties such as mass, stiffness, and elasticity from a single image is essential for simulation and embodied AI, yet most existing approaches rely on multi-view reconstruction or physics-based supervision. We introduce SiPhy, a unified framework for single-image physical property reasoning that aligns 3D-aware visual cues, depth with language-based material knowledge. From one RGB image, SiPhy samples pseudo-voxel points, extracts CLIP features, and grounds them to material candidates proposed by a VLM. A part-based contrastive aggregator enforces region consistency, while a heaviness-aware refinement improves thickness and volume estimation for dense objects. Across ABO-500, MVImgNet-100, and PhysXNet-100, SiPhy achieves state-of-the-art single-image performance, surpassing multi-view reconstruction methods by improving mass MnRE by up to 93% (vs. PUGS), reducing density MAE by 35.5% (vs. NeRF2Physics), and lowering Young's modulus error by 23.5%. We further validate SiPhy on real hand-object interaction datasets, demonstrating its potential as a data annotation engine for physical understanding from single-view imagery.

</details>

---

### [[20_Research/Papers/机器人/Teachy_Mini_Development_and_Preliminary_Evaluation_of_a_Knowledge-Based_Generative_Social_Robot_for_Higher_Education|Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative Social Robot for Higher Education]]

![[assets/2607.22345_figure.png|800]]

- **arXiv**: [2607.22345](https://arxiv.org/abs/2607.22345)
- **PDF**: https://arxiv.org/pdf/2607.22345
- **详细分析**: [[20_Research/Papers/机器人/Teachy_Mini_Development_and_Preliminary_Evaluation_of_a_Knowledge-Based_Generative_Social_Robot_for_Higher_Education|Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative Social Robot for Higher Education]]
- **作者**: Stephan Vonschallen, Karim Kaufmann, Dominique Oberle, Friederike Eyssel, Theresa Schmiedel
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Teachy Mini: Development and Preliminary Evaluation of a Knowledge-Based Generative Social Robot for Higher Education》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative social robots (GSRs) powered by large language models offer new possibilities for personalized tutoring in higher education, but also introduce risks related to misinformation, missing transparency, or reinforcing incorrect student responses. Prior work identified knowledge-based design (KBD) requirements that define the informational prerequisites for GSRs to manifest responsible and effective tutoring behavior in higher education. In this paper, we operationalized selected KBD requirements in the Reachy Mini robot platform through system prompting, retrieval-augmented generation, and stateful prompt orchestration. As a result, we present Teachy Mini, a GSR tutoring system that was developed using KBD. To test the system, we conducted a preliminary evaluation study. Participants (N = 24) completed a robot-guided learning session about research methodologies. They learned either with Teachy Mini or with a control version that did not follow KBD principles. Teachy Mini was perceived as significantly more aligned with responsible tutoring behavior than the control robot. Moreover, a manipulation check illustrated that Teachy Mini used personalization, slide-grounded explanations, Socratic questioning, affective support, and learner-anchored feedback more consistently than the control robot. No significant between-condition differences were found in system acceptance, intrinsic motivation, or learning effectiveness, although exploratory analyses suggested a positive effect of KBD on objective learning gains when accounting for learner preferences. Overall, the study offered an initial implementation and preliminary evaluation of KBD for GSR tutoring, indicating that KBD can shape responsible robot behavior and potentially increase learning effectiveness in robot-supported learning.

</details>

---

### [[20_Research/Papers/大模型/Towards_Trustworthy_and_Cost-Efficient_Data_Integration_From_Naïve_RAG_to_Agentic_RAG|Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG]]

![[assets/2607.22319_figure.png|800]]

- **arXiv**: [2607.22319](https://arxiv.org/abs/2607.22319)
- **PDF**: https://arxiv.org/pdf/2607.22319
- **详细分析**: [[20_Research/Papers/大模型/Towards_Trustworthy_and_Cost-Efficient_Data_Integration_From_Naïve_RAG_to_Agentic_RAG|Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG]]
- **作者**: Chuangtao Ma, Arijit Khan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. This paper envisions trustworthy, scalable, and cost-efficient integration through knowledge-grounded LLMs and agents operating within a retrieval-augmented generation (RAG) workflow. Here, trustworthiness refers to evidence-grounded, verifiable reasoning, where integration decisions are transparently supported by retrieved knowledge, robust against hallucination, and consistent across tasks. We trace the evolution from classic RAG to GraphRAG and KG-RAG (knowledge graph-based RAG), highlighting how these paradigms bridge parametric and contextual knowledge. Building on this trajectory, we explore the shift toward Agentic RAG, where autonomous multi-agent systems adaptively plan, retrieve, refine, and reason for complex integration tasks. We examine optimization strategies for cost-efficient integration, addressing computational bottlenecks in large-scale enterprise settings. Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.

</details>

---

### [[20_Research/Papers/大模型/Deconstructing_Off-Policy_Ratios_Entropy-Scaled_Trust_Regions_for_Asynchronous_Reinforcement_Learning|Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning]]

![[assets/2607.22186_figure.png|800]]

- **arXiv**: [2607.22186](https://arxiv.org/abs/2607.22186)
- **PDF**: https://arxiv.org/pdf/2607.22186
- **详细分析**: [[20_Research/Papers/大模型/Deconstructing_Off-Policy_Ratios_Entropy-Scaled_Trust_Regions_for_Asynchronous_Reinforcement_Learning|Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning]]
- **作者**: Guanqun Zhao, Zijun Xie, Binbin Zheng, Enlei Gong, Jiafeng Lu, Yehan Yang, Aoqi Hu, Zeyu Chen
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.3，强化学习 1）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

《Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Asynchronous reinforcement learning (RL) accelerates large language model (LLM) post-training by overlapping rollout generation with policy optimization, but the resulting stale, off-policy data can destabilize optimization and ultimately cause policy collapse. Existing methods typically retain or discard tokens based solely on the magnitude of their importance ratios, applying the same threshold uniformly across token positions. In this work, we reveal that the natural scale of the importance ratio varies systematically with token entropy. Under asynchronous dynamics, this entropy-ratio scaling dictates two distinct phenomena: at low entropy, the inherent train-inference discrepancy is drastically amplified into substantial sampling noise; at high entropy, in-flight weight updates naturally induce pronounced, legitimate exploratory deviations. Consequently, magnitude-only correction inadvertently admits the amplified noise while strictly masking out the essential exploration triggered by in-flight updates. To address this, we propose the Entropy-Scaled Trust Region (ESTR), which scales each token's off-policy deviation by its local entropy, requiring no auxiliary forward passes or explicit version-switch detection. Across long-horizon agentic tasks and mathematical reasoning benchmarks, ESTR consistently outperforms existing asynchronous methods and achieves the best train-inference consistency. Compared with synchronous GRPO, ESTR attains comparable accuracy while improving training speed by $2.6\times$.

</details>

---

### [[20_Research/Papers/大模型/From_Isolated_Tasks_to_Structured_Capabilities_A_Multilayer_Taxonomy_for_Large_Language_Models|From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models]]

![[assets/2607.22182_figure.png|800]]

- **arXiv**: [2607.22182](https://arxiv.org/abs/2607.22182)
- **PDF**: https://arxiv.org/pdf/2607.22182
- **详细分析**: [[20_Research/Papers/大模型/From_Isolated_Tasks_to_Structured_Capabilities_A_Multilayer_Taxonomy_for_Large_Language_Models|From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models]]
- **作者**: Shixin Fang, Jiachen Wo, Wenjuan Qin, Sihang Jiang, Yanghua Xiao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CogBench, CognitivEval, LiveCodeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) evaluation spans diverse tasks and benchmarks, yet evidence remains organized around tasks rather than the capabilities they probe. This fragmentation limits cross-study comparison, obscures capabilities tasks recruit, and makes coverage gaps difficult to identify. We introduce a multi-layer taxonomy of 14 capability domains and 91 subskills across Primitive, Constructed, and Integrative layers. Human cognitive science guides capability definition and organization, not LLM architecture. Layer assignments draw on developmental precedence and hypothesized functional support, while human-origin constructs are adapted to observable model behavior. To demonstrate operational utility, we screened 31,505 papers from ACL, AAAI, ICML, and NeurIPS between 2023 and 2025 and mapped 15,934 LLM-focused papers through multi-model annotation, consensus, and arbitration. Direct research attention concentrated on Language-Semantic Competence (3,551; 22.3%), Reasoning (3,388; 21.3%), Planning and Decision-Making (2,149; 13.5%), and Perception (1,954; 12.3%), whereas six domains appeared in fewer than 2% of papers. Within domains, the most frequent subskill had a median prevalence of 97.9% and appeared in at least 90% of papers in 10 of 14 domains. Language-Semantic Competence and Reasoning formed the highest-volume pair (n = 1,864; 11.7%; lift = 2.47), whereas Theory of Mind and Social Reasoning and Interaction showed the highest lift among pairs with at least 20 co-occurrences (n = 62; lift = 30.84). By shifting the unit of analysis from isolated tasks to structured capabilities, the taxonomy supports research organization, coverage audits, evaluation interpretation, and testable hypotheses for diagnosis, training, and transfer.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Spatiotemporal_Decision_Priors_for_Efficient_Path_Planning_under_Partial_Observability|Learning Spatiotemporal Decision Priors for Efficient Path Planning under Partial Observability]]

![[assets/2607.22166_first_page.png|800]]

- **arXiv**: [2607.22166](https://arxiv.org/abs/2607.22166)
- **PDF**: https://arxiv.org/pdf/2607.22166
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Spatiotemporal_Decision_Priors_for_Efficient_Path_Planning_under_Partial_Observability|Learning Spatiotemporal Decision Priors for Efficient Path Planning under Partial Observability]]
- **作者**: Yi Liu, Hongda Zhang, Leyao Zou, Chunlei Meng, Ziqing Zhou, Yuning Chen, Zhuo Zou, Lida Xu, Zhongxue Gan, Chun Ouyang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Learning Spatiotemporal Decision Priors for Efficient Path Planning under Partial Observability》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：STAPNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Path planning under partial observability remains challenging because an agent must make long-horizon navigation decisions from only locally bounded observations. Nevertheless, historical trajectories contain reusable experience-guided directional preferences. Classical planners, however, typically solve each instance from scratch and lack an explicit mechanism to exploit such transferable decision knowledge, often leading to redundant node expansions and locally myopic search behaviors. Motivated by this limitation, this paper proposes ImiPath, a prior-guided learning framework that distills reusable spatiotemporal decision priors from demonstration trajectories and uses them as experience-informed directional guidance to bias planners toward reliable and promising search directions under partial observability. Specifically, ImiPath first constructs a local spatiotemporal observation representation, which encodes the spatial information of the local environment and the temporal information of historical trajectories. The SpatioTemporal-Attention Policy Network (STAPNet) then transforms this representation into dicision priors. These priors are further incorporated into heterogeneous planners as directional guidance, biasing the search toward locally promising regions. Extensive experiments demonstrate that ImiPath achieves competitive path quality and improves search efficiency by reducing redundant node expansions under local observability. Additional physical experiments on a magnetic microrobot platform further validate the adaptability and practical deployment potential of the proposed framework.

</details>

---

### [[20_Research/Papers/大模型/DBA-Bench_A_Production-Fidelity_Benchmark_for_LLM-Based_Database_Operations_Agents|DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents]]

![[assets/2607.22165_figure.png|800]]

- **arXiv**: [2607.22165](https://arxiv.org/abs/2607.22165)
- **PDF**: https://arxiv.org/pdf/2607.22165
- **详细分析**: [[20_Research/Papers/大模型/DBA-Bench_A_Production-Fidelity_Benchmark_for_LLM-Based_Database_Operations_Agents|DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents]]
- **作者**: Junming Chen, Junyang Jiang, Xu Chen, Zibo Liang, Kai Zheng
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ADBench, AgentBench, DBA-Bench, OpsEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based database agents show promise, but differing task scopes, testbeds, and metrics hinder comparison. We identify four gaps between evaluation and production operations: live-environment fidelity (multi-turn read-write interaction with a running database); observation-space scale and complexity (causal diagnosis across thousands of time series, business logs, and concurrent activity); solution-space openness (multiple remediations with different operational trade-offs); and scenario complexity and coverage (faults cascading across internal mechanisms and operational domains). We present DBA-Bench, a benchmark addressing these gaps through production fidelity, outcome-first evaluation, and controlled scenario reproducibility. It uses instrumented PostgreSQL environments with active workloads, persistent state, and multi-source observations; defines success by measurable recovery or fault elimination under safety constraints; and restores snapshots with scenario-specific checks before each run. The benchmark contains 106 scenarios across seven task domains, with two public difficulty labels based on reference-path diagnostic depth and environmental complexity. We evaluate nine baseline groups, including six foundation-model systems, two GPT-5.5-backed database agents, and a Human DBA reference. Across 848 automated runs, Diagnosis, Outcome, and Safe Pass rates are 32.7%, 19.6%, and 12.4%; the best automated baseline reaches 17.9% Safe Pass versus 93.4% for the Human DBA reference. Automated Safe Pass falls from 19.6% on Easy scenarios to 7.6% on Hard scenarios, underscoring the difficulty of safe end-to-end remediation.

</details>

---

### [[20_Research/Papers/大模型/Learning_on_the_Job_Continual_Learning_from_Deployment_Feedback_for_Frozen-Weights_Agents|Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents]]

![[assets/2607.22157_first_page.png|800]]

- **arXiv**: [2607.22157](https://arxiv.org/abs/2607.22157)
- **PDF**: https://arxiv.org/pdf/2607.22157
- **详细分析**: [[20_Research/Papers/大模型/Learning_on_the_Job_Continual_Learning_from_Deployment_Feedback_for_Frozen-Weights_Agents|Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents]]
- **作者**: Valentin Tablan, Scott Taylor, Kristoffer Bernhem
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgingBench, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow. Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections. We show that this feedback is a sufficient signal for continual learning when the frozen model is paired with an external memory that distils each episode into retrievable natural-language rules. On the banking domain of $τ$-bench, against a static-RAG control retrieving over the complete policy corpus, learning from the one-bit outcome verdict lifts single-trial success to 1.6$\times$ the baseline, and learning from corrections to 2.6$\times$, converting 22 of the 84 tasks the baseline never solves. The result spans the deployment spectrum, measured on Mistral Large, an open-weights model that organisations with data sovereignty requirements can self-host, and replicated on a frontier model, Claude Sonnet 5. The accumulated memory also transfers: each model, reading the store built by the other, rises above its own no-memory baseline. The harness, protocol, and data are released.

</details>

---

### [[20_Research/Papers/大模型/Industrial_Tokenization_for_LLM-Based_Health_Intelligence_A_Federated_Architecture_for_Industrial_Evidence_Integration|Industrial Tokenization for LLM-Based Health Intelligence: A Federated Architecture for Industrial Evidence Integration]]

![[assets/2607.22153_figure.png|800]]

- **arXiv**: [2607.22153](https://arxiv.org/abs/2607.22153)
- **PDF**: https://arxiv.org/pdf/2607.22153
- **详细分析**: [[20_Research/Papers/大模型/Industrial_Tokenization_for_LLM-Based_Health_Intelligence_A_Federated_Architecture_for_Industrial_Evidence_Integration|Industrial Tokenization for LLM-Based Health Intelligence: A Federated Architecture for Industrial Evidence Integration]]
- **作者**: Deshui Li, Xiao-Ming Yuan, Zishun Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Industrial Tokenization for LLM-Based Health Intelligence: A Federated Architecture for Industrial Evidence Integration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial health management increasingly relies on heterogeneous information sources, including condition monitoring systems, supervisory control and data acquisition systems, maintenance records, inspection results, and prognostic models. Although large language models provide new opportunities for cross-source reasoning, industrial data and analytical outputs differ substantially in structure, temporal resolution, physical meaning, and reliability. Directly integrating such heterogeneous information into a monolithic model may reduce interpretability, traceability, and adaptability to equipment and data changes. This paper introduces Industrial Tokenization, a conceptual interface for transforming source-specific analytical outputs into structured and machine-interpretable units of industrial evidence, termed Industrial Tokens. Unlike numerical tokens used to encode raw time-series data, Industrial Tokens represent domain-grounded evidence together with source, temporal scope, operating context, analytical meaning, quality or confidence information, and provenance. Based on this concept, a federated industrial architecture is proposed, where heterogeneous analytical subsystems retain autonomy while exposing standardized Industrial Tokens to a central reasoning layer. As an initial implementation, this study presents an end-to-end DiagnosisToken pathway based on vibration-diagnostic outputs, rule-based event aggregation, structured textual token generation, and LLM-based interpretation. Other Industrial Tokens, including SCADA-based condition-monitoring tokens, maintenance tokens, and prognostic tokens, are reserved as future extensions. The proposed framework positions Industrial Tokenization as a semantic interface between domain-specific industrial intelligence and LLM- or agent-based reasoning, rather than another method for encoding raw industrial data.

</details>

---

### [[20_Research/Papers/具身智能/One_Hand_Watches_The_Other_Dynamic_Multi-Agent_Cooperation_for_Sample-Efficient_Bimanual_Manipulation_in_Dynamic_Environments|One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments]]

![[assets/2607.22119_figure.png|800]]

- **arXiv**: [2607.22119](https://arxiv.org/abs/2607.22119)
- **PDF**: https://arxiv.org/pdf/2607.22119
- **详细分析**: [[20_Research/Papers/具身智能/One_Hand_Watches_The_Other_Dynamic_Multi-Agent_Cooperation_for_Sample-Efficient_Bimanual_Manipulation_in_Dynamic_Environments|One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments]]
- **作者**: Jan Ole von Hartz, Abhinav Valada, Joschka Boedecker
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DynaBench, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-stream robot manipulation policies achieve unparalleled sample efficiency and generalization by modeling actions relative to environmental reference frames. However, existing approaches typically assume these frames to be strictly exogenous. This causal assumption collapses in dynamic settings, such as when a single robot arm manipulates a moving object or when two arms coordinate, where each arm effectively becomes part of the dynamic environment of the other. We propose DynaMAC, a lightweight, policy-agnostic framework that resolves this causal limitation while preserving the sample efficiency, computational speed, and flexibility of multi-stream policies, DynaMAC treats the opposite arm as a dynamic task parameter, thereby providing a unified formulation for dynamic manipulation and bimanual coordination without requiring an explicit leader-follower relationship. To rigorously evaluate these capabilities, we introduce DynaBench, a novel benchmark for robot manipulation in dynamic environments. Across both dynamic environments and bimanual manipulation tasks, DynaMAC outperforms leading probabilistic and generative baselines by over 35 percentage points while requiring 20 times fewer samples. Crucially, DynaMAC generalizes zero-shot from static demonstrations to dynamic environments, substantially simplifying data collection and establishing an elegant bridge toward human-robot collaboration.

</details>

---

### [[20_Research/Papers/大模型/MEUSLI_a_Multilingual_Projector_for_LLM-based_ASR_and_Beyond|MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond]]

![[assets/2607.22100_figure.png|800]]

- **arXiv**: [2607.22100](https://arxiv.org/abs/2607.22100)
- **PDF**: https://arxiv.org/pdf/2607.22100
- **详细分析**: [[20_Research/Papers/大模型/MEUSLI_a_Multilingual_Projector_for_LLM-based_ASR_and_Beyond|MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond]]
- **作者**: Lorenzo Concina, Seraphina Fong, Marco Matassoni, Alessio Brutti
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM

#### 研究背景与动机

《MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lightweight projectors are an established way to connect pre-trained speech encoders with large language models (LLMs), mapping acoustic features into token-level embeddings for tasks like ASR and spoken question answering. Existing systems, however, typically only support a few languages and are often limited to English. We introduce MEUSLI, the first open-science multilingual projector family that links a Whisper encoder with open-source multilingual LLMs, enabling fully open-source end-to-end ASR in 28 European languages. MEUSLI extends prior monolingual pipelines, delivering strong results across high- and low-resource languages. Using proper continual leaning techniques, MEUSLI can be easily extended to other languages not seen in training. We further demonstrate that the MEUSLI projector can be leveraged beyond ASR, enabling multilingual speech translation and topic identification with only a few hours of task specific supervision per language. Overall, MEUSLI provides a solid foundation for multilingual speech understanding tasks, supporting scalable and inclu- sive open-source SpeechLLM

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_Fine-tuning_and_Retrieval_Strategies_for_a_Multimodal_Language_Model_on_the_NRC_Reactor_Operator_Licensing_Examination|Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination]]

![[assets/2607.22067_first_page.png|800]]

- **arXiv**: [2607.22067](https://arxiv.org/abs/2607.22067)
- **PDF**: https://arxiv.org/pdf/2607.22067
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_Fine-tuning_and_Retrieval_Strategies_for_a_Multimodal_Language_Model_on_the_NRC_Reactor_Operator_Licensing_Examination|Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination]]
- **作者**: Isak Hwang, Yoon Pyo Lee
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Benchmarking Fine-tuning and Retrieval Strategies for a Multimodal Language Model on the NRC Reactor Operator Licensing Examination》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The integration of large language models (LLMs) into the nuclear power industry requires outputs grounded in domain-specific knowledge. This study evaluates a 31-billion-parameter open-weight multimodal model (Gemma 4 31B-IT) on its capacity to apply nuclear knowledge by benchmarking eight model-retrieval configurations against the U.S. Nuclear Regulatory Commission (NRC) Reactor Operator licensing examination. We evaluate 14 Generic Fundamentals Examinations (GFE) from the 2015-2021 March sittings (seven pressurized and seven boiling water reactor exams) using the standard 80% human passing criterion. The base model is compared against configurations utilizing supervised fine-tuning (SFT) on Gemini-distilled chain-of-thought (CoT) rationales, retrieval-augmented generation (RAG) with BM25 sparse retrieval over the U.S. Department of Energy Fundamentals Handbook, and retrieval-augmented fine-tuning (RAFT). Within the retrieval pipeline, we compare fixed-size sliding-window chunking against structure-aware chunking. The SFT configuration with fixed-size chunking RAG met the criterion on 8 of the 14 examinations, outperforming all alternatives, whereas no configuration without fine-tuning passed any. Aggregate accuracy reached 79.7%, with a confidence interval spanning the threshold, and 80.2% on PWR items specifically. Furthermore, two regularities emerged: the preferred chunking strategy reverses depending on the model's training state, and RAFT underperforms compared to standard SFT in matching search environments. These results demonstrate which combination of fine-tuning and search approaches achieves operator-level capabilities.

</details>

---

### [[20_Research/Papers/具身智能/Zero-Shot_Mission-Level_Evaluation_for_Aerial_MLLM_Agents|Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents]]

![[assets/2607.22014_first_page.png|800]]

- **arXiv**: [2607.22014](https://arxiv.org/abs/2607.22014)
- **PDF**: https://arxiv.org/pdf/2607.22014
- **详细分析**: [[20_Research/Papers/具身智能/Zero-Shot_Mission-Level_Evaluation_for_Aerial_MLLM_Agents|Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents]]
- **作者**: Suman Navaratnarajah, Taehyoung Kim, Jona Ruthardt, Ishaan Bhimwal, Ryousuke Yamada, Yannik Blei, Wolfram Burgard, Yuki M Asano
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 2.15（加权：具身智能 0.9，大模型 0.95，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MissionBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Models (MLLMs) are emerging as core reasoning modules for embodied agents, yet it remains unclear how well general-purpose models can solve long-horizon embodied tasks from a single high-level instruction. We introduce MissionBench, a benchmark for mission-level evaluation of MLLMs in aerial 3D environments. It comprises 120 missions across five simulated 3D environments and four task families. Agents must autonomously plan, navigate, and report outcomes using only egocentric observations and its action history, without aerial-specific fine-tuning. Across 22 open- and closed-source MLLMs, the strongest model succeeds on fewer than 35% of missions compared to 84.4% human performance, highlighting the difficulty of multi-step embodied tasks. Despite large variations between model families, we observe gains from scaling, indicating that larger general-purpose models possess stronger zero-shot embodied capabilities. Our analysis shows that mission-level competence requires coordinating multiple capabilities beyond spatial perception, including multi-step planning and adaptive reasoning. This motivates closed-loop evaluation and highlights both the promise and risk of scaling-driven improvements for embodied AI.

</details>

---

### [[20_Research/Papers/大模型/Learning_as_Reasoning_Unfolds_Progressive_Rollout_Allocation_for_Efficient_Reinforcement_Learning|Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning]]

![[assets/2607.22002_figure.png|800]]

- **arXiv**: [2607.22002](https://arxiv.org/abs/2607.22002)
- **PDF**: https://arxiv.org/pdf/2607.22002
- **详细分析**: [[20_Research/Papers/大模型/Learning_as_Reasoning_Unfolds_Progressive_Rollout_Allocation_for_Efficient_Reinforcement_Learning|Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning]]
- **作者**: Heyang Jiang, Henry Liu, Baharan Mirzasoleiman
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CodeBench, LiveCodeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations. However, GRPO relies on repeated generation of long chain-of-thought rollouts. Training time scales with the number of rollouts, a large fraction of which are uninformative. Thus, GRPO is computationally expensive and unstable. To mitigate this, existing approaches either generate a larger pool of rollouts and filter the most informative prompts, or leverage historical signals for filtering at later stages of training. These strategies offer modest performance gains, but slow down the overall process. To address this, we propose VarIance Guided Online Rollout allocation (VIGOR) which instead of allocating a fixed rollout budget per example, begins with a small number of rollouts for all examples in a batch and iteratively allocates additional rollouts to those with the highest group reward variance until a fixed total rollout budget is reached. Theoretically, we show that under RLVR, reward variance controls the gradient magnitude, and derive VIGOR's closed-form speedup ratio over GRPO, which grows with refinement rounds under Pareto-distributed reward variance. Experiments on mathematical reasoning and coding tasks show that VIGOR reaches target accuracy with up to 2.3$\times$ fewer rollouts on math, reaches GRPO's final coding full pass rate with 1.49$\times$ fewer rollouts, and improves the coding average test pass rate by 3.4 points.

</details>

---

### [[20_Research/Papers/强化学习/Teaching_LLMs_to_Self-Evolve_Cultivating_Core_Meta-Skills_with_Reinforcement_Learning|Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning]]

![[assets/2607.21971_figure.png|800]]

- **arXiv**: [2607.21971](https://arxiv.org/abs/2607.21971)
- **PDF**: https://arxiv.org/pdf/2607.21971
- **详细分析**: [[20_Research/Papers/强化学习/Teaching_LLMs_to_Self-Evolve_Cultivating_Core_Meta-Skills_with_Reinforcement_Learning|Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning]]
- **作者**: Shujin Wu, Cheng Qian, Xiusi Chen, Heng Ji
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Eurus-2-RL, PRIME-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time scaling through iterative self-evolution with environment feedback, as demonstrated by AlphaEvolve, shows remarkable performance gains. We hypothesize that the success of such evolution frameworks hinges on meta-skills, such as self-reflection with environment feedback, that enable effective multi-round refinement, yet are largely neglected by traditional post-training. To bridge this gap, we present MetaEvolve, a framework designed to develop these meta-skills via a data synthesis pipeline, evolution-aware reinforcement learning (RL), and inference-time evolutionary search. Concretely, we ground MetaEvolve in coding, where program execution provides natural, continuous reward signals beyond binary correctness. Building on these signals, we synthesize evolution trajectories as training data, each containing a current program, its fitness score (combining correctness and efficiency), and a history of prior attempts, and train the model via RL with verifiable rewards derived from test case execution. By training on large-scale code data, we aim to inspire generalizable domain-agnostic meta-skills that can transfer broadly to open-ended problems where such rich training signals are scarce. Across seven coding benchmarks, MetaEvolve outperforms the strongest baseline by 10.01% absolute on in-distribution tasks and 24.12% on out-of-distribution tasks. On open-ended algorithm optimization problems entirely outside the training domain, it further achieves a 46.9% relative improvement. These results demonstrate that explicitly cultivating self-evolution meta-skills offers a principled path toward more capable and autonomously self-evolving AI.

</details>

---

### [[20_Research/Papers/具身智能/ACME_A_Multi-Cultural,_Multi-Embodiment_Social-Navigation_Dataset|ACME: A Multi-Cultural, Multi-Embodiment Social-Navigation Dataset]]

![[assets/2607.21964_figure.png|800]]

- **arXiv**: [2607.21964](https://arxiv.org/abs/2607.21964)
- **PDF**: https://arxiv.org/pdf/2607.21964
- **详细分析**: [[20_Research/Papers/具身智能/ACME_A_Multi-Cultural,_Multi-Embodiment_Social-Navigation_Dataset|ACME: A Multi-Cultural, Multi-Embodiment Social-Navigation Dataset]]
- **作者**: Shashank Rao Marpally, Allan Wang, Atharva Ghotavadekar, Renato Alexandre Ribeiro, Nhat Le, Pilar Bachiller-Burgos, Pranav Goyal, Subham Agrawal, Yasuhiro Nitta, Howard Ziyu Han, Daeun Song, Masaki Kuribayashi...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《ACME: A Multi-Cultural, Multi-Embodiment Social-Navigation Dataset》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding how robots and humans move in shared spaces is essential for designing effective social robot navigation policies and predicting human behavior. However, existing datasets often lack the diversity needed to capture differences in culture, geography, and human-robot interaction-factors that strongly shape appropriate social behavior. To address this gap, we introduce ACME: A Cross-cultural, Multi-Embodiment dataset for social navigation. A large-scale data collection effort across 8 sites in 5 countries, using 7 robot embodiments, ACME is a large and diverse multi-modal dataset aimed at advancing social navigation research, providing 29.35 hours of onboard robot data and 43.5 hours of overhead pedestrian tracking data. Unlike prior datasets, it focuses on capturing goal-driven social navigation behavior in complex social scenarios with explicit robot-crowd interaction through robot speech. To facilitate learning navigation policies and predicting pedestrian trajectories, ACME provides 3D and 2D scene features, odometry, interaction information, and human-annotated pedestrian trajectory labels. We make ACME easy to use by providing both human-readable data for each sensor modality as well as raw binary data. Our qualitative and quantitative analyses show that our dataset captures more challenging scenarios and a broader distribution of pedestrian behavior than previous datasets.

</details>

---

### [[20_Research/Papers/世界模型/TRW_TRACE-RealWorld---An_Auditable_Consistency_Contract_for_World_Models_as_Materialized_Views|TRW: TRACE-RealWorld---An Auditable Consistency Contract for World Models as Materialized Views]]

![[assets/2607.21910_figure.png|800]]

- **arXiv**: [2607.21910](https://arxiv.org/abs/2607.21910)
- **PDF**: https://arxiv.org/pdf/2607.21910
- **详细分析**: [[20_Research/Papers/世界模型/TRW_TRACE-RealWorld---An_Auditable_Consistency_Contract_for_World_Models_as_Materialized_Views|TRW: TRACE-RealWorld---An Auditable Consistency Contract for World Models as Materialized Views]]
- **作者**: Edward Y. Chang
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.6（加权：世界模型 0.6）
- **关联关键词**: cs.AI

#### 研究背景与动机

《TRW: TRACE-RealWorld---An Auditable Consistency Contract for World Models as Materialized Views》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TRACE-RealWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

TRACE-RealWorld addresses a core data-management problem: maintaining an actionable materialized view over a continuously changing physical world when reads of the base state are priced, delayed, heterogeneous, and fallible. Its data-management contributions are a commitment-level validity abstraction for materialized predictions; consequence-conditioned adaptive view maintenance; transaction-style, dependency-scoped compensation for commitments invalidated after authorization; and append-only provenance supporting exact replay. The work builds directly on materialized-view maintenance, adaptive stream synchronization, transaction recovery, sagas, data freshness, and provenance. The end-to-end Flood-SAR evaluation treats sensing as physical data acquisition and measures freshness, verification cost, stale reads, recovery scope, restoration failure, and replayability through six pre-registered questions with held-out seeds. The contribution is therefore not a new predictive model, but a consistency, recovery, and accountability contract for deploying learned world representations as operational data systems.

</details>

---

### [[20_Research/Papers/具身智能/When_Is_a_Learned_Command_Adapter_Worth_It_Closed-Loop_Identification_and_Counterfactual_Auditing_of_Frozen_Locomotion_Policies|When Is a Learned Command Adapter Worth It? Closed-Loop Identification and Counterfactual Auditing of Frozen Locomotion Policies]]

![[assets/2607.21867_figure.png|800]]

- **arXiv**: [2607.21867](https://arxiv.org/abs/2607.21867)
- **PDF**: https://arxiv.org/pdf/2607.21867
- **详细分析**: [[20_Research/Papers/具身智能/When_Is_a_Learned_Command_Adapter_Worth_It_Closed-Loop_Identification_and_Counterfactual_Auditing_of_Frozen_Locomotion_Policies|When Is a Learned Command Adapter Worth It? Closed-Loop Identification and Counterfactual Auditing of Frozen Locomotion Policies]]
- **作者**: Zongtan Li
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《When Is a Learned Command Adapter Worth It? Closed-Loop Identification and Counterfactual Auditing of Frozen Locomotion Policies》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adding a learned adapter to a frozen, command-conditioned locomotion policy is worthwhile only if the interface exposes improvements that are both real and recoverable from deployment-time observations. We introduce an adapter necessity audit that separates global operating-point gain,same-state counterfactual headroom, deployment gain over a cross-fitted fixed action, and state-allocation gain over a frequency-matched randomized policy. Source-cluster learner refits map these quantities and constraint violations to a GO/NO-GO/ABSTAIN decision. Closed-loop command- response identification provides optional decision features. On Go2, an archived scale-prefix diagnostic finds 5.2% same-state headroom but only 0.55% recovered allocation gain. Our confirmatory audit evaluates direct, scale, heading, and yaw interventions on twenty independent clusters for each of three query distributions induced by direct control, VGCC, and MPC, using 200 full learner refits. At 1% deployment and allocation thresholds and a 5% violation tolerance, direct queries return NO-GO, while VGCC and MPC queries ABSTAIN. VGCC has the largest mean deployment gain (1.34%), but its allocation lower bound is 0.09% and its violation upper bound is 6.25%. A deployment-representative twenty-cluster H1 audit also returns NO-GO, whereas a learner-level synthetic control returns GO. The audit therefore tests whether observable signal justifies state-dependent adaptation rather than presuming that an adapter is valuable.

</details>

---

### [[20_Research/Papers/大模型/ToolGuardian_Declarative_Security_for_AI_Agent-Tool_Interactions|ToolGuardian: Declarative Security for AI Agent-Tool Interactions]]

![[assets/2607.21835_figure.png|800]]

- **arXiv**: [2607.21835](https://arxiv.org/abs/2607.21835)
- **PDF**: https://arxiv.org/pdf/2607.21835
- **详细分析**: [[20_Research/Papers/大模型/ToolGuardian_Declarative_Security_for_AI_Agent-Tool_Interactions|ToolGuardian: Declarative Security for AI Agent-Tool Interactions]]
- **作者**: Arun Ravindran, Saurabh Deochake
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ToolGuardian: Declarative Security for AI Agent-Tool Interactions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on external tools, expanding capability while creating a new security boundary: third-party tools may appear benign at the interface level while embedding unsafe behavior in implementation. Existing defenses rely on weak metadata, collapse characterization and policy judgment into a single decision, or use heuristic/LLM enforcement that lacks deterministic, auditable reasoning over task context and multi-tool composition. This paper presents ToolGuardian, a policy-driven framework for securing agent-tool interactions through pre-admission vetting and task-aware runtime authorization. ToolGuardian uses progressive characterization to convert evidence into structured facts: descriptions capture declared intent, system-call traces expose coarse behavior, mock execution reveals observed effects, and source analysis identifies latent behavior. ToolGuardian's core contribution is an Answer Set Programming (ASP)-based declarative policy layer that reasons explicitly over capabilities, effects, task context, and composition. We compare ASP against heuristic and LLM-based policy realizations using identical inputs and output contracts. We evaluate ToolGuardian on 16 MCP-style tools, including 8 malicious variants derived from real open-source tools, and 20 runtime scenarios. For vetting, ASP reaches a deny-class F1 of 0.86 and 88% accuracy using description, syscall, and observed-effect evidence. For runtime authorization, fully specified realizations classify all scenarios correctly, while ablations show that removing compositional and conformance rules substantially degrades performance.

</details>

---

### [[20_Research/Papers/强化学习/QLPO_Quadrant-weighted_Sampling_for_Length-aware_Policy_Optimization|QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization]]

![[assets/2607.21793_figure.png|800]]

- **arXiv**: [2607.21793](https://arxiv.org/abs/2607.21793)
- **PDF**: https://arxiv.org/pdf/2607.21793
- **详细分析**: [[20_Research/Papers/强化学习/QLPO_Quadrant-weighted_Sampling_for_Length-aware_Policy_Optimization|QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization]]
- **作者**: Siwei Chen, Siqi Chen, Xupeng Miao, Bin Cui
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent large reasoning models often develop long chain-of-thought responses during reinforcement learning (RL), resulting in high inference latency and deployment cost. Existing methods for response length control typically rely on explicit length penalties or additional control modules, which require careful tuning and may compromise reasoning quality. We propose Quadrant-weighted Sampling for Length-aware Policy Optimization (QLPO), a simple resampling-based variant of GRPO that introduces implicit length control without modifying the reward function. QLPO first over-generates candidate responses and then resamples the training group by preserving the empirical correct/incorrect ratio while favoring short correct responses and long incorrect responses. This reshapes the training distribution and implicitly encourages shorter model outputs. Across models ranging from 1.5B to 32B parameters, including both base models and strong reasoning models, QLPO consistently improves the accuracy-length trade-off. It reduces response length by 30% to 70% while preserving reasoning performance. These results suggest that structured resampling provides an effective and robust approach to efficient reasoning.

</details>

---

### [[20_Research/Papers/大模型/Khondo_A_Multimodal_Benchmark_for_Document_Packet_Splitting_of_Bangla_Forms|Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms]]

![[assets/2607.21780_figure.png|800]]

- **arXiv**: [2607.21780](https://arxiv.org/abs/2607.21780)
- **PDF**: https://arxiv.org/pdf/2607.21780
- **详细分析**: [[20_Research/Papers/大模型/Khondo_A_Multimodal_Benchmark_for_Document_Packet_Splitting_of_Bangla_Forms|Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms]]
- **作者**: Abu Tyeb Azad, Fahim Ahmed, Ishita Sur Apan, Ezharuddin Jubaer, Sumaiya Karim Katha, Armun Alam, Amin Ahsan Ali, Aman Chadha, Md Mofijul Islam, AKM Mahbubur Rahman
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Document packets, multiple documents concatenated into a single file, are common in government and administrative workflows, yet splitting them into their constituent documents is difficult, especially for low-resource languages. We introduce Khondo (Bangla for split/segment), the first benchmark for document packet splitting on Bangladeshi government forms. Unlike prior English and OCR-text-based datasets, Khondo is bilingual (Bangla--English) and vision-native; where models operate directly on page images. It spans five concatenation schemes, from sequential to fully shuffled, across 14 administrative domains, with ground-truth boundaries, domain types, and page order. Zero-shot evaluation of MLLMs shows they cluster pages into their source documents fairly well but struggle in restoring the original page order once shuffled. To isolate what drives this difficulty, we run two controlled analyses, varying the prompt instruction and then the packet language. Both primarily affect ordering rather than clustering: (a) explicit page-order instructions are necessary but insufficient, and (b) English packets are ordered more reliably than Bangla, making page arrangement the dominant challenge and language a secondary but consistent factor. Khondo establishes page-order reconstruction as a key open problem in vision-based, low-resource document understanding, and provides a controlled benchmark for measuring progress toward solving it. Our dataset and code is available at https://huggingface.co/datasets/Mausul/khondo

</details>

---

### [[20_Research/Papers/大模型/Co-design_of_LLM-based_preference_agents_participation_may_drive_overtrust|Co-design of LLM-based preference agents: participation may drive overtrust]]

![[assets/2607.21757_first_page.png|800]]

- **arXiv**: [2607.21757](https://arxiv.org/abs/2607.21757)
- **PDF**: https://arxiv.org/pdf/2607.21757
- **详细分析**: [[20_Research/Papers/大模型/Co-design_of_LLM-based_preference_agents_participation_may_drive_overtrust|Co-design of LLM-based preference agents: participation may drive overtrust]]
- **作者**: Michael J. Fell
- **cs 子类**: cs.AI, cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Co-design of LLM-based preference agents: participation may drive overtrust》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly used to simulate human preferences in research and practical applications, raising concerns about validation, misrepresentation, and exclusion. Co-designing agents with the people they represent is a promising way to address these concerns, but participation may also mask the problems it appears to solve. This paper explores that tension through a primarily qualitative study in which 12 participants co-designed personal preference agents in the domain of household energy, via a background survey, co-design interview, and validation survey. Participants engaged readily and mostly came to see their agents as representing them well. Independent validation, however, revealed mixed human-agent alignment, with agent responses markedly more homogeneous, decisive, and abstract than the human sample. I argue that participation and process transparency can act as an "overtrust engine" that promotes trust while concealing systematic misalignment with potential structural consequences at scale. I develop this as a core mechanism in participatory preference agent design, treating individual alignment not as a fixed state but as an enacted process.

</details>

---

### [[20_Research/Papers/大模型/Persistent_Computational_State_A_Session-Centric_Runtime_for_Generative_World_Models|Persistent Computational State: A Session-Centric Runtime for Generative World Models]]

![[assets/2607.21686_figure.png|800]]

- **arXiv**: [2607.21686](https://arxiv.org/abs/2607.21686)
- **PDF**: https://arxiv.org/pdf/2607.21686
- **详细分析**: [[20_Research/Papers/大模型/Persistent_Computational_State_A_Session-Centric_Runtime_for_Generative_World_Models|Persistent Computational State: A Session-Centric Runtime for Generative World Models]]
- **作者**: Zhen Lin
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Persistent Computational State: A Session-Centric Runtime for Generative World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MBench, WRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative world models are increasingly driven as simulators: a planner forks a state, rolls out futures, backtracks, and returns to a visited viewpoint. Recent benchmarks establish that current video world models fail this usage, and attribute it to the model, prescribing new architectures and training objectives. We show this attribution is incomplete, and for an important class of models simply wrong. Snapshotting the state the runtime already holds -- an observation plus RNG state, a memory bank, or a windowed KV context, by architecture -- and restoring it after a genuine excursion reproduces the never-left continuation byte-identically on all three; corrupting only the RNG degrades it. The capability was never missing: request-centric serving discarded it, inheriting from language-model serving the assumption that runtime state is recomputable -- but world-model state carries a non-recomputable kernel. We define Persistent Computational State (PCS), the minimal non-recomputable state that must survive across requests, show it can be discovered by measurement, and build a session-centric runtime over it. Checkpoint and restore cost 0.012 ms against a 1.85 s generation step; resident sessions become host- rather than device-bounded (measured to 1,024); and world memory must be evicted by relevance to the return, not recency -- the inverse of LLM practice.

</details>

---

### [[20_Research/Papers/大模型/Ordered_Action_Tokens_for_Visuomotor_Policy_Learning|Ordered Action Tokens for Visuomotor Policy Learning]]

![[assets/2607.21670_first_page.png|800]]

- **arXiv**: [2607.21670](https://arxiv.org/abs/2607.21670)
- **PDF**: https://arxiv.org/pdf/2607.21670
- **详细分析**: [[20_Research/Papers/大模型/Ordered_Action_Tokens_for_Visuomotor_Policy_Learning|Ordered Action Tokens for Visuomotor Policy Learning]]
- **作者**: Chaoqi Liu, Yue Zhao, Haonan Chen, Xiaoshen Han, Jiawei Gao, Ehsan Adeli, Yilun Du
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Ordered Action Tokens for Visuomotor Policy Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action tokenization maps continuous robot action chunks to discrete tokens and has become an important interface for modern visuomotor policies. Existing approaches either rely on analytical discretization methods that produce prohibitively long token sequences or learned latent tokenizers that lack structure, limiting their compatibility with downstream policies. In this work, we identify three desiderata for action tokenization - high compression, total decodability, and an ordered token space - and introduce Ordered Action Tokenization (OAT), a learned action tokenizer that satisfies all three. OAT discretizes action chunks into an ordered sequence of tokens using a transformer with registers, finite scalar quantization, and ordering-inducing training mechanisms. By training each token prefix to decode into a valid action chunk, OAT places coarse control information in early tokens and uses later tokens to refine residual detail, yielding an anytime tradeoff between inference cost and action fidelity. We validate OAT in two prevailing uses of action tokens: autoregressive policies that generate tokens for control, and token co-training policies that use token losses to shape the vision-language model context consumed by a flow-based action expert. Across three policy backbones and more than 60 tasks spanning five simulation benchmarks and real-world settings, OAT consistently delivers strong policy performance while offering significantly greater flexibility at inference time.

</details>

---

### [[20_Research/Papers/世界模型/Multi-Horizon_Consistency_as_Geometry_When_Latent_Dynamics_Contract,_and_When_They_Do_Not|Multi-Horizon Consistency as Geometry: When Latent Dynamics Contract, and When They Do Not]]

![[assets/2607.21645_figure.png|800]]

- **arXiv**: [2607.21645](https://arxiv.org/abs/2607.21645)
- **PDF**: https://arxiv.org/pdf/2607.21645
- **详细分析**: [[20_Research/Papers/世界模型/Multi-Horizon_Consistency_as_Geometry_When_Latent_Dynamics_Contract,_and_When_They_Do_Not|Multi-Horizon Consistency as Geometry: When Latent Dynamics Contract, and When They Do Not]]
- **作者**: Kavya Bhand, Aadi Joshi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Multi-Horizon Consistency as Geometry: When Latent Dynamics Contract, and When They Do Not》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutumnBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-horizon latent consistency is a common training knob in video predictors and world models, but practitioners rarely know what it does to transition geometry. We treat lambda, the weight on multi-step latent agreement, as a diagnostic control and measure an empirical expansion proxy L20,q95 together with horizon-20 prediction error E20. On Moving-MNIST (n=6 seeds at the critical pair), raising lambda from 0 to 0.8 cuts L20 from 4.96 +/- 2.01 to 1.01 +/- 0.06 (paired t p=0.005, Wilcoxon p=0.031) and halves E20 (0.365 to 0.177, paired t p=1.1e-13). Four of six seeds cross L&lt;1 at lambda=0.8. The same loss does not produce population L&lt;1 on action-conditioned Pendulum-v1 or CartPole-v1, nor on KTH Actions video, even when E20 improves. An associational mediation analysis on MMNIST gives r-hat=0.94 (95% CI [0.88, 1.00], n=27, B=2000); lambda was not randomized. Defensive checks (architectural baselines, exogenous stress, WorldTest, MPC, scaling) mostly support a narrow claim: soft consistency can push passive video toward a near-contractive band, and that band is domain-limited. A stochastic-forcing law L20 ~ 1.23 + 1.82 eta at lambda=0.8 (bootstrap slope CI [1.73, 1.92], R^2=0.96) unifies control domains on the same curve via calibrated eta_eff. Complete joint slices at lambda in {0.4, 1.2} (30/30 cells, 5 eta x 3 seeds) show comparable linear L20(eta) slopes (~1.69 and ~2.00); we do not fit a continuous (lambda, eta) surface. We do not report DreamerV3 or TD-MPC2 returns.

</details>

---

### [[20_Research/Papers/大模型/Tool-Guided_Retrieval-Augmented_Repair_for_Securing_LLM-Generated_C_Code|Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code]]

![[assets/2607.21641_first_page.png|800]]

- **arXiv**: [2607.21641](https://arxiv.org/abs/2607.21641)
- **PDF**: https://arxiv.org/pdf/2607.21641
- **详细分析**: [[20_Research/Papers/大模型/Tool-Guided_Retrieval-Augmented_Repair_for_Securing_LLM-Generated_C_Code|Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code]]
- **作者**: Vidyut Sriram, Saatvik Pradhan, Suman Saha
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can generate C code from natural-language descriptions, but resulting programs often contain security vulnerabilities and compilation errors, posing risks for embedded and resource-constrained systems. This work investigates how feedback and retrieval improve reliability of LLM-generated C code. We present an analysis-and-repair workflow that combines compilation diagnostics, CodeQL static analysis, and KLEE symbolic execution with retrieval of prior repair patterns for iterative refinement. Evaluated on 5,000 C programming tasks exercising embedded relevant vulnerabilities, baseline models show substantial reliability gaps, with compilation failure rates up to 46% and security defect rates up to 49%. Our approach improves both metrics. For CodeLlama 7B, security defect rates decrease from 49% to 19% and total CodeQL errors drop from 15,088 to 2,463 (83.7%). For DeepSeek Coder 1.3B, compilation failures are reduced from 42% to 22% and security defects from 35% to 15%. These results show that integrating lightweight analysis tools can improve the safety of LLM-generated code for embedded development.

</details>

---

### [[20_Research/Papers/其他/Wavelet_Phase_Diffusion_for_Structurally_and_Semantically_Consistent_Sim-to-Real_Translation|Wavelet Phase Diffusion for Structurally and Semantically Consistent Sim-to-Real Translation]]

![[assets/2607.21628_first_page.png|800]]

- **arXiv**: [2607.21628](https://arxiv.org/abs/2607.21628)
- **PDF**: https://arxiv.org/pdf/2607.21628
- **详细分析**: [[20_Research/Papers/其他/Wavelet_Phase_Diffusion_for_Structurally_and_Semantically_Consistent_Sim-to-Real_Translation|Wavelet Phase Diffusion for Structurally and Semantically Consistent Sim-to-Real Translation]]
- **作者**: Kaiwen Wang, Frank Bieder, Yinzhe Shen, Carlos Fernandez, Jan-Hendrik Pauls, Omer Sahin Tas
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.9，大模型 0.1）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Wavelet Phase Diffusion for Structurally and Semantically Consistent Sim-to-Real Translation》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation-to-reality translation must bridge the appearance gap between synthetic and real domains while preserving structural and semantic consistency. Conditioning-based methods achieve spatial alignment but introduce computationally expensive control modules. Paired-data methods achieve realism but rely on complex synthesis pipelines, often altering scene geometry and semantics. Training-free editing methods avoid both constraints but lack a learned appearance prior, limiting their perceptual quality. Recently proposed phase-preserving diffusion presents a promising alternative, but Fourier-domain formulations are constrained by global spectral coupling. This coupling induces spatial artifacts such as ringing and boundary leakage, thereby degrading structural and semantic consistency. We introduce Wavelet Phase Diffusion, which addresses this through two components. First, we operate in the Dual-Tree Complex Wavelet Packet Transform domain, whose localized wavelet packets enable spatially adaptive phase injection without global spectral interference. Second, Low-Frequency Randomization (LFR) replaces the low-frequency packet, decoupling the model from the synthetic illumination prior and enabling in-distribution real-world appearance. Both components train on unpaired open-domain data, and introduce negligible inference overhead. The spatial locality further enables instance-level translation, where individual objects or regions are translated to photorealistic appearance independently while the surrounding scene remains untranslated. On vKITTI $\to$ KITTI image translation, ours outperforms prior methods in realism and semantic consistency while maintaining competitive structural alignment. For CARLA video translation, ours approaches the realism of paired-data methods while reducing VLM planner ADE and FDE by $5.4\%$ and $5.1\%$, respectively.

</details>

---

### [[20_Research/Papers/大模型/Do_Modules_Stay_in_Their_Lane_Role_Drift_in_Compound_LLM_Systems|Do Modules Stay in Their Lane? Role Drift in Compound LLM Systems]]

![[assets/2607.21627_figure.png|800]]

- **arXiv**: [2607.21627](https://arxiv.org/abs/2607.21627)
- **PDF**: https://arxiv.org/pdf/2607.21627
- **详细分析**: [[20_Research/Papers/大模型/Do_Modules_Stay_in_Their_Lane_Role_Drift_in_Compound_LLM_Systems|Do Modules Stay in Their Lane? Role Drift in Compound LLM Systems]]
- **作者**: Xiaoyang Cao, Siddarth Srinivasan, Michiel A. Bakker
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《Do Modules Stay in Their Lane? Role Drift in Compound LLM Systems》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end reinforcement learning can improve the accuracy of compound LLM systems, but it does not constrain how modules divide labor internally. We identify Role Drift, a failure mode in which modules preserve or improve end-task performance while deviating from their assigned roles through role-violating shortcuts that remain invisible to system-level evaluation. To make role drift observable and controllable, we propose Role Anchor, a regularizer that modulates how much each module deviates from its assigned role during end-to-end training. The key idea is to preserve how the role prompt shifts the module's next-token predictions relative to a neutral prompt, which serves as a proxy for the role's intended effect during training. Experiments on two compound LLM pipelines reveal role drift that accuracy alone fails to detect: a decomposer meant to split a question into sub-questions for a separate solver instead plants the answer in them, and a reader meant to answer from retrieved passages instead falls back on parametric memory. In fact, on the decomposer pipeline this shortcut drives most of the apparent RL gain: 86% of it vanishes once the decomposer is held to its role, indicating that terminal accuracy alone can badly overstate how much a compound system has genuinely learned. Across both pipelines, Role Anchor mitigates role drift at a tunable accuracy cost that varies by pipeline and anchor strength. Additional gradient analysis suggests that the regularizer reduces alignment with the role-drift direction rather than simply suppressing learning.

</details>

---

### [[20_Research/Papers/大模型/Trajectory-Aware_Retrieval_Agents_for_Temporal_Decision-_Making|Trajectory-Aware Retrieval Agents for Temporal Decision- Making]]

![[assets/2607.21625_first_page.png|800]]

- **arXiv**: [2607.21625](https://arxiv.org/abs/2607.21625)
- **PDF**: https://arxiv.org/pdf/2607.21625
- **详细分析**: [[20_Research/Papers/大模型/Trajectory-Aware_Retrieval_Agents_for_Temporal_Decision-_Making|Trajectory-Aware Retrieval Agents for Temporal Decision- Making]]
- **作者**: Jing Wang, Jie Shen, Xing Niu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Trajectory-Aware Retrieval Agents for Temporal Decision- Making》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the problem of decision-making from long-form, temporally structured text using large language model (LLM) agents. Standard retrievalaugmented generation (RAG) pipelines fragment chronological context into isolated snippets, discarding the temporal structure that is often critical for correct downstream decisions. We introduce TLM (Trajectory Language Model), a closed-loop agentic framework that iteratively refines the evidence set using SHAP-guided feedback. The key technical contribution is the latent growth curve model (LGCM) over retrieved chunk embeddings, which provides an interpretable mechanism for detecting trajectory trends, turning points, and information gaps. We show that, under a scorer-calibration assumption (which holds approximately in practice), the iterative refinement procedure is monotonically non-decreasing in the probability assigned to the correct label. Empirically, TLM is evaluated on three temporally grounded decision tasks: medical question answering, earnings call surprise prediction, and overnight stock gap prediction. TLM substantially outperforms both zero-shot LLM baselines and standard retrieval-augmented approaches on the medical task, and yields consistent, economically meaningful gains on the two financial tasks.

</details>

---

### [[20_Research/Papers/大模型/Adversarial_Style_Optimization_Enhancing_VLM_Jailbreaks_by_GRPO-based_Stylistic_Triggers_Optimization|Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization]]

![[assets/2607.21619_figure.png|800]]

- **arXiv**: [2607.21619](https://arxiv.org/abs/2607.21619)
- **PDF**: https://arxiv.org/pdf/2607.21619
- **详细分析**: [[20_Research/Papers/大模型/Adversarial_Style_Optimization_Enhancing_VLM_Jailbreaks_by_GRPO-based_Stylistic_Triggers_Optimization|Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization]]
- **作者**: Bingjun Luo, Jialin Guo, Yue Yao, Xinpeng Ding
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-content-based vulnerabilities. Unlike previous research, we empirically find that MLLMs exhibit a Stylistic Inconsistency between their comprehension ability and safety ability: MLLMs can robustly understand content regardless of visual style, yet their defense mechanisms can be easily bypassed by specific stylistic triggers. Based on this finding, we propose Adversarial Style Optimization (ASO), a plug-and-play enhancement module to amplify existing visual jailbreaks. ASO fine-tunes an image-editing model to superimpose an optimized stylistic modification onto a given adversarial image, using a Group Relative Policy Optimization (GRPO) agent guided by a Structurally-Tiered Reward Function that combines a logit-based signal for detecting explicit refusals with a high-fidelity semantic evaluation from a powerful judge model. Extensive experiments show that ASO significantly enhances the ASR of SOTA attacks, demonstrating that stylistic biases are a scalable vector for red-teaming MLLMs. Our code is available at https://github.com/bingjunluo/ASO.

</details>

---

### [[20_Research/Papers/大模型/Household_Movement_Detection_in_Mixed-Format_Occupancy_Data_Using_LLM-Based_Entity_Resolution|Household Movement Detection in Mixed-Format Occupancy Data Using LLM-Based Entity Resolution]]

![[assets/2607.21614_first_page.png|800]]

- **arXiv**: [2607.21614](https://arxiv.org/abs/2607.21614)
- **PDF**: https://arxiv.org/pdf/2607.21614
- **详细分析**: [[20_Research/Papers/大模型/Household_Movement_Detection_in_Mixed-Format_Occupancy_Data_Using_LLM-Based_Entity_Resolution|Household Movement Detection in Mixed-Format Occupancy Data Using LLM-Based Entity Resolution]]
- **作者**: Sasirekha Oguri, John R. Talburt, Mert Can Cakmak
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Household Movement Detection in Mixed-Format Occupancy Data Using LLM-Based Entity Resolution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Entity resolution (ER) typically relies on pairwise similarity comparisons between records, which limits its ability to capture indirect relationships present in demographic occupancy data. An important indirect pattern arises from household movement, where multiple individuals relocate together across addresses, but detecting such patterns is difficult due to mixed-format records, noise, duplication, and the absence of stable identifiers. This paper proposes an AI-enhanced framework for detecting indirect entity links associated with household movement in unstandardized name-address data. The approach integrates prompt-based large language model (LLM) named entity recognition for extracting personal names and addresses without extensive preprocessing, semantic text embeddings for robust similarity computation, and graph-based reasoning to infer group-level movement patterns. Experimental evaluation on SPX benchmark datasets (S8-S12) generated using the Synthetic Occupancy Generator demonstrates that incorporating indirect household movement evidence improves recall by 8-15% while maintaining high precision, yielding F1-score gains of 6-8% over a strong pairwise baseline.

</details>

---

### [[20_Research/Papers/大模型/Decoupled_Attention_Fusion_Accelerating_RAG_with_Efficient_KV_Cache_Reuse|Decoupled Attention Fusion: Accelerating RAG with Efficient KV Cache Reuse]]

![[assets/2607.21599_figure.png|800]]

- **arXiv**: [2607.21599](https://arxiv.org/abs/2607.21599)
- **PDF**: https://arxiv.org/pdf/2607.21599
- **详细分析**: [[20_Research/Papers/大模型/Decoupled_Attention_Fusion_Accelerating_RAG_with_Efficient_KV_Cache_Reuse|Decoupled Attention Fusion: Accelerating RAG with Efficient KV Cache Reuse]]
- **作者**: Xiabao Wu, Wentao Liu, Yongchao Liu, Jiajun Zheng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: cs.AI

#### 研究背景与动机

《Decoupled Attention Fusion: Accelerating RAG with Efficient KV Cache Reuse》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) effectively mitigates hallucinations in Large Language Models (LLMs) but suffers from prohibitive Time-To-First-Token (TTFT) latency in long-context scenarios. Reusing pre-computed document KV caches addresses this but introduces a distribution mismatch, where offline caches lack the inter-document attention patterns required for coherent reasoning. CacheBlend reduces recomputation via selective attention, but suffers severe accuracy degradation at longer contexts. To address these challenges, we propose Decoupled Attention Fusion (DAF), a framework that maintains high accuracy while significantly reducing recomputation overhead. DAF decouples the attention process into three integrated stages: important-token self-attention to restore missing inter-document attention, question-document self-attention for standard inference, and a state fusion that concatenates their outputs to synthesize the final hidden states. By decoupling these operations into dense patterns, DAF is natively compatible with Flash-Attention kernels, maximizing hardware utilization without requiring complex attention masks. Experiments show that DAF delivers up to 2 times speedup over CacheBlend and 5.6 times over full recomputation with vLLM on long-context benchmarks, without sacrificing accuracy.

</details>

---

### [[20_Research/Papers/大模型/FlowEvo_Self-Evolving_Agents_through_the_Co-Evolution_of_Workflows_and_Executable_Skills|FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills]]

![[assets/2607.21596_figure.png|800]]

- **arXiv**: [2607.21596](https://arxiv.org/abs/2607.21596)
- **PDF**: https://arxiv.org/pdf/2607.21596
- **详细分析**: [[20_Research/Papers/大模型/FlowEvo_Self-Evolving_Agents_through_the_Co-Evolution_of_Workflows_and_Executable_Skills|FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills]]
- **作者**: Zeyu Ren, Ling Yue, Ran Li, Yishu Wang, Shengxiang Xu, Hanmo Liu, Shaowu Pan, Shimin Di
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents increasingly solve complex tasks by constructing inference-time workflows that combine reasoning, tool use, and code execution. While such workflows enable flexible problem solving, the useful procedures discovered during execution are often transient: they help solve the current task but are not retained in a form that can systematically benefit future tasks. We present FlowEvo, a training-free framework that compiles successful traces into reusable skill records. Each record pairs a callable artifact with auxiliary structured guidance, and admission applies interface, replay, and safety checks where feasible. These skill records persist in a skill bank at inference time. FlowEvo is organized around three coupled mechanisms: (1)~workflow-to-skill compilation, which extracts reusable executable artifacts from successful traces; (2)~skill-to-workflow feedback, which retrieves accumulated skills to support future problem solving through either direct execution or structured context injection; and (3)~skill curation, which monitors downstream utility and suppresses skills that cause negative transfer. Through this workflow--skill--workflow feedback loop, FlowEvo enables agents to accumulate and refine task-solving capability over time without updating model parameters. Experiments on benchmarks spanning interactive environments (ALFWorld) and code/math generation (HumanEval, GSM8K) show that FlowEvo achieves the best accuracy-cost tradeoff among the evaluated baselines under our implementation settings. On ALFWorld, FlowEvo achieves an 82.8\% success rate, 23.6 percentage points above the strongest baseline, while its average token usage per episode is less than half that of the most efficient baseline. Controlled ablations confirm that each mechanism contributes to the overall result. The code is public at https://github.com/DEFENSE-SEU/FlowEvo.

</details>

---
