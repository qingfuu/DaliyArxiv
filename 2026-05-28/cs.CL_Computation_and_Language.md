# cs.CL | Computation and Language | 2026-05-28

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/大模型/Agent_Explorative_Policy_Optimization_for_Multimodal_Agentic_Reasoning|Agent Explorative Policy Optimization for Multimodal Agentic Reasoning]]

![[assets/2605.28774_first_page.png|800]]

- **arXiv**: [2605.28774](https://arxiv.org/abs/2605.28774)
- **PDF**: https://arxiv.org/pdf/2605.28774
- **详细分析**: [[20_Research/Papers/大模型/Agent_Explorative_Policy_Optimization_for_Multimodal_Agentic_Reasoning|Agent Explorative Policy Optimization for Multimodal Agentic Reasoning]]
- **作者**: Minki Kang, Shizhe Diao, Ryo Hachiuma, Sung Ju Hwang, Pavlo Molchanov, Yu-Chiang Frank Wang, Byung-Kwan Lee
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.75（加权：大模型 0.95，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Agent Explorative Policy Optimization for Multimodal Agentic Reasoning》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models with extended reasoning succeed on complex problems, but many real-world problems require external tools that internal reasoning alone often cannot resolve. Agentic reasoning therefore interleaves two behaviors with a structural asymmetry: thinking (the self-contained default) and tool use (a high-variance auxiliary acting). We refer to this asymmetry as the Thinking-Acting Gap. Under standard RL recipes like GRPO, the gap manifests as two diagnostic symptoms during training: tool use is attempted on only ~30% of rollouts, and when attempted, the tool-using rollouts within a group are all-wrong on ~40% of questions, suppressing the learning signal at the tool calls that needed it. We propose AXPO (Agent eXplorative Policy Optimization): for each all-wrong tool-using subgroup, AXPO fixes the thinking prefix and resamples the tool call and its continuation, paired with uncertainty-based prefix selection. Across nine multimodal benchmarks and three scales of Qwen3-VL-Thinking, SFT+AXPO outperforms SFT+GRPO at average (+1.8pp Pass@1 and +1.8pp Pass@4 at 8B on average) and 8B with SFT+AXPO surpasses the 32B Base on Pass@4 with 4 times fewer parameters.

</details>

---

### [[20_Research/Papers/大模型/Mobile-Aptus_Confidence-Driven_Proactive_and_Robust_Interaction_in_MLLM-based_Mobile-Using_Agents|Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents]]

![[assets/2605.28629_figure.png|800]]

- **arXiv**: [2605.28629](https://arxiv.org/abs/2605.28629)
- **PDF**: https://arxiv.org/pdf/2605.28629
- **详细分析**: [[20_Research/Papers/大模型/Mobile-Aptus_Confidence-Driven_Proactive_and_Robust_Interaction_in_MLLM-based_Mobile-Using_Agents|Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents]]
- **作者**: Zheng Wu, Pengzhou Cheng, Zongru Wu, Yuan Guo, Tianjie Ju, Aston Zhang, Gongshen Liu, Zhuosheng Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Mobile-Aptus: Confidence-Driven Proactive and Robust Interaction in MLLM-based Mobile-Using Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DigiRL, DistRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advancements in multimodal large language models (MLLMs) have shown exceptional potential in enabling mobile-using agents to autonomously execute human instructions. However, fully automated agents often try to execute tasks even when they are unable to resolve them, leading to the problem of over-execution. Previous studies solve it by training a interactive mobile-using agents to let agents request human interaction when agents can not complete user instructions. However, we find that these interactive agents tend to exhibit over-soliciting behavior, relying excessively on human intervention. To mitigate both over-execution and over-soliciting, we propose a universal confidence integration framework that enables confidence-driven proactive and robust interaction in MLLM-based mobile-using agents. The framework consists of two stages: interaction capability empowerment and confidence bias correction. In the interaction capability empowerment stage, agents learn through supervised fine-tuning to output both actions and confidence scores. In the confidence bias correction stage, agents learn to output more accurate confidence scores by combining semantic similarity retrieval with direct preference optimization. Experimental results show Mobile-Aptus achieves state-of-the-art performance on the four popular mobile-using agent benchmarks: OS-Kairos, AITZ, Meta-GUI, and AndroidControl. Mobile-Aptus consistently outperforms all baselines in offline benchmarks, with an average improvement over 17\% in task success rate. In real-world dynamic experiments, Mobile-Aptus surpasses the baseline by 26% in task success rate with only 0.64 intervention steps per instruction. The codes are available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Soft-SVeRL_Self-Verified_Reinforcement_Learning_with_Soft_Rewards|Soft-SVeRL: Self-Verified Reinforcement Learning with Soft Rewards]]

![[assets/2605.28561_figure.png|800]]

- **arXiv**: [2605.28561](https://arxiv.org/abs/2605.28561)
- **PDF**: https://arxiv.org/pdf/2605.28561
- **详细分析**: [[20_Research/Papers/大模型/Soft-SVeRL_Self-Verified_Reinforcement_Learning_with_Soft_Rewards|Soft-SVeRL: Self-Verified Reinforcement Learning with Soft Rewards]]
- **作者**: Saurabh Dash, Pierre Clavier, John Dang, Matthias Galle, Marzieh Fadaee, Ahmet Üstün, Beyza Ermis
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Soft-SVeRL: Self-Verified Reinforcement Learning with Soft Rewards》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IFEval, Soft-SVeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning from Verifiable Rewards (RLVR) has improved language models in domains such as mathematics and code, where correctness can be checked automatically. However, many important tasks are only partially verifiable: prompts contain multiple requirements, responses may satisfy some but not all of them, or no single reference answer might exist. We introduce Soft-RLVR, a framework for reinforcement learning from decomposed, learned verification signals. Soft-RLVR converts each prompt into a checklist of atomic requirements, scores candidate responses item by item with an LLM verifier, and trains on the resulting soft reward. Checklist-based rewards turn sparse pass/fail supervision into a denser partial-credit signal, but they also introduce a tradeoff: averaging item-level judgments can reduce verifier noise, while partial credit can reward incomplete responses. We formalize this tradeoff and identify conditions under which checklist-based verification gives a more reliable RL training signal than holistic verification. We further introduce Soft-SVeRL, a self-verifying variant of Soft-RLVR in which the policy also acts as the verifier. We show that self-verification is prone to reward inflation from overly permissive self-judgments, and that explicit stabilization is needed to prevent this collapse. In a controlled instruction-following setting with rule-based ground-truth evaluation, checklist-based Soft-RLVR improves IFEval by up to 11.1 points using only learned verifier rewards. Our experiments further show that verifier quality and checklist quality both affect downstream RL outcomes, and that explicit stabilization is essential for effective self-verification.

</details>

---

### [[20_Research/Papers/大模型/GUI-CIDER_Mid-training_GUI_Agents_via_Causal_Internalization_and_Density-aware_Exemplar_Reselection|GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection]]

![[assets/2605.28534_figure.png|800]]

- **arXiv**: [2605.28534](https://arxiv.org/abs/2605.28534)
- **PDF**: https://arxiv.org/pdf/2605.28534
- **详细分析**: [[20_Research/Papers/大模型/GUI-CIDER_Mid-training_GUI_Agents_via_Causal_Internalization_and_Density-aware_Exemplar_Reselection|GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection]]
- **作者**: Zheng Wu, Chengcheng Han, Zhengxi Lu, Tianjie Ju, Yanyu Chen, Qi Gu, Xunliang Cai, Zhuosheng Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.95（加权：大模型 0.75，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MMBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the rapid progress of multimodal large language models in building Graphical User Interface (GUI) agents, their real-world task completion is fundamentally bottlenecked by a lack of world knowledge about GUI operations. Existing solutions typically rely on expensive multi-agent scaffolding or conventional post-training paradigms, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). However, post-training only allows agents to implicitly absorb world knowledge through action annotations or reward signals, leading to inefficient trajectory memorization rather than genuine comprehension. Therefore, an approach that enables explicit learning of this knowledge is imperative. To this end, we propose GUI-CIDER, a mid-training method that explicitly internalizes GUI world knowledge through Causal Internalization and Density-aware Exemplar Reselection. GUI-CIDER operates in three stages: (1) data synthesis, which distills static planning and dynamic causal knowledge from GUI trajectories into text; (2) exemplar reselection, which filters the corpus by rewarding causal structures and penalizing semantic redundancy; and (3) mid-training, where the refined data is used to embed the acquired knowledge. Extensive experiments on two GUI knowledge benchmarks and three task completion benchmarks demonstrate that GUI-CIDER consistently improves both the agent's understanding of GUI operations and its task success this http URL codes are available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Skill0.5_Joint_Skill_Internalization_and_Utilization_for_Out-of-Distribution_Generalization_in_Agentic_Reinforcement_Learning|Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning]]

![[assets/2605.28424_figure.png|800]]

- **arXiv**: [2605.28424](https://arxiv.org/abs/2605.28424)
- **PDF**: https://arxiv.org/pdf/2605.28424
- **详细分析**: [[20_Research/Papers/强化学习/Skill0.5_Joint_Skill_Internalization_and_Utilization_for_Out-of-Distribution_Generalization_in_Agentic_Reinforcement_Learning|Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning]]
- **作者**: Jiapeng Zhu, Jianxiang Yu, Yibo Zhao, Chengcheng Han, Qi Gu, Xunliang Cai, Xiang Li, Weining Qian
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.15（加权：大模型 0.35，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Equipping large language models with explicit skills has emerged as a promising paradigm for enabling autonomous agents to solve complex tasks. Agent skills can be inherently divided into general skills for broad cognitive transfer and task-specific skills for dynamic execution. However, existing skill-based reinforcement learning (RL) methods typically force a rigid choice between full externalization, which incurs prohibitive context overhead, and full internalization, which risks overfitting and knowledge conflicts. To address this dilemma, we propose Skill0.5, a novel agentic RL framework that explicitly differentiates skill treatments by combining general skill internalization with task-specific skill utilization. Driven by a dynamic, difficulty-aware router, Skill0.5 streams tasks into distinct mastery tiers to apply tailored optimization strategies: it internalizes general skills via privileged distillation to build a cognitive foundation for hard tasks, while using diagnostic probing on easy tasks to penalize shortcuts and enforce specific skill utilization. Experiments on ALFWorld and WebShop demonstrate that Skill0.5 outperforms both memory-based and skill-based RL baselines, yielding performance improvements across both in-distribution and out-of-distribution scenarios.

</details>

---

### [[20_Research/Papers/大模型/Ask_Now,_Use_Later_Benchmarking_the_Proactivity_Gap_in_Long-Lived_LLM_Agents|Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents]]

![[assets/2605.28108_figure.png|800]]

- **arXiv**: [2605.28108](https://arxiv.org/abs/2605.28108)
- **PDF**: https://arxiv.org/pdf/2605.28108
- **详细分析**: [[20_Research/Papers/大模型/Ask_Now,_Use_Later_Benchmarking_the_Proactivity_Gap_in_Long-Lived_LLM_Agents|Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents]]
- **作者**: Bin Wu, Guanyun Zou, Bingbing Wang, Huan Zhao, Chuan Shi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ATRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A long-lived LLM agent, such as OpenClaw, earns its value by acting on a user's preferences and constraints across sessions, not just the current request. Yet today's agents keep what a user volunteers but rarely ask for what stays unspoken, leaving a proactivity gap in long-lived LLM agents: an agent cannot act on a preference it never obtained. As users delegate more of their affairs to agents, the impact of this gap grows. We isolate one concrete, controllable slice of this gap as Ask-to-Remember (ATR): the agent decides whether to ask now for a reusable user preference that the current task does not need but a later session with the same user will. ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise. ATRBench, to the best of our knowledge the first ATR benchmark, makes it measurable by fixing each user's preferences as hidden ground truth, so success demands asking, not recall. Across eight frontier LLM agents, defaults fall at least 62 points below an oracle handed the relevant preference, and prompting closes little of it. Diagnostics identify acquisition as the bottleneck. ATRBench surfaces this proactivity gap in current agents and offers a diagnostic testbed for closing it.

</details>

---

### [[20_Research/Papers/大模型/Skill-as-Pseudocode_Refactoring_Skill_Libraries_to_Pseudocode_for_LLM_Agents|Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents]]

![[assets/2605.27955_figure.png|800]]

- **arXiv**: [2605.27955](https://arxiv.org/abs/2605.27955)
- **PDF**: https://arxiv.org/pdf/2605.27955
- **详细分析**: [[20_Research/Papers/大模型/Skill-as-Pseudocode_Refactoring_Skill_Libraries_to_Pseudocode_for_LLM_Agents|Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents]]
- **作者**: Xinze Li, Yuhang Zang, Yixin Cao, Aixin Sun
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Skill-as-Pseudocode: Refactoring Skill Libraries to Pseudocode for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Markdown skill libraries for LLM agents ship as free-form prose, forcing the agent to re-derive both the input schema and the concrete invocation syntax on every retrieval. We observe that this often produces a "confused -&gt; re-retrieve -&gt; still confused" loop in which the agent issues a partially-correct action, receives uninformative environment feedback, and re-retrieves the same prose. We propose Skill-as-Pseudocode (SaP), an automatic conversion of markdown skill libraries into typed pseudocode with deterministic quality control. For each cluster of similar procedural passages drawn from one or more skills, SaP extracts a typed contract and filters it through a four-check deterministic verifier (coverage, binding, replacement, risk). Promoted contracts are inlined into a rewritten skill skeleton together with restored concrete action templates, giving the agent two complementary signals: a typed signature for what the skill does and a concrete template for how to invoke it. On the 134-game ALFWorld unseen split with gpt-4o-mini, pooled across three seeds, SaP wins 82/402 paired games versus 47/402 for the Graph-of-Skills (GoS) baseline (pooled McNemar p = 8.2e-5), at -22.8 +/- 6.4% input tokens and -14.5 +/- 4.1% LLM calls per game.

</details>

---

### [[20_Research/Papers/大模型/Escape_the_Language_Prior_Mitigating_Late-Stage_Modality_Collapse_in_Audio_Reasoning_via_Modality-Aware_Policy_Optimization|Escape the Language Prior: Mitigating Late-Stage Modality Collapse in Audio Reasoning via Modality-Aware Policy Optimization]]

![[assets/2605.27741_figure.png|800]]

- **arXiv**: [2605.27741](https://arxiv.org/abs/2605.27741)
- **PDF**: https://arxiv.org/pdf/2605.27741
- **详细分析**: [[20_Research/Papers/大模型/Escape_the_Language_Prior_Mitigating_Late-Stage_Modality_Collapse_in_Audio_Reasoning_via_Modality-Aware_Policy_Optimization|Escape the Language Prior: Mitigating Late-Stage Modality Collapse in Audio Reasoning via Modality-Aware Policy Optimization]]
- **作者**: Cihan Xiao, Yiwen Shao, Chenxing Li, Xiang He, Zhenwen Liang, Steve Yves, Sanjeev Khudanpur, Liefeng Bo
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.45（加权：大模型 0.25，强化学习 1.2）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Escape the Language Prior: Mitigating Late-Stage Modality Collapse in Audio Reasoning via Modality-Aware Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Audio and omni-modal large language models exhibit impressive cross-modal reasoning capabilities. However, applying standard reinforcement learning post-training algorithms to these models exposes a critical structural vulnerability: methods like GRPO apply uniform policy gradients across all tokens, ignoring their unequal dependence on the non-text source modality. This exacerbates late-stage modality collapse during extended chain-of-thought generation, where models progressively abandon the primary source signal in favor of compressed textual priors, leading to confident but ungrounded hallucinations. To address this, we introduce Modality-Aware Policy Optimization (MAPO), a novel dual-branch reinforcement learning framework. First, MAPO dynamically concentrates the policy gradient on modality-critical tokens using a modality relevance mask, which is derived from the cross-modal differential entropy between an audio-ablated reference and the multimodal policy. Second, it integrates an auxiliary attention loss branch that applies a targeted, temporally scaled penalty to the model's internal attention distributions. This ensures the model actively sustains cross-modal grounding deep into the reasoning trace. Evaluations on complex audio reasoning benchmarks demonstrate that MAPO substantially improves long-horizon reasoning fidelity and multimodal instruction following, achieving highly competitive performance and setting new state-of-the-art results on several key benchmarks among open-weight models. By relying strictly on native statistical signals rather than domain-specific inductive biases, MAPO offers a promising foundation for mitigating epistemic collapse across diverse multimodal systems.

</details>

---

### [[20_Research/Papers/大模型/TRACES_Proactive_Safety_Auditing_for_Multi-Turn_LLM_Agents_via_Trajectory-State_Modeling|TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling]]

![[assets/2605.27690_figure.png|800]]

- **arXiv**: [2605.27690](https://arxiv.org/abs/2605.27690)
- **PDF**: https://arxiv.org/pdf/2605.27690
- **详细分析**: [[20_Research/Papers/大模型/TRACES_Proactive_Safety_Auditing_for_Multi-Turn_LLM_Agents_via_Trajectory-State_Modeling|TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling]]
- **作者**: Jiaqian Li, Yanshu Li, Boxuan Zhang, Ruixiang Tang, Kuan-Hao Huang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ATBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly operate through multi-turn tool use and environment interaction, where safety risks often emerge from intermediate steps long before they surface in the final outcome. Reactive auditing is therefore insufficient: post-hoc diagnosis frequently misses the chance to flag risks while they are unfolding. We propose TRACES, a representation-based proactive auditor that learns prefix-level trajectory risk states from the hidden representations of an observer LLM. TRACES induces latent mechanism features from step representations and models their temporal evolution to estimate whether a partial trajectory is drifting toward unsafe behavior. To sidestep the cost and ambiguity of step-level risk annotation, TRACES is trained with weak trajectory-level supervision while still producing dense prefix-level risk estimates. Across multiple agent safety benchmarks, TRACES improves both full-trajectory safety prediction and proactive risk discrimination. Our analyses further suggest that these risk states can help train a safer agent, highlighting the broader potential of proactive auditing for long-horizon agent safety.

</details>

---

### [[20_Research/Papers/大模型/Agents_that_Matter_Optimizing_Multi-Agent_LLMs_via_Removal-Based_Attribution|Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution]]

![[assets/2605.27621_figure.png|800]]

- **arXiv**: [2605.27621](https://arxiv.org/abs/2605.27621)
- **PDF**: https://arxiv.org/pdf/2605.27621
- **详细分析**: [[20_Research/Papers/大模型/Agents_that_Matter_Optimizing_Multi-Agent_LLMs_via_Removal-Based_Attribution|Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution]]
- **作者**: Mingyu Lu, Yushan Huang, Chris Lin, Su-In Lee
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MedEthicsQA, MedQA, WorkBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As multi-agent systems (MAS) become increasingly complex, identifying the contributions of individual agents is critical for system optimization. However, existing approaches lack a rigorous, unified framework for credit assignment. In this work, we formalize agent attribution as a cooperative game, parameterized by the coalition distribution, removal protocol, and target metric. Using this framework, we show that Leave-One-Out (LOO) identifies bottleneck agents as effectively as combinatorial methods, but at a fraction of the computational cost. We also demonstrate that removal protocols induce distinct games: Agent ablation isolates structural bottlenecks, whereas introspective LLM judges fail to faithfully approximate this behavior. Furthermore, to evaluate the utility of specific agent backbones, we introduce attribution via model replacement. By substituting underlying models of low-contribution agents, we improve task performance by up to 17% while reducing cost by up to 35% across three benchmarks. Finally, we apply our framework to audit a medical MAS, revealing that agent contributions to diagnostic accuracy and ethical behavior are often decoupled. By intervening on counterproductive roles, we observe an increase in ethics alignment while maintaining diagnostic accuracy. Overall, this work provides a principled approach for cost-effective MAS attribution and intervention.

</details>

---

### [[20_Research/Papers/大模型/ICG_Improving_Cover_Image_Generation_via_MLLM-based_Prompting_and_Personalized_Preference_Alignment|ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment]]

![[assets/2605.27374_figure.png|800]]

- **arXiv**: [2605.27374](https://arxiv.org/abs/2605.27374)
- **PDF**: https://arxiv.org/pdf/2605.27374
- **详细分析**: [[20_Research/Papers/大模型/ICG_Improving_Cover_Image_Generation_via_MLLM-based_Prompting_and_Personalized_Preference_Alignment|ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment]]
- **作者**: Zhipeng Bian, Jieming Zhu, Qijiong Liu, Wang Lin, Guohao Cai, Zhaocheng Du, Jiacheng Sun, Zhou Zhao, Zhenhua Dong
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ControlNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in multimodal large language models (MLLMs) and diffusion models (DMs) have opened new possibilities for AI-generated content. Yet, personalized cover image generation remains underexplored, despite its critical role in boosting user engagement on digital platforms. We propose ICG, a novel framework that integrates MLLM-based prompting with personalized preference alignment to generate high-quality, contextually relevant covers. ICG extracts semantic features from item titles and reference images via meta tokens, refines them with user embeddings, and injects the resulting personalized context into the diffusion model. To address the lack of labeled supervision, we adopt a multi-reward learning strategy that combines public aesthetic and relevance rewards with a personalized preference model trained from user behavior. Unlike prior pipelines relying on handcrafted prompts and disjointed modules, ICG employs an adapter to bridge MLLMs and diffusion models for end-to-end training. Experiments demonstrate that ICG significantly improves image quality, semantic fidelity, and personalization, leading to stronger user appeal and offline recommendation accuracy in downstream tasks. As a plug-and-play adapter bridging MLLMs and diffusion models, ICG is compatible with common checkpoints and requires no ground-truth labels during optimization.

</details>

---
