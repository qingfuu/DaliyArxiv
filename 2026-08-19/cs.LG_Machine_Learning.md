# cs.LG | Machine Learning | 2026-08-19

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/大模型/Debate_Training_Reduces_Reward_Hacking_in_RLAIF|Debate Training Reduces Reward Hacking in RLAIF]]

![[assets/2608.17776_figure.png|800]]

- **arXiv**: [2608.17776](https://arxiv.org/abs/2608.17776)
- **PDF**: https://arxiv.org/pdf/2608.17776
- **详细分析**: [[20_Research/Papers/大模型/Debate_Training_Reduces_Reward_Hacking_in_RLAIF|Debate Training Reduces Reward Hacking in RLAIF]]
- **作者**: Zachary Kenton, Lili Janzer, Rory Greig, Tian Huey Teh, Kirill Tyshchuk, Jonah Brown-Cohen, Harri Edwards, Senthooran Rajamanoharan, Noah Y. Siegel, Natasha Jaques, Rohin Shah
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Debate Training Reduces Reward Hacking in RLAIF》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We demonstrate that RL finetuning an LLM using debate, a two-player adversarial game between a generator and a critic adjudicated by a weaker LLM judge, reduces reward hacking compared to a reinforcement learning from AI feedback (RLAIF) baseline. Reward hacking is a central obstacle in RLAIF: as training progresses, the policy learns to exploit systematic errors in its AI judge, degrading task performance, a problem that worsens precisely when the judge is weaker than the policy, the setting most relevant to overseeing increasingly capable AI systems. We study mathematics tasks, where final-answer correctness is verifiable, allowing us to measure reward hacking dynamics. We train a Gemini~2.5 Flash-class policy with a frozen, weaker Gemini~2.5 Flash Lite judge, comparing a single-player RLAIF baseline against debate. While the baseline quickly hacks the judge, debate maintains judge performance throughout training, leading to a higher peak validation accuracy (45\% performance gap recovered) that persists through many RL steps. Additional experiments show that: 1) further weakening the judge leads to faster hacking, but this can be compensated by adding an additional debate round; 2) debate incentives override prompted misalignment; 3) RL using an LLM judge has a smaller train/validation reward gap than RL from verifiable rewards; 4) learning to critique to convince the judge using ground truth labels is possible but slow. Taken together, our results are a positive update on the feasibility of debate, while highlighting that balancing multi-agent training is critical: without player constraints, adversarial training risks defaulting to critic judge-hacking. We show that critique word limits (effective up to 150 words) successfully balance the game and avoid judge hacking, though this introduces a trade-off by restricting critic expressive clarity.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_RL_Explainability_Methods_by_How_Much_They_Help_Fix_Bugs_in_Agents|Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents]]

![[assets/2608.17524_first_page.png|800]]

- **arXiv**: [2608.17524](https://arxiv.org/abs/2608.17524)
- **PDF**: https://arxiv.org/pdf/2608.17524
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_RL_Explainability_Methods_by_How_Much_They_Help_Fix_Bugs_in_Agents|Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents]]
- **作者**: Ram Rachum, Yotam Amitai, Bálint Gyevnár, Reuth Mirsky, Cameron Allen
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Evaluating RL Explainability Methods by How Much They Help Fix Bugs in Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AuditBench, Debug-Gym, EvalXRL, LangXRL, RE-Bench, XRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This preliminary paper outlines a planned evaluation benchmark for Explainable Reinforcement Learning (XRL) methods. Current evaluations rely on functionally-grounded metrics like faithfulness and compactness, and on human-grounded proxies like subjective ratings or prediction accuracy. We suggest evaluating XRL methods by how effectively their generated explanations help to diagnose and fix malfunctioning reinforcement learning (RL) agents. We propose EvalXRL, a benchmark in which a Large Language Model (LLM) coding agent uses different XRL methods to diagnose a held-out malfunction in an RL agent, and then repair it. Our proposed benchmark iterates across (environment $\times$ malfunction $\times$ XRL method) tuples and uses the reward signal of the RL agents to form a final score for each XRL method. The coding agent may use the method interactively: invoke the XRL method, process its output, form new hypotheses on what is broken, and invoke the method again with parameters adjusted for testing these hypotheses. This closed-loop structure may be described as a simplified version of the scientific method. Some XRL methods provide self-evaluations that follow this pattern; we propose the first head-to-head comparison of multiple XRL methods in closed-loop usage.

</details>

---

### [[20_Research/Papers/具身智能/Prism-GRPO_Faster_VLA_Policy_Optimization_via_Splitting_Same-outcome_Groups|Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups]]

![[assets/2608.17423_figure.png|800]]

- **arXiv**: [2608.17423](https://arxiv.org/abs/2608.17423)
- **PDF**: https://arxiv.org/pdf/2608.17423
- **详细分析**: [[20_Research/Papers/具身智能/Prism-GRPO_Faster_VLA_Policy_Optimization_via_Splitting_Same-outcome_Groups|Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups]]
- **作者**: Zeyun Deng, Yuzhe Lu, Yawei Wang, Linbo Liu, Qing Ping, Han Ding, Guande Wu, Panpan Xu, Jun Huan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 3.72（加权：具身智能 1.8，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, SimpleVLA-RL, StARe-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

GRPO is increasingly used for reinforcement learning of vision-language-action (VLA) policies because, unlike PPO, it does not require training a critic. This simplification comes with a sampling cost: group-relative advantages require multiple rollouts from each scene. Under binary success rewards, groups whose rollouts all succeed or all fail have zero advantage and are discarded by dynamic sampling. These groups are especially common early in training, when most rollouts fail, wasting much of the expensive robotic rollout budget. We introduce Prism-GRPO, which augments binary outcome reward with a weighted trajectory-level execution-quality score. By splitting same-outcome groups into a quality spectrum, Prism-GRPO recovers training signal while ensuring that every success still outranks every failure. Quality scores can be derived from simulator contacts, executed actions, or visual observations, avoiding task-specific progress rewards. We prove that Prism-GRPO never increases the probability that a sampled group is discarded for having zero advantages, and derive a gradient-alignment condition under which its combined update remains a local ascent direction for task success. Across four RoboTwin tasks spanning different horizons and coordination patterns, Prism-GRPO improves success and quality at matched rollout budgets and reaches target success rates with up to 56% fewer rollouts. It also suppresses a reward-hacking shortcut, with the cleaner behavior transferring under direct deployment to a real robot. Through ablations, we show consistent gains across contact-, smoothness-, and VLM-derived quality signals.

</details>

---

### [[20_Research/Papers/强化学习/GUPO_Gradient_Uncertainty-aware_Policy_Optimization_for_Post-Training_Large_Language_Models|GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models]]

![[assets/2608.17411_figure.png|800]]

- **arXiv**: [2608.17411](https://arxiv.org/abs/2608.17411)
- **PDF**: https://arxiv.org/pdf/2608.17411
- **详细分析**: [[20_Research/Papers/强化学习/GUPO_Gradient_Uncertainty-aware_Policy_Optimization_for_Post-Training_Large_Language_Models|GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models]]
- **作者**: Peizheng Guo, Jianqi Zhang, Xingyu Zhang, Yun Fan, Jiahuan Zhou, Changwen Zheng, Wenwen Qiang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Training Large Language Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group Relative Policy Optimization (GRPO) has become a widely used approach for post-training Large Language Models (LLMs) for reasoning. In GRPO, the group gradients induced by different queries within the same mini-batch are directly averaged to form the policy update. However, these group gradients can point in conflicting directions. Our empirical analysis suggests that group-gradient conflicts tend to be associated with less effective policy updates, motivating the need for a reliable aggregated update direction under such conflicts. Standard GRPO aggregation treats the realized group gradients as deterministic contributions and does not account for differences in their reliability during aggregation. To address this issue, we propose Gradient Uncertainty-Aware Policy Optimization (GUPO), which models each group gradient as a random variable under a Bayesian formulation and estimates its probability distribution. GUPO then derives gradient uncertainty using a Dirichlet-based formulation and uses it to calibrate the contribution of each group gradient during aggregation. Extensive experiments on multiple benchmarks demonstrate the effectiveness of GUPO.

</details>

---

### [[20_Research/Papers/强化学习/Repetition_as_Reinforcement_Enhancing_Sample_Efficiency_via_Instant_Episode_Repetition_in_Reinforcement_Learning|Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning]]

![[assets/2608.17347_figure.png|800]]

- **arXiv**: [2608.17347](https://arxiv.org/abs/2608.17347)
- **PDF**: https://arxiv.org/pdf/2608.17347
- **详细分析**: [[20_Research/Papers/强化学习/Repetition_as_Reinforcement_Enhancing_Sample_Efficiency_via_Instant_Episode_Repetition_in_Reinforcement_Learning|Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning]]
- **作者**: Hoda Yamani, Yuning Xing, Koen van Rijnsoever, Bruce A. MacDonald, Henry Williams
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.82（加权：具身智能 0.3，大模型 0.1，强化学习 0.76，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Repetition as Reinforcement: Enhancing Sample Efficiency via Instant Episode Repetition in Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Repetition is a fundamental mechanism in human learning, where revisiting successful experiences strengthens memory, consolidates skills, and improves future performance. Motivated by this biological principle, we introduce Instant Episode Repetition (IER), a simple and novel mechanism that improves sample efficiency by immediately repeating action sequences from successful episodes during environment interaction. Unlike conventional approaches such as Experience Replay and Self-Imitation Learning (SIL), which passively reuse past experience during training updates, IER directly influences the data collection process. Upon identifying a high-reward episode, the agent repeats its action sequence for a fixed number of subsequent episodes, reinforcing valuable behaviors through renewed interaction with the environment. We integrate IER into state-of-the-art SAC and TD3 algorithms and evaluate its effectiveness on continuous-control benchmarks, including MuJoCo, the DeepMind Control Suite, and a real-world dynamic object translation task with a robotic manipulator. Experimental results demonstrate that this simple mechanism improves learning performance over standard and self-imitation-based baselines.

</details>

---

### [[20_Research/Papers/大模型/Agentic_ESOpt_Fine-Tuning_Long-Horizon_LLM_Agents_with_Minimal_GPU_Requirements|Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements]]

![[assets/2608.17310_figure.png|800]]

- **arXiv**: [2608.17310](https://arxiv.org/abs/2608.17310)
- **PDF**: https://arxiv.org/pdf/2608.17310
- **详细分析**: [[20_Research/Papers/大模型/Agentic_ESOpt_Fine-Tuning_Long-Horizon_LLM_Agents_with_Minimal_GPU_Requirements|Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements]]
- **作者**: Zhi Zheng, Rongsheng Chen, Yunpeng Ba, Zhenkun Wang, Yee Whye Teh, Wee Sun Lee
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DocVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has been promising in single-turn LLM fine-tuning. However, long-horizon agentic reasoning introduces increasingly branching interactions and sparse rewards, exposing several limitations of RL: its heavyweight backpropagation-based training stack makes it impractical to fine-tune larger LLMs, and longer-horizon trajectories make credit assignment in RL substantially harder. This paper argues that evolution strategies (ES) can be a better choice for fine-tuning long-horizon LLM agents. Compared with agentic RL, ES offers three key advantages: 1) Model Scalability: ES enables full-parameter optimization with only minimal, inference-level GPU memory, making it possible to fine-tune large LLMs. 2) Flexibility: its lightweight, black-box feedback interface makes ES fine-tuning easy to compose with prompt-space evolution (e.g., skill optimization &amp; test-time compute); and 3) Long-Horizon Scalability: ES performs trajectory-level parameter attribution without decomposing rewards across horizons, yielding better scalability than Agentic RL as the horizon length grows. Based on this insight, we propose Agentic ESOpt, a full-parameter agentic fine-tuning framework tailored to flexible parameter--context co-evolution. At each step, Agentic ESOpt samples perturbations around the current LLM parameters, evaluates the resulting agents with rewards, and applies an online reward-weighted update. To improve the exploration--adaptation trade-off, Agentic ESOpt further introduces a cosine decay schedule of the perturbation scale $σ$. On WebArena-Lite, full-parameter optimization of Qwen-3.5-27B improves the No Skill baseline by 6.69%. In test-time automatic heuristic design, Agentic ESOpt performs online prompt--parameter co-evolution, improving its matched baseline in 28 of 36 settings.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_as_(Discrete)_Potential_Theory|Reinforcement Learning as (Discrete) Potential Theory]]

![[assets/2608.17181_figure.png|800]]

- **arXiv**: [2608.17181](https://arxiv.org/abs/2608.17181)
- **PDF**: https://arxiv.org/pdf/2608.17181
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_as_(Discrete)_Potential_Theory|Reinforcement Learning as (Discrete) Potential Theory]]
- **作者**: Christopher Connolly
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning as (Discrete) Potential Theory》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) theory fundamentally depends on probability theory through the Markov chain. There is a deep connection between probability theory and potential theory. This paper reviews that connection and explores the potential-theoretic viewpoint for core reinforcement learning representations and algorithms under a fixed-policy assumption. This viewpoint may offer a path for improved sample efficiency and formal constraints that can be applied to RL. When the fixed-policy assumption is relaxed, the linear potential theory framework can be naturally extended to the nonlinear case.

</details>

---

### [[20_Research/Papers/强化学习/Policy_Optimization_and_Statistical_Inference_for_Online_Contextual_Matrix_Games|Policy Optimization and Statistical Inference for Online Contextual Matrix Games]]

![[assets/2608.17173_figure.png|800]]

- **arXiv**: [2608.17173](https://arxiv.org/abs/2608.17173)
- **PDF**: https://arxiv.org/pdf/2608.17173
- **详细分析**: [[20_Research/Papers/强化学习/Policy_Optimization_and_Statistical_Inference_for_Online_Contextual_Matrix_Games|Policy Optimization and Statistical Inference for Online Contextual Matrix Games]]
- **作者**: Liner Xiang, Yixin Wang, Hengrui Cai
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Policy Optimization and Statistical Inference for Online Contextual Matrix Games》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online decision making often requires navigating a landscape shaped by both dynamic contexts and strategic interactions. In competitive pricing, for example, hotels must account for both dynamic contextual factors and rivals' strategic responses. Existing approaches address only part of this challenge: contextual bandits optimize single-agent decisions using observable features but ignore multi-player interactions, while online matrix games capture strategic behavior through Nash equilibrium but assume fixed payoffs, ignoring contextual information. How should agents act then when strategic payoffs evolve with contextual signals? We introduce \emph{online contextual matrix games} to integrate contextual information into multi-player online games. We further propose \emph{OnGameLearn}, an online learning algorithm that efficiently balances exploration and exploitation across both player actions and contexts. This approach comes with statistical guarantees: tail bounds for the estimated payoff matrix, the convergence of the estimated Nash equilibrium, the asymptotic normality of the parameter estimators, and the sublinear regret bound. We also develop the notion of \emph{policy value} in matrix games and develop a doubly robust, $\sqrt{T}$-consistent estimator for it. Across simulated studies and a real-world hotel pricing application, we find that OnGameLearn effectively navigates the intertwined challenges of strategic and contextual decision-making.

</details>

---

### [[20_Research/Papers/具身智能/VLCP_Vision_Language_Control_Policy_Closed-Loop_Code_Replanning_for_Robot_Manipulation|VLCP: Vision Language Control Policy Closed-Loop Code Replanning for Robot Manipulation]]

![[assets/2608.16978_figure.png|800]]

- **arXiv**: [2608.16978](https://arxiv.org/abs/2608.16978)
- **PDF**: https://arxiv.org/pdf/2608.16978
- **详细分析**: [[20_Research/Papers/具身智能/VLCP_Vision_Language_Control_Policy_Closed-Loop_Code_Replanning_for_Robot_Manipulation|VLCP: Vision Language Control Policy Closed-Loop Code Replanning for Robot Manipulation]]
- **作者**: Dhia Naouali, Minghan Wu, Claudia Wong, Abhinav Puthran, Omar G. Younis
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.2，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《VLCP: Vision Language Control Policy Closed-Loop Code Replanning for Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Turning a frontier vision-language model into a robot policy usually means fine-tuning it to emit an action representation it never saw in pretraining, which throws away much of the reasoning that made the model worth reaching for. We go the other way and keep the VLM frozen. It writes the policy as a short Python control function, with no demonstrations and no fine-tuning. Writing that code once is open-loop, though. Existing closed-loop methods react at the wrong level: they retry a fixed policy or pick a different subtask, but never rewrite the code that failed. VLCP closes the loop where the failure actually lives, on the control code, within a single episode. Every $K$ steps the VLM re-observes the scene from multi-view RGB, proprioceptive state, and a state delta, then rewrites the control function from what it just saw, so a failure is caught before it compounds. We evaluate on a 57-task MuJoCo/RoboVerse sweep. This training-free policy reaches $35.1\%$ pooled success, against $3.5\%$ for the identical system queried once per episode. That tenfold gap holds with non-overlapping confidence intervals in every scene family. The gain traces to a $27.3\%$ within-episode recovery rate on failed grasps: a miss an open-loop controller would carry to the end of the episode gets re-observed and fixed at the next replan. And the loop stays cheap. A median $84\%$ of input tokens hit cache, an episode needs only about $10$ compact queries, and control blocks written during any replan persist to a cross-episode skill library reused in later prompts.

</details>

---

### [[20_Research/Papers/强化学习/WONDER_A_Radio_World_Model-based_Negotiation_Framework_for_Multi-Agent_UAV_Coverage_Optimization|WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization]]

![[assets/2608.16955_figure.png|800]]

- **arXiv**: [2608.16955](https://arxiv.org/abs/2608.16955)
- **PDF**: https://arxiv.org/pdf/2608.16955
- **详细分析**: [[20_Research/Papers/强化学习/WONDER_A_Radio_World_Model-based_Negotiation_Framework_for_Multi-Agent_UAV_Coverage_Optimization|WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization]]
- **作者**: Jiahao Huang, Rongpeng Li, Zhifeng Zhao, Guoru Ding, Honggang Zhang
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 强化学习, 大模型
- **相关性评分**: 2.42（加权：大模型 0.3，强化学习 0.36，世界模型 0.96，机器人 0.8）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《WONDER: A Radio World Model-based Negotiation Framework for Multi-Agent UAV Coverage Optimization》归入 世界模型、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-disaster damage to terrestrial infrastructure can disrupt wireless coverage,while Uncrewed Aerial Vehicle (UAV) swarms provide a promising solution for rapid restoration.However, due to the limitations in local geometry observations hidden radio impact,and inter-UAV communication,there exists a significant gap between locally visible movement choices and swarm-level coverage outcomes.To combat this gap,we propose a raido World-model-based Optimized Negotiation framework for Distributed UAV covERage (WONDER).Particularly, to tackle the unavailability of the future radio field from onboard observations, WONDER uses a Joint-Embedding Predictive Architecture (JEPA)-based radio world model to learn and predict the incremental radio effect of each candidate trajectory from deployment-available information.Multi-round negotiation in WONDER then coordinates ranked proposals by committing one trajectory at a time and re-evaluating the remaining proposals under the updated context. Our theoretical analyses further validate the effectiveness of such a world model-based framework. WONDER also adopts a Proximal Policy Optimization (PPO)-style Actor and alternates between updating the world model and the actor. Furthermore,we build RadioDynamics,a comprehensive simulation environment that integrates UAV mobility,radio propagation, inter-UAV communication modeling,and digital-twin geometry with ray-traced fields in $62$ metropolitan scenes.Experiments on $11$ testing scenes in RadioDynamics show that WONDER achieves the highest balanced score among seven evaluated methods,reaching $0.870$ with a $0.162$ coverage advantage over STACCA, while maintaining $100\%$ connectivity between UAVs.

</details>

---

### [[20_Research/Papers/大模型/Data-DPO_Direct_Preference_Optimization_for_Target_Model_Data_Selection_in_LLM_Post-Training|Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training]]

![[assets/2608.16926_figure.jpg|800]]

- **arXiv**: [2608.16926](https://arxiv.org/abs/2608.16926)
- **PDF**: https://arxiv.org/pdf/2608.16926
- **详细分析**: [[20_Research/Papers/大模型/Data-DPO_Direct_Preference_Optimization_for_Target_Model_Data_Selection_in_LLM_Post-Training|Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training]]
- **作者**: Peng Sun, Yi Yang, Antong Zhang, Chunxiao Li, Yanbo Wang, Dianbo Liu, xin chen, Kai Yu, Lu Chen, Tianfan Fu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data selection in supervised fine-tuning aims to select a small set of effective samples from large-scale candidate data, reducing training cost while preserving model performance. However, existing methods usually treat data value as a relatively static property, and pay limited attention to the compatibility between data and the capability distribution of the target model. To address this issue, we propose Data-DPO, a target model-oriented SFT data selection method. Data-DPO observes the local training feedback of the target model on different samples through one-step probing, transforms activation differences among samples into pairwise data preferences, and trains a lightweight reward model to learn target-model-aware data preferences. In the final selection stage, Data-DPO further combines target model preference, external quality scores, and marginal diversity to construct a more stable and effective training subset. Experimental results on Vision-Flan and LLaVA-CoT show that Data-DPO consistently outperforms existing data selection baselines under multiple data budgets and stably surpasses full data training performance.

</details>

---
