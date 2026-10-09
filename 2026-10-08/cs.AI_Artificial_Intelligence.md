# cs.AI | Artificial Intelligence | 2026-10-08

#arxiv #ComputerScience

**论文数**: 22

### [[20_Research/Papers/世界模型/RoboJEPA_Scaling_Robotic_Latent_World_Models|RoboJEPA: Scaling Robotic Latent World Models]]

![[assets/2610.10515_figure.png|800]]

- **arXiv**: [2610.10515](https://arxiv.org/abs/2610.10515)
- **PDF**: https://arxiv.org/pdf/2610.10515
- **详细分析**: [[20_Research/Papers/世界模型/RoboJEPA_Scaling_Robotic_Latent_World_Models|RoboJEPA: Scaling Robotic Latent World Models]]
- **作者**: Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.3，大模型 0.1，世界模型 1，机器人 1.3）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《RoboJEPA: Scaling Robotic Latent World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to predict model quality well beyond the scale at which the law is fit. We further show that downstream robotic planning performance improves predictably with compute, and that imagination error is strongly correlated with it, making it a reliable proxy for real-robot evaluation. Finally, we demonstrate that latent world models can be deployed zero-shot as robotic agents, planning toward a single goal image to solve tasks requiring long-horizon planning on real hardware. We release all model checkpoints together with our training and robot deployment code. To our knowledge, this is the first work to establish scaling laws for multi-embodiment robotic world models trained on real robot data, and RoboJEPA, at 8B parameters, is the largest JEPA predictor model trained to date.

</details>

---

### [[20_Research/Papers/具身智能/Q-Learning_with_Scalar_Adjoint_Matching|Q-Learning with Scalar Adjoint Matching]]

![[assets/2610.10437_figure.png|800]]

- **arXiv**: [2610.10437](https://arxiv.org/abs/2610.10437)
- **PDF**: https://arxiv.org/pdf/2610.10437
- **详细分析**: [[20_Research/Papers/具身智能/Q-Learning_with_Scalar_Adjoint_Matching|Q-Learning with Scalar Adjoint Matching]]
- **作者**: Yonghoon Dong, Minsung Yoon, Jaehyuk Kim, Jungwoo Park, Changyeon Kim, Jinwoo Shin
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Q-Learning with Scalar Adjoint Matching》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow policies capture rich and diverse action distributions, and fine-tuning them with off-policy RL to improve beyond the demonstrations has drawn growing interest. However, fine-tuning a flow policy against a learned value function is not trivial, because the policy generates its action over many flow steps. Adjoint matching offers a principled way to update the flow model itself by propagating value information from the final action back to each flow step, but it requires a vector--Jacobian product through the policy at every step, a cost that grows with the number of flow steps and the policy size. We observe that the batch-averaged velocity Jacobian of pretrained flow policies concentrates on its diagonal. Motivated by this finding, we derive a closed-form scalar adjoint that scales the value gradient at the final action by the flow time, eliminating the per-step vector--Jacobian products. We further find that controlling the critic's value at policy-generated actions is particularly important under the scalar adjoint. Based on these findings, we propose Q-learning with Scalar Adjoint Matching (SQAM), which combines the scalar adjoint with a value penalty at those actions. SQAM's gains concentrate on the four hardest OGBench domains, where its success rate exceeds that of the strongest baseline in each domain by 18 to 35 percentage points. To test whether SQAM extends to large pretrained policies, we also fine-tune a vision-language-action policy on a real bimanual robot. SQAM improves over supervised fine-tuning on all three tasks.

</details>

---

### [[20_Research/Papers/具身智能/RoboQuest_Generalist_Physical_Agents_that_Search,_Inspect_and_Test|RoboQuest: Generalist Physical Agents that Search, Inspect and Test]]

![[assets/2610.10388_figure.png|800]]

- **arXiv**: [2610.10388](https://arxiv.org/abs/2610.10388)
- **PDF**: https://arxiv.org/pdf/2610.10388
- **详细分析**: [[20_Research/Papers/具身智能/RoboQuest_Generalist_Physical_Agents_that_Search,_Inspect_and_Test|RoboQuest: Generalist Physical Agents that Search, Inspect and Test]]
- **作者**: Liu Renhang, Navonil Majumder, Tej Deep Pala, Soujanya Poria
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.6，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboQuest: Generalist Physical Agents that Search, Inspect and Test》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench, RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in multimodal foundation models have made them capable generalist physical agents for a range of manipulation tasks. However, successful operation in an unfamiliar environment may require an agent to seek task-relevant information through interaction when it is absent from the observations: it may need to determine where a relevant object is, inspect an unobserved property, or discover the effect of an unfamiliar tool. We thus introduce RoboQuest, a benchmark for goal-directed embodied exploration, where agents must actively acquire task-relevant information through physical interaction, use the resulting evidence to adapt subsequent actions, and autonomously decide when to commit to task completion. RoboQuest comprises ten mobile manipulation tasks centered on three forms of uncertainty: search, manipulation-based inspection, and interactive testing. We evaluate five frontier multimodal agents through a common visuomotor interface, as well as a $π_{0.5}$ policy fine-tuned on the full-episode demonstrations we release. The best agent succeeds in only 23\% of the episodes, and the fine-tuned policy almost never succeeds. Isolated tests of the execution skills the tasks are built from, with the hidden information supplied, show that the agents can carry out most of the required actions, and our failure analysis attributes only a minority of the failures to execution. Our failure analysis further finds that the agents often stop exploring too early as they make decisions before observing the required evidence for task completion. We also find that agents rarely prevent or repair the disturbances caused by their exploration. Moreover, learning by trial and error remains difficult for most models.

</details>

---

### [[20_Research/Papers/具身智能/A_Scoping_Review_and_Experimental_Study_on_Reinforcement_Learning_from_Human_Feedback_for_Human-Robot_Collaboration|A Scoping Review and Experimental Study on Reinforcement Learning from Human Feedback for Human-Robot Collaboration]]

![[assets/2610.09891_figure.png|800]]

- **arXiv**: [2610.09891](https://arxiv.org/abs/2610.09891)
- **PDF**: https://arxiv.org/pdf/2610.09891
- **详细分析**: [[20_Research/Papers/具身智能/A_Scoping_Review_and_Experimental_Study_on_Reinforcement_Learning_from_Human_Feedback_for_Human-Robot_Collaboration|A Scoping Review and Experimental Study on Reinforcement Learning from Human Feedback for Human-Robot Collaboration]]
- **作者**: Alexandra Coroiu, Andrea Vogt, Viktor Werbilo, Andreas Poppele, Johann Christensen, Sven Hallerbach
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《A Scoping Review and Experimental Study on Reinforcement Learning from Human Feedback for Human-Robot Collaboration》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-Robot Collaboration (HRC) can facilitate mass customisation in Industry 4.0, with Reinforcement Learning from Human Feedback (RLHF) representing a promising approach for developing safe AI-based robots. Practical challenges remain regarding safety during AI development, human feedback quality, and bidirectional human-robot adaptation. We conducted a scoping review of RLHF in HRC systems, mapping methods that address these challenges. Following PRISMA guidelines, we screened 199 records and included 20 peer-reviewed publications (2020-2025) spanning multiple HRC domains. To our knowledge, this is the first review focused on the bidirectional, closed-loop design of RLHF. Our review found multiple feedback modalities enabling data collection in various feedback formats. Collected data can be integrated at different stages of AI training, resulting in a multi-step development process. Pilot experiments are commonly used to evaluate HRC systems based on both human and robot metrics. To empirically test a key gap identified in the review, we conducted a between-subjects VR experiment comparing system- and user-initiated feedback on robot proxemic behaviour for safe navigation. Using Bayesian models, we analysed the relation between the collected feedback and safety metrics: psychological safety (post-experiment questionnaire) and physical safety (inverse time-to-collision). Results show that user-initiated feedback captures perceived safety better than system-initiated feedback, indicating that feedback timing directly affects feedback quality. Our review and experiment findings show that RLHF relies on appropriate feedback methods to ensure AI safety in HRC, and future RLHF research should prioritise realistic HRC experiments evaluating the effects of feedback collection methods on relevant human and robot metrics.

</details>

---

### [[20_Research/Papers/强化学习/Deadline-Aware_Multi-Agent_Reinforcement_Learning_for_TSN-Based_Vehicular_Edge_Networks|Deadline-Aware Multi-Agent Reinforcement Learning for TSN-Based Vehicular Edge Networks]]

![[assets/2610.09870_figure.png|800]]

- **arXiv**: [2610.09870](https://arxiv.org/abs/2610.09870)
- **PDF**: https://arxiv.org/pdf/2610.09870
- **详细分析**: [[20_Research/Papers/强化学习/Deadline-Aware_Multi-Agent_Reinforcement_Learning_for_TSN-Based_Vehicular_Edge_Networks|Deadline-Aware Multi-Agent Reinforcement Learning for TSN-Based Vehicular Edge Networks]]
- **作者**: Bernardo A. C. Pereira, Marcos Carvalho, Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci, Andreas Gavrielides, Johann M. Marquez-Barja, Daniel F. Macedo
- **cs 子类**: cs.AI, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Deadline-Aware Multi-Agent Reinforcement Learning for TSN-Based Vehicular Edge Networks》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL, PDU-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vehicular edge computing (VEC) enables latency-sensitive applications by bringing computing and networking resources closer to vehicles. However, existing approaches often overlook network contention among co-located services with heterogeneous and dynamic latency requirements. While time-sensitive networking (TSN) provides bounded-latency communication, conventional and reinforcement learning-based schedulers struggle to adapt to highly dynamic vehicular environments and inter-queue dependencies. To address these limitations, we propose a multi-agent reinforcement learning (MARL) approach for queue-level scheduling in TSN-enabled VEC. Each TSN queue is assigned an autonomous agent that jointly learns the queue service order and time-slot duration to minimize deadline misses under speed-dependent latency requirements. We employ multi-agent proximal policy optimization (MAPPO) to enable coordinated yet autonomous scheduling decisions. Evaluation against single-agent, multi-agent, and non-learning-based baselines shows that MAPPO provides robust performance across different traffic profiles. Compared with centralized single-agent methods, it reduces service latency by up to 66.2% and improves reliability by up to 271.8%. Furthermore, unlike urgency-based heuristics, MAPPO ensures balanced scheduling while achieving lower inference times compared to other MARL methods.

</details>

---

### [[20_Research/Papers/大模型/Training_Advisors_for_LLM_Agents_from_Task_Outcomes|Training Advisors for LLM Agents from Task Outcomes]]

![[assets/2610.09858_figure.png|800]]

- **arXiv**: [2610.09858](https://arxiv.org/abs/2610.09858)
- **PDF**: https://arxiv.org/pdf/2610.09858
- **详细分析**: [[20_Research/Papers/大模型/Training_Advisors_for_LLM_Agents_from_Task_Outcomes|Training Advisors for LLM Agents from Task Outcomes]]
- **作者**: Sergei Polezhaev, Barys Liskavets, Ori Press, Alexander Golubev
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.67（加权：大模型 1.15，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Training Advisors for LLM Agents from Task Outcomes》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, CTRL, Critique-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents tackle multi-step tasks by interleaving reasoning and tool calls with observations from the environment. Prior work has shown that natural-language feedback can help these agents revise their decisions during task execution. We introduce Caddie, a method for training critics to provide natural-language analysis and advice as agents work through a task. Unlike approaches that rely on step-level labels or reference critiques, Caddie learns from whether the agent ultimately succeeds after receiving the critic's feedback. We optimize the critic through reinforcement learning while keeping the base model frozen. Trained on multi-hop question answering with a single base model, our Qwen3-4B critic improves success rates across four base models of different scales and architectures, including three not used during critic training. On the MuSiQue benchmark, the trained critic improves Qwen3-4B's success rate by more than 25 percentage points, surpassing the performance of Kimi K3 without a critic. The same critic also yields gains on out-of-domain interactive benchmarks, including $τ^3$ and DeepDive, with no additional training. Our results show that agents can decide when to seek help from a critic at inference time and that outcome-based critic training can produce guidance that transfers across base models and task domains.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Policy_Support_Interaction_Constrained_Offline_Reinforcement_Learning_for_Autonomous_Driving|Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving]]

![[assets/2610.09763_figure.png|800]]

- **arXiv**: [2610.09763](https://arxiv.org/abs/2610.09763)
- **PDF**: https://arxiv.org/pdf/2610.09763
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Policy_Support_Interaction_Constrained_Offline_Reinforcement_Learning_for_Autonomous_Driving|Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving]]
- **作者**: Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.16，世界模型 0.36）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CaRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains. A central challenge, however, is distribution shift: policy optimization may favor actions that are weakly supported by the offline data, rendering value estimates unreliable. Existing approaches primarily control this shift in the policy's own action space. In interactive environments such as autonomous driving, this can be insufficient: a candidate ego trajectory may remain well supported under the marginal behavior distribution while being poorly supported jointly with the surrounding-agent behavior observed in the logged interaction. We refer to this degradation in interaction support as \emph{interaction distribution shift} (IDS), and introduce \emph{Interaction-Constrained Drive Policy} (ICDP), an offline reinforcement learning framework that explicitly controls interaction-level distribution shift. Starting from the joint data distribution over ego and surrounding-agent futures, we show that joint-support degradation decomposes exactly into an ego-support component and a residual interaction-support component. We recover the latter through contrastive density-ratio estimation, isolating interaction compatibility without explicit joint-density modeling, surrounding-agent prediction, or rollouts in reactive simulators or learned world models during policy optimization. Closed-loop evaluations on nuPlan, Interplan and real-world truck experiments show that ICDP suppresses high-value yet interaction-unsupported trajectory selections and improves performance in interaction-critical driving scenarios. Project webpage: https://mahmoud-selim.github.io/ICDP/

</details>

---

### [[20_Research/Papers/具身智能/Sparse_Feature_Policy_Unlearning_Mitigates_State_Hallucination_in_Vision-Language-Action_Models|Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models]]

![[assets/2610.09496_figure.png|800]]

- **arXiv**: [2610.09496](https://arxiv.org/abs/2610.09496)
- **PDF**: https://arxiv.org/pdf/2610.09496
- **详细分析**: [[20_Research/Papers/具身智能/Sparse_Feature_Policy_Unlearning_Mitigates_State_Hallucination_in_Vision-Language-Action_Models|Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models]]
- **作者**: Jiho Lee, Jeongeun Park, Heayoun Choi, Taekyung Kim, Eunwoo Kim
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened attention to task-relevant visual regions, and a mechanistic interpretation via sparse autoencoders reveals that hallucination-associated sparse features are activated when these failures occur. Based on this analysis, we propose SOUL (Sparse feature pOlicy UnLearning), which selectively unlearns policy knowledge associated with state hallucination behaviors, where sparse features identified from hallucination failures and successful behaviors serve as explicit forgetting and retention targets, respectively. Experiments across VLA architectures in simulated and real-world environments show that our method substantially reduces hallucinated failures and improves task success without substantially compromising the existing manipulation capabilities. These results suggest that interpretable feature analysis provides a practical basis for selectively modifying undesirable knowledge in robot policies.

</details>

---

### [[20_Research/Papers/大模型/LLM-Enabled_UAV_Dispatch_A_System-Level_Survey_and_Taxonomy|LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy]]

![[assets/2610.09466_figure.png|800]]

- **arXiv**: [2610.09466](https://arxiv.org/abs/2610.09466)
- **PDF**: https://arxiv.org/pdf/2610.09466
- **详细分析**: [[20_Research/Papers/大模型/LLM-Enabled_UAV_Dispatch_A_System-Level_Survey_and_Taxonomy|LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy]]
- **作者**: Xiao Han, Aoyang Quan, Xiangyu Zhao, Xiangjie Kong, Guojiang Shen
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，机器人 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) dispatch is beginning to move beyond isolated path planning and optimization-driven resource allocation toward system-level coordination supported by semantic reasoning and LLM-based interfaces. This survey provides a unified characterization of LLM-enabled UAV dispatch systems that bridges semantic intent, symbolic decision-making, and physical UAV execution. Rather than treating LLMs as standalone add-ons, we conceptualize them as a cross-layer semantic orchestration layer connecting human instructions, external solvers, and distributed control modules. We organize the literature into four representative dispatch paradigms: pipeline dispatch, global assignment dispatch, decentralized agentic dispatch, and divide-and-conquer dispatch. For each paradigm, we analyze its decision logic, system structure, control flow, representative methods, and potential LLM roles. We further examine how LLMs support semantic parsing, retrieval-grounded planning, solver orchestration, local agent reasoning, multi-agent coordination, safety assessment, and human-facing explanation. We discuss the implications of these paradigms for scalability, robustness, coordination burden, and verification requirements, and identify open challenges including latency-aware reasoning, grounding reliability, physical feasibility guarantees, edge deployment, privacy protection, and distributed consistency. This survey provides a system-level taxonomy and design perspective for integrating LLMs into safety-critical UAV dispatch systems.

</details>

---

### [[20_Research/Papers/强化学习/SearchWorld_Spatial_Value-Grounded_Imagination_for_UAV_Object_Search_via_World_Models|SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models]]

![[assets/2610.09335_figure.png|800]]

- **arXiv**: [2610.09335](https://arxiv.org/abs/2610.09335)
- **PDF**: https://arxiv.org/pdf/2610.09335
- **详细分析**: [[20_Research/Papers/强化学习/SearchWorld_Spatial_Value-Grounded_Imagination_for_UAV_Object_Search_via_World_Models|SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models]]
- **作者**: Yatai Ji, Zhengqiu Zhu, Yong Zhao, Yue Hu, Fanglong Yao, Chen Gao, Pengfei Zhu, Quanjun Yin
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 大模型, 强化学习
- **相关性评分**: 2.32（加权：大模型 0.2，强化学习 0.16，世界模型 1.16，机器人 0.8）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models》归入 世界模型、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SearchWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability. Urban environments pose several challenges: large search areas and narrow egocentric views limit coverage, dense 3D geometry constrains safe motion, and open-world instructions require identifying a specific target among distractors. Many existing methods mitigate partial observability through explicit maps or memory representations, yet remain largely reactive, reasoning over past observations without explicitly predicting future states. World models enable prospective reasoning through imagined rollouts. However, image-generating world models can incur high inference latency, while spatially grounded planning remains challenging for latent world models. We propose SearchWorld, a recurrent state-space world model that connects explicit spatial memory with value-guided imagination. The model maintains BEV exploration and obstacle memory and decodes a task-aware spatial value layer to guide search. A cognition-action network uses this learned spatial value prior to improve the policy through imagined rollouts, without training a separate scalar critic. Training progresses from world-model learning to expert imitation and imagination-based exploration refinement. On UAV-ON, SearchWorld improves the success rate to 23.8% (19.5% for the strongest published agent) and raises oracle success to 35.5%, while remaining robust on unseen scenes (19.9% success rate). By grounding imagination in explicit spatial representations, SearchWorld enables UAV agents to plan prospectively rather than react.

</details>

---

### [[20_Research/Papers/具身智能/RT-Safe_Benchmarking_Agent_Safety_in_Real-Time_Embodied_Environment|RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment]]

![[assets/2610.09294_figure.png|800]]

- **arXiv**: [2610.09294](https://arxiv.org/abs/2610.09294)
- **PDF**: https://arxiv.org/pdf/2610.09294
- **详细分析**: [[20_Research/Papers/具身智能/RT-Safe_Benchmarking_Agent_Safety_in_Real-Time_Embodied_Environment|RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment]]
- **作者**: Tianruo Rose Xu, Jiawei Ren, Yichi Yang, Zhaoxu Zheng, Lianhui Qin
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习, 世界模型
- **相关性评分**: 2.22（加权：具身智能 1.2，大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AsyncVLA, SimWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-time constraints: the physical world does not pause while an agent reasons. As pedestrians move and vehicles approach during inference, an action that appears safe at observation time may become unsafe before execution. Real-time embodied safety therefore depends on both decision quality and decision latency. We introduce RT-SAFE, a simulated urban benchmark for evaluating embodied-agent safety under real-time constraints. RT-SAFE combines navigation tasks with moving actors, environmental hazards, and traffic rules, while allowing the world to evolve throughout inference and action execution. Across eight VLMs, agents achieve high task completion yet almost never complete safely: in the hardest setting, only 0.7% of episodes finish without a safety event. More strikingly, matched static and real-time evaluations yield task completion rates of 91.3% and 94.1%, respectively, while real-time execution increases collisions by $12.3\times$. These results reveal that standard task success can mask substantial safety failures, and that decision latency itself can become a source of physical risk. Finally, we show that RT-SAFE can support offline RL training and substantially reduce collision rates while achieving strong task completion.

</details>

---

### [[20_Research/Papers/世界模型/LeCuration_A_Tiny_World_Model_as_a_Data_Curation_Multi-Tool|LeCuration: A Tiny World Model as a Data Curation Multi-Tool]]

![[assets/2610.09285_figure.png|800]]

- **arXiv**: [2610.09285](https://arxiv.org/abs/2610.09285)
- **PDF**: https://arxiv.org/pdf/2610.09285
- **详细分析**: [[20_Research/Papers/世界模型/LeCuration_A_Tiny_World_Model_as_a_Data_Curation_Multi-Tool|LeCuration: A Tiny World Model as a Data Curation Multi-Tool]]
- **作者**: Mayank Sengupta, Nirmit Desai, Eric Song, Kunal Sawarkar
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《LeCuration: A Tiny World Model as a Data Curation Multi-Tool》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a separate, larger downstream model. To build this model, we choose LeWorldModel (LeWM)as our latent encoder and predictor, adding a diffusion transformer (DiT) decoder to add visuals to autoregressive gameplay rollout. We find that the embeddings of this model can be used as an anomaly detection signal and as a content-based clustering heuristic, and that auto-regressively predicting the game state with this model allows us to qualitatively check for action-state consistency. This paper presents a qualitative, proof-of-concept case study on CS:GO gameplay data; we do not yet report quantitative curation metrics or downstream training results, which we identify as the key next step.

</details>

---

### [[20_Research/Papers/具身智能/RLDISCOVER_LLM-driven_co-evolution_of_reinforcement_learning_algorithms|RLDISCOVER: LLM-driven co-evolution of reinforcement learning algorithms]]

![[assets/2610.09218_figure.png|800]]

- **arXiv**: [2610.09218](https://arxiv.org/abs/2610.09218)
- **PDF**: https://arxiv.org/pdf/2610.09218
- **详细分析**: [[20_Research/Papers/具身智能/RLDISCOVER_LLM-driven_co-evolution_of_reinforcement_learning_algorithms|RLDISCOVER: LLM-driven co-evolution of reinforcement learning algorithms]]
- **作者**: Haoran Li, Zengle Ge, Xiaomin Yuan, Yui Lo, Songlin Zhou, Jiahua Ying, Haoxin Li, Qianhui Liu, Yuanhang Liu, Jiaqun Liu, Guokai Chen, Mingju Chen...
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.5，强化学习 0.8）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《RLDISCOVER: LLM-driven co-evolution of reinforcement learning algorithms》归入 强化学习、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DiscoRL, MetaGenRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-guided program evolution has enabled discoveries in mathematics and computational optimization, raising the prospect of reinforcement learning (RL) algorithms that self-evolve to improve how agents learn. However, realizing this prospect faces two obstacles. Joint search over coupled algorithmic components is difficult to scale: simultaneous changes can disrupt learning, while isolated changes overlook their dependencies. Evaluating candidate algorithms also requires costly training, with fitness remaining uncertain across random seeds. We introduce RLDiscover, a framework for the self-evolution of model-free deep RL algorithms. Progressive Co-Evolution advances from targeted component edits to joint evolution, while Progressive Probabilistic Evaluation balances search breadth and evaluation fidelity through staged training and repeated evaluation. Experiments across SAC, PPO, and DQN on four benchmark suites show substantial improvements in mean return, with per-family median gains of 32%-84% and a peak return ratio of approximately 363x over a near-zero baseline. These gains include transitions from failed learning to successful task completion, and improvements persist when evolution starts from stronger open-source implementations. On measured SAC locomotion runs, evaluation uses approximately one-fifteenth the estimated compute required to fully evaluate the same candidate pool. Remarkably, independent searches repeatedly discover interpretable combinations of adaptive robust losses, progress-dependent value targets, and running statistics, with selected programs transferring to unseen tasks. These findings point toward a broader role for self-evolution in AI: discovering interpretable algorithms that improve how agents learn.

</details>

---

### [[20_Research/Papers/具身智能/DIVA_Dual-Space_Intent-Aware_Visual_Attenuation_for_Vision-Language-Action_Policies|DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies]]

![[assets/2610.09144_figure.png|800]]

- **arXiv**: [2610.09144](https://arxiv.org/abs/2610.09144)
- **PDF**: https://arxiv.org/pdf/2610.09144
- **详细分析**: [[20_Research/Papers/具身智能/DIVA_Dual-Space_Intent-Aware_Visual_Attenuation_for_Vision-Language-Action_Policies|DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies]]
- **作者**: Kaixi Feng, Guoheng Sun, Ziyao Wang, Yexiao He, Zheyu Shen, Ang Li
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AVA-VLA, FocusVLA, LightVLA, OpenVLA, Real-World, ReconVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tokens influence policy computation. We introduce DIVA, a Dual-Space Intent-Aware Visual Attenuation module with an anchor-then-attenuate design. DIVA combines high-level task intent with low-level visual evidence to estimate patch-wise relevance anchors, then applies them in two complementary spaces: it reweights projected visual tokens before backbone entry and persistently attenuates low-relevance visual states within the backbone. DIVA preserves the full visual token sequence and requires no external grounding supervision. On LIBERO, DIVA improves OpenVLA-OFT from 96.6% to 98.0% average success and raises its zero-shot LIBERO-Plus score from 69.6 to 72.6. Real-world experiments further show consistent gains under task-irrelevant visual perturbations, supporting the robustness of intent-aware visual attenuation beyond simulation.

</details>

---

### [[20_Research/Papers/强化学习/MimicX_Policy-in-the-Loop_Supervision_Refinement_for_Video-Driven_Humanoid_Motion_Tracking|MimicX: Policy-in-the-Loop Supervision Refinement for Video-Driven Humanoid Motion Tracking]]

![[assets/2610.09055_figure.png|800]]

- **arXiv**: [2610.09055](https://arxiv.org/abs/2610.09055)
- **PDF**: https://arxiv.org/pdf/2610.09055
- **详细分析**: [[20_Research/Papers/强化学习/MimicX_Policy-in-the-Loop_Supervision_Refinement_for_Video-Driven_Humanoid_Motion_Tracking|MimicX: Policy-in-the-Loop Supervision Refinement for Video-Driven Humanoid Motion Tracking]]
- **作者**: Shuaijun Liu, Chenglong Zhang, Xuhao Liu, Feiyang You, Yifan Liao, Shuyang Hao, Chaozhe Zhang, Chengyu Wu, Zhen Sun, Ningxin Su
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《MimicX: Policy-in-the-Loop Supervision Refinement for Video-Driven Humanoid Motion Tracking》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human videos provide rich motion targets for humanoid learning, yet visually plausible references can still produce persistent failures under physics-based execution. These failures reveal where training supervision should change. We present MimicX, a policy-in-the-loop framework that uses execution feedback to refine video-driven humanoid motion tracking. Starting from reconstructed and retargeted motion, MimicX localizes difficult transitions and affected body regions, then jointly adapts tracking objectives and the reset curriculum for policy continuation. Repeated rollout verification selects execution-priority improvements subject to tracking guards. Across four core video tasks, MimicX consistently improves tracking accuracy and Robust Execution Horizon relative to the Fixed Reference baseline. Task-averaged results show a 25.7% reduction in body-tracking error and a 255.6% increase in execution horizon. Additional video, motion-reference, and collision-scene studies evaluate the method beyond the core tasks, while MimicX-HLoop accelerates feedback through heterogeneous execution. Overall, MimicX turns policy failure into actionable supervision for deciding what to refine and which refinement to retain.

</details>

---

### [[20_Research/Papers/机器人/Shared-Roadmap_Generation_and_Evaluator_for_Multi-Agent_Path_Planning_Using_Heterogeneous_Graph_Neural_Network|Shared-Roadmap Generation and Evaluator for Multi-Agent Path Planning Using Heterogeneous Graph Neural Network]]

![[assets/2610.09034_figure.png|800]]

- **arXiv**: [2610.09034](https://arxiv.org/abs/2610.09034)
- **PDF**: https://arxiv.org/pdf/2610.09034
- **详细分析**: [[20_Research/Papers/机器人/Shared-Roadmap_Generation_and_Evaluator_for_Multi-Agent_Path_Planning_Using_Heterogeneous_Graph_Neural_Network|Shared-Roadmap Generation and Evaluator for Multi-Agent Path Planning Using Heterogeneous Graph Neural Network]]
- **作者**: Brandon Ho, Nikola Rogers, Seung-Kyum Choi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Shared-Roadmap Generation and Evaluator for Multi-Agent Path Planning Using Heterogeneous Graph Neural Network》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent path planning (MAPP) in continuous environments often relies on roadmaps to balance safety and search efficiency. However, traditional roadmap generation methods, such as lattice grids or standard sampling-based approaches, frequently face a trade-off between graph density and the likelihood of finding feasible, high-quality solutions. In this paper, we propose a scalable heterogeneous Graph Neural Network (GNN) framework for the automated generation and evaluation of shared multi-agent roadmaps. Our model covers the representation of waypoints, agent locations, and task locations as distinct nodes in a heterogeneous graph, allowing it to reason over global connectivity and inter-agent interactions. By training on occupation density maps aggregated and collected from expert solver trajectories, the GNN learns to identify critical points of interest and prune redundant nodes and edges. This process produces a compact, coordination-aware roadmap that is invariant to task permutations and is reusable for multi-agent pick and delivery tasks. Experimental results demonstrate that our framework can reduce planning effort and can potentially find better solutions, reaching at least 40% reduction in runtime and in graph size for dense roadmaps.

</details>

---

### [[20_Research/Papers/具身智能/PAIR_Bridging_Perception_and_Action_in_Vision-Language-Action_Models|PAIR: Bridging Perception and Action in Vision-Language-Action Models]]

![[assets/2610.09016_figure.png|800]]

- **arXiv**: [2610.09016](https://arxiv.org/abs/2610.09016)
- **PDF**: https://arxiv.org/pdf/2610.09016
- **详细分析**: [[20_Research/Papers/具身智能/PAIR_Bridging_Perception_and_Action_in_Vision-Language-Action_Models|PAIR: Bridging Perception and Action in Vision-Language-Action Models]]
- **作者**: Kaixi Feng, Guoheng Sun, Ang li
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.5，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《PAIR: Bridging Perception and Action in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, UniVLA, VQ-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models map visual observations and language instructions to continuous robot actions. This task requires a transition from representations that describe the scene and instruction to representations that support action generation. Many continuous-action VLAs leave this transition implicit and supervise it mainly through the final action-prediction loss. We introduce PAIR, a framework that learns a shared perception-action representation between these two spaces. During training, a Masked Action Autoencoder encodes expert action chunks into horizon-aligned Action Latent Tokens. A Bridge Module extracts task-relevant features from the current visual-language representations. PAIR aligns these features with the Action Latent Tokens to form Bridge Tokens that preserve task information and capture the structure of expert actions. The Bridge Tokens are then projected into the action-token space and injected into the initial Action Tokens, providing an action-ready starting point for Action Expert refinement. At inference, the autoencoder is removed, and the Bridge Tokens are generated only from the current observation and instruction. Experiments on LIBERO, LIBERO-Plus, and CALVIN ABC-D show gains for the evaluated OpenVLA-OFT and VLA-Adapter models. On LIBERO-Plus, PAIR raises VLA-Adapter's success rate from 59.1% to 64.2%. On CALVIN, it increases VLA-Adapter's average completed sequence length from 4.42 to 4.53. Across seven real-world tasks, PAIR raises OpenVLA-OFT's success rate from 51.4% to 65.0%. Representation analyses show that Bridge Tokens retain task information while making continuous-action information accessible before Action Expert refinement. These results support a shared intermediate representation as a useful interface between perception and action in continuous-action VLAs.

</details>

---

### [[20_Research/Papers/强化学习/LASER_Latent_Space_Adjoint_Matching_for_Support-Constrained_Entropy-Regularized_Offline_RL|LASER: Latent Space Adjoint Matching for Support-Constrained Entropy-Regularized Offline RL]]

![[assets/2610.08989_figure.png|800]]

- **arXiv**: [2610.08989](https://arxiv.org/abs/2610.08989)
- **PDF**: https://arxiv.org/pdf/2610.08989
- **详细分析**: [[20_Research/Papers/强化学习/LASER_Latent_Space_Adjoint_Matching_for_Support-Constrained_Entropy-Regularized_Offline_RL|LASER: Latent Space Adjoint Matching for Support-Constrained Entropy-Regularized Offline RL]]
- **作者**: Songyuan Zhang, Oswin So, Eric Yang Yu, Matthew Cleaveland, Peter Crowley-Dolen, Chuchu Fan
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《LASER: Latent Space Adjoint Matching for Support-Constrained Entropy-Regularized Offline RL》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While offline reinforcement learning (RL) enables policy optimization from static datasets without costly online interaction, it remains bottlenecked by the risk of executing out-of-distribution (OOD) actions. Recent approaches mitigate this by learning a behavior-cloning policy through flow matching and then performing RL within its constrained latent space. However, naively optimizing the latent policy can easily cause the policy to collapse into a brittle mode or exploit sharp artifacts of the learned critic. In this work, we find that entropy regularization is essential in latent-space RL for addressing these challenges. We introduce LASER, a novel offline RL algorithm that applies latent-space adjoint matching to achieve entropy-regularized latent-space RL with expressive flow policies while avoiding backpropagation through time. Through comprehensive experiments on 40 challenging OGBench tasks with varying dataset qualities, we show that LASER achieves state-of-the-art performance. Notably, LASER uses fixed method-specific hyperparameters across all tasks and outperforms the evaluated baselines, including those with task- and dataset-specific tuning, which highlights the robust applicability of LASER. Project website: https://mit-realm.github.io/laser/.

</details>

---

### [[20_Research/Papers/大模型/On_KL-Regularized_Policy_Optimization|On KL-Regularized Policy Optimization]]

![[assets/2610.08963_first_page.png|800]]

- **arXiv**: [2610.08963](https://arxiv.org/abs/2610.08963)
- **PDF**: https://arxiv.org/pdf/2610.08963
- **详细分析**: [[20_Research/Papers/大模型/On_KL-Regularized_Policy_Optimization|On KL-Regularized Policy Optimization]]
- **作者**: Yifan Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.87（加权：大模型 0.55，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《On KL-Regularized Policy Optimization》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Asynchronous reinforcement learning (RL) for large language model (LLM) agents trains one policy on trajectories generated by another: rollouts come from stale checkpoints, and the inference engine's probabilities differ from the trainer's even at identical parameters. Standard remedies either clip importance ratios, which biases the update, or, as in GRPO, sample a group of responses per prompt, which is costly when episodes are long. We propose KL-Regularized Policy Optimization (KLPO), a framework that anchors the KL regularizer at the sampler. The regularized improvement step then has a closed-form Gibbs solution, and KLPO fits its log-ratio optimality condition by least squares on the sampler's own trajectories, so the sampler probability enters through a log-ratio and no importance weights are needed. Profiling out the regression intercept replaces the intractable log-partition function with the signal's sampler mean plus a sampler-to-trainer KL divergence. For token-level policy mirror descent targets, we show that the resulting gradient can be computed from terminal returns without a critic, via sampler-centered scores or a single trajectory residual, even under stochastic tool outputs. We further prove that independent Monte Carlo estimates of the KL term keep these gradients unbiased, derive the exact KL gap of cheaper top-$K$ and binary approximations, and show that SPPO, GPO, REBEL, and BPO arise as special cases of KLPO. The result is a critic-free update that uses one rollout per prompt and requires neither a learned normalizer nor a group of responses.

</details>

---

### [[20_Research/Papers/具身智能/Toward_Evidence-Driven_Human-Agent-Robot_Teaming_for_Earth-Independent_Anomaly_Triage|Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage]]

![[assets/2610.08933_figure.png|800]]

- **arXiv**: [2610.08933](https://arxiv.org/abs/2610.08933)
- **PDF**: https://arxiv.org/pdf/2610.08933
- **详细分析**: [[20_Research/Papers/具身智能/Toward_Evidence-Driven_Human-Agent-Robot_Teaming_for_Earth-Independent_Anomaly_Triage|Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage]]
- **作者**: Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.6，大模型 0.4，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independent anomaly triage. Agentic AI is treated as a stateful coordinator over bounded, inspectable services rather than as a fully autonomous vehicle controller. A triage state manager maintains hypotheses, evidence provenance, uncertainty, operational context, and tool status; a crew-facing embodied agent elicits observations and explains assessment changes; and a mobile robot acquires targeted, localized evidence. Typed interfaces separate dialogue and orchestration from monitoring, robot command, context retrieval, and safety-critical control. Two scenarios illustrate the architecture: a crewed deep-space mission based on an actual ISS ammonia false alarm, where suspected contamination restricts crew access, and a power-interface anomaly at a crewed lunar base, where robotic inspection distinguishes a local connector fault from other causes ambiguous in remote telemetry. Our main contribution is an authority-bounded closed evidence-loop architecture, exercised in a hardware-in-the-loop integration prototype using Reachy Mini and an Innate MARS mobile robot.

</details>

---

### [[20_Research/Papers/具身智能/Taming_an_End-to-End_Autonomous_Driving_Policy_for_Urban_Navigation_of_Quadruped_Robots|Taming an End-to-End Autonomous Driving Policy for Urban Navigation of Quadruped Robots]]

![[assets/2610.08812_figure.png|800]]

- **arXiv**: [2610.08812](https://arxiv.org/abs/2610.08812)
- **PDF**: https://arxiv.org/pdf/2610.08812
- **详细分析**: [[20_Research/Papers/具身智能/Taming_an_End-to-End_Autonomous_Driving_Policy_for_Urban_Navigation_of_Quadruped_Robots|Taming an End-to-End Autonomous Driving Policy for Urban Navigation of Quadruped Robots]]
- **作者**: Joochan Kim, Chanuk Yang, Tackgeun You, Ziran Wang, Hwasup Lim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Taming an End-to-End Autonomous Driving Policy for Urban Navigation of Quadruped Robots》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Go2-DrivoR, a goal-conditioned adaptation of the end-to-end autonomous driving trajectory planning framework DrivoR for urban navigation with quadrupedal robots. By conditioning trajectory generation on a local-frame subgoal through a goal token and adapting the vehicle-centric scoring formulation, the method extends DrivoR to short-horizon goal-conditioned local planning without redesigning its core decoders. Specifically, we redefine drivable-area compliance for sidewalk-oriented navigation and reformulate the original ego progress term as goal-conditioned ego progress. Trained exclusively on TartanGround simulation data, Go2-DrivoR improves waypoint-conditioned planning performance on unseen simulation environments and transfers zero-shot to open-loop real-world trajectory prediction.

</details>

---

### [[20_Research/Papers/大模型/OOM-RL_Out-of-Money_Reinforcement_Learning_Market-Driven_Alignment_for_LLM-Based_Multi-Agent_Systems|OOM-RL: Out-of-Money Reinforcement Learning Market-Driven Alignment for LLM-Based Multi-Agent Systems]]

![[assets/2604.11477_figure.png|800]]

- **arXiv**: [2604.11477](https://arxiv.org/abs/2604.11477)
- **PDF**: https://arxiv.org/pdf/2604.11477
- **详细分析**: [[20_Research/Papers/大模型/OOM-RL_Out-of-Money_Reinforcement_Learning_Market-Driven_Alignment_for_LLM-Based_Multi-Agent_Systems|OOM-RL: Out-of-Money Reinforcement Learning Market-Driven Alignment for LLM-Based Multi-Agent Systems]]
- **作者**: Kun Liu, Liqun Chen
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.6（加权：大模型 0.8，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《OOM-RL: Out-of-Money Reinforcement Learning Market-Driven Alignment for LLM-Based Multi-Agent Systems》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OOM-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The alignment of Multi-Agent Systems (MAS) for autonomous software engineering is constrained by evaluator epistemic uncertainty. Current paradigms, such as Reinforcement Learning from Human Feedback (RLHF) and AI Feedback (RLAIF), frequently induce model sycophancy, while execution-based environments suffer from adversarial "Test Evasion" by unconstrained agents. In this paper, we introduce an objective alignment paradigm: Out-of-Money Reinforcement Learning (OOM-RL). By deploying agents into the non-stationary, high-friction reality of live financial markets, we utilize critical capital depletion as an externally imposed negative gradient. Our longitudinal 20-month empirical study chronicles the system's evolution from a high-turnover, sycophantic baseline to a robust, liquidity-aware architecture. We show that the economic consequences of financial loss---real execution costs, slippage, and capital depletion---exposed failure modes not apparent under internal evaluation alone and motivated architectural and governance changes that were later formalized as the Strict Test-Driven Agentic Workflow (STDAW), a Byzantine-inspired uni-directional state lock (RO-Lock) anchored to a deterministically verified &gt;= 95% code coverage constraint matrix. During the final 94-trading-day observation window, the production system exhibited improved execution-aware performance, including an annualized Sharpe ratio of approximately 2.06. These financial results are observational and temporally bounded; they should not be interpreted as evidence of persistent investment alpha or as a causal estimate of STDAW's contribution. The primary contribution of this work is the use of externally imposed economic consequences as an epistemic constraint on agentic development, laying the groundwork for generalized paradigms where real-world resource depletion acts as an objective physical constraint.

</details>

---
