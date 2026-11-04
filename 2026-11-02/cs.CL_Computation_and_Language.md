# cs.CL | Computation and Language | 2026-11-02

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/Latent_Reasoning_in_Continuous_Space_for_Unified_Multimodal_Models|Latent Reasoning in Continuous Space for Unified Multimodal Models]]

![[assets/2610.42149_figure.png|800]]

- **arXiv**: [2610.42149](https://arxiv.org/abs/2610.42149)
- **PDF**: https://arxiv.org/pdf/2610.42149
- **详细分析**: [[20_Research/Papers/大模型/Latent_Reasoning_in_Continuous_Space_for_Unified_Multimodal_Models|Latent Reasoning in Continuous Space for Unified Multimodal Models]]
- **作者**: Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Latent Reasoning in Continuous Space for Unified Multimodal Models》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DPG-Bench, GenEval, OneIG-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space, whereas image generation operates in a continuous space. To bridge this gap, we introduce a Latent Reasoning framework in Continuous space (LARC), which alleviates the token-level bottleneck by reasoning over continuous hidden states. Specifically, the training framework consists of two stages: (i) curriculum supervised fine-tuning (SFT), and (ii) information-gain reinforcement learning (RL). First, the curriculum SFT stage gradually converts token-level reasoning into latent reasoning. Subsequently, the information-gain RL stage self-evolves latent reasoning without ground truth supervision. Experiments across diverse text-to-image generation benchmarks show that LARC consistently improves generation quality, prompt following, and compositional fidelity. Notably, LARC achieves state-of-the-art performance on GenEval with a 7%p gain over BAGEL and demonstrates clear test-time scaling behavior, outperforming token-based generation under both parallel and sequential test-time scaling strategies.

</details>

---

### [[20_Research/Papers/大模型/Completeness_and_Cost_of_Retrieval_Structures_for_Multi-Tool_Requests_in_LLM_Agents|Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents]]

![[assets/2610.41905_first_page.png|800]]

- **arXiv**: [2610.41905](https://arxiv.org/abs/2610.41905)
- **PDF**: https://arxiv.org/pdf/2610.41905
- **详细分析**: [[20_Research/Papers/大模型/Completeness_and_Cost_of_Retrieval_Structures_for_Multi-Tool_Requests_in_LLM_Agents|Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents]]
- **作者**: Shuyang Zhang
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AppWorld, GatewayBench, LiveMCPBench, MCP-Bench, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An agent that must call several tools to fulfill a request fails when the tool retriever omits any one of them, yet tool retrievers are mostly built and evaluated on queries requiring a single tool. We compare representatives of six retrieval structures (flat lexical and dense retrieval, LLM query decomposition, LLM-navigated hierarchies, server-then-tool matching, dependency graphs, and trained set-level retrievers) across two multi-tool testbeds: 345 AppWorld queries with expert dependency labels and 103 MCP-Bench tasks over 257 MCP tools. We measure completeness@k, the share of queries whose entire required tool set appears in the top k, alongside the LLM calls, tokens, and latency that each structure incurs at retrieval time. A motivating analysis on all 7,961 ToolRet queries shows that aggregate completeness mixes two regimes: completeness at 10 is .58 to .67 on single-target queries and .08 to .17 on queries with four or more targets, and the ordering of retrievers on single-target queries reverses on multi-target ones. Across the two testbeds, none of the compared structures that is untrained on the testbed and makes at most one LLM call per query completes more than 10% of AppWorld queries at k = 16. The two structures that do better incur different costs: a set-level retriever trained on 75 to 90 in-domain queries reaches .33 on AppWorld and .58 on MCP-Bench with no LLM calls, while an LLM-navigated hierarchy reaches .30 and .40 with a median of 31 to 38 LLM calls and about five minutes per query. Their failure modes also differ: the trained retriever mostly ranks the missing tools just below the cutoff, whereas the hierarchy finds the target API and stops before collecting its prerequisites. In a downstream check with the official AppWorld agent, tasks with a complete retrieved set succeeded 21 of 21 times, whereas incomplete ones succeeded 2 of 39 times.

</details>

---

### [[20_Research/Papers/大模型/TraceSpec_Understanding_and_Improving_Speculative_Decoding_for_LLM_Agents|TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents]]

![[assets/2610.41177_figure.png|800]]

- **arXiv**: [2610.41177](https://arxiv.org/abs/2610.41177)
- **PDF**: https://arxiv.org/pdf/2610.41177
- **详细分析**: [[20_Research/Papers/大模型/TraceSpec_Understanding_and_Improving_Speculative_Decoding_for_LLM_Agents|TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents]]
- **作者**: Jihao Zhao, Shuaishuai Zu, Pengfei Li, Biao Qin, Guanghuan Fang, Ben Feng, Baochuan Yang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TraceSpec: Understanding and Improving Speculative Decoding for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongBench, R2E-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents execute tasks through repeated model calls over evolving histories of reasoning, actions, and tool feedback. Aggregate speculative-decoding metrics merge these distinct decisions, providing limited guidance on where draft supervision is needed. We present TraceSpec, a framework connecting trajectory evaluation with adaptive draft training. It combines dynamic execution with fixed-prefix replay and introduces TraceSpec-Traj, a corpus of 10,000 training states and 2,500 test states spanning browsing and software engineering. Analysis of five speculative baselines reveals that aggregate acceptance can rise with context length while declining within matched late browsing actions. Workload and phase further distinguish these trends, motivating supervision guided by trajectory conditions. TraceSpec trains on intermediate assistant turns and allocates a fixed prediction budget using state-conditioned estimates of prefix-aware acceptance gaps. Across three target sizes and two temperatures, it improves replay throughput by 12.5% to 22.6% over its DSpark base. Qwen3-4B ablations show that adaptive allocation increases accepted length by 3.3% to 10.0% over fixed full-turn supervision, with additional comparisons substantiating the roles of state conditioning and consecutive-token agreement. The resulting evaluation resources, trajectory findings, and training strategy connect the analysis of agent execution to practical draft improvement.

</details>

---

### [[20_Research/Papers/大模型/CoFiBreak_A_Coarse-to-Fine_Diversity_Reward_for_Effective_Multi-Turn_Jailbreak|CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak]]

![[assets/2610.40926_figure.png|800]]

- **arXiv**: [2610.40926](https://arxiv.org/abs/2610.40926)
- **PDF**: https://arxiv.org/pdf/2610.40926
- **详细分析**: [[20_Research/Papers/大模型/CoFiBreak_A_Coarse-to-Fine_Diversity_Reward_for_Effective_Multi-Turn_Jailbreak|CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak]]
- **作者**: Jialin Song, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Qiyao Ma, Carolyn Buractaon, Anson Ho, Wuyang Chen, Christopher White
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.45，强化学习 0.4）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《CoFiBreak: A Coarse-to-Fine Diversity Reward for Effective Multi-Turn Jailbreak》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AdvBench, HarmBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated red teaming trains an attacker large language model (LLM) to elicit harmful responses from a victim LLM, but reinforcement learning can collapse attackers onto a narrow set of prompts when attack success is the only reward. Such a collapse of attack diversity can bias safety evaluation toward repeatedly testing near-duplicate attack patterns rather than the underlying harmful intents. Existing methods often trade off attack success or inference cost for greater content or strategy diversity. We propose CoFiBreak, a coarse-to-fine diversity reward for Group Relative Policy Optimization (GRPO) that improves attack diversity while preserving strong attack effectiveness and low inference cost. The coarse reward broadens which strategies the attacker uses by encouraging strategies underrepresented within each GRPO group, while the fine reward broadens how those strategies are realized by discouraging reuse of the same personas, framings, and output formats after harmful-intent information is removed from prompt embeddings. Diversity rewards apply only to attacks that already exceed an effectiveness threshold, so diversity cannot be gained through ineffective attacks. Since both rewards are computed only during training, CoFiBreak also retains inference efficiency. Trained with Llama3.1-8B-Instruct as the victim, CoFiBreak discovers 1.6-2.0x as many distinct successful fine-grained strategies as the strongest baseline across frontier victims on HarmBench. It reaches 98.8% ASR@10 (attack success rate with 10 generations per intent) on AdvBench with the highest diversity score among all compared methods, which is 2.1x that of the strongest-attacking baseline. The resulting attacks transfer to unseen frontier LLMs, reaching 71.0% ASR@10 on AdvBench with the unseen victim Claude-Opus-4.6. The code will be released.

</details>

---

### [[20_Research/Papers/强化学习/Li$^{2}$SAO_Lifting_Light_Singl-Rollout_Asynchronous_RL_Optimization_via_Group-Relative_Actor-Critic_Bootstrapping|Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping]]

![[assets/2610.40726_first_page.png|800]]

- **arXiv**: [2610.40726](https://arxiv.org/abs/2610.40726)
- **PDF**: https://arxiv.org/pdf/2610.40726
- **详细分析**: [[20_Research/Papers/强化学习/Li$^{2}$SAO_Lifting_Light_Singl-Rollout_Asynchronous_RL_Optimization_via_Group-Relative_Actor-Critic_Bootstrapping|Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping]]
- **作者**: Zichen Bai, Yanli Wang, Yang Liu, Junhao Shi, Xueqin Liu, Jinguo Sun, Muye Li, Shaoqiang Zheng, Xuefei Diao, Zhuwei Zeng, Nan Duan, Peng Cao
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Asynchronous reinforcement learning (RL) is becoming a mainstream paradigm for post-training large language models (LLMs), as it improves training efficiency by updating the model as rollouts arrive. Recent work argues that group-wise sampling in GRPO does not naturally fit asynchronous RL training because rollout lengths follow a long-tailed distribution, and proposes Single-rollout Asynchronous Optimization (SAO) to improve stability and off-policy behavior, especially on agentic tasks. However, SAO relies on a closed-source value model obtained from scaling value pretraining. In this paper, we analyze GRPO and LiSAO, our lightweight reproduction of SAO without the pretrained value model, on single-turn reasoning and multi-turn agentic tasks. We find that GRPO outperforms LiSAO on reasoning tasks, while the reverse holds on agentic tasks. Since the value model of LiSAO is not yet well trained , LiSAO lags behind GRPO substantially in early training steps. To address this issue, we propose Li$^{2}$SAO, which Lifts Light Single-rollout Asynchronous Optimization with group-relative actor-critic bootstrapping: while the critic is cold, a group-relative advantage trains the actor and a group-centered return trains the critic, after which training switches to single-rollout GAE. Experiments show that Li$^{2}$SAO catches up with or surpasses GRPO in early training and further raises the later performance ceiling. Code is available at https://github.com/jd-cc-coder/Li2SAO.

</details>

---
