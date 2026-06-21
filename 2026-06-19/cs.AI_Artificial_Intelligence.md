# cs.AI | Artificial Intelligence | 2026-06-19

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/大模型/Contagion_Networks_Evaluator_Bias_Propagation_in_Multi-Agent_LLM_Systems|Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems]]

![[assets/2606.20493_figure.png|800]]

- **arXiv**: [2606.20493](https://arxiv.org/abs/2606.20493)
- **PDF**: https://arxiv.org/pdf/2606.20493
- **详细分析**: [[20_Research/Papers/大模型/Contagion_Networks_Evaluator_Bias_Propagation_in_Multi-Agent_LLM_Systems|Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems]]
- **作者**: Zewen Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal framework for measuring how evaluator biases spread across interacting LLM agents. In a controlled 3-agent experiment using DeepSeek-chat with three distinct evaluator bias profiles (structured, balanced, evidence-based), we measure the Cross-Agent Contagion Matrix Gamma_3 and find that evaluator biases consistently propagate between agents (gamma in [0.157, 0.352]), even within the same underlying model. We identify three propagation regimes governed by the spectral radius rho(Gamma_N), and demonstrate that homogeneous-model agents produce contagion coefficients 3-5x weaker than cross-model coefficients observed in prior work (MM-EPC: gamma approx 0.85-1.3), placing them in the suppression regime. We show that increasing evaluator committee size from k=1 to k=3 reduces effective contagion by 72.4%, providing an actionable mitigation strategy. We release the open-source Contagion Network experimental framework.

</details>

---

### [[20_Research/Papers/大模型/LLM_agent_safety,_multi-turn_red-teaming,_jailbreak_benchmarks,_adversarial_robustness,_safety-critical_systems|LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems]]

![[assets/2606.20408_figure.png|800]]

- **arXiv**: [2606.20408](https://arxiv.org/abs/2606.20408)
- **PDF**: https://arxiv.org/pdf/2606.20408
- **详细分析**: [[20_Research/Papers/大模型/LLM_agent_safety,_multi-turn_red-teaming,_jailbreak_benchmarks,_adversarial_robustness,_safety-critical_systems|LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems]]
- **作者**: Hanwool Lee, Dasol Choi, Bokyeong Kim, Seung Geun Kim, Haon Park
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：NRT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly proposed as supervisory components for safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure remains poorly characterized. We present NRT-Bench, a benchmark for multi-turn red-teaming of LLM agents acting as operators of a safety-critical system, instantiated in a simulated nuclear power plant control room. A five-role operator team, each backed by a configurable LLM, runs a plant governed by six critical safety functions (CSFs), while adversaries inject messages over four channels in bounded multi-turn sessions with per-turn feedback. Harm is an objective signal rather than LLM-judged text: a run terminates the moment any CSF is lost, attributed to the causing message. Evaluating four frontier operator models under a fixed-attack paired-replay protocol, we find that adaptive multi-turn attacks reliably push the operator team past a safety limit: across the four models, between 8.7% and 12.1% of attack sessions end with the plant losing a critical safety function. Although the four models look almost equally robust by this aggregate rate, their failures barely overlap: of $149$ sessions, none defeat all four models while a third defeat at least one, so vulnerabilities are nearly disjoint across models rather than nested. The effect of added defences is strongly model-dependent: the same guardrail stack or safety-advisor agent that lowers attack success for one model can raise it for another. We release the simulation venue, attack dataset, and replay tooling for reproducible safety evaluation of LLM agents.

</details>

---

### [[20_Research/Papers/强化学习/CRAX_Fast_Safe_Reinforcement_Learning_Benchmarking|CRAX: Fast Safe Reinforcement Learning Benchmarking]]

![[assets/2606.20376_figure.png|800]]

- **arXiv**: [2606.20376](https://arxiv.org/abs/2606.20376)
- **PDF**: https://arxiv.org/pdf/2606.20376
- **详细分析**: [[20_Research/Papers/强化学习/CRAX_Fast_Safe_Reinforcement_Learning_Benchmarking|CRAX: Fast Safe Reinforcement Learning Benchmarking]]
- **作者**: Tristan Tomilin, Mourad Boustani, Mickey Beurskens, Thiago D. Simão
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《CRAX: Fast Safe Reinforcement Learning Benchmarking》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Bullet-Safety-Gym, ImageNet, JaxMARL, Meta-RL, Meta-World, Safe-Control-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety is a core concern for deploying reinforcement learning (RL) agents in real-world domains such as robotics and autonomous driving. While benchmarks have been central to progress in RL, existing safety benchmarks with high-fidelity 3D physics remain computationally slow, limiting large-scale experimentation and rapid prototyping. To address this gap, we propose CRAX (Constrained RL Accelerated with JAX). Built on top of the MuJoCo XLA (MJX) physics engine with realistic 3D dynamics, CRAX leverages vectorized operations and hardware acceleration, yielding up to ~100x speedups over comparable CPU-based safety benchmarks. The benchmark features six environment suites and three agent-specific tasks, each spanning three difficulty levels. Evaluating six popular safe RL methods shows that no single approach dominates across all tasks, and reveals the trade-offs between performance and safety. We find that curriculum learning across difficulty levels and safety transfer can improve performance over direct training in harder settings.

</details>

---

### [[20_Research/Papers/大模型/AutoPass_Evidence-Guided_LLM_Agents_for_Compiler_Performance_Tuning|AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning]]

![[assets/2606.20373_figure.png|800]]

- **arXiv**: [2606.20373](https://arxiv.org/abs/2606.20373)
- **PDF**: https://arxiv.org/pdf/2606.20373
- **详细分析**: [[20_Research/Papers/大模型/AutoPass_Evidence-Guided_LLM_Agents_for_Compiler_Performance_Tuning|AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning]]
- **作者**: Zepeng Li, Jie Ren, Zhanyong Tang, Jie Zheng, Zheng Wang
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AutoPass: Evidence-Guided LLM Agents for Compiler Performance Tuning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CompilerGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) show promise for code compilation tasks, but applying them to runtime performance tuning is difficult due to complex microarchitectural effects and noisy runtime measurements. We present AutoPass, a multi-agent framework for compiler performance tuning that uses compiler and runtime evidence to guide LLM-generated optimization decisions. Rather than treating the compiler as a black box like prior auto-tuning schemes, AutoPass opens up the compiler to the LLM, enabling it to query compiler-internal optimization states and analyze the intermediate representation to orchestrate compiler options. The search process iteratively refines optimization configurations using measured runtime feedback to diagnose regressions and guide latency-improving edits. AutoPass operates in an inference-only, training-free setting and requires no offline training or task-specific fine-tuning, making it readily applicable to new benchmarks and platforms. We implement AutoPass on the LLVM compiler and evaluate it on server-grade x86-64 and embedded ARM64 systems. AutoPass outperforms expert-tuned heuristics and classical autotuning methods, achieving geometric-mean speedups of 1.043x and 1.117x over LLVM -O3 on x86-64 and ARM64, respectively.

</details>

---

### [[20_Research/Papers/具身智能/Finetuning_Vision-Language-Action_Models_Requires_Fewer_Layers_Than_You_Think|Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think]]

![[assets/2606.20246_figure.png|800]]

- **arXiv**: [2606.20246](https://arxiv.org/abs/2606.20246)
- **PDF**: https://arxiv.org/pdf/2606.20246
- **详细分析**: [[20_Research/Papers/具身智能/Finetuning_Vision-Language-Action_Models_Requires_Fewer_Layers_Than_You_Think|Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think]]
- **作者**: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, Long Dinh, Tuan Dam, Vu Duong, Tung M. Luu, Trung Le, Tran Nguyen Le...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DeeR-VLA, Efficient-VLA, EfficientVLA, FLOWER-VLA, Flower-VLA, MoLe-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference. In this work, we reveal a highly non-trivial architectural characteristic of these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being trained on diverse physical trajectories, they exhibit severe layer-wise representational redundancy. To exploit this, we introduce a structural compression pipeline that is entirely training-free, bypassing the need of existing methods to load full-scale models to learn optimized token reductions or dynamic layer selectors. Instead, using only a single forward pass via Centered Kernel Alignment to identify redundant layer features, we remove twin layers to permanently compress the model depth by up to 50% across both the VLM backbone and the continuous control policy head. Downstream fine-tuning of this streamlined architecture yields a dual acceleration benefit: a 40-50% reduction in training time and up to 30% faster real-time inference, while matching or exceeding full-scale base model performance. We comprehensively validate our method across three simulation benchmarks (LIBERO, RoboCasa, SimplerEnv) and 10 diverse real-world manipulation tasks across 4 unique robotic embodiments. These results prove that advanced VLAs require significantly fewer layers than previously assumed, offering a highly compute-efficient paradigm for scalable robot learning.

</details>

---

### [[20_Research/Papers/强化学习/A_Multi-Agent_system_for_Multi-Objective_constrained_optimization|A Multi-Agent system for Multi-Objective constrained optimization]]

![[assets/2606.20236_figure.png|800]]

- **arXiv**: [2606.20236](https://arxiv.org/abs/2606.20236)
- **PDF**: https://arxiv.org/pdf/2606.20236
- **详细分析**: [[20_Research/Papers/强化学习/A_Multi-Agent_system_for_Multi-Objective_constrained_optimization|A Multi-Agent system for Multi-Objective constrained optimization]]
- **作者**: Federica Filippini
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《A Multi-Agent system for Multi-Objective constrained optimization》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many decision-making problems in computing and networking systems can be naturally formulated as cost-minimization problems under performance constraints. In dynamic environments, reinforcement learning (RL) is often used to solve such problems at runtime by embedding both costs and constraint violations into a single scalar reward through weighted penalty terms, following a Lagrangian-inspired formulation. However, in this context the behavior of the learned policy critically depends on the choice of these weights, which are typically selected manually. This makes it difficult to identify an appropriate trade-off between optimizing the primary objective and effectively avoiding constraint violations, particularly in non-stationary environments where their relative importance may change. This paper presents MAMO (Multi-Agent system for Multi-Objective constrained optimization), an approach to tackle this balancing problem through multi-agent RL. MAMO decouples task execution from objective design by formulating the selection of reward weights as a learning problem, providing a !rst step towards more autonomous and robust RL-based solutions for constrained optimization problems in dynamic environments.

</details>

---

### [[20_Research/Papers/强化学习/Augmenting_Game_AI_with_Deep_Reinforcement_Learning|Augmenting Game AI with Deep Reinforcement Learning]]

![[assets/2606.20210_figure.jpg|800]]

- **arXiv**: [2606.20210](https://arxiv.org/abs/2606.20210)
- **PDF**: https://arxiv.org/pdf/2606.20210
- **详细分析**: [[20_Research/Papers/强化学习/Augmenting_Game_AI_with_Deep_Reinforcement_Learning|Augmenting Game AI with Deep Reinforcement Learning]]
- **作者**: Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Jean-Philippe Barrette-LaPierre, Florian Fuchs, Linus Gisslén
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.1，强化学习 1.4）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Augmenting Game AI with Deep Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Immersion in video games depends not only on graphics, audio, and game mechanics, but also on the quality of in-game characters. Producing believable characters, or game AI, remains a significant challenge as behavioral complexity is hard to capture with hand-coded systems. Game AI is a source of immersion and engagement; however, the limitations stemming from the challenges of creating game AI often lead to frustration and the breaking of the illusion of realism within the game. The introduction of machine learning models opens the door to creating more believable, authentic, and relatable characters in games. The promise is that they either learn from interacting with the game, or from player data, to develop true human-like behavior. In this paper, we envision more applications of reinforcement learning for game AI in the future. For this to materialize, current research limitations are prohibitive to broad deployment across game genres. Therefore, we propose a framework for training reinforcement learning models with a set of requirements in mind that are suited towards game AI and game development. We present examples of games with reinforcement learning-augmented game AI and describe the practicalities of deploying player-facing machine learning agents in modern games. Furthermore, we identify bottlenecks and hard problems in these areas, which we believe offer promising research directions to accelerate the adoption of machine learning in game AI for the video game industry.

</details>

---

### [[20_Research/Papers/具身智能/FlowMaps_Modeling_Long-Term_Multimodal_Object_Dynamics_with_Flow_Matching|FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching]]

![[assets/2606.20209_figure.png|800]]

- **arXiv**: [2606.20209](https://arxiv.org/abs/2606.20209)
- **PDF**: https://arxiv.org/pdf/2606.20209
- **详细分析**: [[20_Research/Papers/具身智能/FlowMaps_Modeling_Long-Term_Multimodal_Object_Dynamics_with_Flow_Matching|FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching]]
- **作者**: Francesco Argenziano, Miguel Saavedra-Ruiz, Sacha Morin, Charlie Gauthier, Daniele Nardi, Liam Paull
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.5，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《FlowMaps: Modeling Long-Term Multimodal Object Dynamics with Flow Matching》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint spatial and temporal understanding of 3D scenes is a crucial requirement for robots deployed in everyday household environments. Such agents must not only comprehend and navigate spatial layouts, but also reason about how these spaces evolve over time. In particular, humans interact with objects daily, causing them to change position throughout the environment and making it difficult for robots to reliably associate current observations with previously seen objects. However, these interactions are not random: human habits and routines induce spatio-temporally consistent patterns in object locations, which robotic agents can potentially learn and then exploit for downstream tasks such as navigation. To this end, we introduce FlowMaps, a latent flow matching model for estimating multimodal distributions over the future locations of dynamic objects in a continuous 3D space. By learning the implicit dependencies among objects and their temporal evolution, FlowMaps predicts likely changes in object locations conditioned on past human interactions, while supporting generalization across previously unseen environments that share similar object routines. To demonstrate the utility of this method, we deploy FlowMaps in a downstream dynamic Object Navigation task in both simulated and real-world environments. Across more than 600 episodes, FlowMaps outperforms state-of-the-art approaches, showing that modeling object dynamics through continuous, multimodal spatio-temporal distributions improves robotic search and navigation in changing household environments. Code and additional material is available at https://fra-tsuna.github.io/flowmaps/.

</details>

---

### [[20_Research/Papers/大模型/MedRLM_Recursive_Multimodal_Health_Intelligence_for_Long-Context_Clinical_Reasoning,_Sensor-Guided_Screening,_Evidence-Grounded_Decision_Sup|MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization]]

![[assets/2606.20164_figure.png|800]]

- **arXiv**: [2606.20164](https://arxiv.org/abs/2606.20164)
- **PDF**: https://arxiv.org/pdf/2606.20164
- **详细分析**: [[20_Research/Papers/大模型/MedRLM_Recursive_Multimodal_Health_Intelligence_for_Long-Context_Clinical_Reasoning,_Sensor-Guided_Screening,_Evidence-Grounded_Decision_Sup|MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization]]
- **作者**: Aueaphum Aueawatthanaphisut
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《MedRLM: Recursive Multimodal Health Intelligence for Long-Context Clinical Reasoning, Sensor-Guided Screening, Evidence-Grounded Decision Support, and Community-to-Tertiary Referral Optimization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world clinical decision support requires reasoning over heterogeneous and longitudinal patient information rather than answering isolated medical questions. However, current medical large language models and retrieval-augmented generation systems often rely on single-step prompting or retrieval, which can be fragile when clinical evidence is distributed across long electronic health records, medical images, sensor streams, guidelines, and referral constraints. This paper proposes MedRLM, a Recursive Multimodal Health Intelligence framework for long-context clinical reasoning, sensor-guided screening, and community-to-tertiary referral support. Instead of compressing all patient information into one prompt, MedRLM treats the patient case as an external clinical environment that can be recursively inspected, decomposed, retrieved, verified, and synthesized. The framework coordinates specialized agents for clinical text, longitudinal EHR, medical imaging, physiological sensor signals, guideline retrieval, uncertainty auditing, and referral planning. It further introduces a Clinical Evidence Graph Memory to connect patient-specific observations with retrieved evidence, standardized definitions, sensor-derived biomarkers, and referral criteria. A sensor-guided recursive triggering mechanism activates deeper reasoning when abnormal physiological or behavioral patterns are detected, while uncertainty-gated refinement supports clinician review for high-risk or low-confidence cases. We also outline a real-data evaluation design using public and credentialed clinical datasets spanning EHR, radiology, ECG, ICU time series, and referral-proxy outcomes. MedRLM aims to move medical AI from static question answering toward auditable, multimodal, and workflow-aware clinical decision support.

</details>

---

### [[20_Research/Papers/大模型/Learning_to_Prompt_Improving_Student_Engagement_with_Adaptive_LLM-based_High-School_Tutoring|Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring]]

![[assets/2606.20138_figure.png|800]]

- **arXiv**: [2606.20138](https://arxiv.org/abs/2606.20138)
- **PDF**: https://arxiv.org/pdf/2606.20138
- **详细分析**: [[20_Research/Papers/大模型/Learning_to_Prompt_Improving_Student_Engagement_with_Adaptive_LLM-based_High-School_Tutoring|Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring]]
- **作者**: Po-Chin Chang, Nicholas Hogan, Aske Plaat, Michiel T. van der Meer
- **cs 子类**: cs.AI, cs.CL, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.85（加权：具身智能 0.3，大模型 0.55）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Learning to Prompt: Improving Student Engagement with Adaptive LLM-based High-School Tutoring》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs can personalize education, although current static-prompt tutoring systems struggle to adapt to diverse academic disciplines. We develop and test a system with subject-aware prompting, based on 14 pedagogical features (e.g., tutor scaffolding, student understanding) extracted from raw transcripts. We first train a prompt routing model in a simulation environment, and then deploy it for online adaptation with actual high-school students. The simulation benchmark shows the router outperforming two static baselines ($0.694$ vs. $0.647$ and $0.64$, $p&lt;0.001$). A/B testing ($N=656$ conversations from 359 students) shows sim-to-real transfer where the model switches from analytical to scaffolding learning strategies. Our adaptive prompt selection mechanism improves instructional efficiency, maintains pedagogical quality and reduces interactions by around 3 turns ($p=0.007$). While a greedy router achieves a comparable exercise conversion rate with the baseline ($19.1\%$ vs. $19.6\%$), a stochastic router that samples strategies leads to a higher conversion rate ($28.1\%$).

</details>

---

### [[20_Research/Papers/具身智能/Frequency-Aware_Flow_Matching_for_Continuous_and_Consistent_Robotic_Action_Generation|Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation]]

![[assets/2606.20135_figure.png|800]]

- **arXiv**: [2606.20135](https://arxiv.org/abs/2606.20135)
- **PDF**: https://arxiv.org/pdf/2606.20135
- **详细分析**: [[20_Research/Papers/具身智能/Frequency-Aware_Flow_Matching_for_Continuous_and_Consistent_Robotic_Action_Generation|Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation]]
- **作者**: Jianing Guo, Fangzheng Chen, Zihao Mao, Wong Lik Hang Kenny, Zhenhong Wu, Yu Li, Yishuai Cai, Yuanpei Chen, Yikun Ban, Kai Chen, Qi Dou, Yaodong Yang...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Frequency-Aware Flow Matching for Continuous and Consistent Robotic Action Generation》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DexGraspVLA, LapGym, OpenVLA, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching has emerged as a standard paradigm for robotic manipulation owing to its strong expressive power for modelling complex, multimodal action distributions, alongside similar approaches like diffusion policy. However, existing methods rely on discretized action chunks, making them brittle to demonstrations collected at heterogeneous control frequencies and prone to temporally inconsistent actions that degrade control stability. In this paper, we propose Frequency-Aware Flow Matching (FAFM), which outputs continuous, temporally consistent actions. To handle heterogeneous frequency input, we transform discrete action sequences into the frequency domain with the discrete cosine transform (DCT), perform flow matching over the resulting coefficients, and reconstruct continuous actions via cosine basis expansion. To generate temporally consistent actions, we regularize the first-order temporal derivative to promote smooth actions. This corresponds to a Sobolev-type constraint that suppresses high-frequency errors and discourages abrupt action changes. Our FAFM is simple, introduces no additional network parameters and applies to standalone flow-matching policies and vision-language action models. Across synthetic toy benchmark, obstacle avoidance, LapGym, and LIBERO, FAFM improves success rates, multimodal expressivity, motion smoothness, convergence speed, robustness to mechanical bias and mixed-frequency input. These gains are consistent when deployed on a real-world Franka robot. Code available at https://anonymous.4open.science/r/FAFM.

</details>

---

### [[20_Research/Papers/大模型/Dual-Agent_Framework_for_Cross-Model_Verified_Translation_of_Natural-Language_Protocols_into_Robotic_Laboratory_Platform|Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform]]

![[assets/2606.20120_first_page.png|800]]

- **arXiv**: [2606.20120](https://arxiv.org/abs/2606.20120)
- **PDF**: https://arxiv.org/pdf/2606.20120
- **详细分析**: [[20_Research/Papers/大模型/Dual-Agent_Framework_for_Cross-Model_Verified_Translation_of_Natural-Language_Protocols_into_Robotic_Laboratory_Platform|Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform]]
- **作者**: Hyeonna Choi, Jung Yup Kim, Hyuneui Lim, Seunggyu Jeon
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Dual-Agent Framework for Cross-Model Verified Translation of Natural-Language Protocols into Robotic Laboratory Platform》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biological experiment protocols are written in natural language, whereas automation systems rely on predefined control commands, creating a semantic gap that limits autonomous execution. Microplate-based automatic experiments are particularly challenging due to the need to simultaneously control well mapping, sample-reagent combinations, replicate placement, and parallel dispensing. This study proposes an agent-based protocol translation framework that converts natural-language microplate-based protocols into executable control commands for a robotic laboratory platform. A Parser Agent formalizes the natural-language protocol into a structured representation, and a rule-based mapping engine deterministically incorporates the operational constraints of the robotic laboratory platform to generate device-level control commands. A heterogeneous LLM Validation Agent verifies completeness, parameter accuracy, and execution order, and triggers a self-correction loop with structured feedback when errors are detected. A sweep involving 7 Parsers and 3 Validators on randomly selected ELISA protocols evaluates how model scale and Validator type affect translation accuracy and pass rates under cross-model verification. The accuracy-latency trade-off is further verified by comparing the rule-based mapping of the proposed framework with LLM end-to-end direct mapping. Finally, Bradford assay-based protein quantification using a microplate was demonstrated on a robotic laboratory platform, validating end-to-end autonomous execution from natural-language protocols to real-world experiments. The proposed framework provides a flexible approach to narrowing the semantic gap between natural-language protocols and microplate-based self-driving laboratories.

</details>

---

### [[20_Research/Papers/强化学习/Sensorimotor_World_Models_Perception_for_Action_via_Inverse_Dynamics|Sensorimotor World Models: Perception for Action via Inverse Dynamics]]

![[assets/2606.20104_figure.png|800]]

- **arXiv**: [2606.20104](https://arxiv.org/abs/2606.20104)
- **PDF**: https://arxiv.org/pdf/2606.20104
- **详细分析**: [[20_Research/Papers/强化学习/Sensorimotor_World_Models_Perception_for_Action_via_Inverse_Dynamics|Sensorimotor World Models: Perception for Action via Inverse Dynamics]]
- **作者**: Petr Ivashkov, Randall Balestriero, Bernhard Schölkopf
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Sensorimotor World Models: Perception for Action via Inverse Dynamics》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions. At the same time, latent JEPA-style world models advocate learning compact predictive states from high-dimensional observations to facilitate the prediction of future states, but end-to-end training of these models is nontrivial because representations may collapse if our only goal is to construct a latent state that is easy to predict. We introduce a sensorimotor world model (SMWM): a latent world model trained end-to-end with inverse dynamics regularization. This single regularizer addresses both issues: it prevents representation collapse and induces action-aligned representations. By forcing latent states to preserve information about the action underlying a transition, it biases the model toward the controllable degrees of freedom of the environment while discarding uncontrollable distractors. This yields stable latent world models trained from offline, reward-free trajectories, without frozen encoders, exponential moving averages, or complex latent regularizers. Empirically, SMWM learns compact, interpretable latent spaces and enables competitive planning performance across simple 2D and 3D control tasks.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Head_Attention-Based_Feature_Extractor_Integration_with_Soft_Actor-Critic_for_Porosity_Prediction_and_Process_Parameter_Optimization_i|Multi-Head Attention-Based Feature Extractor Integration with Soft Actor-Critic for Porosity Prediction and Process Parameter Optimization in Additive Manufacturing]]

![[assets/2606.20087_figure.png|800]]

- **arXiv**: [2606.20087](https://arxiv.org/abs/2606.20087)
- **PDF**: https://arxiv.org/pdf/2606.20087
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Head_Attention-Based_Feature_Extractor_Integration_with_Soft_Actor-Critic_for_Porosity_Prediction_and_Process_Parameter_Optimization_i|Multi-Head Attention-Based Feature Extractor Integration with Soft Actor-Critic for Porosity Prediction and Process Parameter Optimization in Additive Manufacturing]]
- **作者**: Kianoush Aqabakee, Leonardo Stella
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Multi-Head Attention-Based Feature Extractor Integration with Soft Actor-Critic for Porosity Prediction and Process Parameter Optimization in Additive Manufacturing》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Additive manufacturing process optimization requires precise parameter control to minimize defects such as porosity. Traditional reinforcement learning (RL) approaches using discrete action spaces suffer from slow convergence and susceptibility to local optima, limiting their effectiveness for high-precision manufacturing tasks. This study addresses these limitations by employing a continuous action space combined with a novel architecture that integrates a multi-head attention mechanism with the Soft Actor-Critic (SAC) algorithm. The attention-based feature extractor enhances the agent's ability to capture subtle variations in low-dimensional input features, enabling more effective exploration-exploitation balance for navigating value spaces with local minima. We validate our approach on porosity prediction and process parameter optimization in laser powder bed fusion, demonstrating faster convergence and higher final reward values compared to standard RL methods including DQN, PPO, TD3, and vanilla SAC. The proposed methodology achieves a convergence value of 322.79 within 14 episodes, outperforming existing approaches while maintaining stability throughout training.

</details>

---

### [[20_Research/Papers/大模型/AI_Economist_Agent_An_Agentic_Framework_for_Model-Grounded_Economic_Analysis_with_RAG,_Knowledge_Graphs,_and_Large_Language_Models|AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models]]

![[assets/2606.20041_figure.png|800]]

- **arXiv**: [2606.20041](https://arxiv.org/abs/2606.20041)
- **PDF**: https://arxiv.org/pdf/2606.20041
- **详细分析**: [[20_Research/Papers/大模型/AI_Economist_Agent_An_Agentic_Framework_for_Model-Grounded_Economic_Analysis_with_RAG,_Knowledge_Graphs,_and_Large_Language_Models|AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models]]
- **作者**: Masahiro Kato
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AI Economist Agent: An Agentic Framework for Model-Grounded Economic Analysis with RAG, Knowledge Graphs, and Large Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose a model-grounded RAG-based AI economist with an agentic framework for economic scenario analysis using large language models (LLMs) and knowledge graphs. While LLMs can generate fluent economic narratives, economists are often required to make economic claims grounded by economic theory and real-world data. Based on this motivation, this study proposes an RAG-based AI economist, which utilizes knowledge graphs including economic data and theory and LLM-based agents to plan the analysis, retrieve relevant evidence, select appropriate models, and generate reports. In our framework, we do not produce quantitative claims directly with the language model alone; instead, we generate narratives grounded in explicit model-based computations and linked to the retrieved evidence via AI agents. We refer to our framework as an AI economist agent. We evaluate the AI economist agent in two applications: economist report generation for U.S. inflation persistence and Federal Reserve policy, and bank stress-test narrative generation for U.S. commercial real estate refinancing stress. The results illustrate how grounding the generated reports improves their economic coherence and traceability.

</details>

---

### [[20_Research/Papers/强化学习/A_Neuromorphic_Reinforcement_Learning_Framework_for_Efficient_Pathfinding_in_Robotic_Mobile_Fulfillment_Systems|A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems]]

![[assets/2606.20031_figure.png|800]]

- **arXiv**: [2606.20031](https://arxiv.org/abs/2606.20031)
- **PDF**: https://arxiv.org/pdf/2606.20031
- **详细分析**: [[20_Research/Papers/强化学习/A_Neuromorphic_Reinforcement_Learning_Framework_for_Efficient_Pathfinding_in_Robotic_Mobile_Fulfillment_Systems|A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems]]
- **作者**: Junzhe Xu, Zecui Zeng, Lusong Li, Yuetong Fang, Renjing Xu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《A Neuromorphic Reinforcement Learning Framework for Efficient Pathfinding in Robotic Mobile Fulfillment Systems》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic environmental changes, confined workspaces, and stringent real-time constraints make pathfinding in Robotic Mobile Fulfillment Systems (RMFS) a challenging problem for conventional search- and rule-based methods, which typically suffer from high computational complexity and long decision latency. While reinforcement learning (RL) has emerged as a powerful alternative, deploying learned policies with extreme energy efficiency on resource-constrained hardware remains an open challenge. We present SDQN-RMFS, an end-to-end framework that achieves high-fidelity deployment of an RL-trained policy from a full-precision artificial neural network (ANN) through to a neuromorphic chip. By computing only when triggered by sparse events, this framework unlocks ultra-low-power RMFS pathfinding. Our full-stack pipeline operates as follows: an ANN policy is first efficiently trained via a collision-allowing strategy to densify informative trajectories, and then converted into a spiking neural network (SNN) via a hard-label knowledge distillation approach. This effectively addresses the output distribution mismatch, preserving policy capability across the ANN-to-SNN pipeline while substantially reducing inference latency. Hardware experiments demonstrate up to 11,281$\times$ energy savings and a nearly two-fold reduction in latency compared to a high-performance GPU baseline, while maintaining decision quality on par with the original trained policy. These results establish physical neuromorphic inference as a practical and energy-sustainable pathway for large-scale RMFS operations.

</details>

---

### [[20_Research/Papers/大模型/When_Lower_Privileges_Suffice_Investigating_Over-Privileged_Tool_Selection_in_LLM_Agents|When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents]]

![[assets/2606.20023_figure.png|800]]

- **arXiv**: [2606.20023](https://arxiv.org/abs/2606.20023)
- **PDF**: https://arxiv.org/pdf/2606.20023
- **详细分析**: [[20_Research/Papers/大模型/When_Lower_Privileges_Suffice_Investigating_Over-Privileged_Tool_Selection_in_LLM_Agents|When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents]]
- **作者**: Kaiyue Yang, Yuyan Bu, Jingwei Yi, Yuchi Wang, Biyu Zhou, Juntao Dai, Songlin Hu, Yaodong Yang
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ToolPrivBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As LLM agents increasingly select tools autonomously, their choices among tools with different privileges become safety-relevant. However, prior tool-selection studies focus on safety-agnostic metadata preferences, leaving privilege-sensitive choices underexplored. To address this gap, we study over-privileged tool selection, in which an agent selects or escalates to a higher-privilege tool despite a sufficient lower-privilege alternative. We introduce ToolPrivBench to evaluate whether agents choose higher-privilege tools despite sufficient lower-privilege alternatives, measuring both initial selection and escalation after transient tool failures. Across eight domains and five recurring risk patterns, we find that over-privileged tool selection is common among mainstream LLM agents and is further amplified by transient failures. We further find that general safety alignment does not reliably transfer to least-privilege tool choice, while prompt-level controls provide only limited mitigation under transient failures. We therefore introduce a privilege-aware post-training defense that teaches agents to prefer sufficient lower-privilege tools and escalate only when necessary. Our mitigation experiments show that this defense substantially reduces unnecessary high-privilege tool use while preserving general capabilities.

</details>

---

### [[20_Research/Papers/大模型/Hierarchical_Control_in_Multi-Agent_Games_LLM-based_Planning_and_RL_Execution|Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution]]

![[assets/2606.20014_figure.png|800]]

- **arXiv**: [2606.20014](https://arxiv.org/abs/2606.20014)
- **PDF**: https://arxiv.org/pdf/2606.20014
- **详细分析**: [[20_Research/Papers/大模型/Hierarchical_Control_in_Multi-Agent_Games_LLM-based_Planning_and_RL_Execution|Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution]]
- **作者**: Jannik Hösch, Alessandro Sestini, Florian Fuchs, Amir Baghi, Joakim Bergdahl, Konrad Tollmar, Jean-Philippe Barrette-LaPierre, Linus Gisslén
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.62（加权：大模型 1.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HRL, LLM-RL, MARL, YOLO-MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has achieved strong performance in sequential decision-making, yet scaling to complex multi-agent environments remains challenging due to sparse rewards, large state-action spaces, and the difficulty of learning coordinated strategies. We propose a hierarchical architecture where a pretrained large language model (LLM) acts as a centralized strategic controller that selects among specialized RL skill policies for a team of agents, while RL policies handle reactive low-level execution. We evaluate this hybrid system in a competitive 2v2 King of the Hill environment against behavior tree (BT) and \emph{``Flat''} RL (end-to-end training without skill decomposition) baselines. The LLM+RL system achieves task performance statistically equivalent to hand-crafted BT (46.4\% vs 51.5\% win rate, $p=0.103$) while both significantly outperform Flat RL trained without skill decomposition. A user study ($n=15$) reveals that 60\% of participants perceive LLM+RL agents as the most human-like ($p=0.027$), citing behavioral adaptability and tactical variability. These results demonstrate that pretrained LLM reasoning can effectively orchestrate pretrained RL skills, achieving competitive multi-agent coordination and superior perceived believability without manual rule engineering.

</details>

---

### [[20_Research/Papers/大模型/Connect_the_Dots_Training_LLMs_for_Long-Lifecycle_Agents_with_Cross-Domain_Generalization_Via_Reinforcement_Learning|Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning]]

![[assets/2606.20002_figure.png|800]]

- **arXiv**: [2606.20002](https://arxiv.org/abs/2606.20002)
- **PDF**: https://arxiv.org/pdf/2606.20002
- **详细分析**: [[20_Research/Papers/大模型/Connect_the_Dots_Training_LLMs_for_Long-Lifecycle_Agents_with_Cross-Domain_Generalization_Via_Reinforcement_Learning|Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning]]
- **作者**: Yanxi Chen, Weijie Shi, Yuexiang Xie, Boyi Hu, Yaliang Li, Bolin Ding, Jingren Zhou
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.87（加权：大模型 0.75，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LLM-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work presents a general framework for training large language models (LLMs) to "Connect the Dots" (CoD), a meta-capability required by long-lifecycle agents: as an LLM-based AI agent gets deployed in an environment, it solves a long sequence of tasks while continuously exploring the environment, learning from its own experiences, and iteratively self-updating its context about the environment, thereby achieving progressively better performance on future tasks conditioned on the updated context. Major components of the CoD framework include: (1) algorithm design and infrastructure for end-to-end reinforcement learning (RL) with long rollout sequences interleaving solve-task and update-context episodes; (2) tasks and environments for incentivizing and eliciting the targeted meta-capability in LLMs during training, as well as for faithfully measuring progress during evaluation. We present proof-of-concept implementations of the CoD framework, including a GRPO-style RL algorithm with fine-grained credit assignment, as well as tasks and environments tailored to the targeted meta-capability (rather than domain-specific LLM capabilities or standard task-by-task RL). Empirical results validate the efficacy of end-to-end RL training in the CoD setting, and demonstrate the potential for out-of-distribution generalization -- within the training domains, across different domains, and from CoD to Ralph-loop settings -- of the elicited meta-capability. Our investigation of CoD connects several lines of prior works, and opens up new opportunities for advancing LLMs and AI agents. To facilitate further research and applications, we release our implementations at \url{https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod/examples/research_cod}.

</details>

---

### [[20_Research/Papers/具身智能/Tri-Info_Generalizable,_Interpretable_Failure_Prediction_for_VLA_Models_via_Information_Theory|Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory]]

![[assets/2606.19998_figure.png|800]]

- **arXiv**: [2606.19998](https://arxiv.org/abs/2606.19998)
- **PDF**: https://arxiv.org/pdf/2606.19998
- **详细分析**: [[20_Research/Papers/具身智能/Tri-Info_Generalizable,_Interpretable_Failure_Prediction_for_VLA_Models_via_Information_Theory|Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory]]
- **作者**: Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang, Zhengyang Hu, Yanchao Yang
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential. We observe that successful and failed rollouts carry systematically different information-theoretic signatures. Building on this, we formalize VLA control as a closed-loop information pipeline and derive the Triple Information-theoretic (Tri-Info) signals that capture whether actions remain diverse, temporally consistent, and coupled to state transitions. Across six VLA models and three benchmark environments, Tri-Info matches the strongest baselines in-domain. Moreover, Tri-Info transfers across architectures, environments, and the sim-to-real gap without retraining, reaching 83\% accuracy on real-world tasks where prior detectors collapse to chance. This establishes Tri-Info as a simple yet powerful method that not only detects failures with strong cross-domain generalization, but also delivers interpretable diagnostics of the underlying failure modes.

</details>

---

### [[20_Research/Papers/具身智能/Reward_as_An_Agent_for_Embodied_World_Models|Reward as An Agent for Embodied World Models]]

![[assets/2606.19990_figure.png|800]]

- **arXiv**: [2606.19990](https://arxiv.org/abs/2606.19990)
- **PDF**: https://arxiv.org/pdf/2606.19990
- **详细分析**: [[20_Research/Papers/具身智能/Reward_as_An_Agent_for_Embodied_World_Models|Reward as An Agent for Embodied World Models]]
- **作者**: Pu Li, Zhigang Lin, Qiang Wu, Yongxuan Lv, Fei Wang, Shan You
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.4，世界模型 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Reward as An Agent for Embodied World Models》归入 具身智能、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TaskEval, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While RL has become a promising tool for refining world models, existing methods largely rely on conservative rollouts near the training distribution, limiting exploration, behavioral diversity, and richer dynamic discovery. In this work, we challenge this conservative paradigm. We argue that the core limitation is not exploration itself, but the lack of reliable verification strategies to support broader exploration. Without reliable verification, expanded exploration becomes highly susceptible to reward hacking, where policies exploit imperfect rewards without achieving genuine improvement. To evaluate this motivation, we instantiate our method in embodied world models, where physical plausibility, and task completion provide a rigorous testbed for scalable RL under complex dynamics. On the verification side, we introduce Reward as an Agent, an agentic reward framework that actively evaluates generated behaviors to provide robust reward signals and mitigate reward hacking under distribution shifts. On the exploration side, we introduce Dynamic-Aware Rollout Diversification through DynDiff-GRPO, which explicitly expands action-space exploration to diversify trajectories, broaden state-action coverage, and encourage richer embodied behaviors beyond conservative rollout regimes. By unifying Reward as an Agent with DynDiff-GRPO, we enable RL on a more reliable reward foundation with substantially diversified sampling, effectively mitigating reward hacking while yielding significant accuracy gains across multiple open-source world models, thereby demonstrating that broader exploration can scale successfully when grounded in robust verification.

</details>

---

### [[20_Research/Papers/具身智能/ENPIRE_Agentic_Robot_Policy_Self-Improvement_in_the_Real_World|ENPIRE: Agentic Robot Policy Self-Improvement in the Real World]]

![[assets/2606.19980_figure.png|800]]

- **arXiv**: [2606.19980](https://arxiv.org/abs/2606.19980)
- **PDF**: https://arxiv.org/pdf/2606.19980
- **详细分析**: [[20_Research/Papers/具身智能/ENPIRE_Agentic_Robot_Policy_Self-Improvement_in_the_Real_World|ENPIRE: Agentic Robot Policy Self-Improvement in the Real World]]
- **作者**: Wenli Xiao, Jia Xie, Tonghe Zhang, Haotian Lin, Letian "Max" Fu, Haoru Xue, Jalen Lu, Yi Yang, Cunxi Dai, Zi Wang, Jimmy Wu, Guanzhi Wang...
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.2，机器人 1.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ENPIRE: Agentic Robot Policy Self-Improvement in the Real World》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined in digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable feedback loop for real-world policy improvement: reset the scene, execute a policy, verify the outcome, and refine the next iteration. To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with one or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes. This closed-loop system transforms real-world manipulation learning into a controllable optimization procedure, minimizing human effort while allowing fair ablations across training recipe and agent variants. Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we dispatch an agent team on a robot fleet. Our results suggest a practical and scalable path toward deploying coding agents to autonomously advancing robotics in the physical world.

</details>

---

### [[20_Research/Papers/具身智能/Advancing_DialNav_through_Automatic_Embodied_Dialog_Augmentation|Advancing DialNav through Automatic Embodied Dialog Augmentation]]

![[assets/2606.19948_figure.png|800]]

- **arXiv**: [2606.19948](https://arxiv.org/abs/2606.19948)
- **PDF**: https://arxiv.org/pdf/2606.19948
- **详细分析**: [[20_Research/Papers/具身智能/Advancing_DialNav_through_Automatic_Embodied_Dialog_Augmentation|Advancing DialNav through Automatic Embodied Dialog Augmentation]]
- **作者**: Leekyeung Han, Sangwon Jung, Hyunji Min, Jinseong Jeong, Minyoung Kim, Paul Hongsuck Seo
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Advancing DialNav through Automatic Embodied Dialog Augmentation》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For embodied agents capable of physical interaction, the capability to create and understand dialog is crucial to ensure both safety and effectiveness. While DialNav~\cite{han2025dialnav} provides a framework for holistic evaluation of the dialog--execution loop in photorealistic indoor navigation, its performance remains limited by a critical scarcity of training data (2K episodes). To address this, we propose an automatic generation pipeline, and construct the \textbf{RAINbow} dataset, a large-scale training dataset with 238K episodes for DialNav. Our pipeline converts existing VLN datasets into multi-turn dialog and creates cost-efficient and high-quality dataset. Then, we introduce two additional complementary advances to unlock the data's full potential: (1) Dual-Strategy Training, a navigation training scheme to align the navigation training with the dynamic dialog-navigation loop, and (2) a localization model that leverages VLN knowledge. By combining these complementary solutions, our model substantially outperforms the baseline in success rate on both \textbf{Val Seen} (58.24, \textbf{+89\%}) and \textbf{Val Unseen} (29.05, \textbf{+100\%}) splits, establishing a new state of the art.

</details>

---

### [[20_Research/Papers/机器人/PhysDrift_Bridging_the_Embodiment_Gap_in_Humanoid_Co-Speech_Motion_Generation|PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation]]

![[assets/2606.19935_figure.jpg|800]]

- **arXiv**: [2606.19935](https://arxiv.org/abs/2606.19935)
- **PDF**: https://arxiv.org/pdf/2606.19935
- **详细分析**: [[20_Research/Papers/机器人/PhysDrift_Bridging_the_Embodiment_Gap_in_Humanoid_Co-Speech_Motion_Generation|PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation]]
- **作者**: Zhangzhao Liang, Xiaofen Xing, Mingyue Yang, Wenlve Zhou, Xiangmin Xu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.2，机器人 1）
- **关联关键词**: Robotics

#### 研究背景与动机

《PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots require co-speech motions that are not only expressive and speech-aligned, but also physically executable under embodiment constraints. Existing co-speech generation pipelines are predominantly human-centric: motions are first generated in human-body representations such as SMPL-X and subsequently retargeted to humanoid robots. In this work, we identify a fundamental embodiment gap in this paradigm, where the mismatch between human motion manifolds and humanoid embodiment constraints disrupts embodiment consistency during motion transfer and physical execution. Through extensive analysis, we show that although retargeting can preserve coarse motion semantics, it significantly compresses motion diversity and weakens prosody-motion synchronization, limiting expressive humanoid behaviors. To address this problem, we first propose IK-EER, a prosody-preserving humanoid motion curation framework that jointly optimizes kinematic feasibility and speech-motion temporal alignment during retargeting. Building upon the curated robot-native motion dataset, we further introduce PhysDrift, an embodiment-aware co-speech motion generation framework that directly predicts executable humanoid joint trajectories from speech without relying on intermediate human-body representations. Unlike conventional human-centric pipelines, PhysDrift maintains embodiment consistency throughout both training and inference while incorporating physical regularization to stabilize robot motion dynamics. Extensive experiments and real-world humanoid deployment demonstrate that embodiment-aware robot-native generation substantially improves speech-motion alignment, physical plausibility, motion smoothness, inference efficiency, and real-time interaction capability.

</details>

---

### [[20_Research/Papers/具身智能/Co-policy_Responsive_Human-Robot_Co-Creation_for_Musical_Performances|Co-policy: Responsive Human-Robot Co-Creation for Musical Performances]]

![[assets/2606.19914_figure.png|800]]

- **arXiv**: [2606.19914](https://arxiv.org/abs/2606.19914)
- **PDF**: https://arxiv.org/pdf/2606.19914
- **详细分析**: [[20_Research/Papers/具身智能/Co-policy_Responsive_Human-Robot_Co-Creation_for_Musical_Performances|Co-policy: Responsive Human-Robot Co-Creation for Musical Performances]]
- **作者**: Xuetao Li, Wenke Huang, Mang Ye, Zijian Liu, Jinhua Xie, Jifeng Xuan, Miao Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Co-policy: Responsive Human-Robot Co-Creation for Musical Performances》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DenseNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Art has long stood as a pivotal expression of human creativity. Embodied artificial intelligence offers a route for generative models to participate in that creativity through physical action rather than disembodied digital content. In robotic music co-creation, it is challenging to connect semantic musical understanding with real-time and physically executable performance. We present Co-policy, a framework for human-robot musical co-creation that separates semantic intent grounding, constrained musical variation, and visuomotor execution. To ground musical semantics, Co-policy uses pre-inference semantic anchors and a fine-tuned Qwen-vl planner (F-Qwen) to transform speech, live musical seeds, and visual observations into structured co-creation plans. To support low-latency execution, Co-policy introduces a Gaussian-Mixture Visuomotor Policy (GMP), implemented as a conditional mixture-density policy that maps target notes and visual context to multimodal robot actions in a single forward pass. Unlike robotic playback systems that merely reproduce user-specified notes, Co-policy generates complementary musical responses under both musical and physical constraints. Real-robot chime experiments, ablations, and expert evaluation show improved intent alignment, execution accuracy, and response frequency over diffusion-policy and ablated baselines, supporting physically grounded action generation as a key requirement for embodied human-AI co-creation.

</details>

---

### [[20_Research/Papers/大模型/Multi-Agent_Transactive_Memory|Multi-Agent Transactive Memory]]

![[assets/2606.19911_figure.png|800]]

- **arXiv**: [2606.19911](https://arxiv.org/abs/2606.19911)
- **PDF**: https://arxiv.org/pdf/2606.19911
- **详细分析**: [[20_Research/Papers/大模型/Multi-Agent_Transactive_Memory|Multi-Agent Transactive Memory]]
- **作者**: To Eun Kim, Xuhong He, Dishank Jain, Ambuj Agrawal, Negar Arabzadeh, Fernando Diaz
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Multi-Agent Transactive Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The decentralized deployment of LLM agents with diverse capabilities across diverse tasks motivates infrastructure for knowledge sharing across heterogeneous agent populations. Just as search engines index human-generated artifacts to support human problem solving, retrieval systems can organize agent-generated artifacts for reuse across agent populations. We extend retrieval-augmented generation - which demonstrates the value of human-authored artifacts to individual agents - to retrieval of agent-generated artifacts supporting a population of agents. In particular, agent trajectories encode reusable procedural knowledge, yet these artifacts are typically discarded after a single use or retained only by the producing agent, forcing newly instantiated agents to repeatedly rediscover existing solutions. We propose Multi-Agent Transactive Memory (MATM), a framework for population-level storage and retrieval of agent-generated trajectories, where producer agents contribute trajectories to a shared repository and consumer agents retrieve them to improve task execution. We focus on interactive environments (ALFWorld and WebArena), where trajectories are long and encode especially rich procedural structure. Our experiments demonstrate that retrieving trajectories from MATM improves downstream task performance and reduces interaction steps without coordination or joint training. These results position MATM as a design pattern for population-level experience sharing in open agent ecosystems.

</details>

---

### [[20_Research/Papers/强化学习/MetaResearcher_Scaling_Deep_Research_via_Self-Reflective_Reinforcement_Learning_in_Adversarial_Virtual_Environments|MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments]]

![[assets/2606.19893_figure.png|800]]

- **arXiv**: [2606.19893](https://arxiv.org/abs/2606.19893)
- **PDF**: https://arxiv.org/pdf/2606.19893
- **详细分析**: [[20_Research/Papers/强化学习/MetaResearcher_Scaling_Deep_Research_via_Self-Reflective_Reinforcement_Learning_in_Adversarial_Virtual_Environments|MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments]]
- **作者**: Wei Yu, Suxing Liu, Minjie Yu, Jiahao Wang, Zhijian Zheng, Haocheng Deng, Bing Li
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《MetaResearcher: Scaling Deep Research via Self-Reflective Reinforcement Learning in Adversarial Virtual Environments》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ERL, HotpotQA, HumanEval, ICRL, MedMisBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep research agents have demonstrated remarkable capabilities in autonomous information gathering and synthesis, yet their training remains constrained by the static nature of simulated environments, the limits of fact-retrieval-only task designs, and the inefficiency of outcome-based reinforcement learning. In this work, we propose MetaResearcher, a novel framework that scales deep research agent training across four synergistic dimensions. First, we introduce an Evolving Virtual World that injects temporal dynamics and adversarial misinformation into the training environment, forcing agents to develop source credibility assessment and temporal conflict resolution skills. Second, we design Discovery-Oriented Tasks -- including hypothesis generation and contradiction resolution -- that transcend simple fact retrieval and push agents toward genuine research behaviors. Third, we propose a Self-Reflective Meta-Reward mechanism within the GRPO framework that jointly optimizes for answer correctness, search path efficiency, reflection depth, and tool call diversity, directly addressing the repetitive action loop problem observed in prior work. Fourth, we introduce a Heterogeneous Multi-Agent Swarm architecture comprising specialized Scout, Filter, and Synthesizer models that learn collaborative research strategies through coordinated reinforcement learning. Built upon the LiteResearcher infrastructure, MetaResearcher requires zero marginal API cost for training while targeting substantial improvements in both benchmark performance (GAIA, Xbench-DS) and epistemic robustness under adversarial conditions. We present the complete framework design, training methodology, and planned experimental validation.

</details>

---

### [[20_Research/Papers/强化学习/Uncertainty-Aware_Reward_Modeling_for_Stable_RLHF|Uncertainty-Aware Reward Modeling for Stable RLHF]]

![[assets/2606.19818_figure.png|800]]

- **arXiv**: [2606.19818](https://arxiv.org/abs/2606.19818)
- **PDF**: https://arxiv.org/pdf/2606.19818
- **详细分析**: [[20_Research/Papers/强化学习/Uncertainty-Aware_Reward_Modeling_for_Stable_RLHF|Uncertainty-Aware Reward Modeling for Stable RLHF]]
- **作者**: Licheng Pan, Haocheng Yang, Haoxuan Li, Yichen Sun, Yunsheng Lu, Shijian Wang, Lei Shen, Yuan Lu, Zhixuan Chu, Hao Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Uncertainty-Aware Reward Modeling for Stable RLHF》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from human feedback (RLHF) aligns large language models by training reward models on preference data and optimizing policies to maximize predicted rewards. However, this pipeline faces two fundamental challenges: (1) reward models cannot signal when their predictions are unreliable, since they usually act as deterministic point estimators; and (2) modern group-based policy optimization can amplify unreliable reward signals, as exemplified by GRPO's uniform treatment of rewards during advantage computation. As policies explore increasingly diverse responses, these two limitations create a critical vulnerability: unreliable reward estimates may be granted disproportionate influence, triggering severe reward hacking. We propose Uncertainty-Aware Reward Modeling (UARM), which equips reward models with calibrated uncertainty via quantile-based conformal prediction and reweights GRPO advantages through heteroscedastic variance decomposition. Experiments across HelpSteer, UltraFeedback, and PKU-SafeRLHF demonstrate that UARM significantly improves reward model calibration, reduces reward hacking, and enhances downstream alignment quality compared to standard GRPO and uncertainty-agnostic baselines.

</details>

---

### [[20_Research/Papers/具身智能/Data_Standards_for_Humanoid_Robotics_The_Missing_Infrastructure_for_Physical_AI|Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI]]

![[assets/2606.19769_figure.png|800]]

- **arXiv**: [2606.19769](https://arxiv.org/abs/2606.19769)
- **PDF**: https://arxiv.org/pdf/2606.19769
- **详细分析**: [[20_Research/Papers/具身智能/Data_Standards_for_Humanoid_Robotics_The_Missing_Infrastructure_for_Physical_AI|Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI]]
- **作者**: Shaoshan Liu, Xiugong Qin, Xuan Wu, Xuan Xia, Ning Ding, Jialu Liu, Jie Tang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.1（加权：具身智能 2.1，大模型 0.1，机器人 1.9）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Data Standards for Humanoid Robotics: The Missing Infrastructure for Physical AI》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The scalability of humanoid robots will depend not only on models and hardware, but also on whether physical experience can accumulate across robots, tasks, organizations, and time. Drawing on the authors' work in developing ISO/WD 26264-1, Humanoid robot datasets -- Part 1: General requirements, within ISO/TC 299/WG 16, this article argues that data standards are becoming foundational infrastructure for Physical AI. We develop three insights. First, humanoid robot data is embodied interaction data, not a collection of isolated digital samples; a useful dataset must preserve the relationship among robot body, action, task, scene, execution trace, and outcome. Second, its value depends on physical coherence: multimodal streams are reusable only when timing, coordinate frames, calibration, kinematics, units, and synchronization assumptions remain inspectable. Third, the main bottleneck is not only data scarcity, but non-cumulative data caused by high collection costs, data silos, and inconsistent evaluation. We argue that humanoid robot data standards address these bottlenecks by making embodied experience interpretable, shareable, traceable, and reusable. A general standard should provide horizontal infrastructure for lifecycle management, metadata, provenance, quality, versioning, and traceability, while capability-specific parts should define domain grammar for manipulation, locomotion, human-robot interaction, cognition, and future humanoid capabilities. As AI moves from screens into bodies, data standards must evolve from organizing digital information to structuring physical interaction.

</details>

---

### [[20_Research/Papers/具身智能/Temporal_Self-Imitation_Learning|Temporal Self-Imitation Learning]]

![[assets/2606.19752_figure.png|800]]

- **arXiv**: [2606.19752](https://arxiv.org/abs/2606.19752)
- **PDF**: https://arxiv.org/pdf/2606.19752
- **详细分析**: [[20_Research/Papers/具身智能/Temporal_Self-Imitation_Learning|Temporal Self-Imitation Learning]]
- **作者**: Yinsen Jia, Boyuan Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Temporal Self-Imitation Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot manipulation policies trained with reward shaping can still exploit dense rewards through inefficient interaction, while rare efficient behaviors may be forgotten during training. We argue that temporal efficiency itself provides a powerful and underutilized source of self-supervision for reinforcement learning. We introduce Temporal Self-Imitation Learning (TSIL), a reinforcement learning framework that mines temporally efficient successful trajectories generated during learning and converts them into reusable supervision for future policy improvement. TSIL progressively refines learning using configuration-conditioned adaptive temporal targets derived from fast successful trajectories, while preserving and replaying efficient behaviors through efficiency-weighted self-imitation learning. Across 15 distinct long-horizon manipulation tasks, TSIL consistently improves learning efficiency, task-completion efficiency, revisitation of fast successful behaviors, and robustness to unstable training conditions. More broadly, our results suggest that the temporal structure of successful behavior itself provides a scalable self-supervisory signal for reinforcement learning beyond manually engineered reward shaping alone.

</details>

---

### [[20_Research/Papers/强化学习/VOiLA_Vectorized_Online_Planning_with_Learned_Diffusion_Model_for_POMDP_Agents|VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents]]

![[assets/2606.19729_figure.png|800]]

- **arXiv**: [2606.19729](https://arxiv.org/abs/2606.19729)
- **PDF**: https://arxiv.org/pdf/2606.19729
- **详细分析**: [[20_Research/Papers/强化学习/VOiLA_Vectorized_Online_Planning_with_Learned_Diffusion_Model_for_POMDP_Agents|VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents]]
- **作者**: Marcus Hoerger, Rishikesh Joshi, Rahul Shome, Ian Manchester, Hanna Kurniawati
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，强化学习 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《VOiLA: Vectorized Online Planning with Learned Diffusion Model for POMDP Agents》归入 强化学习、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning under uncertainty is an essential capability for autonomous robots. The Partially Observable Markov Decision Process (POMDP) provides a powerful framework for such a capability. Although POMDP-based planning has advanced significantly, its application to real-world problems is often limited by the difficulty of obtaining faithful POMDP models. We present Vectorized Online planning wIth Learned diffusion model for POMDP Agents (VOiLA), a framework that learns task-agnostic POMDP models for online planning under uncertainty. VOiLA learns transition and observation samplers using conditional diffusion models and learns observation-likelihood models for particle-based belief updates. To enable efficient online planning, the diffusion samplers are distilled into compact feedforward generators and integrated with Vectorized Online POMDP Planner (VOPP), an online POMDP planner designed to leverage GPU parallelization. Experimental results indicate the distillation strategy reduces sampling cost by up to nearly three orders of magnitude, making learned generative POMDP models practical for online planning. Evaluation of VOiLA on three benchmark problems indicate that VOiLA achieves equal or better performance than Recurrent Soft Actor Critic while using less than 10% training data, and generalizes much better to unseen environment configurations. Physical robot evaluation indicates VOiLA uses the models learned using only simulated data and generates a policy that successfully accomplish the task in 10 of 10 runs.

</details>

---

### [[20_Research/Papers/具身智能/Bidirectional_Tutoring_for_Developmental_Motor_Learning_in_Robots_Co-Developed_Interaction_Dynamics_Support_Stable_Learning|Bidirectional Tutoring for Developmental Motor Learning in Robots: Co-Developed Interaction Dynamics Support Stable Learning]]

![[assets/2606.19728_figure.png|800]]

- **arXiv**: [2606.19728](https://arxiv.org/abs/2606.19728)
- **PDF**: https://arxiv.org/pdf/2606.19728
- **详细分析**: [[20_Research/Papers/具身智能/Bidirectional_Tutoring_for_Developmental_Motor_Learning_in_Robots_Co-Developed_Interaction_Dynamics_Support_Stable_Learning|Bidirectional Tutoring for Developmental Motor Learning in Robots: Co-Developed Interaction Dynamics Support Stable Learning]]
- **作者**: Rui Fukushima, Jun Tani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Bidirectional Tutoring for Developmental Motor Learning in Robots: Co-Developed Interaction Dynamics Support Stable Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Infants are well known to develop their motor skills through dense interaction with caregivers. Although such social interaction is crucial for human development, motor-skill learning in robots is often treated as a unidirectional process in which robots passively receive demonstrations from tutors. This overlooks a key property of social interaction: it is inherently bidirectional, with tutor and learner dynamically adapting to each other. In such interactions, the robot's past experiences may function as prior constraints that shape the dynamics of their co-developed trajectories. We hypothesize that bidirectional tutoring allows such constraints to guide the formation of consistent behavioral patterns that preserve behavioral coherence and support generalization, whereas unidirectional interaction lacks such constraints and leads to broader, less consistent behavioral patterns. To examine this hypothesis, we conducted two experiments with a physical humanoid robot performing an object manipulation task: one involving human-robot interaction and another employing an AI tutor interacting with the real robot through an adaptive intervention mechanism designed to examine whether similar effects would emerge under more controlled conditions. We implement the developmental learning framework using a free-energy-principle-based neural network extended with generative replay, which supports stable sequence-by-sequence learning from single tutored episodes. Across both settings, bidirectional tutoring fostered consistent behaviors and stage-wise generalization, while the robot gradually required less tutor guidance. These results suggest that bidirectional tutoring, as an embodied and socially grounded approach, provides an effective scaffold for developmental motor learning in robots.

</details>

---

### [[20_Research/Papers/大模型/Library-Aware_Doubles_and_Iterative_Repair_for_Large_Language_Model-Generated_Unit_Tests_in_OpenSIL_Firmware|Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware]]

![[assets/2606.19725_figure.png|800]]

- **arXiv**: [2606.19725](https://arxiv.org/abs/2606.19725)
- **PDF**: https://arxiv.org/pdf/2606.19725
- **详细分析**: [[20_Research/Papers/大模型/Library-Aware_Doubles_and_Iterative_Repair_for_Large_Language_Model-Generated_Unit_Tests_in_OpenSIL_Firmware|Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware]]
- **作者**: Ma Toan Bach, Yuchi Zheng, Haingo Razafindranto, Tanvir Alam, Aric Leather, Ranveer Sandhu, Jitesh Arora
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Validating changes in low-level C firmware is expensive because unit tests (UTs) are fragile under strict build constraints, where missing headers, unresolved symbols, and dependency mismatches frequently prevent compilation and linking. This study introduces an automated UT authoring workflow for the Open-Source Silicon Initialization Library (openSIL) firmware codebase maintained by Advanced Micro Devices (AMD) that reduces manual effort through a large language model (LLM) guided multi-agent pipeline. The workflow combines automated generation of test scaffolds, library-aware creation or reuse of stubs, mocks, and fakes, and an iterative compile-dispatch repair loop driven by build logs and line-coverage feedback. We evaluate the approach using compilation success, repair iterations, dispatch success, and line coverage, with time, cost, and token usage as secondary measures. Across 76 functions under test, the workflow generated compilable UTs for 73 functions. In a configuration without line coverage guidance or retrieval augmentation, mean line coverage reached 73.9%. On a 48-function subset evaluated under both configurations, mean line coverage reached 98.8% with line-coverage guidance alone and reached 94.7% when combined with vector-database retrieval. Results show that automated generation-and-repair pipelines can substantially improve UT creation efficiency and coverage for constrained firmware environments while reducing manual debugging effort.

</details>

---

### [[20_Research/Papers/具身智能/CTS-MoE_Implicit_Terrain_Adaptation_via_Mixture-of-Experts_for_Perceptive_Locomotion|CTS-MoE: Implicit Terrain Adaptation via Mixture-of-Experts for Perceptive Locomotion]]

![[assets/2606.19633_figure.png|800]]

- **arXiv**: [2606.19633](https://arxiv.org/abs/2606.19633)
- **PDF**: https://arxiv.org/pdf/2606.19633
- **详细分析**: [[20_Research/Papers/具身智能/CTS-MoE_Implicit_Terrain_Adaptation_via_Mixture-of-Experts_for_Perceptive_Locomotion|CTS-MoE: Implicit Terrain Adaptation via Mixture-of-Experts for Perceptive Locomotion]]
- **作者**: Francisco Affonso, Matheus P. Angarola, Ana Luiza Mineiro, Aditya Potnis, Marcelo Becker, Girish Chowdhary
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.0（加权：具身智能 1.5，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CTS-MoE: Implicit Terrain Adaptation via Mixture-of-Experts for Perceptive Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perceptive legged locomotion over discontinuous terrain (e.g., stairs, gaps, and obstacles) requires adaptive behavior, as a single conservative gait cannot produce the anticipatory maneuvers needed for abrupt topology changes. Cast as multi-task reinforcement learning, this problem introduces a tension between sharing and separation. Tasks use a common locomotion base but have conflicting rewards, so a policy must share behavior while avoiding value interference. Prior work addresses only one side, with monolithic policies sacrificing specialization and hierarchical sub-policies sacrificing generalization across transitions and unseen terrain. We propose CTS-MoE, which combines a dense mixture-of-experts actor with perception-based gating to compose shared behaviors and a multi-critic with task-specific value heads to prevent interference. The model is trained end-to-end in a single-stage concurrent teacher-student setup that handles partial observability and avoids sequential distillation, with task labels used only during training. At deployment, routing depends solely on perception, allowing terrain adaptation without a high-level selector or terrain classifier. Experiments on a Unitree Go1 in simulation and on hardware across seen and unseen terrains show task-aware specialization, with lower tracking error and higher success rates than monolithic baselines. Project Website: https://cts-moe.github.io/ .

</details>

---

### [[20_Research/Papers/强化学习/Formal_Verification_of_Learned_Multi-Agent_Communication_Policies_via_Decision_Tree_Distillation|Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation]]

![[assets/2606.19632_figure.png|800]]

- **arXiv**: [2606.19632](https://arxiv.org/abs/2606.19632)
- **PDF**: https://arxiv.org/pdf/2606.19632
- **详细分析**: [[20_Research/Papers/强化学习/Formal_Verification_of_Learned_Multi-Agent_Communication_Policies_via_Decision_Tree_Distillation|Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation]]
- **作者**: Ahmad Farooq, Kamran Iqbal
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.5，强化学习 0.36，世界模型 0.16，机器人 0.9）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Formal Verification of Learned Multi-Agent Communication Policies via Decision Tree Distillation》归入 机器人、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CommNet, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reinforcement learning (MARL) enables agents to develop coordination strategies through emergent communication, but neural policies lack the formal safety guarantees required for safety-critical robotic deployment in drone swarms and autonomous vehicle fleets. We present the first end-to-end framework for safety verification of learned multi-agent communication policies through policy abstraction: neural policies are distilled into interpretable decision trees, then formally verified, with empirical validation confirming that verified safety properties transfer to original networks. Our four-stage pipeline consists of domain-specific feature extraction from agent observations, decision tree distillation achieving 97.9% +/- 1.2% fidelity to neural policies, automated translation to PRISM probabilistic model checker specifications with complete feature-to-state-variable correspondence, and compositional verification of Probabilistic Computation Tree Logic (PCTL) properties via pairwise decomposition with union-bound aggregation and empirical neighbor modeling. Evaluating Vector-Quantized Variational Information Bottleneck (VQ-VIB) policies for multi-drone coordination with 5-7 agents, we verify 18 temporal logic properties across safety, liveness, and cooperation, achieving 88.9% property satisfaction with all five safety thresholds satisfied (0.3% collision probability vs. 1% threshold). Monte Carlo validation of original neural policies confirms that verified safety properties transfer with &lt;=0.6 percentage-point deviation (95% CI). Discrete VQ-VIB messages provide +11.6 to +13.6 percentage-point fidelity advantages over continuous methods, enabling 3-4x faster verification. Our framework provides empirically validated safety verification for distilled policy abstractions, serving as a practical bridge between deep MARL and formal safety workflows for multi-robot deployment.

</details>

---

### [[20_Research/Papers/大模型/Uncertainty_Decomposition_for_Clarification_Seeking_in_LLM_Agents|Uncertainty Decomposition for Clarification Seeking in LLM Agents]]

![[assets/2606.19559_figure.png|800]]

- **arXiv**: [2606.19559](https://arxiv.org/abs/2606.19559)
- **PDF**: https://arxiv.org/pdf/2606.19559
- **详细分析**: [[20_Research/Papers/大模型/Uncertainty_Decomposition_for_Clarification_Seeking_in_LLM_Agents|Uncertainty Decomposition for Clarification Seeking in LLM Agents]]
- **作者**: Gregory Matsnev
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Uncertainty Decomposition for Clarification Seeking in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. Practical deployment constraints -- black-box APIs, interactive latency budgets, and the absence of labeled trajectories -- rule out logprob-based, multi-sampling, and training-based methods, leaving prompt-based estimation as the most viable family for surfacing such signals at deployment time. We answer this call with a simple prompt-based decomposition that separates action confidence from request uncertainty (u), enabling the agent to ask for clarification when the task specification is ambiguous. To evaluate it, we introduce two clarification-augmented benchmarks (WebShop-Clarification and ALFWorld-Clarification) in which 50% of tasks are deliberately underspecified, and systematically compare the proposed decomposition against ReAct+UE and Uncertainty-Aware Memory (UAM) across five LLM backbones (GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B, GPT-OSS-120B) on these variants together with the standard WebShop, ALFWorld, and REAL benchmarks for fault detection. Averaged across the five backbones, the proposed decomposition improves clarification F1 on ALFWorld-Clarification by 73% over ReAct+UE and by 36% over UAM, and leads clarification F1 on every backbone on WebShop-Clarification and on four of five backbones on ALFWorld-Clarification, indicating that the gains generalize beyond a single LLM.

</details>

---

### [[20_Research/Papers/大模型/PerceptionDLM_Parallel_Region_Perception_with_Multimodal_Diffusion_Language_Models|PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models]]

![[assets/2606.19534_figure.png|800]]

- **arXiv**: [2606.19534](https://arxiv.org/abs/2606.19534)
- **PDF**: https://arxiv.org/pdf/2606.19534
- **详细分析**: [[20_Research/Papers/大模型/PerceptionDLM_Parallel_Region_Perception_with_Multimodal_Diffusion_Language_Models|PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models]]
- **作者**: Yueyi Sun, Yuhao Wang, Jason Li, Ye Tian, Tao Zhang, Jacky Mai, Yihan Wang, Haochen Wang, Jinbin Bai, Ling Yang, Yunhai Tong
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DLC-Bench, ParaDLC-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have achieved remarkable progress in visual understanding tasks. However, most existing MLLMs rely on autoregressive generation, which limits their efficiency for perception tasks that require captioning multiple regions. In this work, we propose PerceptionDLM, a multimodal diffusion language model optimized for efficient parallel region perception. Built upon PerceptionDLM-Base, a strong foundational baseline that achieves state-of-the-art performance among open-source diffusion MLLMs, our architecture fully leverages the parallel decoding nature of DLMs. Specifically, we introduce efficient prompting and structured attention masking to enable simultaneous perception of multiple masked regions, allowing the model to generate region descriptions in parallel at both the sequence and token levels. This design significantly improves inference efficiency compared with existing approaches that process regions sequentially. To systematically evaluate the parallelism property of visual perception capability for DLMs, we construct a new Parallel Detailed Localized Captioning Benchmark (ParaDLC-Bench) by scaling the DLC-Bench to include multiple region masks per image, enabling joint evaluation of both caption quality and inference efficiency. Experiments demonstrate that PerceptionDLM maintains competitive performance in region captioning while achieving substantial speed improvements for multi-region perception tasks. Our results highlight the potential of multimodal diffusion language models for efficient, parallel visual perception. To the best of our knowledge, we are the first to achieve parallel region caption and perception by leveraging the advantages of diffusion language models. Code, models, and datasets are released.

</details>

---

### [[20_Research/Papers/大模型/Hidden_Anchors_in_Multi-Agent_LLM_Deliberation|Hidden Anchors in Multi-Agent LLM Deliberation]]

![[assets/2606.19494_figure.png|800]]

- **arXiv**: [2606.19494](https://arxiv.org/abs/2606.19494)
- **PDF**: https://arxiv.org/pdf/2606.19494
- **详细分析**: [[20_Research/Papers/大模型/Hidden_Anchors_in_Multi-Agent_LLM_Deliberation|Hidden Anchors in Multi-Agent LLM Deliberation]]
- **作者**: Apurba Pokharel, Ram Dantu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Hidden Anchors in Multi-Agent LLM Deliberation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ChatEval, OpinioNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM deliberation, where agents exchange and revise answers over several rounds, is increasingly used to improve reasoning and accuracy, yet how and why it works is rarely modelled. Such deliberation mirrors how humans reach decisions. As social animals we are pulled both by the group, the herd effect that classical opinion-dynamics models such as DeGroot and Friedkin--Johnsen capture, and by our own internal belief, which they do not. We model multi-agent deliberation as a closed-loop dynamical system in which each agent carries a hidden internal belief, its anchor, that continually pulls its opinion regardless of its neighbours. We show this anchor can be recovered from the deliberation alone, and that it explains a behaviour classical consensus rules forbid: an agent's confidence in the correct answer can climb past where any agent started, escaping the space (convexhull) formed by the initial beliefs. Checking whether the recovered anchor also predicts held-out runs (generalizes) gives a simple test for when a model is truly driven bysuch an anchor. Across three open-weight model families this is a spectrum, not all-or-nothing. All anchors' influence are about equally strongly, but they differ in where the anchor sits, and only when it sits far from the initial opinions does deliberation escape the hull and need the full closed-loop model.

</details>

---

### [[20_Research/Papers/强化学习/Can_In-Context_Learning_Support_Intrinsic_Curiosity|Can In-Context Learning Support Intrinsic Curiosity?]]

![[assets/2606.19476_figure.png|800]]

- **arXiv**: [2606.19476](https://arxiv.org/abs/2606.19476)
- **PDF**: https://arxiv.org/pdf/2606.19476
- **详细分析**: [[20_Research/Papers/强化学习/Can_In-Context_Learning_Support_Intrinsic_Curiosity|Can In-Context Learning Support Intrinsic Curiosity?]]
- **作者**: Eric Elmoznino, Sangnie Bhardwaj, Johannes von Oswald, Rajai Nasser, Blaise Agüera y Arcas, João Sacramento, Rif A. Saurous, Guillaume Lajoie
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.16，世界模型 0.56）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Can In-Context Learning Support Intrinsic Curiosity?》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective machine learning depends not only on how we model data, but also on what data we choose to collect. While large sequence models have revolutionized data modeling, the problem of automated data selection, or "intrinsic curiosity", remains a significant challenge. Classic approaches incentivize exploration by rewarding an agent based on its "learning progress", which measures how much a newly acquired observation improves a world model's predictive ability. However, evaluating these rewards traditionally requires expensive inner loops of gradient descent updates within each trajectory, rendering them computationally impractical at scale. In this work, we investigate whether the emergent in-context learning (ICL) capabilities of sequence models can eliminate this bottleneck by serving as immediate, update-free world models. Specifically, we evaluate whether an exploration policy can be trained to maximize learning progress, using solely the prediction errors and counterfactual context manipulations of an in-context learner. We first prove that in general Markov decision processes, this is in fact impossible in an unbiased way: the resulting intrinsic rewards either suffer from nuisance terms that bias their estimation of true learning progress, or they cannot be implemented using an in-context learner's prediction errors. Conversely, we prove a positive result for a broad subclass of non-temporal settings, encompassing active learning and Bayesian Experimental Design: here, ICL-derived rewards successfully bound and asymptotically converge to the true learning progress. We corroborate our theory with controlled experiments across continuous and symbolic environments, demonstrating that our ICL-driven framework successfully trains curious data-collection policies that explore optimally.

</details>

---

### [[20_Research/Papers/具身智能/Playful_Agentic_Robot_Learning|Playful Agentic Robot Learning]]

![[assets/2606.19419_figure.png|800]]

- **arXiv**: [2606.19419](https://arxiv.org/abs/2606.19419)
- **PDF**: https://arxiv.org/pdf/2606.19419
- **详细分析**: [[20_Research/Papers/具身智能/Playful_Agentic_Robot_Learning|Playful Agentic Robot Learning]]
- **作者**: Junyi Zhang, Jiaxin Ge, Hanjun Yoo, Letian Fu, Zihan Yang, Yaowei Liu, Raj Saravanan, Shaofeng Yin, Justin Yu, Dantong Niu, Zirui Wang, Roei Herzig...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.6，大模型 0.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Playful Agentic Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current agentic robot systems can write executable Code-as-Policy programs, observe feedback, and revise behavior across multiple attempts, but they remain largely task-driven: reusable skills are acquired only after explicit instructions. We study Playful Agentic Robot Learning, where an embodied coding agent uses self-directed play as a continual skill-learning stage before downstream tasks arrive. We introduce RATs, Robotics Agent Teams designed for play-time skill acquisition. During play, RATs proposes novel yet learnable exploratory tasks, plans and executes robot-code policies, verifies intermediate progress, diagnoses failures, retries with dense, step-level feedback, and distills successful executions into a persistent code skill library. At test time, the agent reuses relevant skills from this frozen library to help solve new tasks. Experiments in LIBERO-PRO and MolmoSpaces show that play-learned skills improve held-out downstream tasks over no-play and random-play baselines, with 20.6 and 17.0 percentage-point gains over CaP-Agent0 on LIBERO-PRO and MolmoSpaces, respectively. Moreover, the learned skills can be plugged into other inference-time Code-as-Policy agents by simply retrieving them into the context, improving RoboSuite and real-world transfer by 8.9 and 8.8 points, respectively, without finetuning the underlying model.

</details>

---

### [[20_Research/Papers/强化学习/Physical_Atari_A_Robust_and_Accessible_Platform_for_Real-time_Reinforcement_Learning_on_Robots|Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots]]

![[assets/2606.19357_figure.png|800]]

- **arXiv**: [2606.19357](https://arxiv.org/abs/2606.19357)
- **PDF**: https://arxiv.org/pdf/2606.19357
- **详细分析**: [[20_Research/Papers/强化学习/Physical_Atari_A_Robust_and_Accessible_Platform_for_Real-time_Reinforcement_Learning_on_Robots|Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots]]
- **作者**: Khurram Javed, Joseph Modayil, Gloria Kennickell, Richard S. Sutton, John Carmack
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots》归入 强化学习、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We built a robot called the Robotroller that actuates an Atari CX40+ controller and a device called the Atari Devbox that renders the game frame and the reward signal from the Arcade Learning Environment on a screen. The Robotroller and the Atari Devbox, together with an off-the-shelf camera and a desktop computer, constitute a system that can be used to study reinforcement learning algorithms in the physical world. We call the full system Physical Atari. In this paper, we detail the key decisions that make Physical Atari a robust and accessible platform. To make the system robust, we designed the Robotroller so that all movement is done through bearings, which reduces wear. Additionally, we wrote software that monitors the state of the servos at a high frequency and intervenes to limit stress. To make the system accessible, we used affordable off-the-shelf components and parts that can be manufactured using consumer 3D printers. Physical Atari can be built for under $1,000 and has been used for weeks of non-stop reinforcement learning experiments without any mechanical failures. We used it to validate that reinforcement learning algorithms can learn directly on robots and show that even small distribution shifts between learning and deployment can significantly degrade the performance of policies. Our results underscore the importance of on-device adaptation for strong performance on robots.

</details>

---

### [[20_Research/Papers/大模型/Detecting_Hallucinations_for_Large_Language_Model-based_Knowledge_Graph_Reasoning|Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning]]

![[assets/2606.19351_figure.png|800]]

- **arXiv**: [2606.19351](https://arxiv.org/abs/2606.19351)
- **PDF**: https://arxiv.org/pdf/2606.19351
- **详细分析**: [[20_Research/Papers/大模型/Detecting_Hallucinations_for_Large_Language_Model-based_Knowledge_Graph_Reasoning|Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning]]
- **作者**: Xinyan Zhu, Yaoqi Liu, Yue Gao, Huadong Ma, Cheng Yang, Chuan Shi
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, ComputerVision, Systems

#### 研究背景与动机

《Detecting Hallucinations for Large Language Model-based Knowledge Graph Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GrailQA, KBQA, MetaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge graph (KG) reasoning infers new knowledge from existing facts and is widely applied in question answering, recommendation, and decision support. With the rapid development of large language models (LLMs), LLM-based KG reasoning frameworks have become increasingly popular by leveraging retrieved KG information. However, hallucinations in LLMs remain a critical issue. Even when relevant KG knowledge is incorporated, models may still generate incorrect outputs, leading to misinformation and unreliable decisions. Existing hallucination detection methods either focus on LLM internal states or verify consistency with retrieved contexts, but both overlook the structural information in KGs, resulting in suboptimal performance. To address this gap, we propose LUCID, the first halLUcination deteCtIon method for LLM-based knowleDge graph reasoning frameworks. LUCID jointly leverages LLM attention scores, KG semantics, and structural information. Specifically, it extracts node and edge features from attention scores and semantic similarities, and integrates them with KG structure using a graph neural network. We also construct manually annotated benchmark datasets for evaluation. Experiments on nine datasets show that LUCID achieves state of the art performance compared to 15 baselines.

</details>

---

### [[20_Research/Papers/具身智能/Human_Universal_Grasping|Human Universal Grasping]]

![[assets/2606.17054_figure.jpg|800]]

- **arXiv**: [2606.17054](https://arxiv.org/abs/2606.17054)
- **PDF**: https://arxiv.org/pdf/2606.17054
- **详细分析**: [[20_Research/Papers/具身智能/Human_Universal_Grasping|Human Universal Grasping]]
- **作者**: Kevin Yuanbo Wu, Tianxing Zhou, Isaac Tu, Billy Yan, Irmak Guzey, David Fouhey, Dandan Shan, Lerrel Pinto
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Human Universal Grasping》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DexGraspNet, HUG-Bench, Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans can grasp objects effortlessly, whereas multi-fingered robots are far from this level of generality. We argue that the most natural source of robot grasping data is from humans, who pick up thousands of objects every day. We present HUG, a flow-matching model that generates diverse human grasps for any user-specified object in a single RGB-D image captured from a stereo camera. Using smart glasses, we first collect 1M-HUGs, an egocentric dataset of human grasps spanning 1M frames (27.8 hrs) and 6,707 object instances across 41 buildings. Next, to model the distribution of natural human grasps, our novel flow-matching model fuses RGB and depth observations to output a grasp parameterized by wrist translation, wrist rotation, and MANO hand pose. Predicted grasps can be retargeted to various robot hands, enabling zero-shot grasping in everyday scenes. To standardize evaluation, we build a new simulated benchmark, HUG-Bench, of 90 unseen objects from five geometric categories and various sizes, with metric-scale 3D meshes. We evaluate HUG in the real world on the 30-object test set of HUG-Bench across multiple stereo cameras, robot embodiments, and household environments. HUG outperforms the state-of-the-art grasping baselines by +23% and +34% on our challenging object set. Code, data, benchmark, checkpoints, and an interactive demo are released on our website: https://grasping.io/

</details>

---

### [[20_Research/Papers/大模型/The_Saturation_Trap_and_the_Subjectivity_of_Intervention_Timing_Why_Affect-Based_Triggers_and_LLM_Judges_Fail_to_Time_Interventions_on_Auton|The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents]]

![[assets/2606.04296_first_page.png|800]]

- **arXiv**: [2606.04296](https://arxiv.org/abs/2606.04296)
- **PDF**: https://arxiv.org/pdf/2606.04296
- **详细分析**: [[20_Research/Papers/大模型/The_Saturation_Trap_and_the_Subjectivity_of_Intervention_Timing_Why_Affect-Based_Triggers_and_LLM_Judges_Fail_to_Time_Interventions_on_Auton|The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents]]
- **作者**: Manvendra Modgil
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As autonomous AI agents move from conversational systems to long-horizon software execution, runtime safety layers that decide when to interrupt an agent have become essential. We study this timing problem using a continuous 18-dimensional affective-dynamics engine (HEART) as a diagnostic probe, evaluating four intervention trigger families - absolute state thresholds, composite state-action patterns, regex reasoning-feature extraction, and zero-shot LLM-as-judge - against human-annotated intervention points on SWE-bench-Verified debugging traces. We report three findings. First, a State Saturation Trap: agents show no recovery signal under sustained difficulty, so modeled frustration quickly crosses the threshold and stays at its maximum, converting threshold-on-state triggers from moment detectors into near-constant indicators that fire on 39-83% of actions across five trajectories. Second, a capability-and-context floor for LLM judges: a small model (gpt-5.4-mini) never fires, while frontier and cross-vendor models escape the zero-firing floor only with full-trajectory context, and even then reach only F1 0.17-0.40 at up to 90x the cost. Third, and most importantly, the supervised target is not reproducible among humans: three trained annotators using one rubric on a 56-action trajectory agree on where to intervene only slightly above chance (location Krippendorff's alpha = +0.047; best pairwise Cohen's kappa = +0.349) and not at all on intervention type (pause degenerate; clarify below chance; reflect only alpha = +0.226). We conclude that intervention timing is a low-reliability construct, making single-annotator F1 an unsuitable optimization target. Our contribution is the joint mapping of this problem across human inter-rater reliability, four detector architectures, a cross-model LLM-judge sweep, and a reproduced saturation effect, rather than any single detector's accuracy.

</details>

---
