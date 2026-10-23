# cs.LG | Machine Learning | 2026-10-21

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/强化学习/Continuous-Time_Policy_Gradient_from_Discrete_Data_Convergence_Analysis_and_Model-Free_Algorithms|Continuous-Time Policy Gradient from Discrete Data: Convergence Analysis and Model-Free Algorithms]]

![[assets/2610.28580_first_page.png|800]]

- **arXiv**: [2610.28580](https://arxiv.org/abs/2610.28580)
- **PDF**: https://arxiv.org/pdf/2610.28580
- **详细分析**: [[20_Research/Papers/强化学习/Continuous-Time_Policy_Gradient_from_Discrete_Data_Convergence_Analysis_and_Model-Free_Algorithms|Continuous-Time Policy Gradient from Discrete Data: Convergence Analysis and Model-Free Algorithms]]
- **作者**: Martin Hernandez, Xinyan Qing, Mo Zhou, Yuhua Zhu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.36，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Continuous-Time Policy Gradient from Discrete Data: Convergence Analysis and Model-Free Algorithms》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous-time reinforcement learning seeks an optimal policy under unknown dynamics driven by stochastic differential equations using observations collected at discrete times. We develop a policy gradient framework that combines rigorous convergence analysis with learning from discrete data. We first establish a performance difference lemma and derive policy gradient formulas for randomized and parametrized policies. We then prove exponential convergence of an entropy-regularized policy flow to the regularized optimum. For discrete parametrized updates, we derive a convergence bound that explicitly separates the contributions of critic error, policy-regression error, and the learning step size. To enable learning under unknown dynamics, we integrate this framework with PhiBE, which constructs a continuous-time surrogate generator from discrete transition data. The resulting on-policy and off-policy model-free actor-critic algorithms preserve the continuous-time structure of the control problem. Numerical experiments on an entropy-regularized linear-quadratic regulator and a nonlinear wheeled robot demonstrate the performance and stability of the proposed methods with both known and data-driven dynamics.

</details>

---

### [[20_Research/Papers/强化学习/Confessions_of_a_Masked_MDP|Confessions of a Masked MDP]]

![[assets/2610.28360_first_page.png|800]]

- **arXiv**: [2610.28360](https://arxiv.org/abs/2610.28360)
- **PDF**: https://arxiv.org/pdf/2610.28360
- **详细分析**: [[20_Research/Papers/强化学习/Confessions_of_a_Masked_MDP|Confessions of a Masked MDP]]
- **作者**: Sebastian Reboul, Lorenzo Croissant, Hélène Halconruy
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Confessions of a Masked MDP》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In reinforcement learning, one presumes the action set to be known ahead of time, and, thus, one must know if any state-action pairs are not permissible ahead of computations. In some applications, determining this action mask is the main computational bottleneck. Isolating this problem to highlight its core properties, we study how to combine the search for an optimal policy with the learning of the mask itself, under a linear MDP model in which each attempted action reveals the exact value of a linear score determining its validity. In this framework, we first construct an algorithm based on deterministic optimistic optimization and show that it is minimax optimal, which we show is also computationally efficient. However, it is sub-optimal on non-degenerate instances, as we show. We propose an alternative, which is also computationally efficient, which plans its exploration strategy. This algorithm admits a formal interpretation as an analogue of information-directed-sampling for deterministic feedback, which may be of independent interest. Finally, we study an application of this framework to transfer learning, where the invalid action set changes over time.

</details>

---

### [[20_Research/Papers/具身智能/RANGER_Retrieval_Agent_for_Navigating_Graphs_with_Semantic_Evaluation_Rewards|RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards]]

![[assets/2610.28010_figure.png|800]]

- **arXiv**: [2610.28010](https://arxiv.org/abs/2610.28010)
- **PDF**: https://arxiv.org/pdf/2610.28010
- **详细分析**: [[20_Research/Papers/具身智能/RANGER_Retrieval_Agent_for_Navigating_Graphs_with_Semantic_Evaluation_Rewards|RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards]]
- **作者**: Artem Mikhaylov, Pavel Konoplev, Nikolay Efanov, Artyom Sorokin, Evgeny Burnaev
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.7，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《RANGER: Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：KGQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The integration of Large Language Models and Reinforcement Learning offers a promising direction for complex sequential decision-making tasks, such as multi-hop question answering over knowledge graphs. While LLMs provide strong semantic understanding and reasoning capabilities, they often struggle with precise, multi-step navigation in structured environments. Conversely, RL agents excel at learning navigation policies but are hindered by the difficulty of designing semantically meaningful reward functions. This paper introduces a novel hybrid approach in which an LLM serves as a mentor to an RL agent during training by providing dense, semantically informed reward signals. The RL agent, built on a Transformer-based policy and trained with Group Relative Policy Optimization, learns to navigate a knowledge graph to retrieve relevant information. The LLM evaluates the semantic relevance of the agent's traversed paths, generating reward signals that align the agent's behavior with the information needs expressed in a query. We integrate this Retrieval Agent for Navigating Graphs with Semantic Evaluation Rewards (RANGER) into a complete question-answering pipeline and evaluate it on the open question answering datasets. Experimental results show that the proposed approach outperforms both a baseline retrieval-augmented system with classical graph search and one using an RL agent trained with heuristic rewards, achieving a significant increase in NLP metrics and LLM-as-a-Judge scores. Our findings demonstrate that deep integration of LLMs into the RL training loop yields more effective and semantically aligned retrieval policies for complex reasoning tasks.

</details>

---

### [[20_Research/Papers/大模型/Elicitation_or_Expansion_Demystifying_Gains_from_Agent_Harness_Optimization|Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization]]

![[assets/2610.27889_first_page.png|800]]

- **arXiv**: [2610.27889](https://arxiv.org/abs/2610.27889)
- **PDF**: https://arxiv.org/pdf/2610.27889
- **详细分析**: [[20_Research/Papers/大模型/Elicitation_or_Expansion_Demystifying_Gains_from_Agent_Harness_Optimization|Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization]]
- **作者**: Younghyun Kim, Wooseok Seo, Minseo Kim, Seunghyuk Oh, Minjae Lee, Donghoon Kim, Hyung Il Koo, Jaehyung Kim, Wonjun Kang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AppWorld, HotpotQA, LawBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent studies in harness optimization have shown substantial performance gains in language model agents without updating model weights. A well-designed harness more effectively leverages the underlying model's capabilities by shaping context, tool use, and execution workflows. However, naïve success rates alone do not fully characterize whether optimized harness yields more reliable success on tasks already within reach (elicitation) or a broader range of solvable tasks (expansion). This distinction is crucial for recursive self-improvement and evolutionary search, as expansion may provide a broader range of successful experiences to push the capability boundaries. Despite the growing significance, this distinction remains underexplored in harness optimization. We conduct a systematic analysis to study the effect of gains from harness optimization. Building on pass@k analyses in the reinforcement learning (RL) literature that compare models before and after RL training, we compare optimized harnesses with their pre-optimization counterparts. Specifically, we assess changes in reachable task coverage, compare harness optimization with model scaling and increased inference-time compute, and examine how gains vary with task difficulty. Across static prediction and dynamic tasks, we find that pass@1 advantages of harness over stronger interventions can reverse at larger attempt budgets and aggregate gains conceal shortfalls on hard tasks, underscoring the need for a fine-grained diagnosis.

</details>

---

### [[20_Research/Papers/强化学习/From_Outcomes_to_Steps_Reliable_Success-Aware_Critic_Learning_for_Long-Horizon_Language_Agents|From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents]]

![[assets/2610.27623_figure.png|800]]

- **arXiv**: [2610.27623](https://arxiv.org/abs/2610.27623)
- **PDF**: https://arxiv.org/pdf/2610.27623
- **详细分析**: [[20_Research/Papers/强化学习/From_Outcomes_to_Steps_Reliable_Success-Aware_Critic_Learning_for_Long-Horizon_Language_Agents|From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents]]
- **作者**: Jiaxi Liu, Shixiong Kai, Zhentao Tang, Yang Li, Yuqi Cui, Mingxuan Yuan, Junchi Yan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.5，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《From Outcomes to Steps: Reliable Success-Aware Critic Learning for Long-Horizon Language Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, AppWorld, SORL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning for long-horizon language agents requires identifying whether intermediate actions make eventual task success more or less likely when supervision is available only at trajectory level. The main difficulty is that a critic with aggregate return-prediction accuracy may still fail to resolve the local value differences needed to assign credit to actions, especially under sparse feedback and function approximation. Conventional critics estimate future return, but policy improvement also depends on knowing whether each intermediate decision makes task success more or less likely. We introduce SCALE, an actor-critic framework that augments conventional return estimation with explicit prediction of eventual task success. At each interaction prefix, the critic predicts a return value and a Success Value, defined as the probability that the task will eventually be completed from that prefix. SCALE converts changes in Success Value into multi-step action credit through Success-GAE and modulates its contribution according to the estimated reliability of the predictor, while retaining the token-level PPO objective. Across five agent benchmarks and three model backbones, SCALE improves task performance over the compared RL baselines in most settings, with gains of up to 4.1 percentage points in success rate. Separate critic-learning analyses show that SCALE also improves critic estimation and training stability.

</details>

---

### [[20_Research/Papers/强化学习/Ask_to_Learn_Query-Based_Collaborative_Reinforcement_Learning|Ask to Learn: Query-Based Collaborative Reinforcement Learning]]

![[assets/2610.27606_first_page.png|800]]

- **arXiv**: [2610.27606](https://arxiv.org/abs/2610.27606)
- **PDF**: https://arxiv.org/pdf/2610.27606
- **详细分析**: [[20_Research/Papers/强化学习/Ask_to_Learn_Query-Based_Collaborative_Reinforcement_Learning|Ask to Learn: Query-Based Collaborative Reinforcement Learning]]
- **作者**: Kaicheng Zhang, Hongqian Niu, Laixi Shi, Didong Li, Guannan Qu, Zhun Deng
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Ask to Learn: Query-Based Collaborative Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning is fundamentally limited by the coverage of the available data, while collecting additional trajectories through online exploration may be costly, unsafe, or infeasible. We study whether this limitation can be overcome without directly interacting with the underlying environment. Motivated by practical settings such as collaborator-mediated simulation, where a collaborator can provide information complementary to the offline data, we introduce query-based collaborative reinforcement learning to study how to acquire this information efficiently. The learner starts with a fixed offline dataset and adaptively queries state-time pairs; the collaborator samples an action according to a fixed, possibly suboptimal policy, and the simulator returns the corresponding reward and next state. For finite-horizon tabular problems, we derive an instance-dependent information-theoretic lower bound on the additional queries required to identify an $ε$-optimal policy and develop a local quadratic approximation. Guided by this characterization, we develop an adaptive query-allocation algorithm whose query complexity nearly matches the local benchmark under suitable conditions. Experiments on multiple synthetic and semi-synthetic environments demonstrate the empirical efficiency of the proposed method.

</details>

---

### [[20_Research/Papers/强化学习/From_POMDP_Theory_to_Deep_RL_with_Particle_Filters|From POMDP Theory to Deep RL with Particle Filters]]

![[assets/2610.27575_figure.png|800]]

- **arXiv**: [2610.27575](https://arxiv.org/abs/2610.27575)
- **PDF**: https://arxiv.org/pdf/2610.27575
- **详细分析**: [[20_Research/Papers/强化学习/From_POMDP_Theory_to_Deep_RL_with_Particle_Filters|From POMDP Theory to Deep RL with Particle Filters]]
- **作者**: Kevin Tan, Ziping Xu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.16，世界模型 0.76）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《From POMDP Theory to Deep RL with Particle Filters》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based reinforcement learning in partially observable environments requires inferring hidden states, learning latent dynamics, and planning under the resulting belief. Practical algorithms often solve one aspect of the above pipeline while relying on approximations for the others that are often poorly understood, while existing POMDP theory typically analyzes computationally inefficient theoretical algorithms far from modern deep RL practice. To fill this gap, we propose a practical end-to-end algorithm that approximately solves the hidden state filtering problem via sequential Monte Carlo (SMC), updates a latent dynamics model online, and performs approximate online planning for $d$ steps before bootstrapping leaves with a state-value critic (a QMDP approximation). We analyze each approximation and prove an end-to-end regret bound decomposing the error into model estimation error, particle filter error, Monte Carlo rollout error, and a structural bias term induced by the QMDP approximation controllable by the planning depth that we further analyze in various special cases. The resulting guarantee makes explicit how statistical sample size, particle budget, rollout budget, and planning depth affect performance. We instantiate our algorithm in an MPC-based deep RL framework, demonstrating its practicality on a variety of environments. On a POMDP that satisfies our assumptions, each term of the bound decays at its predicted rate. Our results provide a practical and theoretically grounded route for bridging theory and practice within online decision-making in POMDPs.

</details>

---

### [[20_Research/Papers/强化学习/Bayesian_Neural_Networks_via_Dirichlet_Process_Priors_on_the_Data-Generating_Distribution_for_Randomized_Value_Functions_in_Deep_Reinforceme|Bayesian Neural Networks via Dirichlet Process Priors on the Data-Generating Distribution for Randomized Value Functions in Deep Reinforcement Learning]]

![[assets/2610.27570_figure.png|800]]

- **arXiv**: [2610.27570](https://arxiv.org/abs/2610.27570)
- **PDF**: https://arxiv.org/pdf/2610.27570
- **详细分析**: [[20_Research/Papers/强化学习/Bayesian_Neural_Networks_via_Dirichlet_Process_Priors_on_the_Data-Generating_Distribution_for_Randomized_Value_Functions_in_Deep_Reinforceme|Bayesian Neural Networks via Dirichlet Process Priors on the Data-Generating Distribution for Randomized Value Functions in Deep Reinforcement Learning]]
- **作者**: Sumit Vashishtha
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Bayesian Neural Networks via Dirichlet Process Priors on the Data-Generating Distribution for Randomized Value Functions in Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bayesian neural networks (BNNs) offer a principled framework for quantifying epistemic uncertainty. However, standard weight-space priors yield complex, high-dimensional neural network posteriors that are computationally prohibitive to sample from, and popular approximate inference schemes often fail to capture epistemic uncertainty effectively---a failure mode particularly acute in reinforcement learning (RL) \citep{osband2018randomized}. To resolve this challenge, we introduce a new class of BNNs that quantify uncertainty by placing Bayesian nonparametric Dirichlet Process (DP) priors directly on the underlying data-generating distribution rather than on network parameters. Building on this foundation, we develop DP-DQN, a reinforcement learning algorithm that leverages DP-BNNs to maintain posterior distributions over value functions and perform efficient Thompson sampling. By grounding randomized value functions in Bayesian nonparametrics, DP-DQN unifies data-driven posterior reweighting (via the Bayesian Bootstrap) with generative prior hypotheses injected directly through the DP base measure, enabling decisive ``deep exploration'' with a single neural network without the overhead of multi-network ensembles.

</details>

---

### [[20_Research/Papers/具身智能/Training_Controllable_World_Models_via_Action_Influence_Maximization|Training Controllable World Models via Action Influence Maximization]]

![[assets/2610.27387_figure.png|800]]

- **arXiv**: [2610.27387](https://arxiv.org/abs/2610.27387)
- **PDF**: https://arxiv.org/pdf/2610.27387
- **详细分析**: [[20_Research/Papers/具身智能/Training_Controllable_World_Models_via_Action_Influence_Maximization|Training Controllable World Models via Action Influence Maximization]]
- **作者**: Samuel M. Bateman, Tenny Yin, Chongyi Zheng, Lei Huang, Brian Wang, Benjamin Eysenbach, Jaime Fernández Fisac, Dhruv Shah
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Training Controllable World Models via Action Influence Maximization》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlayWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video generative models trained on successful, goal-directed demonstrations tend to ignore the commanded action, rendering a plausible expert-like future regardless of what is asked of them. We trace this failure to training data that lack sufficient action influence. We analyze this metric and prove that it upper bounds the action influence that any model trained on that data can express. Expert demonstrations, whose narrow action distributions let next states be predicted without attending to the action, set a low ceiling that no amount of model capacity alone can raise. Raising it requires collecting different data. We introduce Action Influence Maximization (AIM), an algorithm for actively collecting training data for improving dataset action influence. We compare the performance and data-efficiency of AIM against exploration heuristics and intrinsic-motivation methods on simulated navigation and manipulation tasks. In pixel-based manipulation, AIM is the only method that consistently improves controllability: 500 actively collected episodes added to 3k demonstrations match a world model trained on 300k expert episodes on end-effector controllability, an $85\times$ reduction in data.

</details>

---

### [[20_Research/Papers/具身智能/What_Would_Removing_This_Corruption_Change_Failure_Attribution_for_Vision-Language-Action_Models|What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models]]

![[assets/2610.27277_figure.png|800]]

- **arXiv**: [2610.27277](https://arxiv.org/abs/2610.27277)
- **PDF**: https://arxiv.org/pdf/2610.27277
- **详细分析**: [[20_Research/Papers/具身智能/What_Would_Removing_This_Corruption_Change_Failure_Attribution_for_Vision-Language-Action_Models|What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models]]
- **作者**: Carson Sobolewski, Anjali Parashar, Fei Chen, Yingke Li, Chuchu Fan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are sensitive to visual corruptions, but knowing that a corruption is typically harmful does not establish whether removing it would benefit the current episode. Furthermore, when several corruptions co-occur, deciding what to correct requires understanding which ones contribute to failure risk and how much their removal would help. We define this problem as failure attribution. Detecting corruption presence alone cannot answer this question, as corruptions can be present but relatively harmless, while directly measuring removal benefits requires costly paired policy rollouts with and without the corruption present. To address this, we introduce a factorized risk model that learns separate representations of the scene and corruptions, allowing us to estimate removal benefits through latent intervention from the current image and task instruction, without paired clean images or additional counterfactual rollouts. We evaluate our approach on OpenVLA and $π_{0.5}$ in simulation and $π_{0.5}$-DROID on a Franka robot. Our method outperforms monolithic and vision-language-model (VLM) baselines, including achieving approximately 3x lower attribution error than frontier VLMs. We also demonstrate our method adapts to execution context and corruption intensity, and can be used for online failure monitoring on hardware.

</details>

---

### [[20_Research/Papers/强化学习/Deep_catastrophic-risk-aware_reinforcement_learning|Deep catastrophic-risk-aware reinforcement learning]]

![[assets/2610.27214_figure.png|800]]

- **arXiv**: [2610.27214](https://arxiv.org/abs/2610.27214)
- **PDF**: https://arxiv.org/pdf/2610.27214
- **详细分析**: [[20_Research/Papers/强化学习/Deep_catastrophic-risk-aware_reinforcement_learning|Deep catastrophic-risk-aware reinforcement learning]]
- **作者**: Carlos Pérez Octavio Mendoza, Frédéric Godin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Deep catastrophic-risk-aware reinforcement learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Estimating extreme risk in reinforcement learning becomes increasingly difficult as the confidence level increases, since only a small number of observations contribute to empirical estimates of Conditional Value-at-Risk (CVaR). In this paper, we extend an Extreme Value Theory (EVT) approach for CVaR optimization to high-dimensional neural-network policies. Using a peaks-over-threshold representation and method-of-moments estimation, we obtain a differentiable tail-risk objective and show that, conditional on the selected threshold, its finite-sample gradient can be computed directly through automatic differentiation. We first validate the approach in a controlled experiment with a known optimal solution and then investigate its performance in a deep-hedging problem with rare extreme market movements. Our results show similar hedging behavior for EVT- and empirical-CVaR-trained policies under normal conditions, while EVT-trained policies exhibit lower hedging losses under the extreme-scenario evaluation across the training sample sizes considered. These results suggest that EVT can provide a practical alternative for training neural policies when the observations relevant to extreme risk are scarce.

</details>

---

### [[20_Research/Papers/世界模型/Meta-iLaD_Identifiable_Latent_Dynamics_via_Meta-Learning_of_Dynamics_Environments|Meta-iLaD: Identifiable Latent Dynamics via Meta-Learning of Dynamics Environments]]

![[assets/2610.27180_figure.png|800]]

- **arXiv**: [2610.27180](https://arxiv.org/abs/2610.27180)
- **PDF**: https://arxiv.org/pdf/2610.27180
- **详细分析**: [[20_Research/Papers/世界模型/Meta-iLaD_Identifiable_Latent_Dynamics_via_Meta-Learning_of_Dynamics_Environments|Meta-iLaD: Identifiable Latent Dynamics via Meta-Learning of Dynamics Environments]]
- **作者**: Yubo Ye, Sweekar Piya, Xiajun Jiang, Linwei Wang
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Meta-iLaD: Identifiable Latent Dynamics via Meta-Learning of Dynamics Environments》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning latent dynamics is central to assessing the current states and forecasting the future trajectories of high-dimensional time series. For locally-stationary latent dynamics $\mathcal{F}(\mathbf{z}_{&lt;t}; \mathbf{c})$ with latent dynamics state $\mathbf{z}_t$ and environment variable $\mathbf{c}$, prior identifiability results have largely focused on $\mathbf{z}_t$ when conditioned on predefined label $u$ of dynamics environments. This leaves two limitations: reliance on predefined labels that hinder generalization to unseen environments, and a limited understanding of the identifiability of $\mathcal{F}$ and $\mathbf{c}$ which -- although offering important structural properties for the identifiability of $\mathbf{z}_t$ -- are learned jointly with $\mathbf{z}_t$. We address these limitations with Meta-iLaD, a novel identifiable latent dynamics framework attained by meta-learning across dynamics environments. Meta-iLaD introduces a novel conditional prior of $\mathbf{c}$, modeled as a feedforward meta-learner to rapidly extract $\mathbf{c}$ from few-shot examples. Meta-iLaD further establishes identifiability for $\mathbf{z}_t$, $\mathbf{c}$, and $\mathcal{F}$ simultaneously, for a general formulation of $\mathcal{F}(\mathbf{z}_{&lt; t};\mathbf{c})$ without restricting the dimension of $\mathbf{c}$ or how it modulates $\mathcal{F}$. On synthetic and real data, we provide strong empirical evidence that 1) conditioning on few-shot examples enables generalization to out-of-distribution environments, and 2) identifiability for $\mathbf{c}$ and $\mathcal{F}$ is critical for accurate forecasting beyond reconstructing observed trajectories. Code is available at https://github.com/GoForIt-YYB/Meta-iLaD.

</details>

---

### [[20_Research/Papers/强化学习/Glass-Box_Deep_Reinforcement_Learning_for_High-Speed_Flow_Control|Glass-Box Deep Reinforcement Learning for High-Speed Flow Control]]

![[assets/2610.27132_figure.png|800]]

- **arXiv**: [2610.27132](https://arxiv.org/abs/2610.27132)
- **PDF**: https://arxiv.org/pdf/2610.27132
- **详细分析**: [[20_Research/Papers/强化学习/Glass-Box_Deep_Reinforcement_Learning_for_High-Speed_Flow_Control|Glass-Box Deep Reinforcement Learning for High-Speed Flow Control]]
- **作者**: Ameya D. Jagtap
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Glass-Box Deep Reinforcement Learning for High-Speed Flow Control》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) is challenging long-held assumptions in active flow control. By learning directly from interaction with a flow, DRL agents can find actuation strategies for nonlinear, unsteady flows without explicit models, often exploiting mechanisms that classical control would not anticipate. High-speed flows are a demanding test of this promise: shocks, shock/boundary-layer interactions, transition, aerothermal loading and microsecond-scale dynamics strain both algorithms and hardware. Yet most demonstrations remain idealized, low-speed simulations with limited evidence of robustness, interpretability, transferability or experimental deployment. In this perspective, we examine what constrains DRL-based high-speed flow control, including compressible simulation cost and fidelity, data efficiency, sensing in extreme environments, reward design, explainability, and generalization across Mach and Reynolds number. We argue that these limits reflect a tension between data-driven optimization and the structured physics, constraints and uncertainties of real flows. We then highlight where DRL may go beyond conventional approaches: adaptive control of shock-induced separation and turbulent boundary layers, coordination of distributed actuators, and discovery of unconventional flow-manipulation mechanisms.The central challenge, however, is translating these capabilities into reliable technology, which will require validated compressible simulation environments, physics- and constraint-aware learning, robustness to off-design conditions and sensor degradation, real-time operation, hardware-in-the-loop and wind-tunnel validation, and credible pathways to safety and certification.

</details>

---
