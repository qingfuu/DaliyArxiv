# cs.CL | Computation and Language | 2026-06-01

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/机器人/Multi-Turn_Multi-Agent_Dialogue_for_Collaborative_Reconstruction_Improves_VLM_Performance_on_Spatial_Reasoning,_But_Only_Barely|Multi-Turn Multi-Agent Dialogue for Collaborative Reconstruction Improves VLM Performance on Spatial Reasoning, But Only Barely]]

![[assets/2605.31387_figure.png|800]]

- **arXiv**: [2605.31387](https://arxiv.org/abs/2605.31387)
- **PDF**: https://arxiv.org/pdf/2605.31387
- **详细分析**: [[20_Research/Papers/机器人/Multi-Turn_Multi-Agent_Dialogue_for_Collaborative_Reconstruction_Improves_VLM_Performance_on_Spatial_Reasoning,_But_Only_Barely|Multi-Turn Multi-Agent Dialogue for Collaborative Reconstruction Improves VLM Performance on Spatial Reasoning, But Only Barely]]
- **作者**: Chalamalasetti Kranti, Sherzod Hakimov, David Schlangen
- **cs 子类**: cs.CL, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.75（加权：具身智能 0.3，大模型 0.95，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Multi-Turn Multi-Agent Dialogue for Collaborative Reconstruction Improves VLM Performance on Spatial Reasoning, But Only Barely》归入 大模型、机器人、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in diverse environments rely on visual input to interpret objects and spatial layouts. In human-collaborative tasks, they are expected to communicate this understanding through language. Vision-language models (VLMs) support robotic tasks involving visual interpretation, question answering, and instruction following, but their capabilities in collaborative dialogue tasks requiring spatial reasoning remain underexplored. We study this gap through a collaborative structure-building task that combines visual interpretation, grounding, language-guided interaction, and action generation. We develop a framework in which VLMs use dialogue to reconstruct a target structure from visual and textual inputs. We evaluate open-weight and closed VLMs across interaction settings, input modalities, and image representations. Results show that spatial reasoning over visual representations remains difficult for the evaluated VLMs. Detailed text representations of the target yield higher reconstruction success across modality conditions, while decomposed image representations improve performance. These findings reveal limits in visual spatial grounding and grounded instruction generation for collaborative VLM agents.

</details>

---

### [[20_Research/Papers/大模型/Learning_Whom_to_Trust_Market-Feedback_Adaptive_Retrieval_for_Frozen_LLMs_in_Event-Driven_Financial_RAG|Learning Whom to Trust: Market-Feedback Adaptive Retrieval for Frozen LLMs in Event-Driven Financial RAG]]

![[assets/2605.31201_figure.png|800]]

- **arXiv**: [2605.31201](https://arxiv.org/abs/2605.31201)
- **PDF**: https://arxiv.org/pdf/2605.31201
- **详细分析**: [[20_Research/Papers/大模型/Learning_Whom_to_Trust_Market-Feedback_Adaptive_Retrieval_for_Frozen_LLMs_in_Event-Driven_Financial_RAG|Learning Whom to Trust: Market-Feedback Adaptive Retrieval for Frozen LLMs in Event-Driven Financial RAG]]
- **作者**: Zijie Zhao, Roy E. Welsch
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Learning Whom to Trust: Market-Feedback Adaptive Retrieval for Frozen LLMs in Event-Driven Financial RAG》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FinAgentBench, FinRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Financial retrieval-augmented generation (RAG) systems typically rank evidence by textual relevance, but in financial markets the useful evidence source depends on event type, forecast horizon, and market context. We study news-triggered event-impact prediction as a point-in-time financial RAG problem. For each company-news anchor, the system retrieves related financial news and SEC filing passages, appends a pre-decision market-context card, and predicts multi-horizon residual-return signals. Our method keeps the large language model (LLM) reader frozen and adapts the retrieval layer through an external Bayesian source memory updated from matured residual-return feedback. On a fixed 89-stock Nasdaq-oriented universe derived from the FinRL-DeepSeek/FNSPID task, using original FNSPID news and point-in-time EDGAR filing passages, Frozen Reader with Source Memory improves held-out macro-F1 from 0.438 to 0.471 and downstream portfolio Sharpe from 0.52 to 0.84 relative to Frozen Reader with No Memory. A supervised LoRA reader improves static RAG modestly, but does not improve over the frozen source-memory reader. These results suggest that, for financial RAG, learning where to retrieve from can be as important as learning how to read, offering a simple, modular route to market-feedback adaptation.

</details>

---

### [[20_Research/Papers/强化学习/AdaptR1_Reinforcement_Learning_Based_Adaptive_Interleaved_Thinking_in_Multi-hop_Question_Answering|AdaptR1: Reinforcement Learning Based Adaptive Interleaved Thinking in Multi-hop Question Answering]]

![[assets/2605.31062_figure.png|800]]

- **arXiv**: [2605.31062](https://arxiv.org/abs/2605.31062)
- **PDF**: https://arxiv.org/pdf/2605.31062
- **详细分析**: [[20_Research/Papers/强化学习/AdaptR1_Reinforcement_Learning_Based_Adaptive_Interleaved_Thinking_in_Multi-hop_Question_Answering|AdaptR1: Reinforcement Learning Based Adaptive Interleaved Thinking in Multi-hop Question Answering]]
- **作者**: Yuxin Wang, Jiahao Lu, Qifeng Wu, Shicheng Fang, Chuanyuan Tan, Yining Zheng, Xuanjing Huang, Xipeng Qiu
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《AdaptR1: Reinforcement Learning Based Adaptive Interleaved Thinking in Multi-hop Question Answering》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HotpotQA, PopQA, TriviaQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have achieved remarkable performance in complex reasoning tasks through Chain-of-Thought (CoT) prompting. However, this approach often leads to ``over-thinking,'' where models generate unnecessarily long reasoning traces for simple queries and incur avoidable inference cost. While recent work has explored adaptive reasoning, existing methods typically make a single query-level decision about whether to reason. This overlooks the dynamic nature of multi-step tasks, where the need for explicit reasoning varies across intermediate stages. To address this limitation, we introduce AdaptR1, a Reinforcement Learning (RL) based framework for adaptive interleaved thinking in multi-hop Question Answering (QA). Unlike previous approaches that require Supervised Fine-Tuning (SFT) for cold-start initialization, AdaptR1 uses a fully RL-based strategy with a quality-gated efficiency reward to dynamically allocate reasoning budgets at each step. Under the Graph-R1 setting, AdaptR1 reduces average think tokens by 69.71\%, with a 90.35\% reduction on HotpotQA, while maintaining performance comparable to or better than standard baselines. Furthermore, our analysis reveals that overthinking in multi-hop reasoning is not uniformly distributed but occurs predominantly during the initial planning stages, highlighting the effectiveness of step-wise adaptive budget allocation.

</details>

---

### [[20_Research/Papers/具身智能/MineExplorer_Evaluating_Open-World_Exploration_of_MLLM_Agents_in_Minecraft|MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft]]

![[assets/2605.30931_figure.png|800]]

- **arXiv**: [2605.30931](https://arxiv.org/abs/2605.30931)
- **PDF**: https://arxiv.org/pdf/2605.30931
- **详细分析**: [[20_Research/Papers/具身智能/MineExplorer_Evaluating_Open-World_Exploration_of_MLLM_Agents_in_Minecraft|MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft]]
- **作者**: Tianjie Ju, Yueqing Sun, Zheng Wu, Wei Zhang, Yaqi Huo, Xi Su, Qi Gu, Xunliang Cai, Gongshen Liu, Zhuosheng Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.45（加权：具身智能 0.3，大模型 1.15）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《MineExplorer: Evaluating Open-World Exploration of MLLM Agents in Minecraft》归入 大模型、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have shown strong capabilities in perception, reasoning, and action generation. However, their ability to sustain exploration in dynamic open worlds remains unclear. Existing embodied and game-based benchmarks often compress interaction into short-horizon tasks or entangle success with domain-specific game mechanics. In this paper, we introduce MineExplorer benchmark for evaluating open-world exploration capabilities of MLLM agents in Minecraft. We first filter atomic tasks whose solutions rely heavily on Minecraft-specific knowledge to better reflect general open-world reasoning. Then we organize the benchmark around a ReAct-style capability formulation and compose atomic tasks into implicit multi-hop tasks. To further construct reliable instances, MineExplorer uses a multi-agent synthesis workflow that jointly designs task graphs, sandbox scenes, and rule-based milestone evaluators. Human evaluation shows that the multi-agent synthesis workflow produces significantly more reliable instances than a single-agent baseline. Experiments with advanced MLLM agents show that open-world exploration remains challenging, as strong models can handle many single-hop tasks but degrade sharply when hidden prerequisites must be coordinated over longer trajectories. Further analysis finds that task difficulty tracks agent completion, and larger models or thinking modes do not consistently translate into better performance. Code and dataset are available at https://github.com/Jometeorie/MineExplorer.

</details>

---

### [[20_Research/Papers/具身智能/EMBGuard_Constructing_Hazard-Aware_Guardrails_for_Safe_Planning_in_Embodied_Agents|EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents]]

![[assets/2605.30924_figure.png|800]]

- **arXiv**: [2605.30924](https://arxiv.org/abs/2605.30924)
- **PDF**: https://arxiv.org/pdf/2605.30924
- **详细分析**: [[20_Research/Papers/具身智能/EMBGuard_Constructing_Hazard-Aware_Guardrails_for_Safe_Planning_in_Embodied_Agents|EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents]]
- **作者**: Dongwook Choi, Taeyoon Kwon, Bogyung Jeong, Minju Kim, Yeonjun Hwang, Hyojun Kim, Byungchul Kim, Young Kyun Jang, Jinyoung Yeo
- **cs 子类**: cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.95（加权：具身智能 1.2，大模型 0.75）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《EMBGuard: Constructing Hazard-Aware Guardrails for Safe Planning in Embodied Agents》归入 具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IS-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

MLLM-powered embodied agents deployed in real-world environments encounter physical hazards. However, existing approaches lack explicit mechanisms for identifying hazards and reasoning about action-conditioned risks, leading agents to either miss risky interactions or over-identify risks. To address this, we propose EMBGuard, the first MLLM-based safety guardrail for embodied agents designed to decouple physical risk reasoning from agent policy. By evaluating a (visual observation, action) pair, EMBGuard identifies hazardous configurations and provides natural language explanations of potential risks. Alongside EMBGuard, we contribute EMBHazard, a training dataset of 15.1K action-conditioned pairs, and EMBGuardTest, a benchmark of 329 manually curated real-world scenarios spanning seven physical risk categories. Through compositional variation of hazards and actions, we generate diverse risky and benign scenarios that agents may encounter during planning. Despite its compact size (2B, 4B), EMBGuard achieves performance competitive with proprietary MLLMs (e.g., GPT-5.1, Gemini-2.5-Pro) while significantly reducing the false-positive rates that hinder real-time deployment. We make the code, data, and models publicly available at https://github.com/dongwxxkchoi/EMBGuard

</details>

---

### [[20_Research/Papers/大模型/The_Flip_Side_of_RLHF_On-Policy_Feedback_for_Reward_Model_Self-Supervised_Improvement|The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement]]

![[assets/2605.30888_figure.png|800]]

- **arXiv**: [2605.30888](https://arxiv.org/abs/2605.30888)
- **PDF**: https://arxiv.org/pdf/2605.30888
- **详细分析**: [[20_Research/Papers/大模型/The_Flip_Side_of_RLHF_On-Policy_Feedback_for_Reward_Model_Self-Supervised_Improvement|The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement]]
- **作者**: Xiaobo Wang, Tong Wu, Min Tang, Jiaqi Li, Qi Liu, Zilong Zheng
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《The Flip Side of RLHF: On-Policy Feedback for Reward Model Self-Supervised Improvement》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AlpacaEval, JudgeBench, RM-Bench, RewardBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building strong reward models (RMs) for language model alignment is bottlenecked by the cost and difficulty of acquiring diverse and reliable preference data from human annotation or judge models. It is dramatically worse as the policy evolves beyond the static RM training. Therefore, we propose SAVE (Self-supervised reward model improvement via Value-Anchored On-policy feedback), a framework that grades on-policy responses as feedback by using the value function for on-policy RM training. SAVE naturally converts the reward-graded on-policy responses into supervision with a prompt-specific value head as an adaptive anchor. It computes RM advantages and filters ambiguous samples to update the RM via a contrastive objective. The effectiveness of SAVE for enhancing RM training is strongly validated through rigorous empirical evaluation across six diverse benchmarks. It achieves outperforming results across all datasets while maintaining consistent improvements across three RL algorithms (GRPO, RLOO, GSPO) and different policy backbones.

</details>

---

### [[20_Research/Papers/大模型/MosaicLeaks_Privacy_Risks_in_Querying-in-the-Open_for_Deep_Research_Agents|MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents]]

![[assets/2605.30727_figure.png|800]]

- **arXiv**: [2605.30727](https://arxiv.org/abs/2605.30727)
- **PDF**: https://arxiv.org/pdf/2605.30727
- **详细分析**: [[20_Research/Papers/大模型/MosaicLeaks_Privacy_Risks_in_Querying-in-the-Open_for_Deep_Research_Agents|MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents]]
- **作者**: Alexander Gurung, Spandana Gella, Alexandre Drouin, Issam H. Laradji, Perouz Taslakian, Rafael Pardinas
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.05（加权：大模型 0.85，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《MosaicLeaks:Privacy Risks in Querying-in-the-Open for Deep Research Agents》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRBench, DeepResearchGym, TOP-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep research agents increasingly combine private local documents with external tools like web retrieval, creating a privacy risk: an agent's external queries may leak sensitive information from its local context. This risk is amplified by the mosaic effect, where individual queries may appear harmless but become revealing in aggregate. We introduce MosaicLeaks, a benchmark of 1,001 multi-hop deep research tasks that chain private enterprise documents and a public web corpus, forcing agents to make external queries that depend on local information. We evaluate leakage with an adversary LLM that observes only the agent's external queries and attempts to infer private information at three levels: the agent's research intent, answers to specific private questions and verifiable claims about the enterprise documents. We find that models across families and sizes frequently leak at all three levels, that zero-shot privacy prompting reduces but does not eliminate leakage and that reinforcement learning for task performance alone worsens leakage. To address this, we propose Privacy-Aware Deep Research (PA-DR), an RL framework that combines situational rewards for task success with a learned privacy classifier to provide dense credit assignment over both per-query and mosaic-level leakage. Training Qwen3-4B-Instruct with PA-DR improves accuracy from 48.7% to 58.7% and reduces answer and full-information leakage from 34.0% to 9.9%.

</details>

---

### [[20_Research/Papers/大模型/Skill_is_Not_One-Size-Fits-All_Model-Aware_Skill_Alignment_for_LLM_Agents|Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents]]

![[assets/2605.30723_figure.png|800]]

- **arXiv**: [2605.30723](https://arxiv.org/abs/2605.30723)
- **PDF**: https://arxiv.org/pdf/2605.30723
- **详细分析**: [[20_Research/Papers/大模型/Skill_is_Not_One-Size-Fits-All_Model-Aware_Skill_Alignment_for_LLM_Agents|Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents]]
- **作者**: Jianxiang Yu, Jiapeng Zhu, Bochen Lin, Qier Cui, Zichen Ding, Xiang Li
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Skill is Not One-Size-Fits-All: Model-Aware Skill Alignment for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly retrieve externally curated skills-procedural instructions retrieved at decision time-to improve performance on long-horizon interactive tasks. Existing skill libraries are typically treated as model-agnostic, reusing the same skill formulations across backbones with substantially different capacities and behaviors. However, our controlled experiments across multiple model scales show that skill effectiveness is strongly model-dependent: a skill that benefits one backbone can harm another. Motivated by this observation, we propose MASA Model-Aware Skill Alignment, a framework that adapts skills to each target backbone without modifying agent weights. MASA operates in two stages: (1) a hierarchical skill evolution pipeline that iteratively rewrites general and task-specific skills using hill climbing and UCB-driven tree search, guided by environment feedback and model capability profiles; and (2) a lightweight model-conditioned skill rewriter trained on evolution trajectories to reproduce the adaptation in a single forward pass. Experiments across three interactive environments and four backbones show that MASA consistently achieves the best overall performance, with gains of up to 25.8 points over the strongest baseline. The learned rewriter further generalizes to unseen tasks and environments without additional search, consistently outperforming a much larger teacher LLM at a fraction of the inference cost.

</details>

---

### [[20_Research/Papers/大模型/ExpGraph_Model-Agnostic_Experience_Learning_with_Graph-Structured_Memory_for_LLM_Agents|ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents]]

![[assets/2605.30712_figure.png|800]]

- **arXiv**: [2605.30712](https://arxiv.org/abs/2605.30712)
- **PDF**: https://arxiv.org/pdf/2605.30712
- **详细分析**: [[20_Research/Papers/大模型/ExpGraph_Model-Agnostic_Experience_Learning_with_Graph-Structured_Memory_for_LLM_Agents|ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents]]
- **作者**: Tao Feng, Chongrui Ye, Tianyang Luo, Jingjun Xu, Xueqiang Xu, Haozhen Zhang, Zhigang Hua, Yan Xie, Shuang Yang, Ge Liu, Jiaxuan You
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.35（加权：大模型 1.15，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ExpGraph: Model-Agnostic Experience Learning with Graph-Structured Memory for LLM Agents》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, AppWorld, MemRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents have shown strong capabilities in reasoning, tool use, and multi-step interaction, but they often solve tasks from scratch and fail to reuse successful strategies or failure lessons from prior experience. Fine-tuning on collected experience can improve reuse, but it is inflexible when stronger or more suitable executors emerge. We propose ExpGraph, a model-agnostic experience learning framework that enables frozen and replaceable LLM executors to improve through external experience reuse without parameter updates. ExpGraph summarizes historical trajectories into reusable skills and failure lessons, organizes them as nodes in a self-evolving experience graph, and retrieves useful experiences through graph diffusion and utility-aware ranking. A lightweight retrieval copilot is trained with reinforcement learning using feedback that compares executor performance with and without retrieved experiences, while the graph is updated online from downstream task outcomes. We evaluate ExpGraph on ExpSuite, covering question answering, mathematical reasoning, code generation, and multi-step agentic environments including ALFWorld and AppWorld. ExpGraph improves over the strongest baseline by 12.2% and 4.7% on static tasks with smaller and larger executors, and by 21.4% and 12.7% in agentic environments, while reducing average interaction steps by 12.7% and 21.6%. Ablations show that graph-structured experience, utility-aware ranking, and adaptive retrieval jointly enable effective experience reuse across diverse tasks and executor models.

</details>

---

### [[20_Research/Papers/具身智能/ElasticMem_Latent_Memory_as_a_Learnable_Resource_for_LLM_Agents|ElasticMem: Latent Memory as a Learnable Resource for LLM Agents]]

![[assets/2605.30690_figure.png|800]]

- **arXiv**: [2605.30690](https://arxiv.org/abs/2605.30690)
- **PDF**: https://arxiv.org/pdf/2605.30690
- **详细分析**: [[20_Research/Papers/具身智能/ElasticMem_Latent_Memory_as_a_Learnable_Resource_for_LLM_Agents|ElasticMem: Latent Memory as a Learnable Resource for LLM Agents]]
- **作者**: Tao Feng, Chongrui Ye, Tianyang Luo, Jingjun Xu, Xueqiang Xu, Haozhen Zhang, Ge Liu, Jiaxuan You
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 强化学习
- **相关性评分**: 1.55（加权：具身智能 0.3，大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《ElasticMem: Latent Memory as a Learnable Resource for LLM Agents》归入 大模型、具身智能、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, LongMemEval, MemorySuite-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory is essential for LLM agents to reason coherently across extended interactions, personalize responses, and reuse past experience. However, existing memory-augmented methods typically treat memory as a fixed resource: text-space approaches concatenate retrieved memories into the context window, causing substantial token overhead and sensitivity to noisy evidence, while latent-space approaches reduce textual cost but still rely on rigid retrieval or fixed-capacity memory interfaces. This creates a mismatch between query-dependent memory utility and fixed memory allocation. We propose ElasticMem, a memory-augmented LLM framework that learns to use memory as an elastic latent resource. ElasticMem builds an offline latent memory bank with retrieval keys and content caches, retrieves memories adaptively from the reasoner's hidden state, assigns each retrieved memory a variable latent budget through a learned policy, and injects selected latent states as soft memory tokens for generation. The full memory-use process is optimized with downstream task rewards through group-relative policy optimization. We evaluate ElasticMem on MemorySuite, covering memory-intensive QA and embodied agent control. Across Qwen2.5-3B-Instruct and Qwen2.5-7B-Instruct backbones, ElasticMem improves weighted average QA accuracy by 26.2% and 24.6%, and improves ALFWorld success rate by 66.3% and 27.2%, respectively, over the strongest baselines, while achieving the lowest ALFWorld token cost. Ablations and qualitative analyses further show that adaptive retrieval and elastic budget allocation help ElasticMem prioritize useful evidence and transferable plans beyond rigid cosine similarity. Our code for ElasticMem will be released at https://github.com/ulab-uiuc/ElasticMem.

</details>

---

### [[20_Research/Papers/大模型/Counterfactual_Graph_for_Multi-Agent_LLM_Calibration|Counterfactual Graph for Multi-Agent LLM Calibration]]

![[assets/2605.30653_figure.png|800]]

- **arXiv**: [2605.30653](https://arxiv.org/abs/2605.30653)
- **PDF**: https://arxiv.org/pdf/2605.30653
- **详细分析**: [[20_Research/Papers/大模型/Counterfactual_Graph_for_Multi-Agent_LLM_Calibration|Counterfactual Graph for Multi-Agent LLM Calibration]]
- **作者**: Jiatan Huang, Mingchen Li, Ziming Li, Sunjae Kwon, Hong Yu, Chuxu Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Counterfactual Graph for Multi-Agent LLM Calibration》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：TriviaQA, TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems often treat agreement as evidence: when many agents in a panel give the same answer, that answer is assumed to be more reliable. We show that this assumption can fail after agents communicate. Communication can induce correlated failures and false consensus, so the same vote share may reflect reliable agreement in one topology but over-confidence in another. We propose CAGE-CAL, a counterfactual agent-graph calibration framework for multi-agent LLMs. For each query, CAGE-CAL compares an observed post-communication agent graph with a matched counterfactual no-communication graph, capturing both pairwise failure correlations and group-level dependencies. Rather than simply counting how many agents agree, CAGE-CAL estimates the counterfactual shift between observed and no-communication dependence, and calibrates confidence accordingly. Across five benchmarks, CAGE-CAL improves reliability discrimination with competitive ECE, and its calibrated confidence further improves topology selection over the best fixed-topology strategy.

</details>

---

### [[20_Research/Papers/强化学习/Improving_Small_Language_Models_for_Code_Generation_with_Reinforcement_Learning_from_Verification_Feedback|Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback]]

![[assets/2605.30478_figure.png|800]]

- **arXiv**: [2605.30478](https://arxiv.org/abs/2605.30478)
- **PDF**: https://arxiv.org/pdf/2605.30478
- **详细分析**: [[20_Research/Papers/强化学习/Improving_Small_Language_Models_for_Code_Generation_with_Reinforcement_Learning_from_Verification_Feedback|Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback]]
- **作者**: Egor Skopin, Evgeny Kotelnikov
- **cs 子类**: cs.CL, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Improving Small Language Models for Code Generation with Reinforcement Learning from Verification Feedback》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CodeRL, HumanEval, TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) trains language models using programmatically checkable signals such as unit-test outcomes, enabling direct optimization for functional correctness in code generation. We conduct an empirical study of RLVR for Python code generation on the MBPP benchmark using two small models (Qwen3-0.6B and Llama3.2-1B) with LoRA fine-tuning. Across multiple reward formulations such as: unit-test-only rewards, static-analysis-only shaping via the Ruff linter, and a combined reward, we compare group-based policy optimization variants (GRPO and GSPO) and evaluate both functional correctness and behavioral diagnostics. In our experimental setting, RLVR improves pass@1 on MBPP test by up to 13 percentage points under proposed combined reward configuration. However, we find that reward shaping can induce systematic behavioral shifts: using only static-analysis penalties may bias the policy toward shorter completions that reduce lint errors without reliably improving functional correctness. In contrast, combined rewards mitigate this degeneration and yield more stable trade-offs between correctness and style constraints. Overall, our results highlight that RLVR effectiveness for code generation is highly sensitive to reward design and optimization granularity, and that diagnostics beyond pass@1, including generation length, Ruff severity profiles, and execution error types are useful for identifying failure modes.

</details>

---
