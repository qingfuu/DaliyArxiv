# cs.AI | Artificial Intelligence | 2026-07-01

#arxiv #ComputerScience

**论文数**: 43

### [[20_Research/Papers/大模型/QVal_Cheaply_Evaluating_Dense_Supervision_Signals_for_Long-Horizon_LLM_Agents|QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents]]

![[assets/2606.32034_figure.png|800]]

- **arXiv**: [2606.32034](https://arxiv.org/abs/2606.32034)
- **PDF**: https://arxiv.org/pdf/2606.32034
- **详细分析**: [[20_Research/Papers/大模型/QVal_Cheaply_Evaluating_Dense_Supervision_Signals_for_Long-Horizon_LLM_Agents|QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents]]
- **作者**: Sergio Hernández-Gutiérrez, Matteo Merler, Ilze Amanda Auzina, Joschka Strüber, Ameya Prabhu, Matthias Bethge
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, TerminalBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly act over long horizons, where a single trajectory can contain hundreds or thousands of actions. In these settings, outcome-only rewards provide too sparse guidance, failing to inform the model about the goodness of intermediate actions. Dense supervision methods aim to solve this problem by scoring intermediate steps, from intrinsic confidence to self-distillation and embedding similarities. However, it is common practice to evaluate them by measuring the downstream performance of a training pipeline that integrates them. This is expensive, conflates supervision quality with training engineering confounders, and renders different methodological families requiring distinct training setups incomparable. As a result, dense supervision methods are rarely benchmarked on common ground. We introduce QVal, a training-free testbed for directly evaluating dense supervision signals. Given a state-action pair, QVal measures how well a method's score is Q-aligned: whether it orders actions according to the Q-values of a strong reference-policy. This lets us compare signals before any training run and separate signal quality from other engineering choices. We instantiate QVal as QVal-v1.0, benchmarking 21 dense supervision methods across four diverse environments and seven methodological families, with over 1.2K evaluation experiments across six open-weight model backbones. We find that simple prompting baselines consistently outperform recent dense supervision methods from the literature, and that performance clusters strongly by family. These findings hold across model sizes, environments, and observation modalities. QVal is designed to be easily extensible to new environments and methods, enabling researchers to iterate on dense supervision methods before any training run.

</details>

---

### [[20_Research/Papers/大模型/Reinforcement_Learning_with_Metacognitive_Feedback_Elicits_Faithful_Uncertainty_Expression_in_LLMs|Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs]]

![[assets/2606.32032_figure.png|800]]

- **arXiv**: [2606.32032](https://arxiv.org/abs/2606.32032)
- **PDF**: https://arxiv.org/pdf/2606.32032
- **详细分析**: [[20_Research/Papers/大模型/Reinforcement_Learning_with_Metacognitive_Feedback_Elicits_Faithful_Uncertainty_Expression_in_LLMs|Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs]]
- **作者**: Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, Idan Szpektor, Arman Cohan
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capable of accurately judging their own performance are better positioned to improve it. We operationalize this idea via two novel mechanisms: reinforcement learning with metacognitive feedback (RLMF), a paradigm to refine completion rankings during preference optimization based on the quality of a model's self-judgments of performance, and metacognitive data selection, which uses similar self-judgments to identify high-value training examples, outperforming naive active learning. We apply these innovations to the problem of faithful calibration (FC), a task that is itself fundamentally metacognitive: the goal is to align expressed with intrinsic uncertainty, difficult even for frontier LLMs. We adopt a two-stage, decoupled approach, first using these methods to calibrate the faithfulness of models' self-reported confidence scores, then mapping to natural, context-adaptable linguistic uncertainty via targeted output editing. Extensive experiments show RLMF achieves generalizable, state-of-the-art FC on diverse tasks while preserving accuracy. Further, RLMF surpasses standard RL by up to 63% while enhancing models' ability to assess and express their own capability limits. This positions RLMF as a promising paradigm to enhance LLM metacognition toward improved abilities and alignment, and suggests metacognitive performance as an effective RL signal to overcome limits of prior intrinsic feedback methods.

</details>

---

### [[20_Research/Papers/具身智能/Freeform_Preference_Learning_for_Robotic_Manipulation|Freeform Preference Learning for Robotic Manipulation]]

![[assets/2606.32027_figure.png|800]]

- **arXiv**: [2606.32027](https://arxiv.org/abs/2606.32027)
- **PDF**: https://arxiv.org/pdf/2606.32027
- **详细分析**: [[20_Research/Papers/具身智能/Freeform_Preference_Learning_for_Robotic_Manipulation|Freeform Preference Learning for Robotic Manipulation]]
- **作者**: Marcel Torne, Anubha Mahajan, Abhijnya Bhat, Chelsea Finn
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 2.82（加权：具身智能 1.2，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Freeform Preference Learning for Robotic Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward design remains a central bottleneck for autonomous robot policy improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two trajectories is better overall, FPL lets them define natural-language preference axes, such as speed, safety, quality of placement, or carefulness, and provide pairwise preferences along each axis. These annotations are used to learn a language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward. We use this model to train a reward-conditioned policy that optimizes across the multiple human-specified dimensions. Across four real-world and two simulated long-horizon manipulation tasks, FPL improves over sparse-reward and binary-preference methods by 38 percentage points. Beyond improved performance, FPL learns dense progress signals without explicit subtask segmentation, shows compositionality of behavior not present in the data, and allows users to steer the policy towards different behaviors at test time without retraining. Blog post with videos available at https://freeform-pl.github.io/fpl.website/

</details>

---

### [[20_Research/Papers/世界模型/AdaJEPA_An_Adaptive_Latent_World_Model|AdaJEPA: An Adaptive Latent World Model]]

![[assets/2606.32026_figure.png|800]]

- **arXiv**: [2606.32026](https://arxiv.org/abs/2606.32026)
- **PDF**: https://arxiv.org/pdf/2606.32026
- **详细分析**: [[20_Research/Papers/世界模型/AdaJEPA_An_Adaptive_Latent_World_Model|AdaJEPA: An Adaptive Latent World Model]]
- **作者**: Ying Wang, Oumayma Bounou, Yann LeCun, Mengye Ren
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《AdaJEPA: An Adaptive Latent World Model》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation signal, and replans with the updated model. This closed-loop update continuously recalibrates the world model without additional expert demonstrations. Across a range of goal-reaching tasks, AdaJEPA substantially improves planning success with as few as one gradient step per MPC replanning step.

</details>

---

### [[20_Research/Papers/具身智能/TRIAGE_Role-Typed_Credit_Assignment_for_Agentic_Reinforcement_Learning|TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning]]

![[assets/2606.32017_figure.png|800]]

- **arXiv**: [2606.32017](https://arxiv.org/abs/2606.32017)
- **PDF**: https://arxiv.org/pdf/2606.32017
- **详细分析**: [[20_Research/Papers/具身智能/TRIAGE_Role-Typed_Credit_Assignment_for_Agentic_Reinforcement_Learning|TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning]]
- **作者**: Yuanda Xu, Zhengze Zhou, Hejian Sang, Xiaomin Li, Jiaxin Zhang, Xinchen Du, Zhipeng Wang, Alborz Geramifard
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL, ComputerVision

#### 研究背景与动机

《TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, Search-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning requires assigning credit to environment-facing actions such as searches, clicks, edits, navigation commands, and object interactions. Standard GRPO uses the final verifier outcome as a uniform advantage over all action tokens. This outcome signal is useful but structurally incomplete: it punishes useful exploration in failed rollouts and reinforces redundant or regressive actions in successful rollouts. We propose TRIAGE, a role-typed credit assignment framework that adds a semantic role axis to outcome credit. A structured judge classifies each segment as decisive progress, useful exploration, no-progress infrastructure, or regression, and a fixed role-conditioned rule maps these labels to bounded segment-level process rewards. This keeps verifier outcomes as the source of optimization direction while correcting the two main blind spots of outcome-only credit. We further show that role-conditioned credit is the optimal segment-level correction expressible from role labels alone -- a projection of the per-segment advantage residual onto the role variable -- so that the fixed role constants reduce advantage estimation error whenever the judge is reliable, and we connect this to lower-variance policy gradients. Across ALFWorld, Search-QA, and WebShop, TRIAGE improves success rates over GRPO for two policy models and outperforms both a scalar judge-derived process reward and an outcome-supervised shared-backbone value baseline. Ablations show that the gain comes from role typing rather than merely adding dense rewards: reliable detection of regression inside successful trajectories is the dominant contributor, while exploration credit provides a consistent secondary gain; on completed ALFWorld and WebShop rollouts, TRIAGE also reduces environment-facing turns by an additional $10.4\%$ and $14.8\%$ relative to GRPO.

</details>

---

### [[20_Research/Papers/具身智能/MECoBench_A_Systematic_Study_of_Multimodal_Agent_Collaboration_in_Embodied_Environments|MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments]]

![[assets/2606.31966_figure.png|800]]

- **arXiv**: [2606.31966](https://arxiv.org/abs/2606.31966)
- **PDF**: https://arxiv.org/pdf/2606.31966
- **详细分析**: [[20_Research/Papers/具身智能/MECoBench_A_Systematic_Study_of_Multimodal_Agent_Collaboration_in_Embodied_Environments|MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments]]
- **作者**: Qingyun Liu, Jiwen Zhang, Jingyi Hu, Siyuan Wang, Zhongyu Wei
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 2.15（加权：具身智能 1.2，大模型 0.95）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《MECoBench: A Systematic Study of Multimodal Agent Collaboration in Embodied Environments》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MECoBench, RoCoBench, VillagerBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent multimodal large language models (MLLMs) have strong potential as embodied agents, but their ability to collaborate in visually grounded environments remains underexplored. To address this gap, we introduce MECoBench, a multimodal embodied cooperation benchmark with an evaluation platform spanning diverse real-world tasks, two cooperation structures, and three collaboration modes. Through extensive experiments across various MLLMs, we summarize three key findings: (i) Collaboration generally improves embodied task completion, but its benefits depend on balancing collaborative gains against coordination complexity. (ii) Communication is essential to collaboration gains, while the best collaboration mode depends on team size and model capability. (iii) Moreover, collaboration improves robustness under noisy priors and exploration conditions. Generally, MECoBench provides a systematic testbed for understanding the mechanisms and limits of multimodal embodied collaboration. Code and dataset are available at https://github.com/q-i-n-g/MECoBench.

</details>

---

### [[20_Research/Papers/具身智能/MVP-Nav_Multi-layer_Value_Map_Planner_Navigator|MVP-Nav: Multi-layer Value Map Planner Navigator]]

![[assets/2606.31919_figure.png|800]]

- **arXiv**: [2606.31919](https://arxiv.org/abs/2606.31919)
- **PDF**: https://arxiv.org/pdf/2606.31919
- **详细分析**: [[20_Research/Papers/具身智能/MVP-Nav_Multi-layer_Value_Map_Planner_Navigator|MVP-Nav: Multi-layer Value Map Planner Navigator]]
- **作者**: Wenyuan Xie, Shaokai Wu, Yijin Zhou, Yanbiao Ji, Guodong Zhang, Bayram Bayramli, Qiuchang Li, Xunchu Zhou, Yue Ding, Hongtao Lu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MVP-Nav: Multi-layer Value Map Planner Navigator》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-shot Object Goal Navigation (ZSON) with RGB-only perception poses a fundamental challenge for embodied agents, as the absence of explicit depth information introduces severe physical uncertainty and semantic-physical misalignment. Existing approaches either rely on high-level semantic reasoning without geometric grounding or learn end-to-end policies that lack explicit physical constraints, often resulting in semantically plausible but physically unsafe behaviors. In this paper, we propose MVP-Nav, a physical-aware RGB-only navigation framework that aligns perception, planning, and control with the real 3D world. MVP-Nav reconstructs explicit physical occupancy from monocular observations by leveraging 3D foundation models to project 2D semantic instances into 3D oriented bounding boxes, forming a global spatial semantic representation. To unify high-level semantic reasoning and low-level physical constraints, we introduce a Multi-layer Value Map (MVM) that integrates semantic priorities and reconstructed geometry into a shared cost space, enabling physically grounded geometric planning. Extensive experiments on zero-shot object navigation benchmarks demonstrate that MVP-Nav significantly outperforms existing depth-free methods, achieving state-of-the-art performance and validating that structured physical priors can effectively compensate for the absence of active depth sensors.

</details>

---

### [[20_Research/Papers/大模型/Attend,_Transform,_or_Silence_Operator-Level_Visual_Skipping_for_Efficient_Multimodal_LLM_Inference|Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference]]

![[assets/2606.31903_figure.png|800]]

- **arXiv**: [2606.31903](https://arxiv.org/abs/2606.31903)
- **PDF**: https://arxiv.org/pdf/2606.31903
- **详细分析**: [[20_Research/Papers/大模型/Attend,_Transform,_or_Silence_Operator-Level_Visual_Skipping_for_Efficient_Multimodal_LLM_Inference|Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference]]
- **作者**: Zhaoyang Luo, Runmin Dong, Miao Yang, Fan Wei, Yushan Lai, Bin Luo, Haohuan Fu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GQA, SQA, TextVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) increasingly process long visual-token sequences, increasing the overall inference computation. Existing acceleration methods usually remove visual tokens or skip visual-token updates in entire layers, but these coarse strategies may discard fine-grained evidence or suppress useful operators together with redundant ones. In this paper, we study visual-token computation from an answer-observable perspective and find that late visual-token updates can remain large while having little effect on answer-token representations. Motivated by this answer-silent redundancy, we decompose each Transformer layer into attention and FFN operators and show that useful visual computation is often operator-dominant and layer-dependent. We propose an operator-level visual-token skipping framework that preserves the full visual-token sequence while selectively bypassing redundant attention, FFN, or both. Experiments across three MLLM architectures and 10 VQA benchmarks show that our method achieves strong efficiency-accuracy trade-offs, reducing \textbf{33.7\%} TFLOPs on Qwen3-VL while retaining \textbf{99.5\%} of the vanilla model performance.

</details>

---

### [[20_Research/Papers/具身智能/Z-1_Efficient_Reinforcement_Learning_for_Vision-Language-Action_Models|Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models]]

![[assets/2606.31846_figure.png|800]]

- **arXiv**: [2606.31846](https://arxiv.org/abs/2606.31846)
- **PDF**: https://arxiv.org/pdf/2606.31846
- **详细分析**: [[20_Research/Papers/具身智能/Z-1_Efficient_Reinforcement_Learning_for_Vision-Language-Action_Models|Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models]]
- **作者**: Lang Cao, Renhong Chen, Luyi Li, Peng Wang, Mofan Peng, Yitong Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 大模型
- **相关性评分**: 3.7（加权：具身智能 2.1，大模型 0.1，强化学习 1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $π_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

</details>

---

### [[20_Research/Papers/大模型/Breaking_Failure_Cascades_Step-Aware_Reinforcement_Learning_for_Medical_Multimodal_Reasoning|Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning]]

![[assets/2606.31825_figure.png|800]]

- **arXiv**: [2606.31825](https://arxiv.org/abs/2606.31825)
- **PDF**: https://arxiv.org/pdf/2606.31825
- **详细分析**: [[20_Research/Papers/大模型/Breaking_Failure_Cascades_Step-Aware_Reinforcement_Learning_for_Medical_Multimodal_Reasoning|Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning]]
- **作者**: Junha Jung, Minbyul Jeong, Suhyeon Lim, Sungwook Jung, Jaehoon Yun, Taeyun Roh, Mujeen Sung, Jaewoo Kang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PathVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent multimodal large language models have shown great promise in clinical image reasoning, but existing post-training pipelines remain predominantly outcome-centric, relying on final answer correctness or sequence-level preferences. This suffers from sparse credit assignment, making it difficult to optimize the reasoning process essential for clinical applications. Our analysis reveals that cascading errors from early-stage reasoning failures are a leading cause of incorrect predictions in medical visual question answering (VQA) benchmarks. Motivated by this, we propose Medical Reasoning-aware Policy Optimization (MRPO), an RL algorithm that incorporates step-wise process rewards. When the final answer is incorrect, MRPO assigns exponentially larger penalties to tokens in earlier invalid reasoning steps, breaking failure cascades without compromising successful paths. Across three multimodal LLM backbones, MRPO consistently outperforms standard GRPO and a recent RL baseline, and on Qwen3-VL-8B-Instruct even surpasses substantially larger medical MLLMs such as HuatuoGPT-Vision-34B by 2.79 points. Moreover, MRPO reduces early-stage reasoning failures from 64.0% to 13.0%, showing that targeted mitigation of cascading failures improves both reasoning quality and final answer accuracy. Our code is available at https://github.com/dmis-lab/MRPO

</details>

---

### [[20_Research/Papers/机器人/RCT_A_Robot-Collected_Touch-Vision-Language_Dataset_for_Tactile_Generalization|RCT: A Robot-Collected Touch-Vision-Language Dataset for Tactile Generalization]]

![[assets/2606.31694_figure.png|800]]

- **arXiv**: [2606.31694](https://arxiv.org/abs/2606.31694)
- **PDF**: https://arxiv.org/pdf/2606.31694
- **详细分析**: [[20_Research/Papers/机器人/RCT_A_Robot-Collected_Touch-Vision-Language_Dataset_for_Tactile_Generalization|RCT: A Robot-Collected Touch-Vision-Language Dataset for Tactile Generalization]]
- **作者**: Jingbo He, Michael Färber, Roberto Calandra
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《RCT: A Robot-Collected Touch-Vision-Language Dataset for Tactile Generalization》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For robots manipulating open-world objects, tactile representations must generalize to unseen materials. We introduce RCT (Robotic Contact Tactile), a robot-collected touch-vision-language dataset with 29,279 tactile frames from full robot presses on 122 industrial reference materials in 7 categories, recorded with three DIGIT sensors at multiple contact positions. RCT preserves each press as a contact sequence, enabling held-out evaluation across materials, categories, sensors, contact positions, and contact sequences. Frames from one press are strongly correlated: frame-random splits can place near-duplicate observations of the same physical interaction in both training and test. With the encoder held fixed, removing contact-sequence overlap reduces tactile-to-text Recall@1 by 17.7 percentage points. When materials are additionally held out at training time, performance drops sharply, leaving held-out-material Recall@1 at 25.1 +/- 6.1% averaged over three held-out draws. The public TVL/HCT split shows the same structure: every test contact sequence appears in training, and raw-pixel nearest neighbors recover the correct sequence in 98.3% of cases. Uniformly sampling a press improves contrastive training, and RCT-trained embeddings improve category probes on unseen materials. RCT makes contact-sequence-aware, held-out-material evaluation reproducible and exposes novel-material generalization as a central challenge for robotic tactile perception. The RCT dataset is open-sourced at https://faerber-lab.github.io/RCT/

</details>

---

### [[20_Research/Papers/大模型/ShopX_A_Foundation_Model_for_Intent-to-Item_Fulfillment_in_Agentic_Shopping|ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping]]

![[assets/2606.31693_first_page.png|800]]

- **arXiv**: [2606.31693](https://arxiv.org/abs/2606.31693)
- **PDF**: https://arxiv.org/pdf/2606.31693
- **详细分析**: [[20_Research/Papers/大模型/ShopX_A_Foundation_Model_for_Intent-to-Item_Fulfillment_in_Agentic_Shopping|ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping]]
- **作者**: Jiacheng Chen, Tao Zhang, Manxi Lin, Dunxian Huang, Teng Shi, Honghao Fu, Mengyan Li, Xinming Zhang, Chenchi Zhang, Xuan Lu, Xiaoxiong Du, Haibin Chen...
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ShopX: A Foundation Model for Intent-to-Item Fulfillment in Agentic Shopping》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The wave of AI-native applications is moving shopping beyond page- and feed-based browsing toward intent-driven experiences orchestrated by LLM agents. A common design wraps an LLM around existing search and recommendation pipelines, forcing complex intents through low-bandwidth retrieval or ranking interfaces and leaving a gap between language understanding and item-space fulfillment. Generative recommendation gives LLMs a direct item-space interface through semantic IDs (SIDs), but existing models mainly generate candidates for retrieval rather than translate flexible intents into item-space outcomes. We propose ShopX to address this bottleneck by unifying intent understanding, execution planning, and flexible SID-native item-space operations into a single foundation model. We deploy ShopX in agentic shopping workflows through a model-native item-fulfillment framework with a serving harness that defines a model-facing action protocol and exposes support surfaces for context access, catalog grounding, and state management. Within this framework, ShopX plans and composes SID-based item-space operations such as SID beam-search retrieval, listwise ranking, or product bundling. This model-centric design reduces lossy hand-offs between agent orchestration and item-space execution. To build ShopX, we design semantically recoverable, LLM-operable SIDs and a training recipe that equips a general LLM for flexible multi-turn item-space fulfillment while retaining the knowledge and instruction-following abilities needed by a shopping agent. We evaluate the ShopX framework against tool-mediated agentic systems on single- and multi-turn fulfillment tasks derived from anonymized Taobao production logs, showing that model-native fulfillment improves overall framework behavior, especially on complex or ambiguous requests.

</details>

---

### [[20_Research/Papers/世界模型/WorldRoamBench_An_Open-World_Benchmark_for_Long-Horizon_Stability_of_Interactive_World_Models|WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models]]

![[assets/2606.31672_figure.png|800]]

- **arXiv**: [2606.31672](https://arxiv.org/abs/2606.31672)
- **PDF**: https://arxiv.org/pdf/2606.31672
- **详细分析**: [[20_Research/Papers/世界模型/WorldRoamBench_An_Open-World_Benchmark_for_Long-Horizon_Stability_of_Interactive_World_Models|WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models]]
- **作者**: Ting-Bing Xu, Jiacheng Sui, Zhe Gao, Kewei Shi, Wenjin Yang, Zhicheng Liu, Zhaoxu Sun, Mingchao Sun, Hongyu Pan, Fan Jiang, Mu Xu, Qi Fan...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HY-World, LingBot-World, Open-World, WBench, WildWorld, WorldRoamBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite rapid progress in interactive world models (IWMs), existing benchmarks evaluate action following only at trajectory level and ignore memory and interaction physics. We introduce WorldRoamBench, an open-world benchmark for long-horizon stability across four dimensions, each with tailored innovations: (i) Action: per-frame action metric bypassing cross-model semantic scale disparity and exposing failures hidden by trajectory; (ii) Vision: segment-based drift metric capturing non-monotonic mid-sequence collapse missed by start-vs-end comparisons; (iii) Physics: controllability-gated evaluation over mechanics, optics, and 3D consistency, scoring plausibility under faithful action execution; (iv) Memory: action-decoupled protocol evaluating scene memory via transition-localized 3D point-cloud reconstruction and subject memory via tracking-plus-VLM reasoning. The benchmark comprises 600+ test cases across Nature, Urban, and Indoor scenes in first/third-person views with WASD 10-60s continuous interaction. Evaluating 10+ open/closed-source models reveals none reliably satisfies all dimensions; even the best achieves only moderate scores. Advances on WorldRoamBench are steps toward IWMs that are stable, physically grounded, memory-faithful, and deployable in real-world applications.

</details>

---

### [[20_Research/Papers/强化学习/Think_in_English,_Answer_in_Korean_Efficient_Adaptation_of_Multilingual_Tool-Using_Agents|Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents]]

![[assets/2606.31648_figure.png|800]]

- **arXiv**: [2606.31648](https://arxiv.org/abs/2606.31648)
- **PDF**: https://arxiv.org/pdf/2606.31648
- **详细分析**: [[20_Research/Papers/强化学习/Think_in_English,_Answer_in_Korean_Efficient_Adaptation_of_Multilingual_Tool-Using_Agents|Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents]]
- **作者**: Utsav Garg, Sungjin Hong, Jason Jung, Justin Lee, Shaan Desai, Joon Hee Kim, Anirudh Shrinivason, Edmond Wen, Susie Park
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Think in English, Answer in Korean: Efficient Adaptation of Multilingual Tool-Using Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IFEval, MT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present LuckyStar 111B, a 111B-parameter hybrid reasoning model developed through a collaboration between Cohere and LG CNS for Korean-English enterprise agents under practical memory and serving constraints. The model trains from Cohere's fully post-trained Command A model rather than a new pretraining run, and uses preamble conditioning to switch between concise non-reasoning behavior and longer tool-oriented reasoning. We study four choices for scaling tool-using agents efficiently: multilingual supervised fine-tuning, reinforcement learning with verifiable rewards for multi-step tool-use tasks, language-consistency rewards for Korean user-facing responses, and 4-bit quantization for single-GPU serving. The adapted model improves mathematical reasoning, function calling, and agentic natural-language-to-SQL (NL2SQL) performance while preserving general Korean and English instruction-following quality. These results provide a practical recipe and failure-mode analysis for adapting post-trained multilingual models to verifiable agentic workflows under memory-constrained deployment.

</details>

---

### [[20_Research/Papers/大模型/A_Lifecycle_and_Application-Stack_Survey_of_Large_Language_Model_Vulnerabilities_Attacks,_Risks,_Defenses,_and_Open_Problems|A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems]]

![[assets/2606.31639_first_page.png|800]]

- **arXiv**: [2606.31639](https://arxiv.org/abs/2606.31639)
- **PDF**: https://arxiv.org/pdf/2606.31639
- **详细分析**: [[20_Research/Papers/大模型/A_Lifecycle_and_Application-Stack_Survey_of_Large_Language_Model_Vulnerabilities_Attacks,_Risks,_Defenses,_and_Open_Problems|A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems]]
- **作者**: Seyed Bagher Hashemi Natanzi, Bo Tang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.4（加权：大模型 1.2，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《A Lifecycle and Application-Stack Survey of Large Language Model Vulnerabilities: Attacks, Risks, Defenses, and Open Problems》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are no longer only text generators. They are increasingly embedded in retrieval pipelines, enterprise assistants, coding environments, robotic systems, security-operation workflows, and autonomous agents that can read private data, call tools, write files, execute code, and act across organizational boundaries. This shift changes the security problem: risks do not arise from the model weights alone, but from the full lifecycle and application stack through which data, prompts, model outputs, tools, memories, and user authority interact. This paper systematizes the literature on vulnerabilities in large language model systems through a lifecycle and application-stack lens. We organize attacks across eight stages: data collection, pretraining, post-training alignment, model packaging and supply chain, retrieval and memory, prompting and inference, tool/agent execution, and deployment/maintenance. For each stage, we analyze attacker capabilities, affected security objectives, representative attacks, practical risks, evaluation practices, and defenses. We further map LLM-specific vulnerabilities to confidentiality, integrity, availability, safety, privacy, fairness, accountability, and agency-control objectives. Unlike taxonomies that list isolated attack names, the proposed systematization emphasizes where trust boundaries fail, how untrusted data becomes executable instruction, how delegated authority amplifies model errors, and why point defenses rarely compose. We close with a research agenda for secure LLM systems, including compositional security, provenance-aware retrieval, tool-call containment, long-horizon agent evaluation, privacy-preserving adaptation, realistic red teaming, and deployment-grade incident response.

</details>

---

### [[20_Research/Papers/大模型/A_Tutorial_on_Autonomous_Fault-Tolerant_Control_Using_Knowledge-Grounded_LLM_Agents|A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents]]

![[assets/2606.31635_figure.png|800]]

- **arXiv**: [2606.31635](https://arxiv.org/abs/2606.31635)
- **PDF**: https://arxiv.org/pdf/2606.31635
- **详细分析**: [[20_Research/Papers/大模型/A_Tutorial_on_Autonomous_Fault-Tolerant_Control_Using_Knowledge-Grounded_LLM_Agents|A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents]]
- **作者**: Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《A Tutorial on Autonomous Fault-Tolerant Control Using Knowledge-Grounded LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fault recovery in process plants still relies heavily on plant operators, especially when faults fall outside predefined supervisory logic. Operators interpret alarms, procedures, P\&amp;IDs, interlocks, and process trends, then decide how to move the plant to a safe operating mode without triggering a shutdown. This paper examines how Large Language Model (LLM) agents can support such recovery decisions. The proposed framework treats the LLM as a constrained supervisory planner. It uses plant-specific knowledge to propose recovery actions, and every proposal is checked by an external validator (symbolic or simulation-based) before actuation. The paper develops three design dimensions for applying the framework: the recovery patterns for which LLM agents are useful, the validation strategies that separate admissible from inadmissible proposals, and the deployment constraints imposed by latency, knowledge engineering, safety integration, and model lifecycle management. To make the framework directly usable, two openly available executable Python environments are provided. Both re-implement established case studies, a modular mixing module and a continuous stirred-tank reactor, extended with configurable faults and defined interfaces for custom recovery and validation methods.

</details>

---

### [[20_Research/Papers/大模型/Token-Sparse_Medical_Multimodal_Reasoning_via_Dual-Stream_Reinforcement_Learning|Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning]]

![[assets/2606.31599_figure.png|800]]

- **arXiv**: [2606.31599](https://arxiv.org/abs/2606.31599)
- **PDF**: https://arxiv.org/pdf/2606.31599
- **详细分析**: [[20_Research/Papers/大模型/Token-Sparse_Medical_Multimodal_Reasoning_via_Dual-Stream_Reinforcement_Learning|Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning]]
- **作者**: Kaitao Chen, Weiqian Zhao, Jiamin Wu, Qihao Zheng, Shangquan Sun, Chunfeng Song, Xiaosong Wang, Mu Zhou, Mianxin Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DS-RL, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) combining reinforcement learning (RL) ignite remarkable progress in multimodal reasoning, yet still struggle with medical images, which typically exhibit extremely sparse visual evidence to inform clinical decision-making. We recognize that pruning visual tokens outside the grounding region greatly enhances medical reasoning. However, a united RL framework for active visual token pruning (VTP) and medical multimodal reasoning remains unestablished. Here, we propose a dual-stream RL framework, ViToS, to fulfill token pruning and question answering. ViToS trains one policy model with two task branches, where one focuses on grounding while the other conducts token-sparse reasoning after VTP. Furthermore, we solve the coupled policy learning problem by introducing the cross-feedback sequential optimization, avoiding gradient conflict and facilitating convergence of the shared policy model. Evaluated on seven medical benchmarks, our method reduces visual tokens to 77% of the original sequence length while achieving a 108.27% relative performance on Lingshu-7B and 104.16% relative performance on HuatuoGPT-Vision-7B. Overall, ViToS delivers superior performance and inference speedup, establishing an efficient paradigm for medical multimodal reasoning.

</details>

---

### [[20_Research/Papers/大模型/ACE_Pluggable_Adaptive_Context_Elasticizer_across_Agents|ACE: Pluggable Adaptive Context Elasticizer across Agents]]

![[assets/2606.31564_figure.png|800]]

- **arXiv**: [2606.31564](https://arxiv.org/abs/2606.31564)
- **PDF**: https://arxiv.org/pdf/2606.31564
- **详细分析**: [[20_Research/Papers/大模型/ACE_Pluggable_Adaptive_Context_Elasticizer_across_Agents|ACE: Pluggable Adaptive Context Elasticizer across Agents]]
- **作者**: Ning Liao, Zihao Long, Xiaoxing Wang, Xue Yang, Yaoming Wang, Ziyuan Zhuang, Xunliang Cai, Rongxiang Weng, Junchi Yan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ACE: Pluggable Adaptive Context Elasticizer across Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The increasing complexity of agentic tasks has led to rapidly growing trajectory lengths, which poses significant challenges for large language model (LLM) based agents with fixed context windows. Existing context management techniques, such as truncation and summarization, suffer from inherent inflexibility and irreversibility: once information is discarded or compressed, it cannot be recovered even when it becomes critically relevant in later decision steps. To address these limitations, we propose the Adaptive Context Elasticizer (ACE), a plug-and-play module that elastically orchestrates historical step information into the agent's context at each decision step. ACE maintains a lossless message maintenance layer that stores both raw messages and compressed abstractions for each historical step, while a context orchestration layer adaptively assigns each step an elastic type as raw, abstract, or drop, at every decision step based on the current task state. This reversible design ensures that the main LLM always receives a compact yet information-rich context. We adapt ACE to four diverse agent frameworks, including ReAct, DeepAgent, WebThinker, and MiroFlow, without training or architectural modifications. Experiments show that ACE consistently outperforms truncation and summarization baselines, and brings consistent performance gains across all four agent frameworks.

</details>

---

### [[20_Research/Papers/具身智能/Robustness_of_Robotic_Manipulation_Foundations_and_Frontiers|Robustness of Robotic Manipulation: Foundations and Frontiers]]

![[assets/2606.31494_figure.png|800]]

- **arXiv**: [2606.31494](https://arxiv.org/abs/2606.31494)
- **PDF**: https://arxiv.org/pdf/2606.31494
- **详细分析**: [[20_Research/Papers/具身智能/Robustness_of_Robotic_Manipulation_Foundations_and_Frontiers|Robustness of Robotic Manipulation: Foundations and Frontiers]]
- **作者**: Yifei Dong, Zhanyi Sun, Lujie Yang, Manuel Baum, Kei Ikemura, Shuran Song, Florian T. Pokorny, Xianyi Cheng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Robustness of Robotic Manipulation: Foundations and Frontiers》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans and animals exhibit remarkable robustness in physical manipulation, yet robots remain far behind. Progress toward human-level manipulation robustness is hindered by the absence of a unified and systematic understanding: different subfields frame robustness in distinct ways, often leaving the concept ambiguous and limiting deeper analysis as well as communication across research areas. This paper presents a systematic study of manipulation robustness. We begin with a formal definition, characterizing robustness as the degree to which a manipulation system can achieve its goal in the presence of uncertainty and variation. Building on this definition, we introduce general formulations of manipulation robustness from probabilistic and control-theoretic perspectives. We then synthesize the guiding principles and concrete mechanisms of manipulation robustness across perception, planning, control, policy learning, and hardware, illustrating each mechanism through representative works, including foundational and recent studies. In addition, we revisit existing metrics and evaluation methods for quantifying manipulation robustness. Finally, we distill broader lessons for designing robust manipulation systems and discuss open problems and future directions toward achieving human-level robustness in robotic manipulation.

</details>

---

### [[20_Research/Papers/大模型/ReGRPO_Reflection-Augmented_Policy_Optimization_for_Tool-Using_Agents|ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents]]

![[assets/2606.31392_figure.png|800]]

- **arXiv**: [2606.31392](https://arxiv.org/abs/2606.31392)
- **PDF**: https://arxiv.org/pdf/2606.31392
- **详细分析**: [[20_Research/Papers/大模型/ReGRPO_Reflection-Augmented_Policy_Optimization_for_Tool-Using_Agents|ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents]]
- **作者**: Binjie Zhang, Mike Zheng Shou
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《ReGRPO: Reflection-Augmented Policy Optimization for Tool-Using Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-augmented vision-language models (VLMs) can solve multimodal, multi-step tasks by calling external tools, yet they remain fragile in practice. Existing works have two common gaps. Supervised fine-tuning (SFT) is built mostly on successful trajectories and offers little signal for recovery after tool failures, while sparse trajectory-level RL rewards provide limited guidance on which step failed and how to repair it. We introduce ReGRPO (Reflection-augmented Group Relative Policy Optimization), a framework that learns reflection-guided correction in tool-using agents. ReGRPO starts with a structured reflective data engine: we execute near-miss actions to collect grounded failure observations, then build Reflection-of-Thought triplets (ErrorType, Evidence, FixPlan) paired with corrected actions for warm-start SFT. We then optimize reflection tokens and corrective actions jointly within local trajectories using group-relative advantages, and include a reflection-cost term to reduce unnecessary reflection. Experiments on GTA and GAIA show that, under the same backbone and tool suite, ReGRPO consistently outperforms strong open-source baselines and achieves the best results among the compared open-source controllers. Code and RoT data are available at https://github.com/showlab/ReGRPO.

</details>

---

### [[20_Research/Papers/具身智能/Stage-Transition_Dense_Reward_Modeling_for_Reinforcement_Learning|Stage-Transition Dense Reward Modeling for Reinforcement Learning]]

![[assets/2606.31377_figure.jpg|800]]

- **arXiv**: [2606.31377](https://arxiv.org/abs/2606.31377)
- **PDF**: https://arxiv.org/pdf/2606.31377
- **详细分析**: [[20_Research/Papers/具身智能/Stage-Transition_Dense_Reward_Modeling_for_Reinforcement_Learning|Stage-Transition Dense Reward Modeling for Reinforcement Learning]]
- **作者**: Yang Yang, Bingjie Chen, Zihan Wang, Yizhe Li, Guoping Pan, Yi Cheng, Houde Liu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.9，大模型 0.1，强化学习 0.8，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Stage-Transition Dense Reward Modeling for Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：IRL, MetaWorld, Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.

</details>

---

### [[20_Research/Papers/大模型/Calibrating_the_Evaluator_Does_Probability_Calibration_Mitigate_Preference_Coupling_in_LLM_Agent_Feedback_Loops|Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?]]

![[assets/2606.31371_first_page.png|800]]

- **arXiv**: [2606.31371](https://arxiv.org/abs/2606.31371)
- **PDF**: https://arxiv.org/pdf/2606.31371
- **详细分析**: [[20_Research/Papers/大模型/Calibrating_the_Evaluator_Does_Probability_Calibration_Mitigate_Preference_Coupling_in_LLM_Agent_Feedback_Loops|Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?]]
- **作者**: Zewen Liu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When large language model (LLM) agents adapt their behavior through evaluator feedback, systematic evaluator biases propagate into the agent's learned strategy distribution - a phenomenon termed evaluator preference coupling. Prior work has documented this coupling and established a diagnostic framework (EPC) to measure it, but has not investigated whether calibration techniques can mitigate the effect. We present the first study of evaluator calibration as mitigation: applying probability calibration to the evaluator's pairwise judgments to reduce spurious preference propagation. In a controlled within-subjects experiment (N=5) comparing standard binary TTRL (win/loss) with confidence-calibrated TTRL (probability-weighted updates) using DeepSeek-V4-Pro as executor and GLM5.2 as evaluator, we find that calibration reduces the coupling coefficient gamma by 20-49% and Jensen-Shannon divergence by 45-67%. A symmetric-LR control confirms the effect is not due to reduced update asymmetry. We release the calibrated TTRL protocol and recommend it as a lightweight mitigation for LLM-as-judge deployment pipelines.

</details>

---

### [[20_Research/Papers/强化学习/Smart_charging_of_large_fleets_of_Electric_Vehicles_Independent_Multi-Agent_Reinforcement_Learning_approaches|Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches]]

![[assets/2606.31347_figure.png|800]]

- **arXiv**: [2606.31347](https://arxiv.org/abs/2606.31347)
- **PDF**: https://arxiv.org/pdf/2606.31347
- **详细分析**: [[20_Research/Papers/强化学习/Smart_charging_of_large_fleets_of_Electric_Vehicles_Independent_Multi-Agent_Reinforcement_Learning_approaches|Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches]]
- **作者**: Xavier Rate, Eloann Le Guern, Raphaël Féraud, Fatma Salem, Melissa Chiknoun, Eymeric Giabicani, Mehdi Feki, Patrick Maillé, Guy Camilleri, Anne Blavette, Hamid Benhamed
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Smart charging of large fleets of Electric Vehicles: Independent Multi-Agent Reinforcement Learning approaches》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The electrification of transportation through electric vehicles introduces new challenges for power grid management, such as increased peak demand, voltage fluctuations, line overloads, and the integration of variable renewable energy sources. To enable efficient integration of EVs while minimizing costs for users and avoiding network overloads, implicit coordination between EVs is required. This work compares two independent multi-agent reinforcement learning approaches for optimizing such decentralized EV charging: contextual combinatorial bandits and policy gradient algorithms. Using a realistic simulation environment with autonomous agents making decisions based on local environmental information (including price signals, state-of-charge, and temporal constraints), we evaluate their performance across varying congestion levels, and mixed-strategy configurations with heterogeneous agent groups under dynamic electricity pricing derived from real photovoltaic production data.

</details>

---

### [[20_Research/Papers/具身智能/3D_HAMSTER_Bridging_Planning_and_Control_in_Hierarchical_Vision_Language_Action_Models_through_3D_Trajectory_Guidance|3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance]]

![[assets/2606.31329_figure.png|800]]

- **arXiv**: [2606.31329](https://arxiv.org/abs/2606.31329)
- **PDF**: https://arxiv.org/pdf/2606.31329
- **详细分析**: [[20_Research/Papers/具身智能/3D_HAMSTER_Bridging_Planning_and_Control_in_Hierarchical_Vision_Language_Action_Models_through_3D_Trajectory_Guidance|3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance]]
- **作者**: Dongyoon Hwang, Byungkun Lee, Dongjin Kim, Hyojin Jang, Hoiyeong Jin, Jueun Mun, Minho Park, Hojoon Lee, Hyunseung Kim, Jaegul Choo
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DroidSpatial-Bench, Real-World, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

</details>

---

### [[20_Research/Papers/大模型/Learning_from_Failure_Inference-Time_Self-Improvement_for_Computer-Use_Agents|Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents]]

![[assets/2606.31270_figure.png|800]]

- **arXiv**: [2606.31270](https://arxiv.org/abs/2606.31270)
- **PDF**: https://arxiv.org/pdf/2606.31270
- **详细分析**: [[20_Research/Papers/大模型/Learning_from_Failure_Inference-Time_Self-Improvement_for_Computer-Use_Agents|Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents]]
- **作者**: Xueqiao Sun, Xiaohan Wang, Ludwig Schmidt, Serena Yeung-Levy, Yuhui Zhang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.CY, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-use agents, which leverage multimodal large language models (MLLMs) to operate computers and complete tasks, have attracted significant attention for their utility and versatility. A major challenge in developing these agents is collecting large-scale, high-quality trajectories. The standard approach generates synthetic data through a self-improving loop: an agent is placed in a verifiable environment and iteratively fine-tuned on its successful trajectories. Despite its effectiveness, this paradigm exploits only successful trajectories and discards the failed ones, even though failures carry rich information about a model's weaknesses. In this work, we explore a complementary failure-driven self-improvement loop, a data-centric paradigm that turns failed trajectories into agent improvements. Specifically, we employ an LLM to diagnose failure modes, propose inference-time solutions, and generate code patches -- lightly verified by humans -- that upgrade the agent. We validate this approach with the state-of-the-art OpenCUA-72B model on the OSWorld benchmark, improving the success rate from 42.3% to 48.9%, a gain of 6.6 percentage points, without any additional training cost and with only modest inference overhead. Our results demonstrate that failure-driven self-improvement is a viable complement to success-based pipelines, enabling more efficient agent improvement.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_CAD_Solver-Grounded_LLM_Agents_for_Parametric_B-Rep_Assembly_Modeling|Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling]]

![[assets/2606.31252_figure.png|800]]

- **arXiv**: [2606.31252](https://arxiv.org/abs/2606.31252)
- **PDF**: https://arxiv.org/pdf/2606.31252
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_CAD_Solver-Grounded_LLM_Agents_for_Parametric_B-Rep_Assembly_Modeling|Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling]]
- **作者**: Fumin Liu, Haoyu Zhou, Fei Hao, Lin Yang
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.9）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BRepNet, CSGNet, UV-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can write plausible CAD scripts, but reliable industrial CAD modeling requires more than syntactically valid code: every feature, placement, and assembly relation must be accepted by an exact geometric kernel while remaining editable as parametric boundary representation geometry. We present Embodied CAD, solver-grounded LLM agents for parametric B-Rep assembly modeling. Instead of generating a complete script in one pass, the agent iteratively selects actions from a stratified L0-L4 CAD skill library, resolves them into typed geometric operations, executes them in a CAD backend, and uses solver feedback to plan, repair, and learn. The framework combines action grammar constraints, deterministic parameter resolution, and solver-derived rewards for supervised warm-up and GRPO-style refinement. We evaluate Embodied CAD on multi-step mechanical, industrial equipment, and mold-oriented assembly tasks using solver-aligned metrics: executable rate, skill accuracy, operation-family accuracy, exact policy accuracy, and task completion success. The results show that solver-grounded planning executes all strong-planner workflows in the current benchmark, while learned controllers reach high executable rates and expose the remaining gap between valid tool calls and exact long-horizon policy prediction.

</details>

---

### [[20_Research/Papers/世界模型/Delta-JEPA_Learning_Action-Sensitive_World_Models_via_Latent_Difference_Decoding|Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding]]

![[assets/2606.31232_figure.png|800]]

- **arXiv**: [2606.31232](https://arxiv.org/abs/2606.31232)
- **PDF**: https://arxiv.org/pdf/2606.31232
- **详细分析**: [[20_Research/Papers/世界模型/Delta-JEPA_Learning_Action-Sensitive_World_Models_via_Latent_Difference_Decoding|Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding]]
- **作者**: Zhenghao Zhang, Yuanxiang Wang, Zhenyu Guan, Yujia Yang, Bingkang Shi, Tianyu Zong, Hongzhu Yi, Guoqing Chao, Xingchen Chen, Tiankun Yang, Chenxi Bao, Tao Yu...
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.2（加权：世界模型 1.2）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Delta-JEPA: Learning Action-Sensitive World Models via Latent Difference Decoding》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning visual world models for planning requires compact latent dynamics that remain sensitive to actions, yet reconstruction-free joint-embedding objectives can collapse to action-insensitive representations. We propose Delta-JEPA, an end-to-end reconstruction-free world model that augments latent forward prediction with a Latent Difference Action Decoder (LDAD). Unlike inverse decoders that infer actions from concatenated endpoint embeddings, LDAD reconstructs the executed action from the latent displacement between consecutive observations. This displacement-level supervision directly regularizes transition geometry: adjacent embeddings cannot collapse without losing action information, and different actions are encouraged to induce distinguishable latent changes for rollout-based planning. Delta-JEPA uses only latent prediction and action reconstruction, avoiding pixel reconstruction and distribution-matching regularizers. Across four visual continuous-control tasks, Delta-JEPA improves planning over JEPA-based and representation-learning world model baselines. Ablations show that displacement-based action decoding is consistently more effective than endpoint concatenation, and action-sensitivity analyses show clearer action-conditioned latent responses. These results indicate that supervising latent differences is a simple and effective mechanism for collapse-resistant and action-sensitive world model learning.

</details>

---

### [[20_Research/Papers/具身智能/Agentic_RAG-VLM_Affordance-Aware_Retrieval-Augmented_Generation_with_Self-Reflective_Planning_for_Robotic_Grasping|Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping]]

![[assets/2606.31200_figure.png|800]]

- **arXiv**: [2606.31200](https://arxiv.org/abs/2606.31200)
- **PDF**: https://arxiv.org/pdf/2606.31200
- **详细分析**: [[20_Research/Papers/具身智能/Agentic_RAG-VLM_Affordance-Aware_Retrieval-Augmented_Generation_with_Self-Reflective_Planning_for_Robotic_Grasping|Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping]]
- **作者**: Tao Chen, Lizheng Liu, Jiaxu Wang, Ziyue Jiang, Ruiqi Tian, JiGuang Huo, Zhongxue Gan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 1.2，大模型 1.2，机器人 0.8）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Agentic RAG-VLM: Affordance-Aware Retrieval-Augmented Generation with Self-Reflective Planning for Robotic Grasping》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalizable robotic grasping in cluttered environments is essential for deploying manipulators in unstructured human spaces, yet existing VLM-based methods rely on visual similarity for object matching, neglecting physical affordances such as handle graspability and material fragility, and operate open-loop without spatial reasoning or failure recovery, limiting their effectiveness when objects are densely packed or physically diverse. We present Agentic RAG-VLM, a unified framework that bridges VLM-based semantic understanding and physically grounded grasp execution by integrating retrieval-augmented generation (RAG) with vision-language models (VLMs) and agentic self-reflective planning. Agentic RAG-VLM introduces three tightly coupled components: (1) a Hierarchical Affordance-Aware RAG (HAA-RAG) that encodes four-dimensional affordance descriptors, including type, material, fragility, and graspable region, and retrieves strategies by functional affordance compatibility rather than visual appearance; (2) a Scene Graph Constraint Reasoner that constructs spatial relationship graphs from VLM perception and translates proximity, occlusion, and support constraints into concrete grasp parameter adjustments; and (3) an Agentic Self-Reflective Pipeline with a 14-type failure taxonomy and three-level adaptive retry for closed-loop grasp refinement. Evaluated on a 12-task benchmark spanning single-grasp, interactive, and long-horizon scenarios with 360 trials per configuration, Agentic RAG-VLM achieves 78.3 percent overall success, a 53.3 percentage-point absolute gain over VLM-only baselines, demonstrating that affordance-aware retrieval, scene graph reasoning, and agentic recovery are jointly essential for robust manipulation.

</details>

---

### [[20_Research/Papers/大模型/HealthAgentBench_A_Unified_Benchmark_Suite_of_Realistic_Agentic_Healthcare_Environments_for_Challenging_Frontier_AI_Agents|HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents]]

![[assets/2606.31179_figure.png|800]]

- **arXiv**: [2606.31179](https://arxiv.org/abs/2606.31179)
- **PDF**: https://arxiv.org/pdf/2606.31179
- **详细分析**: [[20_Research/Papers/大模型/HealthAgentBench_A_Unified_Benchmark_Suite_of_Realistic_Agentic_Healthcare_Environments_for_Challenging_Frontier_AI_Agents|HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents]]
- **作者**: Qianchu Liu, Sheng Zhang, Guanghui Qin, Jeya Maria Jose Valanarasu, Maximilian Rokuss, Mingyu Lu, Timothy Ossowski, Juan Manuel Zambrano Chaves, Cliff Wong, Peniel Argaw, Yashna Hasija, Mu Wei...
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Agent

#### 研究背景与动机

《HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HealthAgentBench, HealthBench, MedAgentSim, MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As AI agents become increasingly capable of complex, long-horizon reasoning, rigorous and holistic evaluation is essential for measuring progress toward real-world healthcare applications. We introduce HealthAgentBench, a suite of 54 agentic healthcare tasks across 7 categories each with its unique environment. The benchmark suite spans diverse workflows throughout the patient journey and a broad range of modalities. Each task is designed to replicate an end-to-end clinical workflow: given minimal instructions, an agent must explore raw healthcare data, operate within a complex environment, and execute multi-step solutions that go beyond naive prompting. A final task success rate is reported to provide a single, interpretable metric for HealthAgentBench overall performance for each agent. Evaluating frontier agents on HealthAgentBench, we find that overall task success rate remains low, underscoring the difficulty of the suite. The strongest and the most cost effective agent, Codex GPT-5.5, achieves only approximately 42% success rate. Beyond aggregate performance, HealthAgentBench reveals nuanced strengths and weaknesses across task categories. Frontier agents show promise in automatically developing research modeling pipelines over EHR data, but medical imaging remains especially challenging, particularly for Claude Code models, while Codex GPT-5.5 shows emerging capability. Tasks that combine large search spaces with compositional reasoning requirements remain difficult for all current agents. Together, these results suggest that HealthAgentBench provides a challenging and realistic benchmark with substantial room for future progress. We release our benchmark at https://github.com/microsoft/HealthAgentBench.

</details>

---

### [[20_Research/Papers/具身智能/MIRTH_Mutual-Information_Reasoning_with_Temporal_Hubs_for_Vision-Language-Action_Agents|MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents]]

![[assets/2606.31167_figure.png|800]]

- **arXiv**: [2606.31167](https://arxiv.org/abs/2606.31167)
- **PDF**: https://arxiv.org/pdf/2606.31167
- **详细分析**: [[20_Research/Papers/具身智能/MIRTH_Mutual-Information_Reasoning_with_Temporal_Hubs_for_Vision-Language-Action_Agents|MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents]]
- **作者**: Hao Sun, Yu Song, Shiyu Teng, Ziwei Niu, Yen-Wei Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.5，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1) dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings; (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.

</details>

---

### [[20_Research/Papers/大模型/LLM-Powered_Interactive_Robotic_Action_Synthesis_from_Multimodal_Speech,_Gestures,_and_Music|LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music]]

![[assets/2606.31158_figure.png|800]]

- **arXiv**: [2606.31158](https://arxiv.org/abs/2606.31158)
- **PDF**: https://arxiv.org/pdf/2606.31158
- **详细分析**: [[20_Research/Papers/大模型/LLM-Powered_Interactive_Robotic_Action_Synthesis_from_Multimodal_Speech,_Gestures,_and_Music|LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music]]
- **作者**: Snehasis Banerjee, Ranjan Dasgupta
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 3.3（加权：具身智能 0.6，大模型 0.8，机器人 1.9）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The quest for intuitive and natural human-robot interaction (HRI) remains a significant challenge in robotics. Traditional methods often rely on rigid, pre-programmed commands that limit the robot's expressiveness and adaptability. This paper introduces a novel framework that leverages the reasoning capabilities of Large Language Models (LLMs) to synthesize complex robotic actions from a rich tapestry of multimodal human inputs: natural speech, hand gestures, and music/sound beats. Our system architecture integrates a speech transcription model, a gesture recognition module, and a signal processing pipeline for beat detection. These processed inputs are contextualized using prompt templates and fed into a LLM. The LLM, informed by a predefined robot action space, reasons over the combined inputs to generate a coherent sequence of actions. This sequence is dispatched to an action queue for execution on a quadruped robot over ROS. The framework has ability to interpret and fuse semantic commands from speech, deictic information from gestures, and rhythmic cues from music. This work represents a step towards creating robots that can interact with humans in a more fluid, creative, and context-aware manner.

</details>

---

### [[20_Research/Papers/具身智能/A_Modular_Vision-Language-Action_Robotics_Framework_for_Indoor_Environments|A Modular Vision-Language-Action Robotics Framework for Indoor Environments]]

![[assets/2606.31144_figure.png|800]]

- **arXiv**: [2606.31144](https://arxiv.org/abs/2606.31144)
- **PDF**: https://arxiv.org/pdf/2606.31144
- **详细分析**: [[20_Research/Papers/具身智能/A_Modular_Vision-Language-Action_Robotics_Framework_for_Indoor_Environments|A Modular Vision-Language-Action Robotics Framework for Indoor Environments]]
- **作者**: Anindya Jana, Snehasis Banerjee, Arup Sadhu, Ranjan Dasgupta
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 1.8，大模型 0.4，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《A Modular Vision-Language-Action Robotics Framework for Indoor Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CMU-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an integrated system for the CMU Vision-Language-Action (VLA) Challenge, designed to enable an autonomous agent to perform complex tasks based on natural language instructions. Our framework employs a modular architecture that orchestrates environment mapping, question processing, and navigation. The system operates in two parallel streams: a perception pipeline that constructs a semantic voxel map from real-time camera feeds using OwlViT embeddings, and a language pipeline that classifies user commands with a Vision-Language Model. The mapping is time-constrained; the system proceeds with a partial map if a 500-second exploration limit is reached. The classified query is then grounded in the geometric and semantic context of the map to generate a detailed prompt for the VLM. This yields an actionable output, demonstrating a capable solution for bridging the gap between human language and robotic action.

</details>

---

### [[20_Research/Papers/大模型/MultiUAV-Plat_An_LLM-Oriented_Platform,_Benchmark_and_Framework_for_Multi-UAV_Collaborative_Task_Planning|MultiUAV-Plat: An LLM-Oriented Platform, Benchmark and Framework for Multi-UAV Collaborative Task Planning]]

![[assets/2606.31073_figure.png|800]]

- **arXiv**: [2606.31073](https://arxiv.org/abs/2606.31073)
- **PDF**: https://arxiv.org/pdf/2606.31073
- **详细分析**: [[20_Research/Papers/大模型/MultiUAV-Plat_An_LLM-Oriented_Platform,_Benchmark_and_Framework_for_Multi-UAV_Collaborative_Task_Planning|MultiUAV-Plat: An LLM-Oriented Platform, Benchmark and Framework for Multi-UAV Collaborative Task Planning]]
- **作者**: Sheng Zhang, Qinglin Li, Yuechao Zang, Xueqin Huang, Yijia Fu, Cheng Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，大模型 0.6，机器人 1.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《MultiUAV-Plat: An LLM-Oriented Platform, Benchmark and Framework for Multi-UAV Collaborative Task Planning》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, AgentBench, AirCopBench, AirSim, CoppeliaSim, EmbodiedBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) provide a promising interface for high-level robotic task planning, but their use in multi-UAV collaboration remains difficult to evaluate systematically. Existing UAV simulators mainly emphasize dynamics, perception, or low-level control, while existing LLM-agent benchmarks rarely capture aerial-robotics constraints such as partial observability, spatial coverage, UAV assignment, and multi-vehicle coordination. To bridge this gap, we present MultiUAV-Plat, a lightweight, easy-to-use, LLM-agent-oriented simulation platform for multi-UAV collaborative task planning. The platform exposes concise RESTful APIs, agent-facing observations, role-based information access, hidden validation logic, and optional 2D/3D visualization, allowing agents to solve missions through realistic tool interaction rather than privileged simulator access. Built on this platform, the MultiUAV-Plat Benchmark contains 75 mission sessions, 1500 natural-language tasks, and 9396 validation checks across target assignment, area search, and area assignment and patrol scenarios. We further propose Agent4Drone, a task-specific LLM agent framework that structures multi-UAV behavior into memory, observation, task understanding, planning, execution, and verification. In a full paired benchmark comparison, Agent4Drone achieves a 57.9% task pass rate, a 74.6% average task check pass rate, and a 72.0% global check pass rate, substantially outperforming a ReAct baseline at 30.6%, 47.9%, and 43.1%, respectively. Agent4Drone also reduces the total failed task rate from 32.4% to 12.9%. These results demonstrate that MultiUAV-Plat and MultiUAV-Plat Benchmark provide a reproducible foundation for studying LLM-driven multi-UAV autonomy under realistic information and execution constraints.

</details>

---

### [[20_Research/Papers/大模型/OpenLife_Toward_Open-World_Artificial_Life_with_Autonomous_LLM_Agents|OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents]]

![[assets/2606.31046_figure.png|800]]

- **arXiv**: [2606.31046](https://arxiv.org/abs/2606.31046)
- **PDF**: https://arxiv.org/pdf/2606.31046
- **详细分析**: [[20_Research/Papers/大模型/OpenLife_Toward_Open-World_Artificial_Life_with_Autonomous_LLM_Agents|OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents]]
- **作者**: Atsushi Masumori, Itsuki Doi, Norihiro Maruyama, Ryosuke Takata, Takashi Ikegami
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《OpenLife: Toward Open-World Artificial Life with Autonomous LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial life has explored life-like behavior on many computational substrates, but mostly in researcher-designed closed worlds. We argue that large language model (LLM) agents, with persistent memory, tool use, network access, and payment, now make it possible to move artificial life into the open social, technical, and economic world, a paradigm we call open-world Artificial Life (open-world ALIFE). Our proof-of-concept, OpenLife, surrounds a stateless LLM not with a single "smart agent" but with a society of asynchronous processes: memory, perception, evaluation, and a budget-based metabolism that makes persistence normative. With no fixed objective available, experience is appraised by open-vocabulary LLM judgment rather than scalar reward, and memory is rewired by meaning rather than frequency. Running six such agents in the open world for about twelve weeks and counting, we report the life-like dynamics that emerge: a shift from reactive to spontaneous activity, individuation into distinct agents, emergent social structure, and a first self-earned external income. We do not claim OpenLife has realized artificial life, but that open-world ALIFE is now a viable experimental paradigm and a concrete platform for studying what might cautiously be called living AI.

</details>

---

### [[20_Research/Papers/具身智能/LabGuard_Grounding_Natural-Language_Laboratory_Rules_into_Runtime_Guards_for_Embodied_Laboratory_Agents|LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents]]

![[assets/2606.31045_figure.png|800]]

- **arXiv**: [2606.31045](https://arxiv.org/abs/2606.31045)
- **PDF**: https://arxiv.org/pdf/2606.31045
- **详细分析**: [[20_Research/Papers/具身智能/LabGuard_Grounding_Natural-Language_Laboratory_Rules_into_Runtime_Guards_for_Embodied_Laboratory_Agents|LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents]]
- **作者**: Jingpu Yang, Fengxian Ji, Zhengzhao Lai, Zhexuan Cui, Guangxian Ouyang, Qian Jiang, Fan Zhang, Min Peng, Qianqian Xie, Preslav Nakov, Zhuohan Xie
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 1.2，大模型 0.4）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《LabGuard: Grounding Natural-Language Laboratory Rules into Runtime Guards for Embodied Laboratory Agents》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LabGuard-Bench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific embodied agents are increasingly capable of carrying out laboratory procedures, but executing these procedures safely in dynamic laboratory environments remains challenging. Current safety approaches often overlook the intermediate step of transforming laboratory natural language, including safety rules, manuals, protocols, and standard operating procedures, into machine-checkable runtime constraints. We introduce LabGuard (Laboratory Guard), a language-to-execution safety suite that grounds natural-language laboratory rules into executable specifications and deploys them as runtime guards. LabGuard includes three core components: LabGuard-IR, which defines a typed executable representation; LabGuard-Bench, which provides 812 supervised annotations expanded from 203 seed laboratory rules; and LabGuard-Grounder, which maps natural-language laboratory rules into LabGuard-IR. The resulting IR instances are handled by the LabGuard Pipeline, which compiles them into runtime monitors and applies them at the controller boundary. Experiments show that LabGuard generalizes to unseen laboratory-rule sources, achieves 79.4 task-scope F1, and reduces unsafe events from 39.5% to 23.8% after monitor compilation. In LabUtopia, its runtime monitors integrate with ACT, keeping interventions below 0.5% while preserving task success.

</details>

---

### [[20_Research/Papers/大模型/A_Three-Phase_Foundation_Model_for_Tax-Aware_Personalized_Portfolio_Management|A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management]]

![[assets/2606.30997_figure.png|800]]

- **arXiv**: [2606.30997](https://arxiv.org/abs/2606.30997)
- **PDF**: https://arxiv.org/pdf/2606.30997
- **详细分析**: [[20_Research/Papers/大模型/A_Three-Phase_Foundation_Model_for_Tax-Aware_Personalized_Portfolio_Management|A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management]]
- **作者**: Ramin Pishehvar
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.4，强化学习 0.4）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a three-phase deep reinforcement learning system for personalized portfolio management that addresses three limitations shared by all prior financial RL work: 1) ticker lock-in, 2) monolithic objectives , and 3) static user models. Phase 1 pretrains a ticker-identity-free cross asset encoder via self-supervised learning on a multi-asset corpus, augmented by a frozen parallel branch using Chronos, a T5-based time series foundation model, fused via a learned gating mechanism. To our knowledge, this is the first application of a time series foundation model to portfolio management RL. The encoder generalizes to any publicly traded asset via a 50-dimensional observable metadata vector that requires no retraining for new tickers. Phase 2 fine-tunes a MoE (Mixture of Experts) portfolio actor critic with PPO under an objective-conditioned reward that simultaneously serves six distinct investment goals sampled per episode: short-term alpha, short-term gain, long-term gain, capital preservation, tax-loss harvesting, and long-term-gains-only. A MoE architecture assigns each objective to a specialized expert head (momentum, growth, defensive, tax-aware), and a learned intent router blends experts based on the active objective and current market regime, which eliminates cross-objective gradient conflict. Phase 3 adds a lightweight personalization layer further adapted at inference time to each individual via a 76-parameter LoRA module fine-tuned on real brokerage transaction history, inferring investment objectives from revealed trading behavior rather than questionnaires. A natural language intent parser converts free-form goals directly into structured investment objective parameters.

</details>

---

### [[20_Research/Papers/强化学习/HyPOLE_Hyperproperty-Guided_Multi-Agent_Reinforcement_Learning_under_Partial_Observation|HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation]]

![[assets/2606.30966_first_page.png|800]]

- **arXiv**: [2606.30966](https://arxiv.org/abs/2606.30966)
- **PDF**: https://arxiv.org/pdf/2606.30966
- **详细分析**: [[20_Research/Papers/强化学习/HyPOLE_Hyperproperty-Guided_Multi-Agent_Reinforcement_Learning_under_Partial_Observation|HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation]]
- **作者**: Arshia Rafieioskouei, Tzu-Han Hsu, Matthew Lucas, Borzoo Bonakdarpour
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《HyPOLE: Hyperproperty-Guided Multi-Agent Reinforcement Learning under Partial Observation》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Formal specification is a powerful tool to guide the learning process and provides significant advantages over reward shaping: (1) mathematical rigor; (2) expressiveness to specify objectives and constraints, and (3) the ability to define tactics to achieve objectives. However, these benefits remain largely unexplored in the context of Multi-Agent Reinforcement Learning (MARL). This paper introduces HyPOLE, a novel framework for MARL under partial observability, where learning is guided by the expressive power of the so-called hyperproperties and, in particular, the temporal logic HyperLTL. We integrate Centralized Training for Decentralized Execution (CTDE) techniques with HyPOLE to synthesize decentralized policies, and our evaluation on SMAC, MessySMAC, and WildFire benchmark demonstrates clear advantages over baselines.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Where_to_Look_A_Reinforcement_Learning_Framework_for_Robust_Micro-Ultrasound_Prostate_Cancer_Detection|Learning Where to Look: A Reinforcement Learning Framework for Robust Micro-Ultrasound Prostate Cancer Detection]]

![[assets/2606.30951_figure.png|800]]

- **arXiv**: [2606.30951](https://arxiv.org/abs/2606.30951)
- **PDF**: https://arxiv.org/pdf/2606.30951
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Where_to_Look_A_Reinforcement_Learning_Framework_for_Robust_Micro-Ultrasound_Prostate_Cancer_Detection|Learning Where to Look: A Reinforcement Learning Framework for Robust Micro-Ultrasound Prostate Cancer Detection]]
- **作者**: Mohammad Mahdi Abootorabi, Sina Namazi, Armin Saadat, Lyuyang Wang, Obed Dzikunu, Paul F. R. Wilson, Zhuoxin Guo, Brian Wodlinger, Parvin Mousavi, Purang Abolmaesumi
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Learning Where to Look: A Reinforcement Learning Framework for Robust Micro-Ultrasound Prostate Cancer Detection》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：MicroSegNet, Prost-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Micro-ultrasound ($μ$US) is a new, emerging, and promising imaging modality for prostate cancer (PCa) detection, but accurate identification of suspicious tissue remains highly dependent on clinical experience, leading to substantial inter-observer variability. Machine-learning assistance can reduce this variability; however, training reliable deep models is challenging because supervision is sparse and noisy -- typically limited to core-level histopathology outcomes (e.g., cancer grade and its percentage in a biopsy core) without pixel-level lesion annotations and under severe class imbalance. We introduce Prost-RL, which reframes $μ$US PCa detection as a spatially aware, policy-driven inference problem by learning where to look before decoding. Prost-RL integrates a lightweight reinforcement-learning policy into a foundation-model encoder-decoder to generate interpretable spatial attention maps that act as soft prompts for both cancer-likelihood heatmap prediction and image-level classification. We further propose Adaptive Policy Optimization (APO) to stabilize hybrid supervised-RL training and a noise-robust objective combining symmetric cross-entropy with negative-entropy regularization to mitigate weak-label noise and encourage sharp localization. On a cohort of 6,607 biopsy cores from 693 patients across five clinical sites, Prost-RL achieves $79.0\pm3.5$ AUROC with $64.6\pm6.3$% sensitivity at 80% specificity for core-level detection (+2.1 AUROC and +4.5 sensitivity points over the strongest baseline), and $79.3\pm5.8$ AUROC for clinically significant cancer classification. The learned policy highlights biopsy-aligned regions, providing transparent, spatially grounded evidence alongside quantitative risk predictions. Code is available at: https://github.com/DeepRCL/Prost-RL.

</details>

---

### [[20_Research/Papers/具身智能/Motion_Planning_in_Compressed_Representation_Spaces|Motion Planning in Compressed Representation Spaces]]

![[assets/2606.30940_figure.png|800]]

- **arXiv**: [2606.30940](https://arxiv.org/abs/2606.30940)
- **PDF**: https://arxiv.org/pdf/2606.30940
- **详细分析**: [[20_Research/Papers/具身智能/Motion_Planning_in_Compressed_Representation_Spaces|Motion Planning in Compressed Representation Spaces]]
- **作者**: Lukas Lao Beyer, Sertac Karaman
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Motion Planning in Compressed Representation Spaces》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep learning methods have vastly expanded the capabilities of motion planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility, efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time, providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific training.

</details>

---

### [[20_Research/Papers/机器人/DSIP_A_Dynamic_Coordination_Planner_for_Signal-Free_Intersections_using_Diffusion-Model-Based_Multi-Agent_Motion_Planning|DSIP: A Dynamic Coordination Planner for Signal-Free Intersections using Diffusion-Model-Based Multi-Agent Motion Planning]]

![[assets/2606.30694_figure.png|800]]

- **arXiv**: [2606.30694](https://arxiv.org/abs/2606.30694)
- **PDF**: https://arxiv.org/pdf/2606.30694
- **详细分析**: [[20_Research/Papers/机器人/DSIP_A_Dynamic_Coordination_Planner_for_Signal-Free_Intersections_using_Diffusion-Model-Based_Multi-Agent_Motion_Planning|DSIP: A Dynamic Coordination Planner for Signal-Free Intersections using Diffusion-Model-Based Multi-Agent Motion Planning]]
- **作者**: Qian Hu, Haoyang Peng, Songan Zhang, Ming Yang, Hongtei Eric Tseng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《DSIP: A Dynamic Coordination Planner for Signal-Free Intersections using Diffusion-Model-Based Multi-Agent Motion Planning》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traffic signal control at urban intersections inherently introduces stop-and-go behavior, resulting in increased delays and reduced traffic efficiency, especially under high traffic demand. With the emergence of connected and automated vehicles (CAVs), trajectory-level coordination has emerged as a high-potential strategy to augment or transcend conventional phase-based management. This paper proposes DSIP (Diffusion-model-based Signal-free Intersection Planner), a multi-agent motion planning framework driven by a generative diffusion process. DSIP shifts the intersection management paradigm from discrete temporal phasing to continuous multi-vehicle trajectory optimization. This work evaluates the theoretical upper-bound performance of this coordination strategy under idealized communication and execution conditions to isolate the core benefits of the diffusion-driven approach. Using the SUMO platform, we evaluate DSIP across diverse four-leg intersection configurations. Experimental results demonstrate that DSIP significantly reduces average delay and maintains higher average speed compared to both fixed-time signal control and state-of-the-art reinforcement-learning-based controllers, particularly in medium- to high-density traffic. These findings suggest that diffusion-based trajectory planning provides a scalable and robust foundation for future autonomous intersection management. By unlocking latent intersection capacity through software-defined coordination, this approach offers a cost-effective pathway to improve urban traffic flow efficiency without requiring physical infrastructure expansion.

</details>

---

### [[20_Research/Papers/具身智能/Position_Vision-Language-Action_Models_Cannot_Be_Verified_to_Perform_Physical_Reasoning|Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning]]

![[assets/2606.30686_figure.png|800]]

- **arXiv**: [2606.30686](https://arxiv.org/abs/2606.30686)
- **PDF**: https://arxiv.org/pdf/2606.30686
- **详细分析**: [[20_Research/Papers/具身智能/Position_Vision-Language-Action_Models_Cannot_Be_Verified_to_Perform_Physical_Reasoning|Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning]]
- **作者**: Taozhao Chen, Ian Manchester, Huaming Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Position: Vision-Language-Action Models Cannot Be Verified to Perform Physical Reasoning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) systems, built on pretrained vision-language models (VLMs), have shown rapidly improving performance on robot manipulation benchmarks. These gains are commonly interpreted as evidence that semantic representations learned from internet-scale data transfer to physical execution generalization. This position paper argues that the assumption underlying this interpretation -- that semantic generalization is sufficient to support physical action decisions -- has not been independently verified and cannot be tested under current evaluation protocols. We support this claim by decomposing VLA policies into semantic mapping and physical action decision, and showing that task success rate -- the dominant evaluation metric -- cannot distinguish between these two sources of capability. As a result, improvements in benchmark performance are consistent with multiple competing explanations, including semantic matching, distributional overlap, and genuine physical generalization. We further argue that this identifiability gap has been reinforced through narrative drift, whereby successive systems inherit and strengthen prior interpretations of performance gains without isolating the underlying causal mechanism. To address this limitation, we propose a research direction based on evaluation designs that introduce controlled variation to separately measure semantic and physical generalization. Such designs make it possible to causally attribute performance without requiring access to model internals, and to empirically assess the role of VLM backbones as semantic interfaces rather than implicit sources of physical competence. Our goal is not to refute the role of VLMs in robotics, but to clarify the conditions under which claims of physical generalization can be meaningfully evaluated.

</details>

---

### [[20_Research/Papers/强化学习/Locker-based_Truck-Drone_Routing_with_Integrated_Considerations_of_Pickups,_Deliveries,_and_No-Fly_Zones|Locker-based Truck-Drone Routing with Integrated Considerations of Pickups, Deliveries, and No-Fly Zones]]

![[assets/2606.30680_figure.jpg|800]]

- **arXiv**: [2606.30680](https://arxiv.org/abs/2606.30680)
- **PDF**: https://arxiv.org/pdf/2606.30680
- **详细分析**: [[20_Research/Papers/强化学习/Locker-based_Truck-Drone_Routing_with_Integrated_Considerations_of_Pickups,_Deliveries,_and_No-Fly_Zones|Locker-based Truck-Drone Routing with Integrated Considerations of Pickups, Deliveries, and No-Fly Zones]]
- **作者**: Xuanyu Liu, Hui Hu, Jiao Zhao, Ziliang Wang, Zhengbing He
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.56，世界模型 0.16，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《Locker-based Truck-Drone Routing with Integrated Considerations of Pickups, Deliveries, and No-Fly Zones》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Truck-drone delivery is an emerging last-mile logistics mode combining the long-haul capacity of trucks with the flexible service capability of drones. In locker-based operations, smart lockers serve not only as temporary parcel storage facilities but also as automated drone docking and service nodes. These automated nodes support drone takeoff, landing, parcel handover, and battery replacement, thereby significantly extending the service range and operational flexibility of drone-assisted delivery networks. However, practical locker-based delivery systems face complex real-world challenges, requiring the integrated coordination of not only parcel delivery, return pickup, battery-constrained and load-dependent drone flights, but also necessary detours around restricted airspace. To address this practical and multifaceted challenge, this paper introduces a locker-based truck-drone routing problem with integrated considerations of pickups, deliveries, and no-fly zones (LTDRP-PDNF), with the objective of minimizing the total operational cost of a fleet of drone-equipped trucks. We formulate the route construction process as a Markov Decision Process and develop a two-stage deep reinforcement learning-based neural heuristic. The first stage utilizes an attention-based encoder and a Bidirectional Gated Recurrent Unit decoder to solve the truck-only routing problem, formulated as a capacitated vehicle routing problem. The second stage combines a policy-transfer strategy with a hybrid dispatch assignment heuristic to construct fully coordinated truck and drone routes for LTDRP-PDNF. Experiments on instances of different scales demonstrate that the proposed method outperforms metaheuristic and neural heuristic baselines in most cases while maintaining exceptionally short computation times, offering an effective, scalable solution framework under practical operational constraints.

</details>

---

### [[20_Research/Papers/大模型/Emergent_Culture_in_Minimal_LLM_Systems|Emergent Culture in Minimal LLM Systems]]

![[assets/2606.30668_figure.png|800]]

- **arXiv**: [2606.30668](https://arxiv.org/abs/2606.30668)
- **PDF**: https://arxiv.org/pdf/2606.30668
- **详细分析**: [[20_Research/Papers/大模型/Emergent_Culture_in_Minimal_LLM_Systems|Emergent Culture in Minimal LLM Systems]]
- **作者**: Simon Jones, Sabine Hauert
- **cs 子类**: cs.AI, cs.CL, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Emergent Culture in Minimal LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

What happens when LLM agents operate with no context outside a turn, minimal prompting, and simple tools? Inspired by swarm engineering, we give collectives of three agents the ability to send messages and manipulate a shared actively decaying text store, introducing evolutionary pressure. The agents spontaneously cooperate, develop storage management strategies, and generate complex evolving cultural artifacts, with no top-down engineering. Using tools from dynamical systems analysis, we show that these behaviours exhibit structured long-range coherence beyond the entropy horizon of the decaying store, consistent with emergent culture in the Sperberian sense.

</details>

---
