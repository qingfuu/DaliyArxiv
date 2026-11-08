# cs.CL | Computation and Language | 2026-11-06

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Multimodal-SEA_Benchmarking_AI_Agent_Security_under_Multimodal_Social_Engineering_Attacks|Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks]]

![[assets/2611.08281_figure.png|800]]

- **arXiv**: [2611.08281](https://arxiv.org/abs/2611.08281)
- **PDF**: https://arxiv.org/pdf/2611.08281
- **详细分析**: [[20_Research/Papers/大模型/Multimodal-SEA_Benchmarking_AI_Agent_Security_under_Multimodal_Social_Engineering_Attacks|Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks]]
- **作者**: Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Multimodal, Agent, Security

#### 研究背景与动机

《Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HarmBench, M-SEABench, MM-SafetyBench, PhishSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared multimodal content. The tasks span four difficulty levels and reflect the distinct social and cultural contexts of Chinese and English environments. Agents inspect content, verify requests, and execute actions in simulated applications, with attack outcomes grounded in verifiable tool execution logs. To enable controlled red teaming of personal agents, we design a multimodal attack harness that integrates task information, attack progression control, and multimodal content construction to evaluate their intrinsic security against adaptive social engineering attacks in simulated environments. Evaluating seven widely used multimodal models across six dimensions reveals that all are vulnerable, with attack success rates of 7.1% to 34.5%. Adding multimodal content increases attack success from 19.9% to 29.2%, despite increased proactive verification coverage. Stronger safety instructions reduce attack success without improving recognition of deceptive multimodal content, while lower attack success rates for some models accompany excessive refusal of legitimate requests.

</details>

---

### [[20_Research/Papers/大模型/Agent-R$^2$_Scaling_Agents_for_Realistic_Productivity_Work_via_Real-Source_Data_Synthesis|Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis]]

![[assets/2611.08219_figure.png|800]]

- **arXiv**: [2611.08219](https://arxiv.org/abs/2611.08219)
- **PDF**: https://arxiv.org/pdf/2611.08219
- **详细分析**: [[20_Research/Papers/大模型/Agent-R$^2$_Scaling_Agents_for_Realistic_Productivity_Work_via_Real-Source_Data_Synthesis|Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis]]
- **作者**: Teng Pan, Zixuan Wang, Yuchen Yan, Qifei Wu, Yao Chen, Yingqi Qu, Ruiqing Zhang, Yongliang Shen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source Data Synthesis》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OfficeQA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models have made rapid progress in agentic reasoning and tool use, raising expectations for agents that can take over realistic productivity work from humans. However, current agents still struggle to finish such tasks, where success requires following long-horizon professional workflows, understanding heterogeneous file contexts, and producing usable deliverables under fine-grained requirements. A key bottleneck is the lack of scalable post-training data that reflects real work intent, authentic file environments, and deliverable-level evaluation. To close this gap, we introduce Agent-R$^2$, a $\textbf{r}$eal-source data synthesis framework that scales training data for $\textbf{r}$ealistic productivity work. Instead of relying on manually specified workflows or LLM-generated files, Agent-R$^2$ grounds synthesis throughout the pipeline in real occupational seeds, corpus-derived workflow evidence, and authentic web-sourced files. From 10k web-corpus candidates, Agent-R$^2$ distills 4k task instances that pair real multi-format attachments with fine-grained, deliverable-level rubrics. On this data, we train Agent-R$^2$-4B via supervised fine-tuning and rubric-based reinforcement learning, improving both end-to-end productivity performance and file-grounded reasoning. Trained on only 4k instances, Agent-R$^2$-4B surpasses Qwen3-235B-A22B-Thinking-2507 on both GDPval (51.0$\%$ vs. 48.0$\%$) and OfficeQA (14.8$\%$ vs. 13.8$\%$). Further analysis shows that Agent-R$^2$ mitigates shortcut behavior, where agents produce superficially plausible deliverables before sufficiently grounding, constructing, or verifying them, while promoting sustained exploration.

</details>

---

### [[20_Research/Papers/大模型/Octopus_One_Brain,_Many_Branches_for_Latent-KV_Multi-Agent_Reinforcement_Learning|Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning]]

![[assets/2611.06956_figure.png|800]]

- **arXiv**: [2611.06956](https://arxiv.org/abs/2611.06956)
- **PDF**: https://arxiv.org/pdf/2611.06956
- **详细分析**: [[20_Research/Papers/大模型/Octopus_One_Brain,_Many_Branches_for_Latent-KV_Multi-Agent_Reinforcement_Learning|Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning]]
- **作者**: Tianming Sha
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.87（加权：大模型 0.75，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本中出现的评测对象/数据集包括：DeltaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling text summaries, and flatten or drop cross-branch dependencies during reinforcement learning (RL). We introduce Octopus, a single-model multi-agent RL framework in which all threads share one backbone and coordinate over a GPU-resident directed acyclic graph (DAG) of KV states through five primitives (fork, read_thread, wait_threads, rewind, commit). Octopus combines three co-designed mechanisms: (1) Zero-Copy Radix Forking, which spawns branches as $\mathcal{O}(1)$ cursor views over shared physical KV pages; (2) Attention-Only KV Mounting, which mounts a sibling thread's terminal KV blocks directly into full-attention layers while bypassing linear-recurrent states (Gated DeltaNet / Mamba-2), cutting off-task hijacking by $21\times$ ($57.9\% \to 2.7\%$) while retaining $92.2\%$ of full-text mutual information at zero extra KV allocation; and (3) a Packed DAG-GRPO Trainer, which packs all episode branches into one block-sparse attention pass and assigns counterfactual branch credit via leave-one-branch-out marginal rewards. Trained end-to-end with GRPO on Qwen3.5-4B over a sparse BM25 corpus, Octopus reaches $49.6\%$ accuracy on BrowseComp-Plus ($+17.5$ points over single-agent GRPO at 143K context and $+12.5$ points over text-summary multi-agent RL) and $51.2\%$ on OpenResearcher, outperforming dense-retrieval agents up to $250\times$ larger while increasing training throughput $3.3\times$ and cutting peak KV memory $2.8\times$.

</details>

---
