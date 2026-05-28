# cs.CL | Computation and Language | 2026-05-26

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/When_Self-Belief_Misleads_Active_Label_Acquisition_for_Reinforcement_Learning_with_Verifiable_Rewards|When Self-Belief Misleads: Active Label Acquisition for Reinforcement Learning with Verifiable Rewards]]

![[assets/2605.25864_figure.png|800]]

- **arXiv**: [2605.25864](https://arxiv.org/abs/2605.25864)
- **PDF**: https://arxiv.org/pdf/2605.25864
- **详细分析**: [[20_Research/Papers/强化学习/When_Self-Belief_Misleads_Active_Label_Acquisition_for_Reinforcement_Learning_with_Verifiable_Rewards|When Self-Belief Misleads: Active Label Acquisition for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Li Wang, Xiaodong Lu, Xiaohan Wang, Yikun Ban, Jiajun Chai, Wei Lin, Tianhao Peng, Guojun Yin
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《When Self-Belief Misleads: Active Label Acquisition for Reinforcement Learning with Verifiable Rewards》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TTRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have achieved remarkable advancements in reasoning capabilities empowered by Reinforcement Learning with Verifiable Rewards (RLVR). Nonetheless, RLVR intrinsically relies on ground-truth labels for reward computation, the acquisition of which is often prohibitively expensive in real-world scenarios. While unsupervised RLVR paradigms attempt to circumvent this by training on pseudo-labels, they are notoriously susceptible to training collapse. Moreover, different samples often exhibit varying annotation values. In this paper, we propose Reinforcement Learning with Active Verifiable Rewards (RLAVR), which actively acquires ground-truth labels for a small set of selected samples and integrates them with pseudo-labels, thereby stabilizing training dynamics and improving performance under limited annotation budgets. To identify valuable samples, we propose the Corrective Advantage Gap (CAG) metric and analyze the sample-level supervision value. Building on this, we introduce Correction-Aware Reliability Estimation for RLAVR (CARE), which translates the oracle CAG criterion into a practical pre-query acquisition policy to substantially improve training stability. Extensive experiments across diverse domains, model families, and model scales demonstrate the effectiveness and generality of our approach. Our code is available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_from_Denoising_Feedback|Reinforcement Learning from Denoising Feedback]]

![[assets/2605.25638_figure.png|800]]

- **arXiv**: [2605.25638](https://arxiv.org/abs/2605.25638)
- **PDF**: https://arxiv.org/pdf/2605.25638
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_from_Denoising_Feedback|Reinforcement Learning from Denoising Feedback]]
- **作者**: Qi He, Huan Chen, Ya Guo, Huijia Zhu, Yi R. Fung, Baojian Zhou
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning from Denoising Feedback》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policy loss estimation remains a fundamental and long-standing challenge in reinforcement learning (RL) for diffusion language models (dLLMs). We introduce Reinforcement Learning from Denoising Feedback (RLDF), a novel training paradigm that leverages feedback obtained from rollout and training processes to facilitate accurate and efficient policy loss estimation. To balance the trade-off between computational efficiency and estimation effectiveness, RLDF optimizes the model toward the clipped clean state $\hat{x}_0$ from intermediate noisy states $x_t$, combined with weighted timestep sampling over $t$. Extensive experiments demonstrate that RLDF achieves consistent and substantial improvements in both performance and generalizability across two representative dLLM architectures, LLaDA and Dream, on multiple reasoning benchmarks. Our work lays a principled foundation for scalable reinforcement learning in diffusion language models. We build Drift, a training framework for dLLMs, available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/DVAO_Dynamic_Variance-adaptive_Advantage_Optimization_for_Multi-reward_Reinforcement_Learning|DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning]]

![[assets/2605.25604_figure.png|800]]

- **arXiv**: [2605.25604](https://arxiv.org/abs/2605.25604)
- **PDF**: https://arxiv.org/pdf/2605.25604
- **详细分析**: [[20_Research/Papers/强化学习/DVAO_Dynamic_Variance-adaptive_Advantage_Optimization_for_Multi-reward_Reinforcement_Learning|DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning]]
- **作者**: Guochao Jiang, Jingyi Song, Guofeng Quan, Chuzhan Hao, Guohua Liu, Yuewei Zhang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning has become a standard paradigm for aligning Large Language Models with human intent and task requirements. While Group Relative Policy Optimization offers an efficient, value-model-free alternative to Proximal Policy Optimization, adapting it to real-world multi-reward settings remains challenging. Standard scalarization practices, such as Reward Combination and Advantage Combination, suffer from significant drawbacks: Reward Combination frequently generates advantages with excessively large squared magnitudes that lead to training instability, while Advantage Combination relies on static hyperparameters and ignores cross-objective correlations. To address these limitations, we propose Dynamic Variance-adaptive Advantage Optimization (DVAO), which dynamically adjusts combination weights based on the empirical reward variance of each objective within a rollout group, effectively up-weighting objectives with a stronger learning signal while suppressing noisy ones. We mathematically prove that DVAO maintains bounded advantage magnitudes for stable training and introduces a self-adaptive cross-objective regularization mechanism. Extensive experiments on mathematical reasoning and tool-use benchmarks using Qwen3 and Qwen2.5 models demonstrate that DVAO significantly outperforms baseline methods, achieving a superior multi-objective Pareto frontier and robust training stability.

</details>

---

### [[20_Research/Papers/强化学习/CRPO_Character-centric_Group_Relative_Policy_Optimization_for_Role-aware_Reasoning_in_Role-playing_Agents|CRPO: Character-centric Group Relative Policy Optimization for Role-aware Reasoning in Role-playing Agents]]

![[assets/2605.25511_figure.png|800]]

- **arXiv**: [2605.25511](https://arxiv.org/abs/2605.25511)
- **PDF**: https://arxiv.org/pdf/2605.25511
- **详细分析**: [[20_Research/Papers/强化学习/CRPO_Character-centric_Group_Relative_Policy_Optimization_for_Role-aware_Reasoning_in_Role-playing_Agents|CRPO: Character-centric Group Relative Policy Optimization for Role-aware Reasoning in Role-playing Agents]]
- **作者**: Yihong Tang, Kehai Chen, Liang Yue, Benyou Wang, Min Zhang
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.55（加权：大模型 0.55，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《CRPO: Character-centric Group Relative Policy Optimization for Role-aware Reasoning in Role-playing Agents》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CharacterBench, SocialBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advancements in Reinforcement Learning (RL), particularly Group Relative Policy Optimization (GRPO), have significantly enhanced the reasoning capabilities of Large Language Models. However, applying these problem-centric optimization methods to role-playing agents often leads to a loss of character fidelity and style collapse, as they prioritize context-specific utility over persona alignment. To address this, we propose Character-Centric Group Relative Policy Optimization (CRPO), a framework designed to realign RL objectives with the role-playing task. CRPO improves character distinctiveness through three mechanisms: decoupling task logic from stylistic rewards to resolve gradient conflicts, dynamically adapting optimization constraints based on character complexity, and utilizing generic responses as negative baselines to prevent the model from reverting to a common distribution. Extensive experiments demonstrate that CRPO outperforms existing methods in consistency, emotion and others.

</details>

---

### [[20_Research/Papers/大模型/Retrieval_as_Reasoning_Self-Evolving_Agent-Native_Retrieval_via_LLM-Wiki|Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki]]

![[assets/2605.25480_figure.png|800]]

- **arXiv**: [2605.25480](https://arxiv.org/abs/2605.25480)
- **PDF**: https://arxiv.org/pdf/2605.25480
- **详细分析**: [[20_Research/Papers/大模型/Retrieval_as_Reasoning_Self-Evolving_Agent-Native_Retrieval_via_LLM-Wiki|Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki]]
- **作者**: Haoliang Ming, Feifei Li, Xiaoqing Wu, Wenhui Que
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents require retrieval to behave less like one-shot context fetching and more like reasoning: searching, reading, traversing, and deciding when evidence is sufficient. Yet current Retrieval-Augmented Generation (RAG) systems organize external knowledge as flat chunks retrieved by embedding similarity, exposing a retrieval-as-lookup interface ill-suited to iterative reasoning agents. We propose LLM-Wiki, an agent-native retrieval system that operationalizes the Retrieval-as-Reasoning paradigm by treating external knowledge as a compilable, composable, and self-evolving structure rather than a static retrieval index. LLM-Wiki compiles documents into structured Wiki pages with bidirectional links, exposes search, read, and link-following operations through standard tool-calling interfaces, and introduces an Error Book for persistent structural and semantic self-correction. LLM-Wiki achieves state-of-the-art results on HotpotQA, MuSiQue, and 2WikiMultiHopQA, outperforming HippoRAG 2, LightRAG, and GraphRAG by 2.0-8.1 F1 points. On AuthTrace, LLM-Wiki achieves the best overall accuracy, with especially strong gains on multi-document structured queries, confirming that compilation-based retrieval generalizes beyond chain-style multi-hop reasoning.

</details>

---

### [[20_Research/Papers/强化学习/Directional_Alignment_Mitigates_Reward_Hacking_in_Reinforcement_Learning_for_Language_Models|Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models]]

![[assets/2605.25189_figure.png|800]]

- **arXiv**: [2605.25189](https://arxiv.org/abs/2605.25189)
- **PDF**: https://arxiv.org/pdf/2605.25189
- **详细分析**: [[20_Research/Papers/强化学习/Directional_Alignment_Mitigates_Reward_Hacking_in_Reinforcement_Learning_for_Language_Models|Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models]]
- **作者**: Wenlong Deng, Jiaji Huang, Kaan Ozkara, Yushu Li, Christos Thrampoulidis, Xiaoxiao Li, Youngsuk Park
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Directional Alignment Mitigates Reward Hacking in Reinforcement Learning for Language Models》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Big-Math-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward hacking arises when a model improves a proxy reward by exploiting shortcuts rather than solving the intended task. We study this failure mode through the geometry of reinforcement learning updates in language models and argue that hacking emerges when optimization drifts away from a stable low-dimensional learning trajectory. We analyze this drift through dominant singular directions of parameter updates and show that reward-hacking runs exhibit substantially larger directional change than clean runs. Motivated by this observation, we introduce trusted-direction projection, which constrains gradients to remain within a clean reference subspace. Across reward-hacking experiments on mathematical reasoning, the proposed approach delays shortcut exploitation and better preserves task performance.

</details>

---

### [[20_Research/Papers/具身智能/ECHO_Terminal_Agents_Learn_World_Models_for_Free|ECHO: Terminal Agents Learn World Models for Free]]

![[assets/2605.24517_figure.png|800]]

- **arXiv**: [2605.24517](https://arxiv.org/abs/2605.24517)
- **PDF**: https://arxiv.org/pdf/2605.24517
- **详细分析**: [[20_Research/Papers/具身智能/ECHO_Terminal_Agents_Learn_World_Models_for_Free|ECHO: Terminal Agents Learn World Models for Free]]
- **作者**: Vaishnavi Shrivastava, Piero Kauffmann, Ahmed Awadallah, Dimitris Papailiopoulos
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 具身智能, 强化学习
- **相关性评分**: 1.87（加权：具身智能 0.3，大模型 0.65，强化学习 0.16，世界模型 0.76）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《ECHO: Terminal Agents Learn World Models for Free》归入 世界模型、大模型、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Internal-Eval, TerminalBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

CLI agents are the closest thing language models have to an embodied setting: the model emits commands, the terminal executes them, and the returned stream -- stdout, errors, files, logs, and traces -- records the consequences. We argue that this stream is a supervision signal, but standard agent RL discards it: GRPO-style training updates action tokens with sparse outcome-level rewards while ignoring environment responses already in the rollout. Failed rollouts provide little policy-gradient signal despite containing rich evidence about how the environment responds. We introduce ECHO (Environment Cross-entropy Hybrid Objective), a hybrid objective that combines the standard policy-gradient loss on action tokens with an auxiliary loss that trains the policy to predict environment observation tokens resulting from its own actions. ECHO reuses the same forward pass as GRPO, requires no additional rollouts, and turns terminal feedback into dense supervision for all rollouts. ECHO doubles GRPO pass@1 on TerminalBench-2.0: Qwen3-8B improves from 2.70% to 5.17%, and Qwen3-14B from 5.17% to 10.79%. ECHO also produces policies that better predict terminal dynamics, even on trajectories they did not generate: across held-out rollouts, it sharply reduces environment-token cross-entropy while GRPO alone barely changes it. From base Qwen3-8B, ECHO matches expert-SFT-then-GRPO performance on held-out terminal tasks without expert demonstrations, and recovers roughly half of the expert-SFT initialization benefit on TerminalBench-2.0. In some settings, the environment prediction loss alone enables verifier-free self-improvement, allowing policies to improve on unseen OOD tasks by learning only from environment interactions. Together, these results suggest that environment observations are not merely context for future actions, but a dense, on-policy supervision signal already present in every rollout.

</details>

---

### [[20_Research/Papers/大模型/SEAL_Synergistic_Co-Evolution_of_Agents_and_Learning_Environments|SEAL: Synergistic Co-Evolution of Agents and Learning Environments]]

![[assets/2605.24426_figure.png|800]]

- **arXiv**: [2605.24426](https://arxiv.org/abs/2605.24426)
- **PDF**: https://arxiv.org/pdf/2605.24426
- **详细分析**: [[20_Research/Papers/大模型/SEAL_Synergistic_Co-Evolution_of_Agents_and_Learning_Environments|SEAL: Synergistic Co-Evolution of Agents and Learning Environments]]
- **作者**: Yihao Hu, Zhihao Wen, Xiujin Liu, Pan Wang, Xin Zhang, Wei Wu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.15（加权：大模型 0.95，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SEAL: Synergistic Co-Evolution of Agents and Learning Environments》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents are increasingly improved through interaction, yet most self-evolution methods adapt either the policy or the learning environment in isolation. We identify this structural gap as \emph{Agent-Environment Misalignment}: the agent's capability frontier changes during training, while the environment that provides supervision remains static or only weakly coupled to the agent's revealed failures. We propose SEAL, a closed-loop co-evolution framework for interactive tool-use agents. SEAL collects on-policy trajectories under executable verification, diagnoses failed rollouts into turn-level failure labels, and uses these diagnoses as a shared signal for both environment-side adaptation and model-side policy optimization. The environment evolves its training-time learning interface by exposing clearer tool affordance cues, constraint information, and recovery-oriented feedback, while the policy is updated with diagnosis-guided advantage reweighting. Extensive experiments across in-distribution and out-of-distribution multi-turn tool-use evaluations show that SEAL improves low-resource agent learning: with only 400 training samples, it yields +8.25 to +26.25 average-point gains across three backbones and exhibits positive out-of-distribution transfer. These results demonstrate the value of jointly adapting the learner and its training-time learning substrate for robust self-improving LLM agents.

</details>

---
