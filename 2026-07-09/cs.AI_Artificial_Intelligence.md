# cs.AI | Artificial Intelligence | 2026-07-09

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/大模型/Accurate,_Interdisciplinary_and_Transparent_Structure-property_Understanding_with_Deep_Native_Structural_Reasoning|Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning]]

![[assets/2607.07708_first_page.png|800]]

- **arXiv**: [2607.07708](https://arxiv.org/abs/2607.07708)
- **PDF**: https://arxiv.org/pdf/2607.07708
- **详细分析**: [[20_Research/Papers/大模型/Accurate,_Interdisciplinary_and_Transparent_Structure-property_Understanding_with_Deep_Native_Structural_Reasoning|Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning]]
- **作者**: Chen Tang, Yizhou Wang, Jianyu Wu, Lintao Wang, Shixiang Tang, Pengze Li, Encheng Su, Jun Yao, Jiabei Xiao, Yuqi Shi, Jielan Li, Hongxia Hao...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint challenge of representation and reasoning: models must preserve domain-native structural information while showing how specific evidence supports predictions under these constraints. Here we introduce SciReasoner, a multimodal scientific foundation model for native structural reasoning across proteins, small molecules and inorganic crystals. SciReasoner discretizes coordinates, topologies and periodic connectivities into a unified structure-aware vocabulary, treating structural tokens as addressable evidence units during reasoning. In homology-controlled Gene Ontology prediction, SciReasoner improves Cellular Component annotation for low-homology and orphan-like proteins, increasing $F_{\max}$ from 0.42 to 0.55. In chemistry, it raises single-step retrosynthesis accuracy from 0.63 to 0.72 while generating fragment-level disconnection and precursor-verification traces. In materials science, its representations separate elemental and compound phases and resolve high- and low-band-gap regimes. Across 86 benchmarks, SciReasoner achieves state-of-the-art performance on 67 tasks. Double-blind expert evaluation rates its reasoning traces as preferred or at least comparable to those of a frontier large language model in 98% of cases. By making structure an inspectable substrate for reasoning under scientific constraints, SciReasoner connects accurate prediction with interpretable scientific inference.

</details>

---

### [[20_Research/Papers/强化学习/Selective_Timestep_Weighting_and_Advantage-Based_Replay_for_Sample-Efficient_Diffusion_RLHF|Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF]]

![[assets/2607.07693_figure.png|800]]

- **arXiv**: [2607.07693](https://arxiv.org/abs/2607.07693)
- **PDF**: https://arxiv.org/pdf/2607.07693
- **详细分析**: [[20_Research/Papers/强化学习/Selective_Timestep_Weighting_and_Advantage-Based_Replay_for_Sample-Efficient_Diffusion_RLHF|Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF]]
- **作者**: Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：B2-DiffuRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that substantially improve the feedback efficiency of diffusion RLHF while preserving generalization to unseen prompts. Our key observation is that reward information in diffusion trajectories is unevenly distributed: not all denoising timesteps or trajectories contribute equally to learning from a reward signal. By emphasizing informative timesteps and trajectories during optimization, we obtain more effective gradient updates. First, we introduce a per-timestep weighting scheme that reweights denoising steps during policy optimization. We theoretically connect this weighting to the optimal convergence properties of proximal policy optimization (PPO) and approximate the resulting weighting trend empirically. Second, we introduce a replay mechanism that prioritizes informative trajectories, enabling the model to reuse past samples instead of repeatedly querying new rewards. Together, these strategies significantly improve the feedback efficiency of diffusion RLHF. Under identical hyperparameter settings, our approach achieves up to a 6$\times$ improvement in sample efficiency compared to widely used diffusion RLHF baselines.

</details>

---

### [[20_Research/Papers/强化学习/Agon_Competitive_Cross-Model_RL_with_Implicit_Rival_Grading_of_Reasoning|Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning]]

![[assets/2607.07690_first_page.png|800]]

- **arXiv**: [2607.07690](https://arxiv.org/abs/2607.07690)
- **PDF**: https://arxiv.org/pdf/2607.07690
- **详细分析**: [[20_Research/Papers/强化学习/Agon_Competitive_Cross-Model_RL_with_Implicit_Rival_Grading_of_Reasoning|Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning]]
- **作者**: Vladislav Beliaev
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.97（加权：大模型 0.25，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from verifiable rewards (e.g. GRPO) is the engine behind today's reasoning models, yet it grades only the final answer. On hard problems this trains models to write more rather than to think better, since the trace itself is never graded and no label for good thinking exists. We introduce Agon, which makes two competing models each other's graders. Both attempt the same problem; in alternating roles, one drafts a solution and the other reads it while solving, and each is rewarded for out-solving the other. To win, a model must out-reason a rival that has seen its work, so reasoning is judged implicitly during training, with no process labels and no reward model. Because both models are optimized, each faces a progressively stronger rival, which single-model RL cannot provide. The two need only be comparably strong and behaviorally different. At inference the pair deploys as it trains, a two-stage cascade in which one model drafts and the other answers after reading the draft. On the hard split of DeepMath with Qwen3, this doubles GRPO's pass@1, roughly eight times the gain of an untrained Mixture-of-Agents pass over the same base. The ordering replicates on competitive-programming code and across model families (Qwen3.5, Gemma 4). For now the models talk in text; the next step is to let them reason together in latent space.

</details>

---

### [[20_Research/Papers/强化学习/Single-Rollout_Asynchronous_Optimization_for_Agentic_Reinforcement_Learning|Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning]]

![[assets/2607.07508_figure.png|800]]

- **arXiv**: [2607.07508](https://arxiv.org/abs/2607.07508)
- **PDF**: https://arxiv.org/pdf/2607.07508
- **详细分析**: [[20_Research/Papers/强化学习/Single-Rollout_Asynchronous_Optimization_for_Agentic_Reinforcement_Learning|Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning]]
- **作者**: Zhenyu Hou, Yujiang Li, Jie Tang, Yuxiao Dong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Single-Rollout Asynchronous Optimization for Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IMOAnswerBench, SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is becoming increasingly important for post-training large language models (LLMs). Previous RL pipelines for LLMs were mostly synchronous and batch-interleaved, which is inefficient for long-horizon agentic tasks. Recently, asynchronous RL has emerged as a more efficient alternative by updating the model as rollouts arrive. However, existing asynchronous RL systems often emphasize throughput, while leaving training stability and task effectiveness largely underexplored. For example, a key challenge is that group-wise sampling in the widely-used GRPO framework does not naturally fit asynchronous agentic training. In this paper, we present Single-rollout Asynchronous Optimization (SAO) to address the stability and off-policy challenges in asynchronous RL. To reduce off-policy effects and improve generalization, we replace group-wise sampling with single-rollout sampling, that is, using one rollout per prompt. We further improve this single-rollout strategy with practical value-model training designs. To improve optimization stability, we introduce a strict double-side token-level clipping strategy. SAO is able to train stably for one thousand steps and consistently outperform GRPO and its variants on agentic coding and reasoning benchmarks, such as SWE-Bench Verified, BeyondAIME, and IMOAnswerBench. We also demonstrate that single-rollout RL is particularly effective in a simulated online learning setting, where the model must adapt to changing evolving environments. To this end, SAO is successfully deployed in the agentic RL pipeline for training the open GLM-5.2 model (750B-A40B).

</details>

---

### [[20_Research/Papers/大模型/Do_LLM-Generated_Skills_Make_Better_AI_Data_Scientists_A_Component_Ablation_Across_Data-Science_Workflows|Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows]]

![[assets/2607.07504_figure.png|800]]

- **arXiv**: [2607.07504](https://arxiv.org/abs/2607.07504)
- **PDF**: https://arxiv.org/pdf/2607.07504
- **详细分析**: [[20_Research/Papers/大模型/Do_LLM-Generated_Skills_Make_Better_AI_Data_Scientists_A_Component_Ablation_Across_Data-Science_Workflows|Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows]]
- **作者**: Wei-Jung Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DataSciBench, PrepBench, SkillLearnBench, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck. We ask whether LLM-generated skills offer a useful low-curation alternative: do they improve performance over the task prompt alone? We test this question across four lifecycle stages: data preparation, data extraction, statistical analysis, and reporting, using one generated skill per stage. We find no reliable improvement from full generated skills over No-Skill prompting. We then ask whether any part of the skill is useful by ablating different skill components. The main ablation covers 56 tasks, nine model configurations, and three providers, yielding 7,560 runs. Compared with prompting using the task alone, neither the full generated skill nor any ablated skill variant significantly improves performance; all p-values are at least 0.396, and the total spread across variants is only 1.2 pp. A supplemental token-matched control adds 1,512 runs and finds that Full skills perform similarly to task-irrelevant skill-formatted content. The results caution against using one LLM-generated skill per data-science workflow as a default single-shot prompting strategy.

</details>

---

### [[20_Research/Papers/强化学习/Reward-Adaptive_Iterative_Discovery_A_Case_Study_on_Automated_Game_Testing_for_NHL26|Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26]]

![[assets/2607.07498_figure.png|800]]

- **arXiv**: [2607.07498](https://arxiv.org/abs/2607.07498)
- **PDF**: https://arxiv.org/pdf/2607.07498
- **详细分析**: [[20_Research/Papers/强化学习/Reward-Adaptive_Iterative_Discovery_A_Case_Study_on_Automated_Game_Testing_for_NHL26|Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26]]
- **作者**: Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin, Michele Petteni, Alessandro Sestini, Joakim Bergdahl, Amir Baghi, Linus Gisslén
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploits using an iterative Reinforcement Learning (RL) approach that trains a population of goal scoring agents. While previous approaches can already successfully find exploits, RL algorithms tend to overfit to a single solution. We introduce a simple extension on top of existing RL algorithms, such that they find multiple diverse high-quality solutions. For our first deployment of this approach, within a single experiment we were able to find six hockey scoring exploit strategies that were qualitatively similar to those that playtesters had found in hours-long manual testing sessions.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Attack-Success_Rate_Action-Graded_Severity_Scale_for_Tool-Using_AI_Agents|Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents]]

![[assets/2607.07474_figure.png|800]]

- **arXiv**: [2607.07474](https://arxiv.org/abs/2607.07474)
- **PDF**: https://arxiv.org/pdf/2607.07474
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Attack-Success_Rate_Action-Graded_Severity_Scale_for_Tool-Using_AI_Agents|Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents]]
- **作者**: Harry Owiredu-Ashley
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, HarmBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another party, and whether it expanded privilege. We compute the scale two ways: a deterministic oracle that reads the trajectory and the attacker's stated goal, and a panel of three frontier language-model judges that read a tag-free account of the same trajectory. Across four victim models and two defenses on the AgentDojo workspace suite, severity grading exposes three cases the binary metric hides, including a defense that reports a zero attack-success rate while still permitting an externally visible cross-scope leak through an unfiltered tool. The judge panel reproduces the oracle with high ordinal agreement (Krippendorff's alpha = 0.91) but shares systematic blind spots that we characterize, most notably a failure to recognize escalation chains. Unlike prior work that provides harm taxonomies, harmful-task completion tests, execution-level safety benchmarks, or severity-aware simulation, our contribution is a reusable, trace-grounded severity instrument applied to the actual actions recorded in existing red-team logs. All code, prompts, and per-episode logs are released.

</details>

---

### [[20_Research/Papers/大模型/SpaCellAgent_A_Self-Evolving_LLM-Based_Multi-Agent_Framework_for_Trajectory_Analysis|SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis]]

![[assets/2607.07467_figure.png|800]]

- **arXiv**: [2607.07467](https://arxiv.org/abs/2607.07467)
- **PDF**: https://arxiv.org/pdf/2607.07467
- **详细分析**: [[20_Research/Papers/大模型/SpaCellAgent_A_Self-Evolving_LLM-Based_Multi-Agent_Framework_for_Trajectory_Analysis|SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis]]
- **作者**: Songhan Wang, Haoang Chi, He Li, Zhiheng Zhang, Jiayan Yuan, Cheems Wang, Hao Peng, Xinwang Liu, Wenjing Yang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end spatiotemporal analysis and narrative generation. SpaCellAgent utilizes a multi-agent architecture for strategic workflow planning, a dynamic tool-orchestration engine for adaptive algorithm selection, and a self-evolution module that iteratively refines performance through feedback. We evaluate SpaCellAgent on six heterogeneous datasets encompassing complex temporal developmental trajectories, diverse sequencing platforms, and spatially-resolved tissue architectures. SpaCellAgent consistently demonstrates over 40\% improvement in analytical efficiency while maintaining expert-aligned performance. By converting natural language specifications into optimized analytical workflows and fully automating the pipeline, SpaCellAgent democratizes advanced spatiotemporal modeling and establishes a scalable, agent-driven paradigm for computational biology. The code and materials are available at https://github.com/LittleXH-shw/SpaCellAgent.

</details>

---

### [[20_Research/Papers/大模型/The_Blind_Curator_How_a_Biased_Judge_Silently_Disables_Skill_Retirement_in_Self-Evolving_Agents|The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents]]

![[assets/2607.07436_figure.png|800]]

- **arXiv**: [2607.07436](https://arxiv.org/abs/2607.07436)
- **PDF**: https://arxiv.org/pdf/2607.07436
- **详细分析**: [[20_Research/Papers/大模型/The_Blind_Curator_How_a_Biased_Judge_Silently_Disables_Skill_Retirement_in_Self-Evolving_Agents|The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents]]
- **作者**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted-reward analysis and, isolating the causal channel by injecting corruption on top of a deterministic reward, a behavioral study on a reference-free report-writing testbed with a code-generation cross-check. Symmetric noise leaves retirement intact, but \emph{false-pass} bias (failures slipping through as passes) disables contribution-based retirement past a sharp threshold that no amount of data can cross. Separating genuine retirement from cap-eviction churn shows this \emph{mechanism} failure is universal, holding across domains and failure rates and sparing only near-zero-false-pass, verifier-like graders. The downstream \emph{outcome}, though, is regime-dependent: eval quality degrades only where the same corruption also starves skill synthesis, and otherwise holds steady, so the disabled curator is \emph{silent}, surfacing in no aggregate metric. The contribution is a behavioral safety result, not a performance one. A cheap defect-injection audit then tells an operator, before deployment, which side of the threshold their judge occupies.

</details>

---

### [[20_Research/Papers/强化学习/RLVP_Penalize_the_Path,_Reward_the_Outcome|RLVP: Penalize the Path, Reward the Outcome]]

![[assets/2607.07435_figure.png|800]]

- **arXiv**: [2607.07435](https://arxiv.org/abs/2607.07435)
- **PDF**: https://arxiv.org/pdf/2607.07435
- **详细分析**: [[20_Research/Papers/强化学习/RLVP_Penalize_the_Path,_Reward_the_Outcome|RLVP: Penalize the Path, Reward the Outcome]]
- **作者**: Bojie Li, Noah Shi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RLVP: Penalize the Path, Reward the Outcome》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them frequently improves apparent success. Second, because each interaction is expensive, the agent must learn efficiently from very few examples. Reinforcement learning from verifiable rewards (RLVR) is blind to both challenges: it optimizes solely on the outcome and wastes expensive rollouts on all-fail groups where group-relative advantage collapses to zero. Attempts to densify supervision by rewarding progress target the hard-to-verify direction. In contrast, real agentic environments can cheaply detect bad moves. Since group-relative advantage is equivalent to within-group variance, a dense signal helps only when it supplies variance the outcome lacks. A verifiable penalty on the path meets this condition reliably, while a progress potential helps only where partial progress is reachable. The resulting recipe "penalize the path, reward the outcome" achieves high task success with near-zero violations, where outcome-only training violates constraints on nearly every episode. We provide four design rules for effective penalties, including avoidance of the inaction trap that arises when a penalty is used in isolation.

</details>

---

### [[20_Research/Papers/大模型/Reason_Less,_Verify_More_Deterministic_Gates_Recover_a_Silent_Policy-Violation_Failure_Mode_in_Tool-Using_LLM_Agents|Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents]]

![[assets/2607.07405_first_page.png|800]]

- **arXiv**: [2607.07405](https://arxiv.org/abs/2607.07405)
- **PDF**: https://arxiv.org/pdf/2607.07405
- **详细分析**: [[20_Research/Papers/大模型/Reason_Less,_Verify_More_Deterministic_Gates_Recover_a_Silent_Policy-Violation_Failure_Mode_in_Tool-Using_LLM_Agents|Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents]]
- **作者**: Vikas Reddy, Sumanth Reddy Challaram, Abhishek Basu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully. In policy-permissive environments, a tool may execute any well-formed call even when the corresponding state transition is forbidden by domain policy. The result is a silent wrong state (a booking cancelled, a passenger count changed, a claim acted on without verification) that neither the tool nor the agent's self-report exposes. We study this failure mode in the $τ^2$-bench airline domain. On a budget agent, 78% of observed failures are silent wrong-state failures with no tool error, and the aggregate failure rate is reproducible across disjoint seeds, not sampling noise. We then evaluate a lightweight intervention: deterministic, read-only pre-execution gates that inspect the proposed call and current state before allowing a write. A four-gate suite raises full-benchmark success from 29.6% to 42.0% on gpt-4o-mini (+12.4pp; paired task-level bootstrap P=0.0012), and the lift reproduces on a disjoint 15-seed set (+12.3pp; P=0.0008). The effect is concentrated where the gates fire: on the 26/50 firing tasks, success rises by +19.2pp, while movement on the 24 non-firing tasks does not exclude zero. Two negative controls (a self-enforcing retail domain and BFCL) bound the mechanism: gates help when tools are policy-permissive and add little where tools already self-enforce. As suggestive evidence, not a central claim, the same failure mode persists at the frontier: gpt-5.2 at default reasoning still attempts policy-violating writes, and the same suite improves success from 61.2% to 71.6% (+10.4pp; P=0.020; n=5, no replication). The contribution is a bounded evaluation and reliability result: deterministic gates do not guarantee task success, but they can deterministically prevent a known class of silent policy-violating writes at the action boundary.

</details>

---

### [[20_Research/Papers/具身智能/Behavior_Foundations_for_Quadruped_Robots_ABot-C0_Technical_Report|Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report]]

![[assets/2607.07370_figure.png|800]]

- **arXiv**: [2607.07370](https://arxiv.org/abs/2607.07370)
- **PDF**: https://arxiv.org/pdf/2607.07370
- **详细分析**: [[20_Research/Papers/具身智能/Behavior_Foundations_for_Quadruped_Robots_ABot-C0_Technical_Report|Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report]]
- **作者**: Xufeng Zhao, Fuzhi Yang, Jianhui Chen, Li Gao, Zhang Meng, Jie Gao, Yao Zheng, Wenyu Liu, Menglin Yang, Minqi Gu, Yaru Zhao, Honglin Han...
- **cs 子类**: cs.AI, cs.HC, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.8（加权：具身智能 2.4，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In embodied intelligence systems, the motion controller serves as the critical bridge between semantic reasoning and physical execution. Humanoid control has progressed rapidly through large-scale human motion-capture data and motion-tracking paradigm. However, producing quadruped robots motion corpora with scalability and physical feasibility faces more fundamental obstacles: animal motion data is scarce, and cross-embodiment retargeting remains fragile. We present ABot-C0, a generalist motion-control system for quadruped robots that establishes three complementary behavior foundations: a scalable multi-source motion-data pipeline, robust policy learning across motion tracking, locomotion, and scene interaction, and a unified deployment stack for reliable real-world operation. Fundamentally, we construct a data pyramid through conditional video-generation synthesis, annotated motion capture, teleoperation and human design, producing 16,074 physically feasible motion clips as the data foundation for various motion learning demands. We then train a Flow-Matching generalist policy that demonstrates for the first time quadruped motion tracking scaling law that its performance improves consistently as training scales up, with zero-shot capability to track unseen motions. Then, we push a step further for robust all-terrain traversal locomotion by adopting a three-stage privileged-to-perceptive framework with temporal LiDAR memory and terrain-predictive supervision. Collectively, these components form a motion generalist that coordinates multi-policy execution, smooth behavior transitions, energy-efficient control, and safety mechanisms for real-world deployment. Extensive experiments on urban-terrain autonomous navigation and companion-style multimodal interaction demonstrate that quadruped robots move beyond single-function demos toward product-level behavioral intelligence.

</details>

---

### [[20_Research/Papers/具身智能/HumAIN_Human-Aware_Implicit_Social_Robot_Navigation|HumAIN: Human-Aware Implicit Social Robot Navigation]]

![[assets/2607.07357_figure.png|800]]

- **arXiv**: [2607.07357](https://arxiv.org/abs/2607.07357)
- **PDF**: https://arxiv.org/pdf/2607.07357
- **详细分析**: [[20_Research/Papers/具身智能/HumAIN_Human-Aware_Implicit_Social_Robot_Navigation|HumAIN: Human-Aware Implicit Social Robot Navigation]]
- **作者**: Daeun Song, Nhat Le, Jeffrey Chen, Mohammad Nazeri, Amirreza Payandeh, Rohan Chandra, Reuth Mirsky, Ross Mead, Ling Xiao, Xuesu Xiao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《HumAIN: Human-Aware Implicit Social Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation. We first employ a transformer-based teacher model that fuses rich multi-modal inputs, including historic images, skeletal keypoints, robot state, and a robot's target goal, to learn robust, human-aware representations for the robot's future trajectory planning. To enable real-time deployment, we then distill this knowledge into a lightweight student model. By optimizing for both trajectory reconstruction and latent feature alignment with the teacher, the student learns to infer complex social dynamics from minimal inputs. Bridging the prediction-planning gap with an efficient distilled architecture, our method enables robots to reason about human behavior in a manner that is adaptive, robust, and socially compliant. We validate HumAIN through extensive experiments, where it improves trajectory prediction metrics by an average of 29.8% across all metrics compared to state-of-the-art baselines. These results highlight the benefit of using implicit, whole-body cues to achieve human-like navigation awareness on resource-constrained platforms.

</details>

---

### [[20_Research/Papers/大模型/From_Atomic_Actions_to_Standard_Operating_Procedures_Iterative_Tool_Optimization_for_Self-Evolving_LLM_Agents|From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents]]

![[assets/2607.07321_figure.png|800]]

- **arXiv**: [2607.07321](https://arxiv.org/abs/2607.07321)
- **PDF**: https://arxiv.org/pdf/2607.07321
- **详细分析**: [[20_Research/Papers/大模型/From_Atomic_Actions_to_Standard_Operating_Procedures_Iterative_Tool_Optimization_for_Self-Evolving_LLM_Agents|From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents]]
- **作者**: Haipeng Ding, Yuexiang Xie, Zhewei Wei, Yaliang Li, Bolin Ding
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates. In this study, we propose that agents can achieve self-evolution by synthesizing these atomic actions into reusable Standard Operating Procedures (SOPs), which function as callable higher-order tools that encapsulate multi-step logic. We further introduce EvoSOP, a framework that empowers agents to extract SOPs from execution trajectories and iteratively optimize the toolset through a systematic lifecycle of construction, merging, evaluation, and pruning. Extensive experiments demonstrate that EvoSOP significantly boosts task success rates while substantially reducing the number of interaction rounds compared to baselines. Our analysis also reveals that iterative tool optimization fosters reliable and efficient tool-use patterns, providing a scalable pathway for the development of self-evolving agents.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Voice_Activity_Projection_for_Turn-Taking_in_Social_Robots_with_Voice-Activity-Related_Pretrained_Encoders|Multimodal Voice Activity Projection for Turn-Taking in Social Robots with Voice-Activity-Related Pretrained Encoders]]

![[assets/2607.07294_figure.png|800]]

- **arXiv**: [2607.07294](https://arxiv.org/abs/2607.07294)
- **PDF**: https://arxiv.org/pdf/2607.07294
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Voice_Activity_Projection_for_Turn-Taking_in_Social_Robots_with_Voice-Activity-Related_Pretrained_Encoders|Multimodal Voice Activity Projection for Turn-Taking in Social Robots with Voice-Activity-Related Pretrained Encoders]]
- **作者**: Antonio Cano, Guillermo Pérez, Luis Merino, Randy Gomez
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.35（加权：具身智能 0.3，大模型 0.55，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Multimodal Voice Activity Projection for Turn-Taking in Social Robots with Voice-Activity-Related Pretrained Encoders》归入 大模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TalkNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Turn-taking prediction is a key requirement for social robots involved in human-human interaction, particularly in mediator settings, where the robot must anticipate conversational dynamics rather than merely react to pauses. This work presents a Multimodal Voice Activity Projection (MM-VAP) framework that extends the original audio-only VAP formulation to synchronized audio-visual inputs while preserving its self-supervised future-projection objective. The proposed approach builds on pretrained audio-visual backbones originally optimized for speech-related tasks and adapts them through Low-Rank Adaptation to the multimodal turn-taking problem. After independent speaker encoding, an inter-speaker attention stage models the relational dynamics required to project future voice activity. In addition, a semantic consistency loss is introduced to regularize the 256-state output space according to higher-level dialogue activity patterns. Experiments on NoXi and NoXi+J showed improvements over the current baselines, particularly for some turn-taking events. Additional evaluation on the Haru EDR corpus further supported the suitability of this direction for mediation-oriented human-robot interaction.

</details>

---

### [[20_Research/Papers/强化学习/ORCAID_Oblique_Rule-Based_Continuous-Action_Interpretation_for_Deep_RL_Policies|ORCAID: Oblique Rule-Based Continuous-Action Interpretation for Deep RL Policies]]

![[assets/2607.07235_first_page.png|800]]

- **arXiv**: [2607.07235](https://arxiv.org/abs/2607.07235)
- **PDF**: https://arxiv.org/pdf/2607.07235
- **详细分析**: [[20_Research/Papers/强化学习/ORCAID_Oblique_Rule-Based_Continuous-Action_Interpretation_for_Deep_RL_Policies|ORCAID: Oblique Rule-Based Continuous-Action Interpretation for Deep RL Policies]]
- **作者**: Ignacio D. Lopez-Miguel, Ezio Bartocci, Thomas Eiter, Martin Tappler
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《ORCAID: Oblique Rule-Based Continuous-Action Interpretation for Deep RL Policies》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Explainability remains a key issue in reinforcement learning (RL). Distilling an interpretable policy from an agent trained in a complex environment is particularly challenging when the action space is continuous. We introduce ORCAID, a novel method for extracting interpretable rule-based policies from RL agents operating in mixed continuous-discrete environments with continuous action spaces. Our main contribution is an efficient oblique decision tree training algorithm that partitions the state space by hyperplanes and fits local linear models. The key idea lies in a three-stage split search: efficient random initialization, local refinement, and backward elimination. Finally, adjacent leaves are merged to yield a concise set of interpretable rules describing a given deep RL policy. We evaluate ORCAID across multiple RL environments, demonstrating that the extracted rule-based policies maintain strong performance with a low number of parameters and can even be used to improve the performance of the original deep RL policy.

</details>

---

### [[20_Research/Papers/强化学习/Validate_the_Dream_Before_You_Trust_Its_Verdict_Admissibility_for_World-Model_Simulators|Validate the Dream Before You Trust Its Verdict: Admissibility for World-Model Simulators]]

![[assets/2607.07196_first_page.png|800]]

- **arXiv**: [2607.07196](https://arxiv.org/abs/2607.07196)
- **PDF**: https://arxiv.org/pdf/2607.07196
- **详细分析**: [[20_Research/Papers/强化学习/Validate_the_Dream_Before_You_Trust_Its_Verdict_Admissibility_for_World-Model_Simulators|Validate the Dream Before You Trust Its Verdict: Admissibility for World-Model Simulators]]
- **作者**: Christian Oefinger, Finn Rasmus Schäfer, Korbinian Moller, Mattia Piccinini, Johannes Betz
- **cs 子类**: cs.AI, cs.LG, cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.16，世界模型 0.36，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Validate the Dream Before You Trust Its Verdict: Admissibility for World-Model Simulators》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Target-Bench, World-in-World, WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Across robotics, World Models (WMs) are increasingly used to evaluate action policies by simulating the consequences of actions in an imagined world, and returning a success or safety verdict. Yet a verdict is only as trustworthy as the WM that produced it, and the WM itself needs to be certified. In video-generation WMs, fidelity metrics such as Fréchet Video Distance (FVD) reward visual realism, but ignore whether the world responds correctly to the policy's actions, including those unseen in training. Classical simulation-based validation assumes a trusted simulator evaluating an untrusted policy, whereas generative WMs are themselves unverified learned artifacts. Hence, we argue that any WM used as a test oracle must first be accredited before its verdicts can serve as evidence. Building on credibility practices from safety-critical simulation, including Verification, Validation &amp; Accreditation (VV&amp;A), Safety of the Intended Functionality (SOTIF), and scenario-based testing standards, we define an admissibility ladder (L0-L4) that a WM must climb before its closed-loop verdicts are accepted as assurance evidence. Our framework is embodiment-agnostic, and is instantiated in autonomous driving (AD), where assurance methods for traditional simulation are most mature. Applied to two driving WMs, the lower rungs reveal a reversal: the model that ranks higher on visual generation quality (L0) ranks lower on action-following (L1-L2), so visual fidelity does not predict the action-robustness a closed-loop verdict depends on.

</details>

---

### [[20_Research/Papers/大模型/Entropy_Pacing_Policy_Optimization_for_Multi-Task_Agentic_Reinforcement_Learning|Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning]]

![[assets/2607.07178_figure.png|800]]

- **arXiv**: [2607.07178](https://arxiv.org/abs/2607.07178)
- **PDF**: https://arxiv.org/pdf/2607.07178
- **详细分析**: [[20_Research/Papers/大模型/Entropy_Pacing_Policy_Optimization_for_Multi-Task_Agentic_Reinforcement_Learning|Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning]]
- **作者**: Zetian Hu, Shunyu Liu, Junjie Zhang, Yongcheng Jing, Ting-En Lin, Yongbin Li, Dacheng Tao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.32（加权：大模型 0.4，强化学习 1.76，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent breakthroughs of Reinforcement Learning (RL) have highlighted its potential for complex agentic Large Language Model (LLM) tasks. However, existing efforts largely focus on single-task settings, whereas real-world deployment necessitates a generalist agent capable of solving multiple tasks simultaneously. In this work, we identify a critical yet underexplored phenomenon in multi-task agentic RL: different tasks can exhibit exploration-exploitation pace mismatch. Specifically, easier tasks may converge early to low-entropy policies that hinder learning on harder tasks, while harder tasks can, in turn, push easier tasks back toward high-entropy exploration. This back-and-forth interaction creates inter-task entropy crossovers and frequent entropy spikes. Inspired by this observation, we introduce Entropy Pacing Policy Optimization (EPPO) for multi-task agentic LLMs, which coordinates entropy across tasks to stabilize multi-task optimization. At the core of EPPO is a task-wise dynamic clipping mechanism that replaces the fixed clipping threshold in Group Relative Policy Optimization (GRPO) with a task entropy-aware adaptive bound, tightening updates for over-confident tasks while relaxing them for under-explored ones. Experiments on the multi-task agentic benchmarks demonstrate that the proposed EPPO yields results superior to its counterparts.

</details>

---

### [[20_Research/Papers/具身智能/GeoProp_Grounding_Robot_State_in_Vision_for_Generalist_Manipulation|GeoProp: Grounding Robot State in Vision for Generalist Manipulation]]

![[assets/2607.07101_figure.png|800]]

- **arXiv**: [2607.07101](https://arxiv.org/abs/2607.07101)
- **PDF**: https://arxiv.org/pdf/2607.07101
- **详细分析**: [[20_Research/Papers/具身智能/GeoProp_Grounding_Robot_State_in_Vision_for_Generalist_Manipulation|GeoProp: Grounding Robot State in Vision for Generalist Manipulation]]
- **作者**: Guoyang Zhao, Quanhao Qian, Gongjie Zhang, Wenhao Li, Jiuniu Wang, Xiaowei Lu, Deli Zhao, Ran Xu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《GeoProp: Grounding Robot State in Vision for Generalist Manipulation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proprioception is fundamental to robotic manipulation, yet standard fusion methods often treat it as an isolated vector lacking explicit alignment with visual tokens. Without a direct correspondence between 3D kinematics and 2D feature maps, manipulation policies struggle to ground the robot's state within the scene, frequently underperforming even vision-only baselines. To address this, we introduce GeoProp, a lightweight, plug-and-play adapter that aligns proprioception with vision through explicit geometric grounding and spatial feature sampling. GeoProp projects the robot state onto the image plane to sample localized visual features, constructing a grounded state token. It then injects state-derived spatial priors into the corresponding visual features via FiLM modulation. To capture motion intent, GeoProp further samples features at a short-horizon predicted coordinate derived from recent kinematics, providing look-ahead visual context. Across 67 tasks, GeoProp improves Diffusion Policy by 8.7% on 63 simulation tasks and pi_0 by 4.0% on the RoboTwin subset, and yields a 10.6% average gain across both policy families in the real world, while adding only 2-3% to the parameter count. These results demonstrate that GeoProp is a simple yet high-impact inductive bias for generalist embodied policies. Project page: https://alibaba-damo-academy.github.io/GeoProp/.

</details>

---

### [[20_Research/Papers/大模型/Operational_Reframing_and_Approval-Framed_Delegation_in_Multi-Agent_LLM_Safety|Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety]]

![[assets/2607.07097_figure.png|800]]

- **arXiv**: [2607.07097](https://arxiv.org/abs/2607.07097)
- **PDF**: https://arxiv.org/pdf/2607.07097
- **详细分析**: [[20_Research/Papers/大模型/Operational_Reframing_and_Approval-Framed_Delegation_in_Multi-Agent_LLM_Safety|Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety]]
- **作者**: Lifei Liu, Haoran Yu, Xiaochong Jiang, Su Wang, Pin Qian, Yihang Chen
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench, AgentCollabBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety evaluations of multi-agent LLM systems often compare a direct prompt with a planner-executor pipeline and report the difference as a single "pipeline effect." We argue that this aggregate is difficult to interpret because it conflates three mechanisms: harmful intent may be reframed as plausible operational work, the planner may refuse or transform the request, and the executor may act under delegation prompts implying prior approval. To separate these factors, we introduce a five-condition controlled contrast design, evaluated on 30 synthetic harmful scenarios and an exploratory external validation set from four agent-safety benchmarks using LLM-judged compliance. Our results show that aggregate pipeline safety is not a stable architectural property. Operational reframing is the most portable risk signal, increasing compliance for GPT, Gemini, and DeepSeek across both scenario sets, while Claude is comparatively resistant. Planner behavior can offset this risk mainly through refusal; however, when the planner produces executable steps, the executor may become more compliant than under the direct operational baseline. Approval-framed delegation is sensitive to prompt design, model pairing, and scenario source, and a skeptical executor prompt sharply reduces compliance. Raw-direct model rankings can also mispredict deployed planner-executor behavior. Gemini is safest under raw direct prompts in the primary set yet shows the largest amplification with a Claude planner, rising from 8.9 percent to 38.9 percent compliance. GPTs near-zero aggregate pipeline effect instead hides a reframing increase canceled by planner refusal. These findings suggest that multi-agent safety evaluations should report reframing, planner behavior, delegation framing, and model pairing separately before attributing failures to architecture itself.

</details>

---

### [[20_Research/Papers/大模型/Progressive_Crystallization_Turning_Agent_Exploration_into_Deterministic,_Lower-Cost_Workflows_in_Production|Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production]]

![[assets/2607.07052_figure.png|800]]

- **arXiv**: [2607.07052](https://arxiv.org/abs/2607.07052)
- **PDF**: https://arxiv.org/pdf/2607.07052
- **详细分析**: [[20_Research/Papers/大模型/Progressive_Crystallization_Turning_Agent_Exploration_into_Deterministic,_Lower-Cost_Workflows_in_Production|Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production]]
- **作者**: Arun Malik
- **cs 子类**: cs.AI, cs.DC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents deployed for IT operations are typically permanent cost centers because every execution requires full LLM inference, even for previously solved problems. This paper introduces progressive crystallization, a lifecycle that treats agent exploration as a discovery mechanism rather than a permanent execution model. It defines a three-stage execution taxonomy, from fully agent-orchestrated to hybrid to fully deterministic workflows, together with an evidence-based promotion mechanism that converts repeatedly validated agent behaviors into cheaper and more reproducible deterministic workflows, while automatically demoting workflows that regress. Evaluated on a production cloud networking AIOps system processing tens of thousands of incidents per month, the approach increased deterministic execution from 0% to 45% over eight months, reduced per-incident agent costs by more than 70% despite doubling incident volume, and improved safety through greater reproducibility and auditability. The paper also presents the execution taxonomy, promotion and demotion criteria, trace extraction methodology, economic model, safety considerations, and discusses limitations and threats to validity.

</details>

---

### [[20_Research/Papers/强化学习/Gimitest_A_Comprehensive_Tool_for_Testing_Reinforcement_Learning_Policies|Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies]]

![[assets/2607.07029_figure.png|800]]

- **arXiv**: [2607.07029](https://arxiv.org/abs/2607.07029)
- **PDF**: https://arxiv.org/pdf/2607.07029
- **详细分析**: [[20_Research/Papers/强化学习/Gimitest_A_Comprehensive_Tool_for_Testing_Reinforcement_Learning_Policies|Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies]]
- **作者**: Dennis Gross, Quentin Mazouni, Helge Spieker, Arnaud Gotlieb
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and multi-agent RL policies under varying conditions. Our implementation of this framework, Gimitest, is an open-source tool that supports various gym frameworks and allows for modifications of their integrated components. This article describes the framework and details Gimitest's functionality and architecture. It showcases its effectiveness in testing multiple RL policies in environments such as the official Farama Gymnasium and PettingZoo.

</details>

---

### [[20_Research/Papers/大模型/WAM-TTT_Steering_World-Action_Models_by_Watching_Human_Play_at_Test_Time|WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time]]

![[assets/2607.06988_figure.png|800]]

- **arXiv**: [2607.06988](https://arxiv.org/abs/2607.06988)
- **PDF**: https://arxiv.org/pdf/2607.06988
- **详细分析**: [[20_Research/Papers/大模型/WAM-TTT_Steering_World-Action_Models_by_Watching_Human_Play_at_Test_Time|WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time]]
- **作者**: Yusen Feng, Bingchen Han, Jiangran Lyu, Kai Liu, Yixin Zheng, Yuxuan Wan, Weiheng Liu, Sun Han, Ruiqin Li, Yulong Zhang, Fangfu Liu, Xuesong Shi...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Steering robot foundation models (RFMs) toward new task variants or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning, or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight adaptive memory inside a frozen WAM through self-supervised video prediction. To make this memory useful for control, we introduce a meta-training stage that aligns human demonstrations with robot behaviors using paired human-robot data and a key--value memory reconstruction objective. At test time, only unlabeled human videos are required to adapt the memory, while the pretrained WAM remains frozen. This enables efficient and reusable steering without robot actions, human-side annotations, or task-specific fine-tuning, while preserving the generalization ability of the foundation model. Extensive experiments show that WAM-TTT consistently outperforms in-context human-video conditioning baselines across diverse manipulation tasks and generalization settings.

</details>

---

### [[20_Research/Papers/大模型/End-to-End_LLM_Flight_Planning_with_RAG-based_Memory_and_Multi-modal_Coach_Agent|End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent]]

![[assets/2607.06964_figure.png|800]]

- **arXiv**: [2607.06964](https://arxiv.org/abs/2607.06964)
- **PDF**: https://arxiv.org/pdf/2607.06964
- **详细分析**: [[20_Research/Papers/大模型/End-to-End_LLM_Flight_Planning_with_RAG-based_Memory_and_Multi-modal_Coach_Agent|End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent]]
- **作者**: Amin Tabrizian, Arsyi Aziz, Aarifah Ullah, Mahyar Ghazanfari, Pouria Razzaghi, Peng Wei
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bridging the gap between human pilot intent and autonomous flight operation is critical for real-world electric vertical takeoff and landing (eVTOL) aircraft deployment. Flight planning traditionally relies on classic algorithms that struggle to incorporate flexible human preferences. We present FRAMe, an End-to-End Large Language Model (LLM) Flight Planning tool with RAG-based Memory and Multi-modal Coach Agent. Our system integrates a planner LLM with a multi-modal coach agent and retrieval augmented generation (RAG)-based memory to generate flight plans that satisfy mission constraints while aligning with human flight operator preferences. We demonstrate the system in a range of real-world-inspired scenarios of varying difficulty levels. Across four LLMs, the full FRAMe system (RAG and coach) yields the highest validity for every planner (up to 93.8% aggregate, 99% on Easy scenarios for the strongest planner) and shifts preference-relevant metrics in the operator-favored direction where the metric has headroom. FRAMe signifies how advanced LLMs can be deployed for human-centric mission planning, translating natural language instructions into safe, efficient, and flexible flight routes. The code is available at: github.com/amin-tabrizian/FlightPlanningLLMs

</details>

---

### [[20_Research/Papers/大模型/Comprehensive_Evaluation_of_Large_Language_Model_Responses_A_Multi-Factor_Scoring_System|Comprehensive Evaluation of Large Language Model Responses: A Multi-Factor Scoring System]]

![[assets/2607.06940_first_page.png|800]]

- **arXiv**: [2607.06940](https://arxiv.org/abs/2607.06940)
- **PDF**: https://arxiv.org/pdf/2607.06940
- **详细分析**: [[20_Research/Papers/大模型/Comprehensive_Evaluation_of_Large_Language_Model_Responses_A_Multi-Factor_Scoring_System|Comprehensive Evaluation of Large Language Model Responses: A Multi-Factor Scoring System]]
- **作者**: Yiming Gai, Junde Lu, Xuefei Huang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Comprehensive Evaluation of Large Language Model Responses: A Multi-Factor Scoring System》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The remarkable performance of large language models (LLMs) in linguistic tasks underscores an urgent need for comprehensive evaluation of their response quality. Prevailing methods, often confined to singular dimensions, fall short of capturing the full spectrum of model capabilities. This study introduces a multifactor scoring paradigm, integrating accuracy, conciseness, factual consistency, readability, and coherence, complemented by a graphical user interface (GUI) for visualizing outcomes. Evaluations on the TruthfulQA dataset unveil mainstream LLMs' strengths in reasoning tasks (peaking at a composite score of 0.6104) alongside pervasive limitations in navigating complex facts and ambiguities. Transcending the narrow lens of traditional metrics, this framework offers a transparent, adaptable avenue to illuminate model potential and deficiencies. Though presently focused on English tasks, its horizons beckon toward multilingual domains. This work carves a novel path for knowledge engineering and model refinement.

</details>

---

### [[20_Research/Papers/世界模型/Grounding_Spatial_Relations_in_a_Compact_World_Model_Instruction_Leakage_and_a_Goal-Free_Dynamics_Fix|Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix]]

![[assets/2607.06925_figure.png|800]]

- **arXiv**: [2607.06925](https://arxiv.org/abs/2607.06925)
- **PDF**: https://arxiv.org/pdf/2607.06925
- **详细分析**: [[20_Research/Papers/世界模型/Grounding_Spatial_Relations_in_a_Compact_World_Model_Instruction_Leakage_and_a_Goal-Free_Dynamics_Fix|Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix]]
- **作者**: Yufeng Wang, Lu Wei, Haibin Ling
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compact world models that condition on a language goal promise to ground relations such as ``put the red block left of the blue block'' using a sparse set of explicit \emph{reference anchors}. We ask when such references actually ground a relation, and identify a trap: a goal-conditioned predictor reaches a striking $0.90$ relation-readout accuracy, yet this is \emph{instruction transcription}, not perception. Withholding the goal collapses it to chance ($0.90\!\to\!0.27$, three seeds) and a counterfactual instruction makes the predicted anchors follow the \emph{false} instruction $94.5\%$ of the time (true scene $2.3\%$; $N{=}256$). Tested across three settings and a within-task ablation, our central claim characterizes the confound: \textbf{instruction leakage occurs when the scored quantity is transcribable from the instruction (when the instruction names the answer) and is essentially independent of how predictive the non-instruction inputs are.} Our tabletop and the external BabyAI benchmark leak, whereas a Language-Table forward-dynamics world model whose instruction names \emph{referents} does not, until the instruction is augmented to name the direction; and degrading the action never increases leakage, the opposite of what predictor-competition predicts. The diagnosis prescribes the fix: keep the goal out of the dynamics (it belongs to the planner's cost) and supervise the \emph{read} path, recovering genuine, instruction-independent grounding ($0.88$, identical with and without the goal). The detection protocol and remedy apply to any goal-conditioned world model whose instruction names the scored quantity.

</details>

---

### [[20_Research/Papers/具身智能/GemNav_Discrete-Token_Visual_Robot_Navigation_using_a_Multimodal_Large_Language_Model|GemNav: Discrete-Token Visual Robot Navigation using a Multimodal Large Language Model]]

![[assets/2607.06882_figure.png|800]]

- **arXiv**: [2607.06882](https://arxiv.org/abs/2607.06882)
- **PDF**: https://arxiv.org/pdf/2607.06882
- **详细分析**: [[20_Research/Papers/具身智能/GemNav_Discrete-Token_Visual_Robot_Navigation_using_a_Multimodal_Large_Language_Model|GemNav: Discrete-Token Visual Robot Navigation using a Multimodal Large Language Model]]
- **作者**: Peter Bohm, Saimunur Rahman, Abdelwahed Khamis, Sagun Man Singh Shrestha, Chris McCool, Peyman Moghadam
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 4.0（加权：具身智能 1.5，大模型 1.4，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《GemNav: Discrete-Token Visual Robot Navigation using a Multimodal Large Language Model》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BridgeVLA, OmniVLA, VLM2VLA, VLM4VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual navigation policies built on large pretrained models have so far followed a common recipe: a dedicated visual encoder, a bespoke action head, and training on thousands of hours of cross-embodiment datasets. We ask whether this recipe is necessary. In this paper, we introduce GemNav, a visual robot navigation policy that adapts a frozen Multimodal Large Language Model (MLLM) for short-to-medium horizon waypoint navigation using Low-Rank Adaptation (LoRA) on the language tower alone, with no auxiliary visual encoder and no continuous regression head. Waypoints and categorical navigation signals share a single discrete token vocabulary generated by the language-model head, and a soft-decoded auxiliary loss recovers the metric structure that pure cross-entropy training discards. On a single 8.7-hour open corpus, roughly three orders of magnitude smaller than competing training sets, the policy transfers zero-shot to four physically distinct unseen environments and stops within 0.25-0.42m of the goal across 20 real-world trials covering an open carpark, an obstacle carpark, a long outdoor chemical yard, and an indoor warehouse. Conditioning on short image histories improves offline metrics but yields no robot benefit, pointing to a ceiling on what temporal context adds once pretrained vision features are in place. These results indicate that discrete-token adaptation of frozen MLLMs can provide a data-efficient, deployable alternative for foundation model robot navigation.

</details>

---

### [[20_Research/Papers/大模型/A_Gold-Standard_Study_of_What_Makes_a_Lightweight_Game-Playing_Agent_Strong|A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong]]

![[assets/2607.06854_figure.png|800]]

- **arXiv**: [2607.06854](https://arxiv.org/abs/2607.06854)
- **PDF**: https://arxiv.org/pdf/2607.06854
- **详细分析**: [[20_Research/Papers/大模型/A_Gold-Standard_Study_of_What_Makes_a_Lightweight_Game-Playing_Agent_Strong|A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong]]
- **作者**: Nima Kelidari, Mohammadsaeed Haghi, Mahdi Salmani
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.22（加权：大模型 0.7，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning agents for imperfect-information card games are only as strong as the opponents they train against, and they are hard to grade, since they beat a random opponent over 99 percent of the time and only tie copies of themselves. So we build a strong, fixed, rule-based expert for Gin Rummy and use it only as a yardstick, never for training. It beats every agent we trained 70 to 99 percent of the time. Across more than a hundred runs, we isolate what makes a lightweight agent stronger. Trust region updates, a well-aimed reward, a curriculum of tougher opponents, warm starting, and keeping the best checkpoint all help, and stacking them lifts a self-play champion from about 30 to 36 percent against the expert. Several ideas did not pay off. Short-term and longer-term reward shaping, learned state embeddings, imitation and DAgger, and a live large language model opponent were each unhelpful, too slow, or too heavy to train at scale. Comparing MLP, convolutional, set-based, attention, and recurrent encoders shows that extra capacity does little to break the ceiling, suggesting the limit is information rather than network size. We add standard baselines (neural fictitious self-play and information set Monte Carlo search) and confirm the approach carries over to Leduc Hold'em, where the optimum is computable. The result is a lightweight, game-agnostic recipe that trains competitive agents without training on the expert, for any game a small model can handle, reported with robust statistics and released as a reusable package.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_SageMath-Augmented_LLM_Agents_for_Computational_and_Experimental_Mathematics|Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics]]

![[assets/2607.06820_figure.png|800]]

- **arXiv**: [2607.06820](https://arxiv.org/abs/2607.06820)
- **PDF**: https://arxiv.org/pdf/2607.06820
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_SageMath-Augmented_LLM_Agents_for_Computational_and_Experimental_Mathematics|Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics]]
- **作者**: Pavel Snopov, German Magai
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IMProofBench, IntegralBench, PutnamBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in AI for Mathematics have focused largely on autoformalization and theorem proving, leaving the role of Computer Algebra Systems (CAS) in agentic LLM workflows underexplored. We propose a ReAct-style agentic setup that combines LLM reasoning with verifiable feedback from SageMath, together with Context7 for the up-to-date documentation. We evaluate this agentic setup across frontier models for solving research-level mathematical problems from the RealMath benchmark in a setting that emulates a computational-mathematics research loop. We also propose a refinement to the RealMath benchmark by introducing a multi-step post-processing procedure and a multi-stage validation pipeline, both of which improve the quality and reliability of the extracted problem set. Our experiments reveal substantial performance gains from SageMath access across all evaluated models on +9.7~pp on average, the gains range from 1.5~pp to 27.8~pp and narrow the gap between open-weight and closed models. Qwen~3.7-Max benefits from SageMath the most, while GPT-5.5 achieves the highest solve rate of $75.2\%$ and the lowest token usage among tool-enabled configurations. Our findings suggest that CAS-augmented agents represent a promising direction for assisting mathematicians in computational exploration, and we believe that this work is a step towards automated conjecture discovery. The project repository is available online.

</details>

---

### [[20_Research/Papers/大模型/Ad_Headline_Generation_using_Self-Critical_Masked_Language_Model|Ad Headline Generation using Self-Critical Masked Language Model]]

![[assets/2607.06818_figure.png|800]]

- **arXiv**: [2607.06818](https://arxiv.org/abs/2607.06818)
- **PDF**: https://arxiv.org/pdf/2607.06818
- **详细分析**: [[20_Research/Papers/大模型/Ad_Headline_Generation_using_Self-Critical_Masked_Language_Model|Ad Headline Generation using Self-Critical Masked Language Model]]
- **作者**: Yashal Shakti Kanungo, Sumit Negi, Aruna Rajan
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.45，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Ad Headline Generation using Self-Critical Masked Language Model》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For any E-commerce website it is a nontrivial problem to build enduring advertisements that attract shoppers. It is hard to pass the creative quality bar of the website, especially at a large scale. We thus propose a programmatic solution to generate product advertising headlines using retail content. We propose a state of the art application of Reinforcement Learning (RL) Policy gradient methods on Transformer based Masked Language Models. Our method creates the advertising headline by jointly conditioning on multiple products that a seller wishes to advertise. We demonstrate that our method outperforms existing Transformer and LSTM + RL methods in overlap metrics and quality audits. We also show that our model-generated headlines outperform human submitted headlines in terms of both grammar and creative quality as determined by audits.

</details>

---

### [[20_Research/Papers/大模型/When_Agents_Go_Rogue_Activation-Based_Detection_of_Malicious_Behaviors_in_Multi-Agent_Systems|When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems]]

![[assets/2607.06807_figure.png|800]]

- **arXiv**: [2607.06807](https://arxiv.org/abs/2607.06807)
- **PDF**: https://arxiv.org/pdf/2607.06807
- **详细分析**: [[20_Research/Papers/大模型/When_Agents_Go_Rogue_Activation-Based_Detection_of_Malicious_Behaviors_in_Multi-Agent_Systems|When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems]]
- **作者**: Haowen Xu, Xue Tan, Lei Ma, Zhihao Zhang, Chao Wang, Qingze Wang, Ping Chen, Jun Dai, Xiaoyan Sun
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HotPotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchronous without the temporal alignment assumed by graph-based propagation models. To address these limitations, we propose AcMAS, an activation-based framework for malicious-behavior detection in MAS. By analyzing internal reasoning states in the activation space of local agents, AcMAS detects even stealthy attacks in a synchronization-robust fashion, without relying on explicit interaction graphs. Moreover, our activation analysis provides critical signals to guide AcMAS in restoring the functionality of compromised agents, rather than the disruptive agent isolation commonly used by the state-of-the-art methods. Comprehensive evaluation demonstrates that AcMAS significantly outperforms graph-based baselines against stealthy attacks, by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38), with generalization across diverse open-source LLM backbones, attack intensity, and MAS scale.

</details>

---

### [[20_Research/Papers/其他/QANTIS_Hardware-Calibrated_Sequential_POMDP_Belief_Updates_on_IBM_Heron|QANTIS: Hardware-Calibrated Sequential POMDP Belief Updates on IBM Heron]]

![[assets/2607.06760_first_page.png|800]]

- **arXiv**: [2607.06760](https://arxiv.org/abs/2607.06760)
- **PDF**: https://arxiv.org/pdf/2607.06760
- **详细分析**: [[20_Research/Papers/其他/QANTIS_Hardware-Calibrated_Sequential_POMDP_Belief_Updates_on_IBM_Heron|QANTIS: Hardware-Calibrated Sequential POMDP Belief Updates on IBM Heron]]
- **作者**: Bayram Yuksel Eker, Suayb S. Arslan, Ozgur Nazli, Mustafa Serhat Demirgil, Furkan Deligoz
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《QANTIS: Hardware-Calibrated Sequential POMDP Belief Updates on IBM Heron》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：QBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems under partial observability act on beliefs, not raw sensor events. QANTIS treats the quantum processor as a calibrated belief-update service in that loop: it receives a prior and an observation model, estimates the rare-event evidence term, and returns an ordinary posterior to a classical planner. This paper asks whether that service can be reused across a sequential Tiger POMDP horizon on present IBM Heron hardware without corrupting the planner-facing posterior. We answer with a controlled hardware case study rather than an end-to-end autonomy or wall-clock speedup claim. The study compares no amplification, guarded Grover amplification, and all-step fixed-point amplification on the same trajectory, then checks whether the returned posterior would change the downstream action. All-step FPAA preserves the Tiger posterior across the reported 8-step and 12-step primary runs, and the 20-step and 32-step controls remain inside the same operating band. In every reported decision check, the hardware posterior and the exact Bayes posterior select the same immediate action. Boundary-aware BIQAE stabilizes amplitude estimation near zero and near one, while a rare-event sweep maps the logical sample-complexity envelope for one-in-a-million evidence. The result is an operating envelope for a hardware-calibrated belief-update primitive, not a standalone hardware-advantage claim.

</details>

---

### [[20_Research/Papers/大模型/LLM-powered_reasoning_in_agent-based_modeling|LLM-powered reasoning in agent-based modeling]]

![[assets/2607.06757_figure.png|800]]

- **arXiv**: [2607.06757](https://arxiv.org/abs/2607.06757)
- **PDF**: https://arxiv.org/pdf/2607.06757
- **详细分析**: [[20_Research/Papers/大模型/LLM-powered_reasoning_in_agent-based_modeling|LLM-powered reasoning in agent-based modeling]]
- **作者**: Sifat Afroj Moon, Dakotah Maguire, Adam Spannaus, Joe Tuccillo, Maksudul Alam, Sudip K. Seal, John Gounley, Heidi Hanson
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《LLM-powered reasoning in agent-based modeling》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent-based modeling (ABM) has the capability to model millions of individuals and their interactions, which is useful for policy making. However, ABMs have traditionally relied on static prior, which prevents the models from adapting to real-time changes. Our research provides a novel approach to addressing this information gap. Large language models (LLMs) offer new opportunities to predict human decision-making. Here, we introduce a scalable Hybrid Agent-based and Language-driven Epidemic (HALE) modeling framework that leverages LLMs to predict human decision-making in an ABM simulation. As a proof-of-concept, we use HALE to simulate COVID-19 and its effects in Salt Lake County, UT.

</details>

---

### [[20_Research/Papers/具身智能/A_Continual_Learning_Framework_for_Adaptive_Control_of_Modular_Soft_Robots|A Continual Learning Framework for Adaptive Control of Modular Soft Robots]]

![[assets/2607.06740_figure.png|800]]

- **arXiv**: [2607.06740](https://arxiv.org/abs/2607.06740)
- **PDF**: https://arxiv.org/pdf/2607.06740
- **详细分析**: [[20_Research/Papers/具身智能/A_Continual_Learning_Framework_for_Adaptive_Control_of_Modular_Soft_Robots|A Continual Learning Framework for Adaptive Control of Modular Soft Robots]]
- **作者**: Nilay Kushawaha, Muhammad Sunny Nazeer, Baljinder Singh Bal, Cecilia Laschi, Egidio Falotico
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Continual Learning Framework for Adaptive Control of Modular Soft Robots》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft robots have attracted significant attention in applications such as medical intervention, rehabilitation, and robotic manipulation due to their inherent compliance, flexibility, and high degrees of freedom. Modular soft robots (MSRs), composed of multiple interconnected segments, represent an emerging class of robotic systems with highly deformable and reconfigurable structures capable of performing complex tasks. However, designing controllers for MSRs remains challenging due to their nonlinear dynamics, modeling complexity, and hyper-redundant nature. Existing approaches typically require controllers to be retrained from scratch whenever the robot morphology changes. In this work, we address these challenges through a continual learning inspired control framework capable of incrementally adapting to changes in robot morphology while preserving previously acquired knowledge. Specifically, the proposed framework enables the controller to sequentially learn new MSR configurations without forgetting previously learned ones. In addition, for MSRs with fixed configurations, the same framework can be employed in a distributed manner to learn module-specific dynamics, enabling localized control and improved precision. The proposed approach is validated through closed-loop trajectory tracking experiments in simulation using a tendon-driven soft robot, as well as on a real-world three-module pneumatic soft robotic arm. Furthermore, we demonstrate the adaptive capabilities of the framework through a reaching experiment in which the controller selectively activates only the necessary modules to reach a virtual target position, thereby reducing computational overhead.

</details>

---

### [[20_Research/Papers/具身智能/Vision_Language_Action_(VLA)_Models_for_Unmanned_Aerial_Robotics_and_Bimanual_Manipulation_A_Review|Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review]]

![[assets/2607.06706_first_page.png|800]]

- **arXiv**: [2607.06706](https://arxiv.org/abs/2607.06706)
- **PDF**: https://arxiv.org/pdf/2607.06706
- **详细分析**: [[20_Research/Papers/具身智能/Vision_Language_Action_(VLA)_Models_for_Unmanned_Aerial_Robotics_and_Bimanual_Manipulation_A_Review|Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review]]
- **作者**: Inkyu Sa, Chanoh Park, Hea-Min Lee, Donghee Noh, Ho Seok Ahn
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 强化学习, 大模型
- **相关性评分**: 3.82（加权：具身智能 1.5，大模型 0.1，强化学习 0.16，世界模型 0.36，机器人 1.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision Language Action (VLA) models unify visual perception, natural-language understanding, and action generation within a single foundation model, allowing a robot to follow instructions such as fold the towel or fly to the red building directly from camera images. Because VLAs inherit world knowledge from internet-scale pre-training, they have become the dominant framework for learning-based manipulation, with bimanual coordination serving as the most demanding testbed: two arms with 7 degrees of freedom each must move in concert to fold, assemble, and reorient objects. Unmanned aerial robotics faces a structurally similar challenge: a drone must coordinate thrust, attitude, and increasingly gripper commands from visual observations under strict latency and payload constraints. This review covers 183 contributions spanning 2017-2026 and organized along seven dimensions: VLA architectures, training recipes, action representations, bimanual coordination (2022-2026), unmanned aerial vehicle (UAV) navigation and control (2017-2026), language grounding, and cross-cutting concerns including memory and world models. We show that the coordination strategies, training recipes, and action representations developed for bimanual VLAs transfer to unmanned aerial systems and identify fourteen research directions across both domains.

</details>

---

### [[20_Research/Papers/具身智能/SPEAR_A_Simulator_for_Photorealistic_Embodied_AI_Research|SPEAR: A Simulator for Photorealistic Embodied AI Research]]

![[assets/2607.06701_figure.jpg|800]]

- **arXiv**: [2607.06701](https://arxiv.org/abs/2607.06701)
- **PDF**: https://arxiv.org/pdf/2607.06701
- **详细分析**: [[20_Research/Papers/具身智能/SPEAR_A_Simulator_for_Photorealistic_Embodied_AI_Research|SPEAR: A Simulator for Photorealistic Embodied AI Research]]
- **作者**: Mike Roberts, Renhan Wang, Rushikesh Zawar, Rachith Dey-Prakash, Quentin Leboutet, Stephan R. Richter, Matthias Müller, German Ros, Rui Tang, Stefan Leutenegger, Yannick Hold-Geoffroy, Kalyan Sunkavalli...
- **cs 子类**: cs.AI, cs.CV, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 2.7，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《SPEAR: A Simulator for Photorealistic Embodied AI Research》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AirSim, IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive simulators have become powerful tools for training embodied agents and generating synthetic visual data, but existing photorealistic simulators suffer from limited generality, programmability, and rendering speed. We address these limitations by introducing SPEAR: A Simulator for Photorealistic Embodied AI Research. At its core, SPEAR is a Python library that can connect to, and programmatically control, any Unreal Engine (UE) application via a modular plugin architecture. SPEAR exposes over 14K unique UE functions to Python, representing an order-of-magnitude increase in programmable functionality over existing UE-based simulators. Additionally, a single SPEAR instance can render 1920x1080 photorealistic beauty images directly into a user's NumPy array at 73 frames per second - an order of magnitude faster than existing UE plugins - while also providing ground truth image modalities that are not available in any existing UE-based simulator (e.g., a non-diffuse intrinsic image decomposition, material IDs, and physically based shading parameters). Finally, SPEAR introduces an expressive high-level programming model that enables users to specify complex graphs of UE work with arbitrary data dependencies among work items, and to execute these graphs deterministically within a single UE frame. We demonstrate the utility of SPEAR through a diverse collection of example applications: controlling multiple embodied agents with distinct action spaces (e.g., humans, cars, and robots) across several in-the-wild UE projects; rendering photorealistic city-scale environments; manipulating UE's procedural content generation systems; rendering synchronized multi-view images of detailed human faces; coordinating an interactive co-simulation with the MuJoCo physics simulator; and editing scenes with natural language via an AI coding assistant.

</details>

---

### [[20_Research/Papers/大模型/Healthier_LLMs_Retrieval-Augmented_Generation_for_Public_Health_Question_Answering|Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering]]

![[assets/2607.06641_figure.png|800]]

- **arXiv**: [2607.06641](https://arxiv.org/abs/2607.06641)
- **PDF**: https://arxiv.org/pdf/2607.06641
- **详细分析**: [[20_Research/Papers/大模型/Healthier_LLMs_Retrieval-Augmented_Generation_for_Public_Health_Question_Answering|Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering]]
- **作者**: Felix Feldman, Joshua Harris, Timothy Laurence, Leo Loman, Ollie Higgins, Fan Grayson, Poonam Soma, Bethany Pace-Bonello, Michael Borowitz, Toby Nonnenmacher
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AfriMed-QA, MCQA, MedMCQA, MedQA, PubHealthBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) achieve promising results on medical question answering benchmarks, yet their use in public health is constrained by hallucinations and the rapid evolution of official guidance. Retrieval-Augmented Generation (RAG) mitigates these risks by grounding responses in an explicitly maintained corpus, but end-to-end performance depends critically on retrieval configuration and on evaluation beyond multiple-choice formats. We extend PubHealthBench, a question answering (QA) benchmark of 7,929 questions derived from UK Government public health guidance, into a retrieval-augmented setting and systematically evaluate retrieval and generation choices. We compare dense, sparse, and hybrid retrieval across multiple embedding models and corpus variants, and show that hybrid retrieval consistently improves recall and ranking quality, with chunk length and topic interacting with ranking performance. Providing retrieved context substantially increases multiple-choice accuracy across a diverse set of LLMs, enabling smaller open-weight models to match or outperform larger models used without retrieval, with gains primarily driven by retrieval quality and careful context selection. To assess realistic free-form answering, we introduce a rubric-based LLM-as-a-judge covering faithfulness, completeness, clarity, and factual consistency, and validate it against dual human annotations. Judge-human agreement is strongest for faithfulness and completeness, while factual consistency and clarity are less reliably reproduced, motivating caution when interpreting those dimensions at scale. Overall, our results highlight retrieval as a primary lever for reliable public health QA and provide practical guidance for building and evaluating RAG systems grounded in official guidance.

</details>

---

### [[20_Research/Papers/强化学习/The_Rank-One_Corner_How_Much_Value_Equivalence_Does_a_Task_Need_from_a_World_Model|The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?]]

![[assets/2607.06640_figure.png|800]]

- **arXiv**: [2607.06640](https://arxiv.org/abs/2607.06640)
- **PDF**: https://arxiv.org/pdf/2607.06640
- **详细分析**: [[20_Research/Papers/强化学习/The_Rank-One_Corner_How_Much_Value_Equivalence_Does_a_Task_Need_from_a_World_Model|The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?]]
- **作者**: Donna Vakalis
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A learned world model is usually judged by how faithfully it reconstructs its observations or predicts reward, as though quality were something the model simply has or lacks. But what a task actually needs from a model is narrower: the few predictive coordinates its queries depend on, which we call the closure. We show that how much of that closure a latent comes to represent is set not by the model's capacity or its observations but by the dimensionality of the objective it is trained against, and we measure this directly on a DreamerV3 stack in a controlled environment with known ground-truth closure. An aligned scalar value signal -- the objective at the heart of value equivalence -- installs only a one-dimensional projection of a closure that needs several dimensions: read through a single linear probe, the recoverable structure rises from R^2=0.10 to 0.76 as the scalar is replaced by the full objective. Sweeping the objective's dimensionality from one to four installs exactly that many predictive directions through an auxiliary head, and the same staircase appears -- at attenuated magnitude but the same rank -- through the model's own value head, so the dissociation is dimensional rather than an artifact of head form. Capacity-matched comparisons and in-situ pressure checks rule out the obvious alternatives. The law governs a regime, and we measure its boundary: on a companion closed-loop task whose structure is observable frame by frame, reconstruction installs that structure and the scalar objective suffices -- the objective decides what a latent represents exactly where cheaper training signals cannot already recover it. Value equivalence is thus not all-or-nothing but dimensional: the familiar single-reward objective is its rank-one corner, and a model installs as much of a task's structure as the objective it is asked to predict.

</details>

---

### [[20_Research/Papers/大模型/AgentLens_Production-Assessed_Trajectory_Reviews_for_Coding_Agent_Evaluation|AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation]]

![[assets/2607.06624_first_page.png|800]]

- **arXiv**: [2607.06624](https://arxiv.org/abs/2607.06624)
- **PDF**: https://arxiv.org/pdf/2607.06624
- **详细分析**: [[20_Research/Papers/大模型/AgentLens_Production-Assessed_Trajectory_Reviews_for_Coding_Agent_Evaluation|AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation]]
- **作者**: Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy, Maksim Parshin, Sergey Nikolenko
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present AgentLens, a production-assessed benchmark for interactive code agents. Most code-agent benchmarks reduce a run to a single bit -- did the task pass? -- but the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory. It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: we use it to diagnose model behavior, compare successive versions of our own agent, and catch product regressions in a nightly evaluation pipeline. We release the benchmark as open source at https://github.com/agent-lens/agent-lens-bench.

</details>

---

### [[20_Research/Papers/大模型/LLM-Guided_Task-Semantic_Field_Factorization_for_Industrial_Process_Forecasting|LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting]]

![[assets/2607.06623_figure.png|800]]

- **arXiv**: [2607.06623](https://arxiv.org/abs/2607.06623)
- **PDF**: https://arxiv.org/pdf/2607.06623
- **详细分析**: [[20_Research/Papers/大模型/LLM-Guided_Task-Semantic_Field_Factorization_for_Industrial_Process_Forecasting|LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting]]
- **作者**: Youcheng Zong, Runda Jia, Mingxuan Ren, Dakuo He
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Process industries rely on time-series forecasting and soft sensing to estimate quality variables that are hard to measure online. Labeled data are scarce, operating regimes change frequently, and retraining models or rebuilding alignment pipelines for each scenario is costly. Such settings often provide variable tables and process documents that record variable names, units, physical meanings, and process roles. However, standard time-series backbones usually treat inputs as anonymous numerical columns. Existing text-enhanced methods also rarely make the semantic-logical relations between input variables and the prediction target available to the model within each numerical window. To address this problem, this article proposes Task-Semantic Field Factorization (TSF), a large language model (LLM)-guided framework. TSF builds a task-semantic field from task protocols and variable documents before training and uses the LLM only for offline semantic construction. Online training and inference remain with conventional time-series backbones. During training and inference, the current numerical window activates variable semantics, so semantic information participates in each prediction and supports adaptation to different prediction targets and operating shifts. On multiple complex industrial forecasting and soft-sensing tasks, TSF reduces MAE by 6.4\% on average in improved settings, with the largest reduction reaching 25.5\%. It adds only about 1.8--3.0k parameters, with less than 0.008 ms/step of additional online inference overhead. These results show that TSF turns existing process documents into measurable forecasting gains across backbones and semantic generators while remaining lightweight for deployment.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Reliability_Based_Bi-Objective_Portfolio_Optimization|Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization]]

![[assets/2607.06610_figure.png|800]]

- **arXiv**: [2607.06610](https://arxiv.org/abs/2607.06610)
- **PDF**: https://arxiv.org/pdf/2607.06610
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Reliability_Based_Bi-Objective_Portfolio_Optimization|Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization]]
- **作者**: Sounaq Das, Tanmay Sen, Raghu Nandan Sengupta, Aditya Gupta
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 2.12（加权：强化学习 1.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Deep Reinforcement Learning for Reliability Based Bi-Objective Portfolio Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MORP-DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Portfolio optimization under uncertainty is inherently a multi-objective decision problem involving complex interactions among return, risk, market dynamics, and practical investment constraints. Existing reliability based portfolio optimization approaches primarily rely on static optimization frameworks and often fail to capture sequential decision making, tail risk, and market frictions such as transaction costs. To address these limitations, we propose a deep reinforcement learning framework for multi-objective reliability based portfolio optimization (MORP-DRL). The proposed framework jointly optimizes expected return and downside risk using three complementary risk measures: variance, Conditional Value-at-Risk (CVaR), and Entropic Value-at-Risk (EVaR). To model uncertainty and heavy-tailed market behavior, asset returns are represented using GARCH(1,1), Extreme Value Theory, and a t-copula dependence structure, while realistic scenarios are generated through quasi-Monte Carlo simulation. A Proximal Policy Optimization (PPO) based strategy is developed under practical constraints including transaction costs and portfolio bounds, and is benchmarked against NSGA-II. Experiments on ten global equity indices across pre-COVID, COVID, and post-COVID market regimes demonstrate that MORP-DRL achieves competitive risk-return performance, reduced downside risk during periods of market stress, and scalability to high-dimensional portfolio settings.

</details>

---

### [[20_Research/Papers/机器人/MiLSD_A_Micro_Line-Segment_Detector_for_Resource-Constrained_Devices|MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices]]

![[assets/2607.06600_figure.png|800]]

- **arXiv**: [2607.06600](https://arxiv.org/abs/2607.06600)
- **PDF**: https://arxiv.org/pdf/2607.06600
- **详细分析**: [[20_Research/Papers/机器人/MiLSD_A_Micro_Line-Segment_Detector_for_Resource-Constrained_Devices|MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices]]
- **作者**: Parsa Hassani Shariat Panahi, Amir Hossein Jalilvand, M. Hassan Najafi
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《MiLSD: A Micro Line-Segment Detector for Resource-Constrained Devices》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LSDNet, MCUNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Line segment detection is a key building block in visual SLAM, 3D reconstruction, and industrial inspection. Recent deep learning methods have greatly improved accuracy, yet even the smallest models require several megabytes of memory, exceeding low-cost MCU capacity. This work investigates the maximum achievable accuracy under a sub-megabyte budget. We propose MiLSD, a detector tailored for MCU-level constraints, and systematically compare three output representations within a compact fully-convolutional backbone. Our study shows that the proposed F-Clip center-with-length-and-angle formulation learns most effectively at small model sizes. We find that 8-bit quantization preserves full-precision performance, while 4-bit quantization causes significant degradation, particularly in angle regression, with quantization-aware training recovering only part of the loss. With a one-megabyte activation budget and inference enhancements including sub-pixel decoding, test-time augmentation, and a lightweight verifier, MiLSD improves sAP10 on ShanghaiTech Wireframe from 10.6 (25k parameters, 0.25 MB) to 24.1 within 1 MB. Rather than competing with GPU-scale parsers, we map the accuracy memory trade-off across representations, bit-widths, capacities, and post-processing strategies for embedded vision systems.

</details>

---

### [[20_Research/Papers/大模型/When_Agents_Remember_Too_Much_Memory_Poisoning_Attacks_on_Large_Language_Model_Agents|When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents]]

![[assets/2607.06595_figure.png|800]]

- **arXiv**: [2607.06595](https://arxiv.org/abs/2607.06595)
- **PDF**: https://arxiv.org/pdf/2607.06595
- **详细分析**: [[20_Research/Papers/大模型/When_Agents_Remember_Too_Much_Memory_Poisoning_Attacks_on_Large_Language_Model_Agents|When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents]]
- **作者**: George Torres, Sharad Shrestha, Satyajayant Misra
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities. In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store. GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents. This attack is possible due to the lack of security-focused memory governance. In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility.

</details>

---

### [[20_Research/Papers/强化学习/Can_Reinforcement_Learning_Efficiently_Discover_Price_Manipulation|Can Reinforcement Learning Efficiently Discover Price Manipulation?]]

![[assets/2607.06121_figure.png|800]]

- **arXiv**: [2607.06121](https://arxiv.org/abs/2607.06121)
- **PDF**: https://arxiv.org/pdf/2607.06121
- **详细分析**: [[20_Research/Papers/强化学习/Can_Reinforcement_Learning_Efficiently_Discover_Price_Manipulation|Can Reinforcement Learning Efficiently Discover Price Manipulation?]]
- **作者**: Ioanna-Yvonni Tsaknaki, Andrea Macrì, Fabrizio Lillo
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Can Reinforcement Learning Efficiently Discover Price Manipulation?》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we investigate whether a model-free RL agent can identify and exploit price manipulation opportunities more effectively than a traditional model-based approach that assumes correct specification of the data-generating process but relies on noisy parameter estimates. We consider a single-asset market in which prices evolve according to an Almgren-Chriss framework with non-linear permanent impact and linear temporary impact. We first establish the existence of price-manipulative strategies in discrete time and compute the optimal benchmark strategy using Sequential Least Squares Quadratic Programming under full information. We then compare two finite-sample learning approaches: a model-based procedure that estimates impact parameters from simulated execution data and an agnostic RL approach based on Deep Deterministic Policy Gradient, trained directly on the same amount of data. For intermediate volatility, the RL agent successfully discovers profitable manipulative strategies without explicit knowledge of the underlying model, even when training data are quite limited. More importantly, RL consistently outperforms the model-based approach when parameter estimates are affected by sampling error, despite the latter benefiting from the correct model specification. For large volatility, all methods are unable to identify manipulation opportunities, while for small volatility, the model based approach outperforms RL. These findings highlight both the effectiveness of RL in complex control problems and the risks associated with deploying learning algorithms in financial markets without appropriate safeguards.

</details>

---
