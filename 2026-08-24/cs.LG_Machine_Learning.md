# cs.LG | Machine Learning | 2026-08-24

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/大模型/ConceptTS_LLM-Guided_Concept_Bottlenecks_for_Interpretable_Multivariate_Time-Series_Forecasting|ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series Forecasting]]

![[assets/2608.21277_figure.png|800]]

- **arXiv**: [2608.21277](https://arxiv.org/abs/2608.21277)
- **PDF**: https://arxiv.org/pdf/2608.21277
- **详细分析**: [[20_Research/Papers/大模型/ConceptTS_LLM-Guided_Concept_Bottlenecks_for_Interpretable_Multivariate_Time-Series_Forecasting|ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series Forecasting]]
- **作者**: Yichen Jiang, Yueqiao Chen, Dongyu Liu
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM

#### 研究背景与动机

《ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series Forecasting》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

State-of-the-art multivariate time-series forecasters can model complex temporal and cross-variable dependencies, yet their opaque representations provide limited insight into why a particular forecast is produced. This lack of transparency restricts their use in settings where practitioners must understand and assess the factors underlying a prediction. We introduce ConceptTS, an interpretable forecasting framework that organizes its predictions around named, human-readable concepts. ConceptTS uses a large language model to propose task-relevant concepts and generate executable labeling rules, translating the language model's domain knowledge into direct supervision without costly manual concept annotation. The proposed concepts are organized into three complementary bottlenecks that describe the historical context, local forecast intervals, and the full forecast horizon. A shared decoder combines representations derived from their predicted activations to construct the forecast, making the model's decision process explicit and supporting direct concept-level interventions. Experiments on the Beijing Multi-Site Air Quality dataset show that ConceptTS achieves accuracy competitive with strong black-box baselines while producing semantically meaningful concept activations.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Imitation_Self-Improving_Robot_Policies_via_Off-Policy_Q-Planning|Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning]]

![[assets/2608.21204_figure.png|800]]

- **arXiv**: [2608.21204](https://arxiv.org/abs/2608.21204)
- **PDF**: https://arxiv.org/pdf/2608.21204
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Imitation_Self-Improving_Robot_Policies_via_Off-Policy_Q-Planning|Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning]]
- **作者**: Varun Giridhar, Anant Khandelwal, Jeremy A. Collins, Ignat Georgiev, Animesh Garg
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DSRL, IBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations. Reinforcement Learning fine-tuning offers a path to self-improvement but has proven difficult to scale to the multi-billion-parameter models underpinning modern robot policies. We propose Q-Planning, which equips a large visuomotor BC policy with a small off-policy Q-function. Because a Q-function estimates value rather than imitates actions, it can be trained on the same successful demonstrations as the BC policy and later absorb both successful and failed deployment rollouts, an asymmetry BC does not have. We exploit this asymmetry to enable value-guided action selection at inference (a single-step Q-weighted average over BC draws) and online self-improvement that fine-tunes only the Q-function, leaving the BC weights untouched. On LIBERO and bimanual RoboTwin, ten iterations of self-improvement lift every benchmark score we tested (LIBERO-10 93% to 99%, RoboTwin 83.8% to 91.4%) and shorten successful episodes on the near-ceiling suites (LIBERO-Object, LIBERO-Goal). On two contact-rich bimanual real-robot tasks, the same loop (BC frozen, no human intervention) improves purely from its own deployment rollouts: stack-cups 40% to 90% and insert-wallet 25% to 80% in five iterations, whereas SFT on successful rollouts alone stalls at 55% and 30%. Under an identical online budget Q-Planning is the only method, among Best-of-N, filtered SFT, IBRL, DSRL, and DAWR, that improves stably from failures without training an auxiliary actor.

</details>

---

### [[20_Research/Papers/大模型/Causal_Modeling_of_Adverse_Pregnancy_Outcomes_via_Adaptive_LLM_Proposals|Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals]]

![[assets/2608.21079_first_page.png|800]]

- **arXiv**: [2608.21079](https://arxiv.org/abs/2608.21079)
- **PDF**: https://arxiv.org/pdf/2608.21079
- **详细分析**: [[20_Research/Papers/大模型/Causal_Modeling_of_Adverse_Pregnancy_Outcomes_via_Adaptive_LLM_Proposals|Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals]]
- **作者**: Kavimayil P. Komarasamy, Saurabh Mathur, Ameet Soni, David M. Haas, Kristian Kersting, Sriraam Natarajan
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《Causal Modeling of Adverse Pregnancy Outcomes via Adaptive LLM Proposals》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adverse Pregnancy Outcomes (APOs) such as preterm birth and gestational diabetes can have long-term consequences for both the mother and child, yet an understanding of their causes remains elusive. Causal discovery in this domain is especially challenging due to a paucity of data and incomplete domain knowledge. As a result, pure data-driven methods fail, and Large Language Model (LLM) outputs remain inconsistent or contradictory. We introduce a neurosymbolic framework for generating plausible causal hypotheses that iteratively combines the broad prior knowledge of LLMs with empirical scoring on data. Our method treats the LLM as an adaptive proposal distribution, generating hypotheses that are scored against empirical data; the resulting high-scoring graphs are then used to update the LLM's context, steering subsequent generations toward more promising regions of the hypothesis space. We evaluate our approach on a real-world clinical dataset for modeling APOs and their risk factors, comparing our results against an expert-constructed causal graph. Our method recovers all expert-validated edges and identifies additional plausible causal relations not previously listed by experts, potentially providing new insights for targeted interventions.

</details>

---

### [[20_Research/Papers/世界模型/AudioWorldSim_Realistic_Binaural_Audio_Datasets_For_World_Models|AudioWorldSim: Realistic Binaural Audio Datasets For World Models]]

![[assets/2608.21075_figure.png|800]]

- **arXiv**: [2608.21075](https://arxiv.org/abs/2608.21075)
- **PDF**: https://arxiv.org/pdf/2608.21075
- **详细分析**: [[20_Research/Papers/世界模型/AudioWorldSim_Realistic_Binaural_Audio_Datasets_For_World_Models|AudioWorldSim: Realistic Binaural Audio Datasets For World Models]]
- **作者**: Luis Vitor Zerkowski, Luiz Velho
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent

#### 研究背景与动机

《AudioWorldSim: Realistic Binaural Audio Datasets For World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AudioWorldSim, Habitat-Sim, ThreeDWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This technical report presents AudioWorldSim, an open-source platform designed to generate realistic binaural audio datasets and advance research in audio-based machine learning, particularly world models. Built as a custom extension of Meta's SoundSpaces 2.0 platform, AudioWorldSim leverages their comprehensive acoustics framework, but focuses on the automatic rollout of random agent navigations, as well as implements crucial fixes to how continuous sound is composed. AudioWorldSim is made publicly available to the research community at https://github.com/Luizerko/AudioWorldSim to facilitate reproducibility.

</details>

---

### [[20_Research/Papers/大模型/Designing_a_Robust_LLM-Based_Evaluation_System_for_Agentic_AI_in_Drug_Discovery_Through_Human_Alignment|Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment]]

![[assets/2608.21057_figure.png|800]]

- **arXiv**: [2608.21057](https://arxiv.org/abs/2608.21057)
- **PDF**: https://arxiv.org/pdf/2608.21057
- **详细分析**: [[20_Research/Papers/大模型/Designing_a_Robust_LLM-Based_Evaluation_System_for_Agentic_AI_in_Drug_Discovery_Through_Human_Alignment|Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment]]
- **作者**: Emma Granqvist, Rocío Mercado, Samuel Genheden
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ChemCoTBench, MolBench, SciToolEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. Reference-based metrics such as BLEU and ROUGE fail to capture semantic correctness, while expert human evaluation does not scale to the iteration speed these systems demand. The LLM-as-a-Judge paradigm has emerged as a scalable alternative, but existing drug discovery benchmarks deploy LLM judges without validating their alignment with human experts. In this work, we present an LLM-as-a-Judge evaluation framework for ChatInvent, an agentic drug discovery assistant deployed at AstraZeneca, with four contributions. First, we define four output-quality evaluation dimensions---Completeness, Relevancy, Structural Clarity, and Scope Adherence---alongside deterministic Tool Call Correctness checks. Second, we validate the judge through a human alignment study with five expert annotators, comparing Gemini 3.1 Pro, Claude Opus 4.7, GPT-5, and Llama 3.1 70B as candidate judges. Third, we optimize the best-performing judge using few-shot demonstrations of human-annotated examples, improving alignment with the human majority vote from 0.80 to 0.86. Fourth, applying the optimized judge to 70 held-out questions, we surface concrete limitations and find that informal phrasings do not systematically degrade output quality; if anything, it is helpful to have the LLM rewrite the original question before querying the agent. Our framework provides a reusable template for human-aligned evaluation of agentic systems in scientific domains.

</details>

---

### [[20_Research/Papers/强化学习/Decoupling_Policy_Extraction_for_Offline_Reinforcement_Learning|Decoupling Policy Extraction for Offline Reinforcement Learning]]

![[assets/2608.20909_figure.png|800]]

- **arXiv**: [2608.20909](https://arxiv.org/abs/2608.20909)
- **PDF**: https://arxiv.org/pdf/2608.20909
- **详细分析**: [[20_Research/Papers/强化学习/Decoupling_Policy_Extraction_for_Offline_Reinforcement_Learning|Decoupling Policy Extraction for Offline Reinforcement Learning]]
- **作者**: Xuyao Lin, Yixiang Shan, Jinru Duan, Tao Yang, Xinyu Zhao, Runyu Lei, Yiming Zhao, Jiaxin Fan, Zongbao Feng, Peng Jia
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Decoupling Policy Extraction for Offline Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL, GCRL, QRL, TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline RL methods commonly jointly train the actor and critic, where the critic is used to guide the actor toward higher-value actions. This coupled learning process is well motivated in online RL, where an improved actor collects new data that can further update the actor and the critic. However, training data remains fixed in offline RL, making actor-side policy improvement unable to generate new data to validate or correct the critic. Moreover, retaining this coupled paradigm leads to two related challenges. Firstly, actor updates can drift toward high-valued but potentially out-of-distribution (OOD) actions and amplify critic overestimation. Secondly, conservative value estimation or behavior-cloning regularization creates a difficult trade-off between suppressing OOD actions and selecting high-value actions within the data-supported region. Motivated by this observation, we revisit the conventional offline RL paradigm and propose decoupling policy improvement from actor training. Specifically, we train the actor solely to model the behavior distribution and perform policy improvement at inference time by reranking multiple actor-generated proposals with a separately learned critic. We refer to this paradigm as the decoupled policy extraction paradigm. Under such paradigm, the actor provides behavior-supported action candidates, while the critic performs value-based selection within this candidate set. Extensive experiments show that the decoupled policy extraction paradigm outperforms both behavior cloning and jointly learned offline RL methods, while remaining effective even with a naive Q-learning critic.

</details>

---

### [[20_Research/Papers/强化学习/Sharing_the_Control_Authority_Between_Deep_Reinforcement_Learning_and_Model_Predictive_Control_Application_to_Multi-Class_Transportation_Net|Sharing the Control Authority Between Deep Reinforcement Learning and Model Predictive Control: Application to Multi-Class Transportation Networks]]

![[assets/2608.20858_figure.png|800]]

- **arXiv**: [2608.20858](https://arxiv.org/abs/2608.20858)
- **PDF**: https://arxiv.org/pdf/2608.20858
- **详细分析**: [[20_Research/Papers/强化学习/Sharing_the_Control_Authority_Between_Deep_Reinforcement_Learning_and_Model_Predictive_Control_Application_to_Multi-Class_Transportation_Net|Sharing the Control Authority Between Deep Reinforcement Learning and Model Predictive Control: Application to Multi-Class Transportation Networks]]
- **作者**: Giray Onur, Azita Dabiri, Bart De Schutter
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Sharing the Control Authority Between Deep Reinforcement Learning and Model Predictive Control: Application to Multi-Class Transportation Networks》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transportation networks, in particular multi-class transportation networks (i.e., networks with mixed vehicle types), are complex systems that are challenging to control. Recently, Deep Reinforcement Learning (DRL), which learns control policies from interactions with the environment, and Model Predictive Control (MPC), which uses a system model to optimize control inputs, have been increasingly utilized for transportation network control. However, nonlinear system dynamics and high-dimensional state spaces in large-scale networks limit DRL's learning capacity under time-constrained training and increase MPC's computation time, hindering real-time implementation with limited computational resources. Moreover, MPC depends on an accurate network model, which is often unavailable for complex systems such as multi-class transportation networks. This paper proposes a novel DRL-MPC framework for multi-class transportation networks that divides control authority between DRL and MPC, combining DRL's fast online computation and model independence with MPC's built-in optimization and constraint-handling capabilities. In the hierarchical framework, MPC operates at the higher level and determines low-frequency control inputs whose slower update rate accommodates its high computation time, while DRL operates at the lower level and determines high-frequency control inputs using its fast online deployment. The framework is evaluated on a multi-class freeway network against a hierarchical MPC controller and a hybrid state-feedback-MPC controller, including scenarios with model mismatch and noisy traffic demands. Results show that the proposed framework outperforms the hybrid state-feedback-MPC controller, substantially reduces online computation time compared with the hierarchical MPC controller, and provides more effective constraint enforcement under model mismatch.

</details>

---

### [[20_Research/Papers/强化学习/Rethinking_Demonstration_Unlearning_in_Imitation_Learning_for_Robotics|Rethinking Demonstration Unlearning in Imitation Learning for Robotics]]

![[assets/2608.20784_figure.png|800]]

- **arXiv**: [2608.20784](https://arxiv.org/abs/2608.20784)
- **PDF**: https://arxiv.org/pdf/2608.20784
- **详细分析**: [[20_Research/Papers/强化学习/Rethinking_Demonstration_Unlearning_in_Imitation_Learning_for_Robotics|Rethinking Demonstration Unlearning in Imitation Learning for Robotics]]
- **作者**: Jiazhuo Li, Yu Zhang, Yiming Fei, Kangkang Dong, Xiaojun Zhu, Houde Liu, Jinze Tao
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《Rethinking Demonstration Unlearning in Imitation Learning for Robotics》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning for robotics depends on human demonstrations, some of which people may later ask to remove. Retraining without them is the natural reference, but its cost grows with policy and dataset scale, motivating cheaper operators that edit a trained policy. Metrics inherited from machine unlearning, such as forgetting loss or a single membership attack, do not establish what an edit removed from a policy acting in closed loop. We therefore introduce a retrain-calibrated audit that reads demonstration unlearning along two axes: behavior, whether the edited policy acts like one retrained without the removed demonstrations, and evidence, whether an auditor can still detect it was trained on them. The behavior axis measures action divergence to that retrain at matched states, calibrated by a floor built from independent retrains, so a policy at the floor is as close to a retrain as retrains are to each other. The evidence axis applies a per-demonstration membership attack against a retrain null, reporting both its rank and its absolute member-loss level, since rank alone accepts operators that inflate member losses past the null. A conformal test then combines both axes into one hypothesis of joint retrain consistency, against a fleet of independent retrains large enough to reject at conventional significance. Across five preregistered conditions on three real-robot policy classes and two simulation suites, the axes dissociate in both directions on one checkpoint, as an edit may repair task behavior while leaving evidence unchanged, or reduce evidence while moving behavior away from retraining. On the ACT arm, a redirect edit restores blind-scored robot success to 18 of 20 trials.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Continuous-Time_Jump_Markov_Decision_Processes_with_Applications_to_Network_Dynamic_Pricing|Reinforcement Learning for Continuous-Time Jump Markov Decision Processes with Applications to Network Dynamic Pricing]]

![[assets/2608.20680_first_page.png|800]]

- **arXiv**: [2608.20680](https://arxiv.org/abs/2608.20680)
- **PDF**: https://arxiv.org/pdf/2608.20680
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Continuous-Time_Jump_Markov_Decision_Processes_with_Applications_to_Network_Dynamic_Pricing|Reinforcement Learning for Continuous-Time Jump Markov Decision Processes with Applications to Network Dynamic Pricing]]
- **作者**: Huiling Meng, Ningyuan Chen, Xuefeng Gao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Reinforcement Learning for Continuous-Time Jump Markov Decision Processes with Applications to Network Dynamic Pricing》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study reinforcement learning (RL) in Continuous-Time Jump Markov Decision Processes (CTJMDPs) featuring general discrete state spaces (which need not possess a vector space structure) and continuous/discrete action spaces. The setup covers many well-known applications in operations such as multi-product dynamic pricing with capacitated resources (Gallego and van Ryzin 1997). To model the exploration-exploitation tradeoff, we formulate an entropy-regularized continuous-time control problem with stochastic policies. Recent continuous-time RL techniques such as $q$-learning for controlled diffusions in (Jia and Zhou 2023) focus on continuous state spaces $\mathbb{R}^d$ and rely heavily on semimartingale theory in $\mathbb{R}^d$ for their theoretical analysis. Consequently, their methods cannot be directly applied to CTJMDPs with general discrete state spaces, which may lack the algebraic addition and subtraction structures inherent to Euclidean spaces. To bridge this gap, we establish the theoretical foundations of $q$-learning for CTJMDPs and develop model-free $q$-learning algorithms. Compared to naïve time discretization and approximating CTJMDPs using discrete-time MDPs, our approach has several conceptual and empirical benefits. Numerical experiments in network dynamic pricing (Gallego and van Ryzin 1997) show that our proposed RL algorithm reliably learns near-optimal policies and consistently outperforms standard benchmark methods, demonstrating superior solution quality and effective scalability to large-scale network instances.

</details>

---
