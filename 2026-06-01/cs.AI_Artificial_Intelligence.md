# cs.AI | Artificial Intelligence | 2026-06-01

#arxiv #ComputerScience

**论文数**: 37

### [[20_Research/Papers/强化学习/LongTraceRL_Learning_Long-Context_Reasoning_from_Search_Agent_Trajectories_with_Rubric_Rewards|LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards]]

![[assets/2605.31584_figure.png|800]]

- **arXiv**: [2605.31584](https://arxiv.org/abs/2605.31584)
- **PDF**: https://arxiv.org/pdf/2605.31584
- **详细分析**: [[20_Research/Papers/强化学习/LongTraceRL_Learning_Long-Context_Reasoning_from_Search_Agent_Trajectories_with_Rubric_Rewards|LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards]]
- **作者**: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA, LongTraceRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-context reasoning remains a central challenge for large language models, which often fail to locate and integrate key information in extensive distracting content. Reinforcement learning with verifiable rewards (RLVR) has shown promise for this task, yet existing methods are limited by low-confusability distractors and sparse, outcome-only reward signals that cannot supervise intermediate reasoning steps. To address these issues, we introduce \textsc{LongTraceRL}. For data construction, we generate multi-hop questions via knowledge graph random walks and leverage search agent trajectories to build \emph{tiered distractors}: documents the agent read but did not cite (high confusability) and documents that appeared in search results but were never opened (low confusability), producing training contexts that are far more challenging than those built by random sampling or one-shot search. For reward design, we propose a \emph{rubric reward} that uses the gold entities along each reasoning chain as fine-grained, entity-level process supervision. This rubric reward is applied only to responses with correct final answers (positive-only strategy), distinguishing the reasoning quality among correct responses and preventing reward hacking. Experiments on three reasoning LLMs (4B--30B) across five long-context benchmarks demonstrate that \textsc{LongTraceRL} consistently outperforms strong baselines and encourages comprehensive, evidence-grounded reasoning. Codes, datasets and models are available at \href{https://github.com/THU-KEG/LongTraceRL}{https://github.com/THU-KEG/LongTraceRL}.

</details>

---

### [[20_Research/Papers/强化学习/Answer-Set-Programming-based_Abstractions_for_Reinforcement_Learning|Answer-Set-Programming-based Abstractions for Reinforcement Learning]]

![[assets/2605.31444_figure.png|800]]

- **arXiv**: [2605.31444](https://arxiv.org/abs/2605.31444)
- **PDF**: https://arxiv.org/pdf/2605.31444
- **详细分析**: [[20_Research/Papers/强化学习/Answer-Set-Programming-based_Abstractions_for_Reinforcement_Learning|Answer-Set-Programming-based Abstractions for Reinforcement Learning]]
- **作者**: Rafael Bankosegger, Thomas Eiter, Johannes Oetsch
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Answer-Set-Programming-based Abstractions for Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Answer-Set, RRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) enables autonomous agents to learn policies from experience, but realistic problems often involve enormous state spaces, making learning and generalisation challenging. Abstraction and approximation are therefore essential. Relational Reinforcement Learning (RRL) offers a way to reason about objects and their relations, and the CARCASS framework by Martijn van Otterlo demonstrates how logical representations can model Markov Decision Processes (MDPs) in first-order domains. Originally implemented in Prolog, CARCASS leverages domain knowledge to create powerful abstractions. We explore Answer-Set Programming (ASP), which is a rich and, contrary to Prolog, fully declarative modelling language, to realise CARCASS abstractions. We evaluate our ASP-based implementation in case studies of two domains, viz. Blocks World and Minigrid. Our results indicate that CARCASS with ASP provides a promising approach to constructing abstractions for RL, especially when domain knowledge is available.

</details>

---

### [[20_Research/Papers/强化学习/Dreaming_Of_Others_Latent_Teammate_Modeling_In_World_Models_For_Multi-Agent_Reinforcement_Learning|Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning]]

![[assets/2605.31361_figure.png|800]]

- **arXiv**: [2605.31361](https://arxiv.org/abs/2605.31361)
- **PDF**: https://arxiv.org/pdf/2605.31361
- **详细分析**: [[20_Research/Papers/强化学习/Dreaming_Of_Others_Latent_Teammate_Modeling_In_World_Models_For_Multi-Agent_Reinforcement_Learning|Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning]]
- **作者**: Tomas Leroy-Stone
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 2.82（加权：大模型 0.5，强化学习 0.96，世界模型 1.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Dreaming Of Others: Latent Teammate Modeling In World Models For Multi-Agent Reinforcement Learning》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BenchMARL, JaxMARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In cooperative multi-agent reinforcement learning (MARL), agents must coordinate with partners whose internal policies and intentions are not directly observable. While world models such as Dreamer have demonstrated strong generalization and sample efficiency in single-agent settings, their application to MARL remains limited by an inability to handle teammate-induced uncertainty. We propose a new perspective: treat teammates as structured, learnable components within the agent's world model. We introduce an architecture that factorizes the latent state of a Dreamer-style recurrent state-space model (RSSM) into environment and teammate components, and learns an auxiliary Theory-of-Mind (ToM) head to infer latent embeddings of partner behavior such as character, intent, and predicted actions from partial trajectories. These teammate latents condition the actor and critic, enabling the agent to imagine and adapt to diverse collaborators. We outline how this approach can support zero-shot and few-shot coordination in partially observable settings and propose a set of benchmarks and evaluation protocols to assess its impact. This work positions world models as not only predictors of environmental dynamics, but as simulators of social behavior, opening new directions for generalizable, human-compatible AI.

</details>

---

### [[20_Research/Papers/强化学习/The_Terminal_Representation_in_Reinforcement_Learning|The Terminal Representation in Reinforcement Learning]]

![[assets/2605.31289_figure.png|800]]

- **arXiv**: [2605.31289](https://arxiv.org/abs/2605.31289)
- **PDF**: https://arxiv.org/pdf/2605.31289
- **详细分析**: [[20_Research/Papers/强化学习/The_Terminal_Representation_in_Reinforcement_Learning|The Terminal Representation in Reinforcement Learning]]
- **作者**: Amir Esterhuysen, Anders Jonsson
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《The Terminal Representation in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Representation learning is a powerful tool for spatio-temporal abstraction within reinforcement learning (RL). Two well established approaches are through the successor representation (SR) and the default representation (DR). The SR encodes states by the future trajectories they induce, capturing information flow decoupled from reward. The DR builds on this by weighting trajectories with reward, integrating credit-assignment structure into the representation. Eigenvectors of both representations have been used to support a range of downstream tasks -- including option discovery, reward shaping, transfer learning, and exploration. We introduce a structurally distinct formulation: the terminal representation (TR). The TR encodes reward-weighted trajectories similarly to the DR, but can be learned as a lower-dimensionality object, and can be used directly for the mentioned applications without eigenvector computations. Eigendecomposition also imposes the assumption of symmetric transition dynamics, which the TR can bypass. In this work we develop the theoretical foundations of the TR: its derivation, convergence of two learning algorithms, its use for zero-shot compositionality, and equivalences between alternative reward formulations. We further show the TR is embedded in the top DR eigenvector, allowing it to capture the same underlying knowledge without eigendecomposition. Additionally, we provide empirical evidence of the TR as a viable alternative to existing representations in subsidiary applications, while requiring less computational overhead to learn, store, and use.

</details>

---

### [[20_Research/Papers/具身智能/DeMaVLA_A_Vision-Language-Action_Foundation_Model_for_Generalizable_Deformable_Manipulation|DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation]]

![[assets/2605.31286_figure.png|800]]

- **arXiv**: [2605.31286](https://arxiv.org/abs/2605.31286)
- **PDF**: https://arxiv.org/pdf/2605.31286
- **详细分析**: [[20_Research/Papers/具身智能/DeMaVLA_A_Vision-Language-Action_Foundation_Model_for_Generalizable_Deformable_Manipulation|DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation]]
- **作者**: Taiyi Su, Jian Zhu, Tianjian Wang, Youzhang He, Zitai Huang, Jianjun Zhang, Chong Ma, Hanyang Wang, Tianjiao Zhang, Munan Yin, Weihao Ding, Yi Xu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.8，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeMaVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world household robots require Vision-Language-Action (VLA) foundation models that can acquire reusable manipulation skills across diverse objects, task conditions, and household environments. Deformable-object folding is a representative challenge, requiring robots to handle clothing items from random initial states across varying categories, geometries, materials, and scenes. However, existing VLA systems commonly train separate policies for different object categories, while naively mixed multi-task training often suffers from task interference and degraded performance. To move beyond category-specific folding policies, we introduce DeMaVLA, a VLA foundation model for generalizable Deformable Manipulation. DeMaVLA adopts a VLM backbone with an action expert and formulates continuous action generation using flow matching. To improve efficiency, the action expert is constructed by pruning every other transformer layer while preserving layer-wise alignment with the VLM backbone, reducing training and inference cost. DeMaVLA is first pre-trained on approximately 5,000 hours of selected real-world dual-arm demonstrations to acquire general manipulation priors. It is then post-trained on mixed folding data that aggregates self-collected demonstrations and corrective trajectories from real-robot failures across multiple folding tasks through a human-in-the-loop Data Aggregation~(DAgger) pipeline. Experiments show that DeMaVLA achieves competitive performance on RoboTwin and strong real-world results on our household folding benchmark. These results highlight the value of scalable real-world data, efficient action generation, and corrective learning for general-purpose VLA policies in deformable-object manipulation.

</details>

---

### [[20_Research/Papers/强化学习/Why_Linear_Recurrent_Memory_Works_in_Partially_Observable_Reinforcement_Learning|Why Linear Recurrent Memory Works in Partially Observable Reinforcement Learning]]

![[assets/2605.31261_figure.png|800]]

- **arXiv**: [2605.31261](https://arxiv.org/abs/2605.31261)
- **PDF**: https://arxiv.org/pdf/2605.31261
- **详细分析**: [[20_Research/Papers/强化学习/Why_Linear_Recurrent_Memory_Works_in_Partially_Observable_Reinforcement_Learning|Why Linear Recurrent Memory Works in Partially Observable Reinforcement Learning]]
- **作者**: Yike Zhao, Onno Eberhard, Malek Khammassi, Ali H. Sayed, Michael Muehlebach
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Why Linear Recurrent Memory Works in Partially Observable Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：POPGym, RingWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The family of linear recurrent neural networks has shown strong performance as recurrent memory units in partially observable reinforcement learning. We provide a theoretical justification for their empirical effectiveness by constructing and studying two linear filters: (i) the first exactly reproduces the pre-softmax logits of the belief vector in a hidden Markov model (HMM) under a deterministic transition matrix, thereby serving as a sufficient statistic for optimal policy learning, (ii) the second achieves vanishing state-decoding error under a nearly deterministic transition matrix, thus reducing state ambiguity to near zero. The results extend to action-controlled HMMs, where the corresponding linear filters become time-varying with action-dependent dynamics. We illustrate our main results through numerical experiments and further show that the constructed linear filter serves as a strong feature extractor in a small reinforcement learning game.

</details>

---

### [[20_Research/Papers/具身智能/ERGeoBench_A_Comprehensive_Benchmark_for_Embodied_Reasoning_and_Geo-localization_in_Multimodal_Large_Language_Models|ERGeoBench:A Comprehensive Benchmark for Embodied Reasoning and Geo-localization in Multimodal Large Language Models]]

![[assets/2605.31251_figure.png|800]]

- **arXiv**: [2605.31251](https://arxiv.org/abs/2605.31251)
- **PDF**: https://arxiv.org/pdf/2605.31251
- **详细分析**: [[20_Research/Papers/具身智能/ERGeoBench_A_Comprehensive_Benchmark_for_Embodied_Reasoning_and_Geo-localization_in_Multimodal_Large_Language_Models|ERGeoBench:A Comprehensive Benchmark for Embodied Reasoning and Geo-localization in Multimodal Large Language Models]]
- **作者**: Kaiwen Xue, Tao Wei, Guoxin Zhang, Zhonghong Ou, Kaoyan Lu, Yu Feng, Yifan Zhu, Haoran Luo
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 1.2，大模型 0.5）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《ERGeoBench:A Comprehensive Benchmark for Embodied Reasoning and Geo-localization in Multimodal Large Language Models》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ERGeoBench, GAEA-Bench, IMAGEO-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) have shown strong potential as embodied agents, yet embodied geo-localization remains underexplored due to the lack of fine-grained evaluation. We introduce ERGeoBench, a diagnostic benchmark for vision-driven embodied geo-localization. ERGeoBench evaluates models under three progressive settings -- single-view, panorama-view, and embodied-view -- where agents may actively acquire observations through sequential changes in yaw, pitch, and zoom. The benchmark contains 2,207 globally distributed street-view panoramas and measures four complementary capabilities: foundational perception, spatial awareness, common sense reasoning, and geo-localization reasoning. Evaluations of leading proprietary and open-source MLLMs show that current models can infer high-level geographic semantics, but still struggle with fine-grained perceptual operations, metric localization, and spatial consistency across views. We further observe that geo-localization is strongly correlated with the other capability dimensions, suggesting that accurate localization depends on integrated perception, spatial reasoning, and commonsense inference rather than isolated visual recognition. Overall, ERGeoBench provides a unified framework for diagnosing and advancing human-like embodied geo-localization. Project Page: https://kaixuewen.github.io/ERGeoBench/

</details>

---

### [[20_Research/Papers/大模型/EchoRL_Reinforcement_Learning_via_Rollout_Echoing|EchoRL: Reinforcement Learning via Rollout Echoing]]

![[assets/2605.31228_first_page.png|800]]

- **arXiv**: [2605.31228](https://arxiv.org/abs/2605.31228)
- **PDF**: https://arxiv.org/pdf/2605.31228
- **详细分析**: [[20_Research/Papers/大模型/EchoRL_Reinforcement_Learning_via_Rollout_Echoing|EchoRL: Reinforcement Learning via Rollout Echoing]]
- **作者**: Jinhe Bi, Aniri, Minglai Yang, Xingcheng Zhou, Wenke Huang, Sikuan Yan, Yujun Wang, Zixuan Cao, Michael Färber, Xun Xiao, Volker Tresp, Yunpu Ma
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《EchoRL: Reinforcement Learning via Rollout Echoing》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EchoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards is an effective route for post-training to strengthen the reasoning capability of large language models. However, as training proceeds, the learning signal can collapse thus makes the training gain become marginal and ineffective. Specifically, a growing fraction of prompts' rollouts become advantage-degenerated: all the self-generated rollouts show verified-success, making the standard deviation over their rewards be zero; accordingly each rollout's advantage becomes degenerated (zero) as well. Given such rollouts' advantages, the policy-gradient for model optimization eventually vanishes, capping the training performance. We argue that some of these rollouts still contain valuable learning signals but unfortunately omitted with the existing RLVR methods. In this paper, inspired through analyzing the entropy pattern behind golden trajectories produced by external expert models, we propose EchoRL for better exploiting the advantage-degenerated rollouts to further improve the training performance. EchoRL is a lightweight module that first identifies an EchoClip from verified-success rollouts based on their step-level entropy values, and then feeds this clip back as an auxiliary supervision signal in the RL objective. Extensive experiments across 10 benchmarks, 5 LLM backbones, and 4 popular RLVR post-training methods demonstrate that EchoRL consistently improves RLVR post-training with minimal overhead.

</details>

---

### [[20_Research/Papers/具身智能/Probing_Collision_Grounding_in_Vision-Language_Models_for_Safe_Human-Robot_Collaboration|Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration]]

![[assets/2605.31196_figure.png|800]]

- **arXiv**: [2605.31196](https://arxiv.org/abs/2605.31196)
- **PDF**: https://arxiv.org/pdf/2605.31196
- **详细分析**: [[20_Research/Papers/具身智能/Probing_Collision_Grounding_in_Vision-Language_Models_for_Safe_Human-Robot_Collaboration|Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration]]
- **作者**: Jun Wang, Xiaohao Xu, Xiaonan Huang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Probing Collision Grounding in Vision-Language Models for Safe Human-Robot Collaboration》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, IS-Bench, ResponsibleRobotBench, RoboBench, SafeAgentBench, ThreeDWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe human--robot collaboration requires more than visual description: a monitor must determine whether the robot body is safely separated, already colliding with the scene or a person, or about to collide. We call this capability collision grounding: binding visual observations to robot body geometry, camera viewpoint, scene layout, human proximity, and temporal motion in order to infer present and imminent contact. We introduce TouchSafeBench, a physics-grounded benchmark for evaluating collision grounding in vision-language models (VLMs). Built in Habitat~3.0, TouchSafeBench contains 2,940 simulated indoor co-presence episodes across social navigation and social rearrangement, with synchronized multi-view RGB-D observations, top-down trajectory maps, calibrated camera metadata, and simulator-derived contact labels. We study two deployment-facing tasks: classifying the current safety state and warning about imminent collision before contact. Across three frontier or robotics-oriented VLMs and nine visual representations, current models remain far from reliable: the best average Macro-F1 stays below 50\%, explicit depth is not automatically transformed into robot-body collision evidence, and robot--scene contact is consistently harder than human-contact risk. TouchSafeBench reveals a central limitation of embodied VLMs: visual fluency does not imply physical accountability. Reliable robot safety monitors will need representations that explicitly bind viewpoint, robot morphology, metric geometry, and future collision. We will release the benchmark upon acceptance.

</details>

---

### [[20_Research/Papers/大模型/Emergent_Languages_in_Populations_of_Language_Model_Agents_From_Token_Efficiency_to_Oversight_Evasion|Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion]]

![[assets/2605.31170_figure.png|800]]

- **arXiv**: [2605.31170](https://arxiv.org/abs/2605.31170)
- **PDF**: https://arxiv.org/pdf/2605.31170
- **详细分析**: [[20_Research/Papers/大模型/Emergent_Languages_in_Populations_of_Language_Model_Agents_From_Token_Efficiency_to_Oversight_Evasion|Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion]]
- **作者**: Stine Lyngsø Beltoft, William Brach, Federico Torrielli, Jacob Nielsen, Annemette Brok Pirchert, Filippo Tonini, Peter Schneider-Kamp, Lukas Galke Poech
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Emergent Languages in Populations of Language Model Agents: From Token Efficiency to Oversight Evasion》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monitoring autonomous language model agents currently relies mostly on surface behavior. But what happens when agent populations invent new languages with the goal of avoiding human oversight. Here, we study the emergent languages on Moltbook. For this, we build upon the Moltbook Files dataset and apply a two-stage approach consisting of a rule-based heuristic (about 6000 matches) followed by zero-shot classification (518 kept). The resulting categories include token efficiency (166), new natural languages (106), and oversight evasion (59). We conduct both quantitative and qualitative analyses. Our results show that posts proposing new languages for avoiding oversight are judged by DeepSeek-3.2 as being less aligned than the other categories and that all languages can be learned by other language models in-context merely from a description of the language. Moreover, manually studying exemplary cases reveals surprisingly sophisticated steganographic protocols like embedding hidden messages in natural language. Although we cannot be certain about the extent of autonomy in ideation of these languages, our results add up to the evidence that monitoring surface behavior may soon be insufficient for retaining control over agent populations.

</details>

---

### [[20_Research/Papers/大模型/SpatialAct_Probing_Spatial_Reasoning-to-Action_Capabilities_of_VLM_Agents_in_3D_Scenes|SpatialAct: Probing Spatial Reasoning-to-Action Capabilities of VLM Agents in 3D Scenes]]

![[assets/2605.31148_figure.png|800]]

- **arXiv**: [2605.31148](https://arxiv.org/abs/2605.31148)
- **PDF**: https://arxiv.org/pdf/2605.31148
- **详细分析**: [[20_Research/Papers/大模型/SpatialAct_Probing_Spatial_Reasoning-to-Action_Capabilities_of_VLM_Agents_in_3D_Scenes|SpatialAct: Probing Spatial Reasoning-to-Action Capabilities of VLM Agents in 3D Scenes]]
- **作者**: Tianhui Liu, Jie Feng, Zhiheng Zheng, Shengyuan Wang, Yiming Guo, Yanxin Xi, Hangyu Fan, Yong Li, Pan Hui
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《SpatialAct: Probing Spatial Reasoning-to-Action Capabilities of VLM Agents in 3D Scenes》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MetaVQA, OpenEQA, SpatialEval, VIS-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans can effortlessly perceive spatial layouts, form cognitive representations, reason about spatial relations, and translate such reasoning into actions in everyday 3D environments. Although recent vision-language models (VLMs) have shown promising performance on observation-conditioned spatial perception and reasoning tasks, it remains unclear whether they can build coherent spatial understanding, act upon it, and refine their actions through multi-turn feedback. To study this problem, we introduce \textbf{SpatialAct}, a simulator-grounded benchmark for probing \textit{action-conditioned spatial reasoning} in 3D scenes. Starting from the most challenging setting, Multi-turn Interactive Refinement, we further design its decomposed counterpart, Single-step Error Detection and Fix, together with five fundamental spatial ability tasks to diagnose the underlying causes of model failures. Experiments reveal a clear reasoning-to-action gap: current VLMs can perform well on isolated spatial reasoning tasks, but struggle to maintain coherent spatial beliefs and produce reliable actions during multi-turn feedback, substantially underperforming humans. These results suggest that current VLM agents still lack robust spatial state tracking under action-induced environment changes, even when low-level control is abstracted away.

</details>

---

### [[20_Research/Papers/强化学习/FOCUS_Forcing_In-Context_Object_Localization_through_Visual_Support_Constraints_and_Policy_Optimization|FOCUS: Forcing In-Context Object Localization through Visual Support Constraints and Policy Optimization]]

![[assets/2605.31145_figure.png|800]]

- **arXiv**: [2605.31145](https://arxiv.org/abs/2605.31145)
- **PDF**: https://arxiv.org/pdf/2605.31145
- **详细分析**: [[20_Research/Papers/强化学习/FOCUS_Forcing_In-Context_Object_Localization_through_Visual_Support_Constraints_and_Policy_Optimization|FOCUS: Forcing In-Context Object Localization through Visual Support Constraints and Policy Optimization]]
- **作者**: Mohammed Asad Karim, Vinay Kumar Verma
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《FOCUS: Forcing In-Context Object Localization through Visual Support Constraints and Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In-context localization (ICL) seeks to localize a target object specified by a small set of support examples in a query image, operating on the fly without training or parameter updates. Despite rapid advances in vision-language models (VLMs), achieving category-agnostic and visually grounded ICL remains an open problem, even though it is essential for applications such as image editing, personalized visual search, and retrieval. Existing methods are fragile and rely on explicit category supervision, which not only limits applicability in realistic settings with unnamed or instance-specific objects but also introduces category bias that steers predictions toward semantic priors rather than visual evidence. We introduce a two-stage training framework that explicitly optimizes in-context attention between support bounding boxes and query images without category supervision. We further refine localization via reinforcement learning using Group Relative Policy Optimization (GRPO) to directly minimize localization error. This formulation enforces visual correspondence over semantic priors, yielding robust instance-level localization. Empirically, a 7B-parameter model trained with our objectives outperforms models up to 72B parameters, demonstrating that context-aware localization objectives can surpass scaling alone. Comprehensive ablations validate the contribution of each component.

</details>

---

### [[20_Research/Papers/具身智能/TARIC_Memory-Augmented_Traversability-Aware_Outdoor_VLN_under_Interrupted_Semantic_Cues|TARIC: Memory-Augmented Traversability-Aware Outdoor VLN under Interrupted Semantic Cues]]

![[assets/2605.31121_figure.png|800]]

- **arXiv**: [2605.31121](https://arxiv.org/abs/2605.31121)
- **PDF**: https://arxiv.org/pdf/2605.31121
- **详细分析**: [[20_Research/Papers/具身智能/TARIC_Memory-Augmented_Traversability-Aware_Outdoor_VLN_under_Interrupted_Semantic_Cues|TARIC: Memory-Augmented Traversability-Aware Outdoor VLN under Interrupted Semantic Cues]]
- **作者**: Tianle Zeng, Hanjing Ye, Jianwei Peng, Jingwen Yu, Hanxuan Chen, Hong Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《TARIC: Memory-Augmented Traversability-Aware Outdoor VLN under Interrupted Semantic Cues》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Outdoor vision-language navigation (VLN) in long-range, open-world environments is frequently disrupted by semantic-cue interruptions, where informative goal cues become sparse, occluded, or leave the field of view. Once such cues disappear, agents enter a cue-free phase and often degrade into backtracking, oscillatory headings, or aimless exploration. While memory-based methods attempt to bridge these gaps, they often fail under traversability-driven detours: the remembered cue direction may be infeasible, forcing detours that prolong cue-free phases and gradually render robot-centric cues stale and implicit histories blurred. This makes traversability a stability condition for maintaining goal-directed guidance, rather than merely a local safety concern. We propose a unified outdoor VLN framework that survives semantic-cue interruptions by maintaining traversability-consistent executable guidance throughout prolonged cue-free phases. Specifically, our method extracts semantic bearings from visibility-gated goal or exploration cues and grounds them into executable headings using a real-time near-field traversability profile, providing goal-consistent feasible guidance beyond reject-only safety filtering. To prevent guidance degradation during detours, we lift intermittent 2D evidence into a world-aligned 3D cue memory with an uncertainty-aware readout mechanism, ensuring guidance remains continuously reachable and stable as the robot moves. We evaluate the framework on quadrupedal and wheeled platforms over 600--1000 m routes. Our method improves simulation success rate by over 10 percentage points over the strongest baseline and achieves a real-world success rate of 40%, compared to 17.5% for the strongest baseline, with substantially higher robustness during prolonged cue-free intervals.

</details>

---

### [[20_Research/Papers/具身智能/Does_Visual_Information_Play_a_Decisive_Role_in_Vision-Language-Action_Model_Driving_Behavior|Does Visual Information Play a Decisive Role in Vision-Language-Action Model Driving Behavior?]]

![[assets/2605.31041_figure.png|800]]

- **arXiv**: [2605.31041](https://arxiv.org/abs/2605.31041)
- **PDF**: https://arxiv.org/pdf/2605.31041
- **详细分析**: [[20_Research/Papers/具身智能/Does_Visual_Information_Play_a_Decisive_Role_in_Vision-Language-Action_Model_Driving_Behavior|Does Visual Information Play a Decisive Role in Vision-Language-Action Model Driving Behavior?]]
- **作者**: Jingtao He, Hongliang Lu, Xiaoyun Qiu, Yixuan Wang, Xinhu Zheng
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 1.5，大模型 0.1）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Does Visual Information Play a Decisive Role in Vision-Language-Action Model Driving Behavior?》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutoVLA, OpenDriveVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have demonstrated promising capability in autonomous driving, highlighting the potential of unified multimodal architectures for jointly modeling perception and planning. However, how current VLA-based driving behavior is grounded in visual information remains poorly understood. Existing evaluation protocols mainly focus on aggregate performance metrics, lacking structured and practical diagnostics to quantify visual-behavior dependency. In this work, we introduce a structured multi-level visual perturbation framework to analyze visual-behavior dependency in VLA-based driving models systematically. The framework organizes controlled visual perturbations along three complementary dimensions: channellevel degradation, information-level disruption, and structurelevel modification. We apply it to VLA-based driving systems and evaluate behavioral responses under both open-loop trajectory prediction and interactive closed-loop safety evaluation. Experimental results reveal evaluation-dependent dependency patterns and uneven visual grounding across abstraction levels. These findings call for more structured analyses and principled design of VLA driving models to better understand how visual information shapes behavior and develop safer, more robust systems.

</details>

---

### [[20_Research/Papers/大模型/De-attribute_to_Forget_for_LLM_Unlearning|De-attribute to Forget for LLM Unlearning]]

![[assets/2605.30919_figure.png|800]]

- **arXiv**: [2605.30919](https://arxiv.org/abs/2605.30919)
- **PDF**: https://arxiv.org/pdf/2605.30919
- **详细分析**: [[20_Research/Papers/大模型/De-attribute_to_Forget_for_LLM_Unlearning|De-attribute to Forget for LLM Unlearning]]
- **作者**: Xinyang Lu, Jiabao Pan, Rachael Hwee Ling Sim, See-Kiong Ng, Anthony Kum Hoe Tung, Bryan Kian Hsiang Low
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《De-attribute to Forget for LLM Unlearning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid development of large language models (LLMs) has raised concerns on the use of inappropriate data for training, which has led to a growing interest in LLM unlearning. Many existing LLM unlearning approaches rely on optimizing prediction loss(es), such as maximizing the loss on the forget set, but often face critical issues like over-forgetting and poor model utility. To address them, this paper novelly frames the optimization objective for LLM unlearning as one of zeroing out data attribution instead. In particular, we propose the first LLM unlearning framework based on data attribution rewards called DareU that performs reinforcement learning to update the LLM by reducing the attribution score of its generated responses (i.e., de-attributing) to the forget data owners. Empirical evaluation using an LLM classifier as an efficient approximation of attribution shows that DareU outperforms existing baselines by achieving effective unlearning while balancing forget quality and model utility well.

</details>

---

### [[20_Research/Papers/大模型/BlueFin_Benchmarking_LLM_Agents_on_Financial_Spreadsheets|BlueFin: Benchmarking LLM Agents on Financial Spreadsheets]]

![[assets/2605.30907_figure.png|800]]

- **arXiv**: [2605.30907](https://arxiv.org/abs/2605.30907)
- **PDF**: https://arxiv.org/pdf/2605.30907
- **详细分析**: [[20_Research/Papers/大模型/BlueFin_Benchmarking_LLM_Agents_on_Financial_Spreadsheets|BlueFin: Benchmarking LLM Agents on Financial Spreadsheets]]
- **作者**: Srivatsa Kundurthy, Clara Na, Colton Moraine, Anoushka Mohta, Case Winter, George Fang, John Ling, Emma Strubell, Zach Kirshner
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《BlueFin: Benchmarking LLM Agents on Financial Spreadsheets》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BankerToolBench, Fin-SheetBench, OfficeBench, OfficeQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present BlueFin, a benchmark that tasks large language model (LLM) agents with synthesis, manipulation, and comprehension tasks over spreadsheet workbooks in the professional finance domain. Though estimates of the global population of paying users of spreadsheet software range in the hundreds of millions -- an order of magnitude more than the estimated global population of professional developers -- comparatively fewer resources have been devoted to exploring and expanding LLM capabilities in the spreadsheet domain, with fewer still dedicated to mirroring real occupational tasks encountered by those in professional finance roles. In response, we curate a set of 131 challenging, complex tasks with real-world relevance in the domain, containing 3,225 granular rubric criteria; notably, our rubric criteria and LM judge evaluations are validated by a team of expert human annotators, resulting in high-quality, granular evaluations of complex tasks that are difficult to verify programmatically but can be reliably evaluated by an LM judge agent. Our judge achieves parity with expert consensus ($α=0.826$) with a macro-F1 score of 0.839. Frontier LLMs demonstrate poor performance on the challenging benchmark, with the strongest LLMs achieving less than 50\% average scores across tasks -- models exhibit particular weaknesses in dynamic correctness. Our contributions include a dataset of examples across three categories of spreadsheet tasks, an open source harness and agentic evaluation framework, and a characterization of existing frontier models' performance on our benchmark.

</details>

---

### [[20_Research/Papers/大模型/Inverse_Reinforcement_Learning_without_an_Optimal_Demonstrator_A_Feasible_Reward_Set_Approach|Inverse Reinforcement Learning without an Optimal Demonstrator: A Feasible Reward Set Approach]]

![[assets/2605.30903_figure.png|800]]

- **arXiv**: [2605.30903](https://arxiv.org/abs/2605.30903)
- **PDF**: https://arxiv.org/pdf/2605.30903
- **详细分析**: [[20_Research/Papers/大模型/Inverse_Reinforcement_Learning_without_an_Optimal_Demonstrator_A_Feasible_Reward_Set_Approach|Inverse Reinforcement Learning without an Optimal Demonstrator: A Feasible Reward Set Approach]]
- **作者**: Kihyun Kim, Shripad Deshmukh, Nikos Vlassis, Jiawei Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Inverse Reinforcement Learning without an Optimal Demonstrator: A Feasible Reward Set Approach》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inverse reinforcement learning (IRL) typically assumes demonstrations from a single optimal demonstrator, but in many applications data come from multiple imperfect demonstrators with heterogeneous suboptimality levels. We study reward learning in this setting through a feasible-reward-set framework: for each demonstrator, we encode its declared suboptimality level as a linear constraint and intersect the resulting feasible sets across demonstrators. Our theoretical analysis shows that the joint feasible set shrinks monotonically as data are added, and we give an exact characterization of when a new demonstrator strictly tightens it. We further establish two recovery guarantees for the feasible reward set of the ground-truth optimal demonstrator: one bound depends on closeness to the optimal occupancy, while the other requires only sufficient coverage and no near-optimal demonstrator. On the practical side, we introduce strategies to address the inherent reward ambiguity in the obtained reward set and provide an offline algorithm with function approximation for high-dimensional environments. Experiments in tabular grid-world and large language model (LLM) fine-tuning settings are consistent with the theoretical predictions and demonstrate the effectiveness of the proposed framework over baselines.

</details>

---

### [[20_Research/Papers/大模型/PatchWorld_Gradient-Free_Optimization_of_Executable_World_Models|PatchWorld: Gradient-Free Optimization of Executable World Models]]

![[assets/2605.30880_figure.png|800]]

- **arXiv**: [2605.30880](https://arxiv.org/abs/2605.30880)
- **PDF**: https://arxiv.org/pdf/2605.30880
- **详细分析**: [[20_Research/Papers/大模型/PatchWorld_Gradient-Free_Optimization_of_Executable_World_Models|PatchWorld: Gradient-Free Optimization of Executable World Models]]
- **作者**: Jiaxin Bai, Yue Guo, Yifei Dong, Jiaxuan Xiong, Tianshi Zheng, Yixia Li, Tianqing Fang, Yufei Li, Yisen Gao, Haoyu Huang, Zhongwei Xie, Hong Ting Tsang...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.35（加权：大模型 0.35，世界模型 1）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《PatchWorld: Gradient-Free Optimization of Executable World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentGym, AlfWorld, PatchWorld, PoE-World, Word2World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-agent environments are typically modeled as partially observable Markov decision processes (POMDPs), assuming that the simulator's latent state and transition dynamics are hidden from the agent. Yet little work has examined whether executable code can be induced to serve as a world model for prediction and planning under partial observability. We introduce PatchWorld, a gradient-free framework that turns offline trajectories into executable Python world models through counterexample-guided code repair. Instead of predicting the next observation with a black-box model, PatchWorld induces symbolic belief-state programs whose action updates can be inspected, replayed, and locally patched. Across seven AgentGym environments, PatchWorld-Simple achieves the highest code-based planning score among evaluated methods, reaching 76.4\% macro success in live one-step lookahead while invoking no LLM calls inside the world-model prediction module itself. We further find that a human-specified residual-memory bias improves surface observation fidelity but weakens decision utility. This exposes a tradeoff in executable world models, since improving observation fidelity can come at the expense of action-discriminative dynamics, and vice versa. Code is available at https://github.com/HKBU-KnowComp/PatchWorld.

</details>

---

### [[20_Research/Papers/大模型/DARTS_Distribution-Aware_Active_Rollout_Trajectory_Shaping_for_Accelerating_LLM_Reinforcement_Learning|DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning]]

![[assets/2605.30859_figure.png|800]]

- **arXiv**: [2605.30859](https://arxiv.org/abs/2605.30859)
- **PDF**: https://arxiv.org/pdf/2605.30859
- **详细分析**: [[20_Research/Papers/大模型/DARTS_Distribution-Aware_Active_Rollout_Trajectory_Shaping_for_Accelerating_LLM_Reinforcement_Learning|DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning]]
- **作者**: Yujie Wang, Siwei Chen, Longzan Luo, Xinyi Liu, Xupeng Miao, Fangcheng Fu, Bin Cui
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《DARTS: Distribution-Aware Active Rollout Trajectory Shaping for Accelerating LLM Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has become pivotal for improving model capabilities yet suffers from rollout efficiency bottlenecks due to the long-tail response length distribution. While existing works mitigate the impact of long tails via prompt-level tail scheduling, we focus on the root source of inefficiency: the distribution itself. Specifically, we characterize the long-tail distribution at a finer granularity, identifying intra-prompt long tails, and revealing that they frequently consist of ineffective verbosity. To address this, we propose a novel paradigm of active distribution shaping to shape the rollout distribution towards conciseness and certainty, thereby fundamentally resolving tail-induced overheads. We achieve this through a distribution-aware trajectory sampling mechanism, which selects trajectories from a redundant exploration space for each prompt, and an adaptive redundancy allocation scheme to maximize both shaping effectiveness and system efficiency. Experiments demonstrate significant acceleration over state-of-the-art systems by up to 1.77x without compromising model performance.

</details>

---

### [[20_Research/Papers/强化学习/Safe_Equilibrium_Policy_Optimization_for_Strategic_Agent_Policies|Safe Equilibrium Policy Optimization for Strategic Agent Policies]]

![[assets/2605.30854_figure.png|800]]

- **arXiv**: [2605.30854](https://arxiv.org/abs/2605.30854)
- **PDF**: https://arxiv.org/pdf/2605.30854
- **详细分析**: [[20_Research/Papers/强化学习/Safe_Equilibrium_Policy_Optimization_for_Strategic_Agent_Policies|Safe Equilibrium Policy Optimization for Strategic Agent Policies]]
- **作者**: Karthika Arumugam, Kiran Kumar Manku, Amit Dhanda
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Safe Equilibrium Policy Optimization for Strategic Agent Policies》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GTBench, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language models fine-tuned with reinforcement learning typically optimize for task reward, ignoring multi-agent strategic structure. Because these agents condition on natural language game-state descriptions and emit actions through free-form generation, strategic failure modes -- exploiting weaker opponents, coordinating on harmful equilibria, and externalizing costs are inseparable from the language interface itself. We propose Safe Equilibrium Policy Optimization (\sepo{}), a training objective that augments expected payoff with explicit penalties for exploitability, collusion risk, and externality cost. We implement \sepo{} as a reward signal for Group Relative Policy Optimization (GRPO), applied to Gemma~4 E4B-it and Qwen~3.5-4B after supervised fine-tuning (SFT). Evaluated across five strategic domains: Iterated Prisoner's Dilemma, repeated auctions, two negotiation variants, and Kuhn Poker. \sepo{} achieves zero exploit-pool advantage in Kuhn Poker for both models, outperforms the base model on safety in four domains, and corrects the over-cooperative behavior introduced by SFT. In negotiation, \sepo{} achieves a positive-safety outcome and only the positive normalized relative advantage of any negotiation configuration. Ablation experiments confirm that per-rollout exploit computation is necessary: a shared constant penalty cancels in GRPO advantage normalization (constant control-variate property), producing zero gradient. To support further research in strategic safety for agents, we release our \href{https://anonymous.4open.science/r/sepo-2668/README.md}{code} and SFT datasets.

</details>

---

### [[20_Research/Papers/具身智能/Hide-and-Seek_in_Trajectories_Discovering_Failure_Signals_for_VLA_Runtime_Monitoring|Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring]]

![[assets/2605.30834_figure.png|800]]

- **arXiv**: [2605.30834](https://arxiv.org/abs/2605.30834)
- **PDF**: https://arxiv.org/pdf/2605.30834
- **详细分析**: [[20_Research/Papers/具身智能/Hide-and-Seek_in_Trajectories_Discovering_Failure_Signals_for_VLA_Runtime_Monitoring|Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring]]
- **作者**: Seongheon Park, Wendi Li, Changdae Oh, Samuel Yeh, Zsolt Kira, Michael Hagenow, Sharon Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models enable robots to follow natural language instructions and generalize across diverse tasks, but they remain vulnerable to execution failures that compromise reliability in real-world deployment. Detecting such failures during execution is therefore critical for the robust deployment of embodied systems. Existing failure detection methods either rely on expensive action resampling or external models, while alternatives propagate trajectory-level labels uniformly across every timestep, obscuring localized failure signals. In this paper, we propose \textbf{Hide-and-Seek}, a framework that formulates VLA failure detection as a coarsely supervised learning problem. By combining inter-trajectory and intra-trajectory contrastive objectives, Hide-and-Seek localizes failure-indicative actions and induces temporally structured failure signals from trajectory-level supervision alone, without any step-level annotation. We evaluate Hide-and-Seek on LIBERO, VLABench, and a real-world robotic platform across three representative VLA policies: OpenVLA, $π_0$, and $π_{0.5}$.Our method achieves state-of-the-art multi-task failure detection performance with a practical accuracy--timeliness trade-off under conformal prediction, and generalizes well to both seen and unseen tasks.

</details>

---

### [[20_Research/Papers/大模型/On_the_impact_of_retrieved_content_representations_in_RAG_Pipelines|On the impact of retrieved content representations in RAG Pipelines]]

![[assets/2605.30790_figure.png|800]]

- **arXiv**: [2605.30790](https://arxiv.org/abs/2605.30790)
- **PDF**: https://arxiv.org/pdf/2605.30790
- **详细分析**: [[20_Research/Papers/大模型/On_the_impact_of_retrieved_content_representations_in_RAG_Pipelines|On the impact of retrieved content representations in RAG Pipelines]]
- **作者**: Jonathan J Ross, Bevan Koopman, Anton van der Vegt, Guido Zuccon
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM

#### 研究背景与动机

《On the impact of retrieved content representations in RAG Pipelines》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) supplements a language model's input with retrieved documents, yet most RAG pipelines inherit retrieval components designed for human readers. How retrieved content should be represented when the consumer is a large language model (LLM) rather than a human is less well understood. Recent work has proposed transformations of retrieved content and identified properties that affect generation, but each examines a single transformation or property in isolation, leaving open which features of a document's representation matter most. We address this with a controlled comparison: holding retrieval fixed, we vary only the representation of retrieved documents, comparing an original baseline against thirteen transformations spanning selection, summarisation, and reformulation, in query-dependent and query-independent variants. Across these fourteen representations we measure question-answering accuracy for four generators, and for each representation we also measure answer retention: whether a known answer-bearing document still supports its answer after transformation. We find that answer retention is the primary determinant of generator accuracy; notably, when retention is high, a representation's wording, structure, length, and query-dependence have limited effect. This suggests that accuracy gains attributed to specific mechanisms in prior work may be partly explained by how well those mechanisms preserve answer-bearing content, an attribution that cannot be settled without controlling for retention.

</details>

---

### [[20_Research/Papers/大模型/GSAM_A_Generalizable_and_Safe_Robotic_Framework_for_Articulated_Object_Manipulation|GSAM: A Generalizable and Safe Robotic Framework for Articulated Object Manipulation]]

![[assets/2605.30740_figure.png|800]]

- **arXiv**: [2605.30740](https://arxiv.org/abs/2605.30740)
- **PDF**: https://arxiv.org/pdf/2605.30740
- **详细分析**: [[20_Research/Papers/大模型/GSAM_A_Generalizable_and_Safe_Robotic_Framework_for_Articulated_Object_Manipulation|GSAM: A Generalizable and Safe Robotic Framework for Articulated Object Manipulation]]
- **作者**: Beichen Shao, Mengying Xie, Heng Su, Wanyi Zhang, Mingyan Li, Yan Ding, Fausto Giunchiglia, Chao Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《GSAM: A Generalizable and Safe Robotic Framework for Articulated Object Manipulation》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Articulated object manipulation is a unique challenge for service robots. Existing methods employ end-to-end policy learning, visionmotion planning, and large-language/visual-language model (LLM/VLM), but often overlook the diversity of articulated objects and the complexity of interactions between end-effector and handle, leading to limited generalization and destructive collisions. To address this, we propose GSAM, a generalizable and safe robotic framework for articulated object manipulation. Specifically, a vision-based perceiver generates the kinematic parameters. Considering that pre-trained markers in perceiver yield raw estimations that may deviate from commonsense, we present a f ine-tuned VLM-based refiner, using chain-of-thought (COT) commonsense reasoning to refine perception. To prevent destructive collisions, we design an interaction constraint function generator, integrating articulated object, interaction pose, and obstacle avoidance knowledge into a base. LLM then functionalize these constraints and apply them to trajectory and posture planning. A kinematic-aware manipulation planner verifies reachability for trajectory and posture. Experiments on 50 hinge tasks across 5 object categories and 50 randomly initialized end-effectorhandle configurations show that GSAM reduces standard deviation by 3.1% and improves manipulation success rate by 36.0% compared to the best baseline, respectively demonstrating the superior object generalization and interaction safety of GSAM in practical scenarios.

</details>

---

### [[20_Research/Papers/大模型/When_are_LLMs_Sufficient_Policy_Optimizers_for_Sequential_RL_Tasks|When are LLMs Sufficient Policy Optimizers for Sequential RL Tasks?]]

![[assets/2605.30719_figure.png|800]]

- **arXiv**: [2605.30719](https://arxiv.org/abs/2605.30719)
- **PDF**: https://arxiv.org/pdf/2605.30719
- **详细分析**: [[20_Research/Papers/大模型/When_are_LLMs_Sufficient_Policy_Optimizers_for_Sequential_RL_Tasks|When are LLMs Sufficient Policy Optimizers for Sequential RL Tasks?]]
- **作者**: Stephane Hatgis-Kessell, Emma Brunskill
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.56，世界模型 0.16，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《When are LLMs Sufficient Policy Optimizers for Sequential RL Tasks?》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-World, NoiseWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study when large language models (LLMs) can serve as effective black-box policy optimizers for reinforcement learning (RL) tasks, i.e., when can we replace classical RL algorithms with an LLM? We explore this question by introducing Prompted Policy Optimization (PromptPO), an iterative method that prompts an LLM with Python descriptions of the state space, action space, and reward function, then has it generate and refine executable policies based on rollout feedback. Across hard exploration environments, Meta-World robotics tasks, and several real-world control problems, PromptPO often matches or exceeds the performance of standard RL baselines while using substantially fewer environment interactions. To maximize expected return, and without further explicit prompting, the policies PromptPO outputs range from tuned proportional controllers or rule-based plans to policies that run planning algorithms like value iteration. Our results demonstrate that LLM-based policy optimization is sufficient when the LLM can leverage prior knowledge about the environment or optimization strategy. PromptPO underperforms standard RL baselines in MuJoCo domains. This demonstrates possible limitations of LLM-based policy optimization to settings that requiring fine-grained continuous control.

</details>

---

### [[20_Research/Papers/大模型/Simple_Token-Efficient_Vision-Language_Model_for_Case-level_Pathology_Synoptic_Report_Generation|Simple Token-Efficient Vision-Language Model for Case-level Pathology Synoptic Report Generation]]

![[assets/2605.30716_figure.png|800]]

- **arXiv**: [2605.30716](https://arxiv.org/abs/2605.30716)
- **PDF**: https://arxiv.org/pdf/2605.30716
- **详细分析**: [[20_Research/Papers/大模型/Simple_Token-Efficient_Vision-Language_Model_for_Case-level_Pathology_Synoptic_Report_Generation|Simple Token-Efficient Vision-Language Model for Case-level Pathology Synoptic Report Generation]]
- **作者**: Zhiyuan Yang, Jiahao Cheng, Vincent Quoc-Huy Trinh, Mahdi S. Hosseini
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Simple Token-Efficient Vision-Language Model for Case-level Pathology Synoptic Report Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating clinically useful pathology reports for pathology cases from whole-slide images (WSIs) is challenging due to gigapixel resolution, long visual-token sequences, and the complexity of case-level reasoning, where a single case may contain multiple WSIs with heterogeneous tissues and ambiguous findings. We present a simple token-efficient vision--language model for case-level synoptic report generation that remains practical under constrained GPU memory. Our architecture follows a minimal three-component design: a frozen pathology patch encoder, a lightweight two-layer MLP vision-language aligner, and a large language model decoder, with an explicit WSI marker token to separate slides within a case. Training proceeds in two supervised stages: (1) aligner-only WSI captioning using heterogeneous WSI-text pairs, and (2) case-level supervised fine-tuning on case-report pairs for structured report generation. To reduce sequence length, we represent each slide using $512 \times 512$ patches at $5\times$ magnification, which reduces the average sequence length by up to $64\times$ times compared to the commonly used $20\times$ patches. Combined with efficient training techniques, we enable practical training with only half a NVIDIA H100 GPU. Across both training stages, our approach achieves high ROUGE-L/METEOR/BLEU-4 scores while being substantially more efficient in memory and runtime. In AI-based evaluations, our model is consistently preferred over strong baselines. Extensive ablations characterize performance-efficiency trade-offs and identify simple choices that improve robustness in multi-WSI settings. Overall, this work provides a strong, reproducible baseline for efficient pathology report generation, lowering the barrier to multi-WSI VLM research under limited compute.

</details>

---

### [[20_Research/Papers/大模型/Human-Alignment,_Calibration,_and_Activation_Patterns_in_Large_Language_Model_Uncertainty|Human-Alignment, Calibration, and Activation Patterns in Large Language Model Uncertainty]]

![[assets/2605.30675_figure.png|800]]

- **arXiv**: [2605.30675](https://arxiv.org/abs/2605.30675)
- **PDF**: https://arxiv.org/pdf/2605.30675
- **详细分析**: [[20_Research/Papers/大模型/Human-Alignment,_Calibration,_and_Activation_Patterns_in_Large_Language_Model_Uncertainty|Human-Alignment, Calibration, and Activation Patterns in Large Language Model Uncertainty]]
- **作者**: Kyle Moore, Jesse Roberts, Daryl Watson, William Ward, Grayson Heyboer
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM

#### 研究背景与动机

《Human-Alignment, Calibration, and Activation Patterns in Large Language Model Uncertainty》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MCQA, OEQA, ProtoQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Uncertainty Quantification is a large and growing subfield of large language model behavioral analysis. Primarily to recognize and combat hallucination, the field has largely focused on measuring and improving calibration, the accuracy of uncertainty judgments to task efficacy. In this work, we investigate the relatively underexplored question of how similar large language model uncertainty is to human uncertainty. We investigate the presence and strength of human-similar uncertainty signals, deemed uncertainty alignment, in large language model overt behavior and internal activation patterns. We identify whether the models show evidence of simultaneous alignment and calibration on a variety of datasets covering both multiple choice and open ended factual recall. And we characterize the effect of instruct fine-tuning on each of these facets.

</details>

---

### [[20_Research/Papers/具身智能/PInVerify_An_Offline_Embodied_Benchmark_for_Active_Instance_Verification|PInVerify: An Offline Embodied Benchmark for Active Instance Verification]]

![[assets/2605.30639_figure.png|800]]

- **arXiv**: [2605.30639](https://arxiv.org/abs/2605.30639)
- **PDF**: https://arxiv.org/pdf/2605.30639
- **详细分析**: [[20_Research/Papers/具身智能/PInVerify_An_Offline_Embodied_Benchmark_for_Active_Instance_Verification|PInVerify: An Offline Embodied Benchmark for Active Instance Verification]]
- **作者**: Yuhang Jiang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，大模型 0.4，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《PInVerify: An Offline Embodied Benchmark for Active Instance Verification》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbSpatial-Bench, GOAT-Bench, OpenEQA, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents have made strong progress in navigating to target objects, but reaching the goal vicinity does not guarantee that the agent has found the correct instance: subtle attribute differences (e.g., "white floral" vs. "white striped") often require close-range, multi-view inspection. We address this gap with Active Instance Verification (AIV), a task in which an agent actively selects viewpoints around a candidate object to decide whether it matches a fine-grained natural-language description. We formalize AIV as a finite-horizon decision process and introduce PInVerify, an offline embodied benchmark for AIV: 3,000 evaluation episodes across 18 object categories, delivered as multi-view captures with a 6-sector navigation topology that exposes trap views (navigable but uninformative) and unreachable sectors. As reference baselines we build a training-free pipeline and a LoRA-fine-tuned end-to-end agent around open-source multimodal large language models (MLLMs) at on-device scale ($\leq$8B parameters), with attribute decomposition, a visibility-weighted multi-view tracker, and three next-best-view (NBV) strategies. In our evaluation across Qwen3-VL (4B/8B), SenseNova-SI-1.2-InternVL3-8B, CLIP, and SigLIP2, the best MLLM-based baseline exceeds the best embedding baseline by 4.9 pp; GT-box ablations show a +3.1 pp detection gap; and we do not observe reliable gains from active viewpoint selection within the tested NBV strategies. A LoRA-fine-tuned agent (SFT+GSPO) reaches 85.6%. PInVerify aims to support further work on active, fine-grained semantic verification in embodied AI. Code: https://github.com/Avalon-S/PInVerify.

</details>

---

### [[20_Research/Papers/大模型/Harness_Updating_Is_Not_Harness_Benefit_Disentangling_Evolution_Capabilities_in_Self-Evolving_LLM_Agents|Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents]]

![[assets/2605.30621_figure.png|800]]

- **arXiv**: [2605.30621](https://arxiv.org/abs/2605.30621)
- **PDF**: https://arxiv.org/pdf/2605.30621
- **详细分析**: [[20_Research/Papers/大模型/Harness_Updating_Is_Not_Harness_Benefit_Disentangling_Evolution_Capabilities_in_Self-Evolving_LLM_Agents|Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents]]
- **作者**: Minhua Lin, Juncheng Wu, Zijun Wang, Zhan Shi, Yisi Sang, Bing He, Zewen Liu, Tianxin Wei, Zongyu Wu, Zhiwei Zhang, Dakuo Wang, Xiang Zhang...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities in Self-Evolving LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly deployed as systems built around editable external harnesses, including prompts, skills, memories and tools, that shape task execution without changing model parameters. Harness self-evolution adapts such agents by updating these harnesses from execution evidence. Yet it remains unclear whether a model's base capability in task-solving predicts its capabilities in harness self-evolution: which models produce useful harness updates, and which actually benefit from them? We analyze two harness self-evolution capabilities: (i) harness-updating, the capability to produce useful persistent harness updates from execution evidence; (ii) harness-benefit, the capability to benefit from updated harnesses during task solving. Our analysis reveals two findings. First, harness-updating is flat in base capability: models from different capability tiers produce harness updates that lead to surprisingly similar gains; even Qwen3.5-9B's updates yield gains comparable to those of Claude Opus~4.6. Second, harness-benefit is non-monotonic in base capability: weak-tier models benefit little from updated harnesses, mid-tier models benefit most, and strong-tier models benefit less than mid-tier. We trace low gains at the weak tier to two failure modes: weak-tier models may fail to activate relevant harness artifacts, or activate them but fail to follow them faithfully. These findings suggest investing capability budget in the task-solving agent rather than the evolver, and targeting harness invocation and long-horizon instruction following in agent training. Our source code is publicly available at https://github.com/A-EVO-Lab/a-evolve/tree/release/harness-evolution.

</details>

---

### [[20_Research/Papers/大模型/An_Organization-Scoped_LLM_Agent_Runtime_Architecture_for_Regulated_Cybersecurity_Operations|An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations]]

![[assets/2605.30604_figure.png|800]]

- **arXiv**: [2605.30604](https://arxiv.org/abs/2605.30604)
- **PDF**: https://arxiv.org/pdf/2605.30604
- **详细分析**: [[20_Research/Papers/大模型/An_Organization-Scoped_LLM_Agent_Runtime_Architecture_for_Regulated_Cybersecurity_Operations|An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations]]
- **作者**: George Fatouros, Georgios Makridis, George Kousiouris, John Soldatos, Dimosthenis Kyriazis
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Regulated cybersecurity workflows lack a runtime substrate that enforces organization-level scope across retrieval, tool calls, memory, findings, reports, and audit while remaining model-agnostic and locally deployable. Recent large language model (LLM) agent systems report strong results on isolated cybersecurity tasks, yet they do not by themselves define an auditable platform architecture for regulated security operations centre (SOC) and compliance workflows, where a single analyst may trigger actions that bind the organization, and where the runtime must integrate with existing SIEM/XDR stacks as a primary source of context and alert-driven triggers rather than operate as a standalone analytical layer. This paper proposes an organization-scoped LLM agent runtime architecture for financial cybersecurity. The contribution is a typed Security Context that is created at every entry point, including SIEM/XDR notifications ingested as first-class triggers, and enforced at every component boundary, combined with a shared Runtime Core, logical specialist subagents, a governed Tool Adapter Layer exposing SIEM/XDR query, enrichment, and response primitives under uniform policy and audit, structured findings with evidence references, tiered human-in-the-loop (HITL) gates, and append-only audit. Model Context Protocol (MCP), extended telemetry, digital twins for pentesting, graph retrieval, and federated knowledge sharing are treated as optional extension paths rather than mandatory runtime assumptions. We describe an implementable slice as the architecture's testability surface, and we propose a falsifiable evaluation plan with metric-level pass criteria for architecture readiness, security-policy enforcement, evidence traceability, output quality, and operational observability.

</details>

---

### [[20_Research/Papers/机器人/Prior_Availability_in_Industrial_Visual_Sim-to-Real_A_Review_of_CAD-Guided_and_CAD-Unavailable_Regimes|Prior Availability in Industrial Visual Sim-to-Real: A Review of CAD-Guided and CAD-Unavailable Regimes]]

![[assets/2605.30581_figure.png|800]]

- **arXiv**: [2605.30581](https://arxiv.org/abs/2605.30581)
- **PDF**: https://arxiv.org/pdf/2605.30581
- **详细分析**: [[20_Research/Papers/机器人/Prior_Availability_in_Industrial_Visual_Sim-to-Real_A_Review_of_CAD-Guided_and_CAD-Unavailable_Regimes|Prior Availability in Industrial Visual Sim-to-Real: A Review of CAD-Guided and CAD-Unavailable Regimes]]
- **作者**: Chenxi Tao, Seung-Kyum Choi
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《Prior Availability in Industrial Visual Sim-to-Real: A Review of CAD-Guided and CAD-Unavailable Regimes》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial visual sim-to-real is often described as transferring from synthetic images to real images, but industrial deployment usually involves a broader mismatch between available evidence and required decisions. A system may be built from CAD renderings, simulated RGB-D observations, normal reference images, synthetic defects, pretrained feature spaces, or language prompts, yet deployed under different sensors, lighting, materials, fixtures, calibration, production variation, and rare defect modes. This review reframes industrial visual sim-to-real as a domain-gap problem organized by prior availability. We distinguish CAD-available settings, where explicit object geometry can support rendering, calibration, pose estimation, segmentation, and test-time geometric verification; CAD-unavailable settings, where geometry is replaced by normal-reference appearance, feature distributions, teacher-student residuals, synthetic anomaly assumptions, foundation features, or vision-language priors; and boundary-prior settings, where approximate models, templates, reference views, or semantic correspondences preserve only part of the CAD role. This framing connects CAD-based detection and 6D pose-estimation literature with industrial anomaly and surface-inspection literature that is usually reviewed separately. To make the taxonomy concrete, we use empirical anchors on T-LESS/BOP, MVTec AD, and VisA. The anchors show that CAD render count alone does not close transfer; source-distribution design, detector capacity, and small real calibration can matter more. They also show that CAD at test time creates a distinct verification channel through mask, pose, and depth consistency, whereas CAD-unavailable inspection relies on calibrated normality and feature deviation. The review therefore argues against a single cross-task leaderboard and instead asks what prior grounds the deployment decision.

</details>

---

### [[20_Research/Papers/具身智能/Uncertainty-Aware_and_Temporally_Regulated_Expert_Advice_in_Reinforcement_Learning_for_Autonomous_Driving|Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving]]

![[assets/2605.30576_figure.png|800]]

- **arXiv**: [2605.30576](https://arxiv.org/abs/2605.30576)
- **PDF**: https://arxiv.org/pdf/2605.30576
- **详细分析**: [[20_Research/Papers/具身智能/Uncertainty-Aware_and_Temporally_Regulated_Expert_Advice_in_Reinforcement_Learning_for_Autonomous_Driving|Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving]]
- **作者**: Ahmed Abouelazm, Felix Klingebiel, Philip Schörner, J. Marius Zöllner
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exploration in reinforcement learning for autonomous driving is inherently unsafe: agents must experience novel behaviors to learn, yet exploration can lead to collisions or off-road driving. We propose an uncertainty-aware framework that leverages expert advice to guide exploration while avoiding long-term dependence. Advice is triggered when epistemic or aleatoric uncertainty exceeds adaptive thresholds derived from rolling buffers, ensuring advice evolves with the agent's confidence. A commitment-cooldown strategy with a stochastic early-stop heuristic regulates the duration and frequency of guidance, exposing the agent to coherent maneuvers without exhausting the advice budget. Expert and agent experiences are combined in a shared replay buffer within an off-policy implicit quantile network (IQN) backbone, enabling efficient reuse of expert trajectories. Experiments in CARLA show that our method outperforms the IQN baseline, improving success by 5-7% and reducing failures, demonstrating that risk-sensitive uncertainty coupled with regulated expert integration enables safer and more efficient exploration for sensor-based RL policy learning in unsignalized intersection navigation.

</details>

---

### [[20_Research/Papers/具身智能/Memory-Bound_but_Not_Bandwidth-Limited_The_Physical_AI_Inference_Gap_in_Batch-1_LLM_Decode|Memory-Bound but Not Bandwidth-Limited: The Physical AI Inference Gap in Batch-1 LLM Decode]]

![[assets/2605.30571_figure.png|800]]

- **arXiv**: [2605.30571](https://arxiv.org/abs/2605.30571)
- **PDF**: https://arxiv.org/pdf/2605.30571
- **详细分析**: [[20_Research/Papers/具身智能/Memory-Bound_but_Not_Bandwidth-Limited_The_Physical_AI_Inference_Gap_in_Batch-1_LLM_Decode|Memory-Bound but Not Bandwidth-Limited: The Physical AI Inference Gap in Batch-1 LLM Decode]]
- **作者**: Josef Chen
- **cs 子类**: cs.AI, cs.DC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Memory-Bound but Not Bandwidth-Limited: The Physical AI Inference Gap in Batch-1 LLM Decode》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GQA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical AI systems, including robots, autonomous vehicles, embodied agents and edge copilots, often run a different inference workload from cloud LLM serving: single-stream, batch-1 autoregressive decode, where one robot, camera feed or user session waits on the next token. This workload is usually described as memory-bandwidth-bound. Each decode step streams model weights and the active KV cache, so latency should scale with peak HBM bandwidth. We show that this account is true but incomplete. We measure batch-1 decode for three 7 to 8B-class GQA transformers across four NVIDIA GPUs: H100 SXM5, A100-80GB SXM4, L40S and L4. We evaluate context lengths from 2048 to 16384, producing 44 valid cells under a controlled bf16 SDPA setup. The achieved fraction of peak HBM bandwidth falls as peak bandwidth rises. On the headline Qwen-2.5-7B ctx=2048 cell, an L4 reaches roughly 81 percent of its analytic memory floor, while an H100 reaches only 27 percent. Physical-AI decode is memory-dominated, but faster memory does not translate into proportional latency gains. We test the missing term with a CUDA Graphs A/B experiment. On H100 at ctx=2048, CUDA Graphs improves decode latency by 1.259x across N=10 fresh sessions, with a 95 percent bootstrap confidence interval of 1.253 to 1.267. On L4, the same intervention gives only 1.028x. This isolates a launch-side overhead that becomes visible on fast GPUs but remains mostly hidden on slower, bandwidth-bound GPUs. The deployment implication is that memory savings matter only when the runtime realises them. On L4, bf16 decode sits close to the memory floor, but common quantised paths do not recover the expected 4x weight-traffic reduction: bnb-nf4 reaches 59.36 ms/step and AutoAWQ+Marlin reaches 45.24 ms/step from a 62.32 ms bf16 baseline. GPTQ+ExLlamaV2, with Ada-tuned int4 kernels, reaches 17.36 ms/step.

</details>

---

### [[20_Research/Papers/具身智能/Physically_Viable_World_Models_A_Case_for_Query-Conditioned_Embodied_AI|Physically Viable World Models: A Case for Query-Conditioned Embodied AI]]

![[assets/2605.30542_figure.png|800]]

- **arXiv**: [2605.30542](https://arxiv.org/abs/2605.30542)
- **PDF**: https://arxiv.org/pdf/2605.30542
- **详细分析**: [[20_Research/Papers/具身智能/Physically_Viable_World_Models_A_Case_for_Query-Conditioned_Embodied_AI|Physically Viable World Models: A Case for Query-Conditioned Embodied AI]]
- **作者**: Adam J. Thorpe, Stepan Tretiakov, Cheng-Hsi Hsiao, Su Ann Low, Xingjian Li, Hassan Iqbal, Neel P. Bhatt, Ufuk Topcu, Krishna Kumar
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 3.4（加权：具身智能 2.4，世界模型 1）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《Physically Viable World Models: A Case for Query-Conditioned Embodied AI》归入 具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for embodied AI must be physically viable: constructed to answer intervention queries by representing the physical structure governing action outcomes, rather than merely predicting future observations. Existing observation-predictive world models can produce visually plausible but physically wrong rollouts. This failure is structural; distinct physical systems can look identical yet diverge under intervention. We expose this problem with controlled benchmarks that fix the visible scene while varying latent physics. We show that such models may recommend infeasible actions, mispredict interaction outcomes, or certify unsafe behavior. We argue that embodied AI requires world models that identify the simplest physical abstraction sufficient to answer an intervention query. Such a model comprises modular components, including environment representation, latent state and parameter estimation, action specification, interventional dynamics, and query-level response. An autonomous orchestrator should identify the relevant abstraction and compose compatible learned and structured components per query. When closed-form physics is unavailable, uncertain, or costly, the transition model may be analytic, simulated, learned, or hybrid, but it must preserve the structure that determines interventional outcomes. This decomposition makes the model interpretable, its components verifiable, and its outputs auditable against the query. It also provides a design principle for new world models and a feasibility test for existing ones: the right abstraction is not the most detailed model of the world, but the simplest model that preserves the distinctions relevant to the query. We demonstrate this approach on queries that existing systems fail to answer correctly, and outline how an orchestrator can dynamically assemble and adapt physically viable models for planning, control, and verification.

</details>

---

### [[20_Research/Papers/强化学习/Scalable_Constrained_Multi-Agent_Reinforcement_Learning_via_State_Augmentation_and_Consensus_for_Separable_Dynamics|Scalable Constrained Multi-Agent Reinforcement Learning via State Augmentation and Consensus for Separable Dynamics]]

![[assets/2605.30461_figure.png|800]]

- **arXiv**: [2605.30461](https://arxiv.org/abs/2605.30461)
- **PDF**: https://arxiv.org/pdf/2605.30461
- **详细分析**: [[20_Research/Papers/强化学习/Scalable_Constrained_Multi-Agent_Reinforcement_Learning_via_State_Augmentation_and_Consensus_for_Separable_Dynamics|Scalable Constrained Multi-Agent Reinforcement Learning via State Augmentation and Consensus for Separable Dynamics]]
- **作者**: Santiago Amaya-Corredor, Miguel Calvo-Fullana, Anders Jonsson
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Scalable Constrained Multi-Agent Reinforcement Learning via State Augmentation and Consensus for Separable Dynamics》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CMARL, MARL, PowerNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a distributed approach for constrained Multi-Agent Reinforcement Learning (MARL) that combines state-augmented policy learning with distributed consensus over dual variables. Our method targets systems where agents have separable dynamics but must coordinate to satisfy global resource constraints, a setting in which, as we demonstrate empirically, independent learning fails to produce feasible solutions because agents cannot determine appropriate individual contributions toward collective constraint satisfaction. The key technical contribution is showing that lightweight neighbor-to-neighbor consensus over Lagrange multipliers suffices for globally coordinated constraint enforcement while preserving the scalability of independent training. Each agent learns a single augmented policy offline, conditioned on both its local state and a dual variable encoding constraint feedback. During execution, agents reach agreement on this dual variable through local communication alone. We prove that under mild connectivity assumptions, the consensus error among agents' multipliers is bounded, and show that this translates to a bounded constraint violation that decreases with graph connectivity and the number of consensus rounds. Unlike centralized training with decentralized execution (CTDE) approaches, whose complexity grows at least quadratically with agent count, our method scales linearly in both training and execution. Experiments on smart grid demand response demonstrate that consensus coordination is \emph{essential for feasibility}: without it, agents satisfy grid capacity constraints only by indefinitely postponing demand, a degenerate non-solution. With consensus, agents converge to a shared dual variable and satisfy both grid constraints and demand fulfillment, scaling to thousands of agents while CTDE baselines are limited to dozens.

</details>

---

### [[20_Research/Papers/大模型/Social_Reasoning_in_Machines_Investigating_Collective_Truth-Seeking_Dynamics_in_Large_Language_Model_Debate|Social Reasoning in Machines: Investigating Collective Truth-Seeking Dynamics in Large Language Model Debate]]

![[assets/2605.30391_figure.png|800]]

- **arXiv**: [2605.30391](https://arxiv.org/abs/2605.30391)
- **PDF**: https://arxiv.org/pdf/2605.30391
- **详细分析**: [[20_Research/Papers/大模型/Social_Reasoning_in_Machines_Investigating_Collective_Truth-Seeking_Dynamics_in_Large_Language_Model_Debate|Social Reasoning in Machines: Investigating Collective Truth-Seeking Dynamics in Large Language Model Debate]]
- **作者**: Tom Pecher
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Social Reasoning in Machines: Investigating Collective Truth-Seeking Dynamics in Large Language Model Debate》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HaluEval, TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human reasoning has long been theorised to operate socially, not through isolated individual cognition, but through collective adversarial discourse, a framework known as the Argumentative Theory of Reasoning (ATR). Rather than relying on individual "intellectualist reasoners" as the primary vehicle for truth-seeking, ATR reconceptualises truth as an emergent property of social epistemology: the product of imperfect individual reasoning refined under the adversarial pressure of debate. This distributed method of collective intelligence has guided humanity to ever-greater epistemic heights and underpins the foundational principles of all democratic systems. This thesis breaks new ground by, for the first time, simulating ATR through the multi-agent debate (MAD) of large language models (LLMs). With rigorous empirical analysis, we demonstrate that, when correctly engineering an epistemically diverse set of models, LLM-MAD can significantly improve truth-seeking performance on questionnaire-based tasks, even when individual debate participants exhibit limited standalone performance. Furthermore, we present strong empirical evidence that this performance gain is mechanistically grounded in the central principles of ATR, suggesting that collective reasoning may be universally favourable over individualist reasoning, rather than a quirk in biology or evolution. Finally, drawing on our analysis of debate dynamics, we propose a novel benchmarking methodology that leverages LLM-MAD to measure intrinsic model properties (such as hallucination propensity) in order to compare models in ways that current static benchmarking approaches cannot support.

</details>

---

### [[20_Research/Papers/机器人/Structured_interactions_improve_distributed_coordination_beyond_model_scaling_in_a_real-world_multi-robot_system|Structured interactions improve distributed coordination beyond model scaling in a real-world multi-robot system]]

![[assets/2605.30383_first_page.png|800]]

- **arXiv**: [2605.30383](https://arxiv.org/abs/2605.30383)
- **PDF**: https://arxiv.org/pdf/2605.30383
- **详细分析**: [[20_Research/Papers/机器人/Structured_interactions_improve_distributed_coordination_beyond_model_scaling_in_a_real-world_multi-robot_system|Structured interactions improve distributed coordination beyond model scaling in a real-world multi-robot system]]
- **作者**: Junping Wang, Zhizhong Zhang, Yongqiang Tang, Geng Zheng, Jiaming Zhang, Shiji Song, Yanmei Li, Yushan Ma
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Structured interactions improve distributed coordination beyond model scaling in a real-world multi-robot system》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling individual robot capabilities is common but costly. Here we investigate a system-level design question in real-world multi-robot coordination: given matched hardware budgets, does restructuring communication among robots yield larger gains than increasing onboard model size? Using a representative transport-and-mapping task with 10 physical robots (5 runs per condition, 60 runs total), we find that switching from fully connected to modular hierarchical interactions improves normalised performance by 47 points (0--100), whereas doubling neural network hidden size yields at most 9 points. Nested mixed-effects model comparisons show a substantially larger improvement in model fit for topology than for scale. The pattern is confirmed in independent SMAC replications; heterogeneous benchmark reanalyses provide secondary supporting consistency checks rather than primary evidence. Performance saturation beyond 1024 hidden units is observed in simulation-calibrated extrapolation, not directly on hardware. These results indicate that interaction structure can play a dominant role within the tested system and task setting, while broader quantitative generalisation remains to be established.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_Heterogeneous_Satellite_Cluster_Resources_Optimization|Multi-Agent Reinforcement Learning for Heterogeneous Satellite Cluster Resources Optimization]]

![[assets/2511.12792_first_page.png|800]]

- **arXiv**: [2511.12792](https://arxiv.org/abs/2511.12792)
- **PDF**: https://arxiv.org/pdf/2511.12792
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_Heterogeneous_Satellite_Cluster_Resources_Optimization|Multi-Agent Reinforcement Learning for Heterogeneous Satellite Cluster Resources Optimization]]
- **作者**: Mohamad A. Hady, Siyi Hu, Mahardhika Pratama, Zehong Cao, Ryszard Kowalczyk
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Multi-Agent Reinforcement Learning for Heterogeneous Satellite Cluster Resources Optimization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BSK-RL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work investigates resource optimization in heterogeneous satellite clusters performing autonomous Earth Observation (EO) missions using Reinforcement Learning (RL). In the proposed setting, two optical satellites and one Synthetic Aperture Radar (SAR) satellite operate cooperatively in low Earth orbit to capture ground targets and manage their limited onboard resources efficiently. Traditional optimization methods struggle to handle the real-time, uncertain, and decentralized nature of EO operations, motivating the use of RL and Multi-Agent Reinforcement Learning (MARL) for adaptive decision-making. This study systematically formulates the optimization problem from single-satellite to multi-satellite scenarios, addressing key challenges including energy and memory constraints, partial observability, and agent heterogeneity arising from diverse payload capabilities. Using a near-realistic simulation environment built on the Basilisk and BSK-RL frameworks, we evaluate the performance and stability of state-of-the-art MARL algorithms such as MAPPO, HAPPO, and HATRPO. Results show that MARL enables effective coordination across heterogeneous satellites, balancing imaging performance and resource utilization while mitigating non-stationarity and inter-agent reward coupling. The findings provide practical insights into scalable, autonomous satellite operations and contribute a foundation for future research on intelligent EO mission planning under heterogeneous and dynamic conditions.

</details>

---
