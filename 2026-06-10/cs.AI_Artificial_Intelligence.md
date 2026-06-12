# cs.AI | Artificial Intelligence | 2026-06-10

#arxiv #ComputerScience

**论文数**: 46

### [[20_Research/Papers/强化学习/TRACE_A_Unified_Rollout_Budget_Allocation_Framework_for_Efficient_Agentic_Reinforcement_Learning|TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning]]

![[assets/2606.11119_figure.png|800]]

- **arXiv**: [2606.11119](https://arxiv.org/abs/2606.11119)
- **PDF**: https://arxiv.org/pdf/2606.11119
- **详细分析**: [[20_Research/Papers/强化学习/TRACE_A_Unified_Rollout_Budget_Allocation_Framework_for_Efficient_Agentic_Reinforcement_Learning|TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning]]
- **作者**: Heming Zou, Qi Wang, Yun Qu, Yuhang Jiang, Lizhou Cai, Yixiu Mao, Ru Peng, Xin Xu, Weijie Liu, Kai Yang, Saiyong Yang, Xiangyang Ji
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) is a promising approach for enhancing reasoning and agentic behavior in large language models. However, rollout-intensive policy optimization is often limited by insufficient reward contrast, arising when overly simple or complex prompts generate low-variance feedback and when outcome-only rewards assign the same terminal assessment to every decision in a multi-turn rollout. Past efforts have focused on allocating available rollout resources to promising prompts, yet they only leverage sample informativeness at the prompt level and neglect variation in prefix-level informativeness across turns within the same rollout. This work targets multi-turn agentic RL by modeling each ReAct-style thought-action-observation turn as a semantically distinct node, allowing budget allocation to extend from prompt roots to turn-level prefixes with further continuations, which naturally forms tree-structured rollouts. We introduce Tree Rollout Allocation for Contrastive Exploration (TRACE), a unified rollout allocation framework that enhances reward contrast within a fixed sampling budget. Technically, TRACE allocates rollout budget to both prompt roots and intermediate prefixes that are most likely to yield mixed terminal rewards. A shared generalizable predictor estimates conditional success probability at these anchors from prefix histories to guide this allocation. The resulting adaptive tree structure enriches outcome-only feedback and amplifies the policy-update signal. Empirically, TRACE achieves competitive performance and efficiency gains on typical agentic benchmarks, e.g., improving Qwen3-14B Multi-Hop QA average accuracy by 2.8 points over competitive baselines at equal sampling cost.

</details>

---

### [[20_Research/Papers/具身智能/RoboNaldo_Accurate,_Stable_and_Powerful_Humanoid_Soccer_Shooting_via_Motion-Guided_Curriculum_Reinforcement_Learning|RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning]]

![[assets/2606.11092_figure.png|800]]

- **arXiv**: [2606.11092](https://arxiv.org/abs/2606.11092)
- **PDF**: https://arxiv.org/pdf/2606.11092
- **详细分析**: [[20_Research/Papers/具身智能/RoboNaldo_Accurate,_Stable_and_Powerful_Humanoid_Soccer_Shooting_via_Motion-Guided_Curriculum_Reinforcement_Learning|RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning]]
- **作者**: Yichao Zhong, Yidan Lu, Yuhang Lu, Tianyang Tang, Haoguang Mai, Yixuan Pan, Tianyu Li, Li Chen, Jingbo Wang, Zhongyu Li, Peng Lu, Hongyang Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.7（加权：具身智能 1.8，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RSL-RL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven RL struggles to explore and discover valid kicks from scratch. We therefore introduce RoboNaldo, a three-stage motion-guided curriculum RL framework for high-impulse humanoid interaction. A single human-kick reference is used as a scaffold and progressively shifts optimization towards shooting performance. The curriculum first learns a stable whole-body kicking prior, then adapts the kick to free-kick settings where the ball is stationary at random positions, and finally extends it to moving-ball shooting through a locomotion-command and kick-trigger interface. A high-level heuristic planner controls this interface during training, while alternative high-level controllers can drive the same low-level policy at inference. In simulation, RoboNaldo demonstrates free-kick shot error 48.6% lower and shoot velocity 2.96x than prior work baselines. In real world on a Unitree G1 with onboard perception, RoboNaldo attains 0.73 m and 0.86 m average target shooting error from 3 m away in free-kick and moving-ball cases, accordingly. And the post-contact ball velocity reaches 13.10 m/s, which is 59-71% of reported professional open-play shot speed. Project page: $\href{https://opendrivelab.com/RoboNaldo}{\text{opendrivelab.com/RoboNaldo}}$.

</details>

---

### [[20_Research/Papers/强化学习/Test-Time_Gradient_Guidance_of_Flow_Policies_in_Reinforcement_Learning|Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning]]

![[assets/2606.11087_figure.png|800]]

- **arXiv**: [2606.11087](https://arxiv.org/abs/2606.11087)
- **PDF**: https://arxiv.org/pdf/2606.11087
- **详细分析**: [[20_Research/Papers/强化学习/Test-Time_Gradient_Guidance_of_Flow_Policies_in_Reinforcement_Learning|Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning]]
- **作者**: Zhiyuan Zhou, Andy Peng, Charles Xu, Qiyang Li, Tobias Springenberg, Kevin Frans, Sergey Levine
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.56，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Test-Time Gradient Guidance of Flow Policies in Reinforcement Learning》归入 强化学习、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CFGRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Expressive continuous control policies, such as diffusion and flow models, form the backbone of recent advances in scaling imitation learning for simulated and real robot control. While they are known to scale stably in the supervised imitation learning setting, incorporating them into reinforcement learning (RL) pipelines for policy improvement has proven more difficult. It often requires specialized training objectives or backpropagating through denoising processes, which cause well-known issues with stability and affect scalability. In this paper we study the question of whether simple policy improvement schemes at test time alone, leaving stable supervised policy training intact, can be a competitive alternative which sidesteps these issues. To this end, we propose QGF (Q-Guided Flow), an RL algorithm that performs policy optimization entirely at test time. QGF works by pre-training both a reference flow policy (via a standard behavioral cloning objective) and a value function critic and, at test time, using the value gradient to guide the reference policy to generate higher-value actions without any additional policy learning. Empirically, QGF outperforms prior test-time RL methods on single-task and goal-conditioned offline RL benchmarks with high-dimensional action spaces, and is competitive with state-of-the-art training-time algorithms while being much cheaper to run. Moreover, it exhibits favorable scaling with model size by avoiding the instability of actor-critic training, offering a practical and effective alternative RL algorithm with expressive policies.

</details>

---

### [[20_Research/Papers/大模型/Null-Space_Constrained_Low-Rank_Adaptation_for_Response-Specified_Large_Language_Model_Unlearning|Null-Space Constrained Low-Rank Adaptation for Response-Specified Large Language Model Unlearning]]

![[assets/2606.10989_figure.png|800]]

- **arXiv**: [2606.10989](https://arxiv.org/abs/2606.10989)
- **PDF**: https://arxiv.org/pdf/2606.10989
- **详细分析**: [[20_Research/Papers/大模型/Null-Space_Constrained_Low-Rank_Adaptation_for_Response-Specified_Large_Language_Model_Unlearning|Null-Space Constrained Low-Rank Adaptation for Response-Specified Large Language Model Unlearning]]
- **作者**: Bocheng Ju, Jianhua Wang, Chengliang Liu, Xiaolin Chang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM

#### 研究背景与动机

《Null-Space Constrained Low-Rank Adaptation for Response-Specified Large Language Model Unlearning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model unlearning aims to suppress designated undesirable knowledge while preserving benign capabilities. Many unlearning objectives focus on suppressing undesired answers, while recent target-guided variants specify replacement behavior but still leave update locality largely unconstrained. This paper introduces \emph{Null-Space Constrained Response-Specified Unlearning} (NSRU), a projection-constrained low-rank framework for controlled LLM unlearning. NSRU uses an explicitly structured safe target response to specify the desired behavior for each forget query, while suppressing the original undesired content. To localize adaptation, NSRU estimates per-module retain subspaces from benign hidden representations and uses an orthogonal-projected low-rank parameterization to confine LoRA updates to the null space of the retain subspace. The resulting objective jointly optimizes safe-target learning, undesired-response suppression, and retention preservation under this constrained parameterization. We provide a local first-order analysis showing that the projected update reduces retain-side perturbations while preserving editable directions for shaping forget-query behavior. Experiments on TOFU show that NSRU effectively suppresses extractable forget-set knowledge while improving retain QA performance, model utility, and safe-target alignment over representative baselines. On WMDP, NSRU keeps hazardous-domain accuracy near the random-choice region while preserving broad and domain-adjacent MMLU utility. Ablation studies support the complementary roles of safe-target supervision, undesired-response suppression, retention loss, and null-space projected updates, while sensitivity and robustness analyses indicate stable behavior across the tested hyperparameter and prompt variations.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Uniform_Token-Level_Trust_Region_in_LLM_Reinforcement_Learning|Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning]]

![[assets/2606.10968_figure.png|800]]

- **arXiv**: [2606.10968](https://arxiv.org/abs/2606.10968)
- **PDF**: https://arxiv.org/pdf/2606.10968
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Uniform_Token-Level_Trust_Region_in_LLM_Reinforcement_Learning|Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning]]
- **作者**: Renjie Mao, Xiangxin Zhou, Lvfang Tao, Yixin Ding, Yu Shi, Yongguang Lin, Yuheng Wu, Honglin Zhu, Qian Qiu, Wenxi Zhu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Beyond Uniform Token-Level Trust Region in LLM Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has become standard for improving LLM reasoning. However, existing PPO-style trust-region mechanisms remain position-agnostic by enforcing uniform thresholds across all tokens independently. This pointwise treatment conflicts with autoregressive generation in two critical ways. First, uniform thresholds ignore autoregressive asymmetry. Early-stage deviations produce compounding sequence-level drift, causing static thresholds to under-regulate early divergence and excessively constrain late-stage exploration. Second, evaluating token-level divergence in isolation overlooks cumulative prefix drift, granting the same divergence allowance regardless of how far the conditioning history has already deviated from the rollout policy. To address this limitation, we propose CPPO (Cumulative Prefix-divergence Policy Optimization), a token-level masking rule that aligns updates with a finite-horizon policy-improvement bound via two coupled mechanisms. First, a position-weighted threshold imposes stricter limits at early positions whose effects persist longer, relaxing constraints for late-stage tokens. Second, a cumulative prefix budget tracks historical deviations, dynamically restricting further token-level deviation to prevent compounding errors along the prefix. Empirically, CPPO enhances training stability and significantly improves reasoning accuracy across various model scales.

</details>

---

### [[20_Research/Papers/大模型/Role-Agent_Bootstrapping_LLM_Agents_via_Dual-Role_Evolution|Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution]]

![[assets/2606.10917_figure.png|800]]

- **arXiv**: [2606.10917](https://arxiv.org/abs/2606.10917)
- **PDF**: https://arxiv.org/pdf/2606.10917
- **详细分析**: [[20_Research/Papers/大模型/Role-Agent_Bootstrapping_LLM_Agents_via_Dual-Role_Evolution|Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution]]
- **作者**: Xucong Wang, Ziyu Ma, Shidong Yang, Tongwen Huang, Pengkun Wang, Yong Wang, Xiangxiang Chu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, ARL, Agent-In-World, Search-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although Large Language Model (LLM) agents have demonstrated strong performance on complex tasks, their learning is often limited by inefficient interaction feedback and static training environments, which hinder broader generalization. To address these limitations, this paper introduces Role-Agent, \textcolor{black}{a framework} that harnesses a single LLM to function concurrently as both the agent and the environment, enabling a bootstrapped co-evolution. Role-Agent comprises two synergistic components: World-In-Agent (WIA) and Agent-In-World (AIW). In WIA, the LLM acts as the agent and predicts future states after each action; the alignment between predicted and actual states is then used as a process reward, encouraging environment-aware reasoning. In AIW, the LLM analyzes failure modes from failed trajectories and retrieves tasks with similar failure patterns, thereby reshaping the training data distribution for targeted practice. Experiments on multiple benchmarks show that Role-Agent consistently improves performance, yielding an average gain of over 4\% over strong baselines.

</details>

---

### [[20_Research/Papers/具身智能/LIBERO-Occ_Evaluating_and_Improving_Vision-Language-Action_Models_under_Scene-Induced_Occlusion_via_Viewpoint_Imagination|LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination]]

![[assets/2606.10862_figure.png|800]]

- **arXiv**: [2606.10862](https://arxiv.org/abs/2606.10862)
- **PDF**: https://arxiv.org/pdf/2606.10862
- **详细分析**: [[20_Research/Papers/具身智能/LIBERO-Occ_Evaluating_and_Improving_Vision-Language-Action_Models_under_Scene-Induced_Occlusion_via_Viewpoint_Imagination|LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination]]
- **作者**: Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models achieve strong performance on standard manipulation benchmarks, but most evaluations assume that task-relevant objects are fully visible. This assumption often fails in realistic settings, where occlusion makes manipulation partially observable. In this paper, we study \textit{scene-induced occlusion} as a fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-oriented extension of LIBERO. Experiments show that state-of-the-art VLAs suffer substantial performance degradation under occlusion. To address this issue, we propose \textbf{Viewpoint Imagination (VIM)}, which generates a complementary view from an occluded primary observation and conditions action prediction on both observed and imagined evidence. VIM improves robustness across task suites, occlusion types, and severity levels without requiring additional cameras at deployment time, suggesting that viewpoint imagination is an promising mechanism for perception completion in partially observable manipulation. Our benchmark and corresponding code are available at: \href{https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ}.

</details>

---

### [[20_Research/Papers/强化学习/Geometrically_Averaged_Hard_Target_Updates_for_Linear_Q-Learning|Geometrically Averaged Hard Target Updates for Linear Q-Learning]]

![[assets/2606.10835_first_page.png|800]]

- **arXiv**: [2606.10835](https://arxiv.org/abs/2606.10835)
- **PDF**: https://arxiv.org/pdf/2606.10835
- **详细分析**: [[20_Research/Papers/强化学习/Geometrically_Averaged_Hard_Target_Updates_for_Linear_Q-Learning|Geometrically Averaged Hard Target Updates for Linear Q-Learning]]
- **作者**: Donghwan Lee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Geometrically Averaged Hard Target Updates for Linear Q-Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Periodic hard target updates are among the most common stabilization devices in modern deep Q-learning. Recent studies suggest that target updates can improve stability in Q-learning with function approximation, including linear function approximation. We introduce and analyze the so-called $λ$-target update, obtained by averaging the $m$-periodic target update maps with $λ$-geometric weights $(1-λ)λ^{m-1}$, $λ\in [0,1]$. The endpoint $λ=0$ recovers the one-period target update, while the continuous endpoint $λ\uparrow1$ recovers projected Q-value iteration. We study this mechanism for Q-learning with linear function approximation, namely linear Q-learning, using a switching-system model and related tools. For clarity, the paper treats a deterministic version; the formulation extends to stochastic reinforcement-learning settings.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_APIs_Probing_the_Limits_of_MLLMs_in_Physical_Tool_Use|Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use]]

![[assets/2606.10803_figure.png|800]]

- **arXiv**: [2606.10803](https://arxiv.org/abs/2606.10803)
- **PDF**: https://arxiv.org/pdf/2606.10803
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_APIs_Probing_the_Limits_of_MLLMs_in_Physical_Tool_Use|Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use]]
- **作者**: Zhixin Ma, Yutong Zhou, Yongqi Li, Chong-Wah Ngo, Wenjie Li
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.85（加权：具身智能 0.6，大模型 0.25）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PhysTool-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and increasingly serve as the "brain" of embodied AI, instructing robots to interact with the physical world. In such embodied settings, a central capability is the use of physical tools, which underpins MLLMs' ability to assist humans in real-world tasks. Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios, identify physical tools, and plan their use. PhysTool-Bench comprises 2,510 queries over 2,678 real-world physical tools spanning diverse domains, including manufacturing, electrical work, agriculture, and healthcare. Concretely, models are evaluated along two primary dimensions: 1) recognizing all physical tools present in the scene, and 2) planning the tool selection and use sequence based on the instruction and visual context. Across 13 leading MLLMs, even the strongest model (Gemini-3.1-Pro) identifies only 58.7% of tools in a scene and completes merely 21.0% of queries end-to-end. Our analysis reveals a two-level deficit: MLLMs struggle to perceive tools in realistic scenes, and the much larger drop at the planning stage further indicates a lack of functional commonsense for mapping perceived tools onto task semantics, pinpointing a critical bottleneck for the development of practical embodied AI.

</details>

---

### [[20_Research/Papers/大模型/Toward_Secure_LLM_Agents_Threat_Surfaces,_Attacks,_Defenses,_and_Evaluation|Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation]]

![[assets/2606.10749_figure.png|800]]

- **arXiv**: [2606.10749](https://arxiv.org/abs/2606.10749)
- **PDF**: https://arxiv.org/pdf/2606.10749
- **详细分析**: [[20_Research/Papers/大模型/Toward_Secure_LLM_Agents_Threat_Surfaces,_Attacks,_Defenses,_and_Evaluation|Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation]]
- **作者**: Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are rapidly moving from conversational interfaces to software components that plan, invoke tools, maintain memory, and act on external environments. This transition changes the nature of security risk. In agentic settings, failures are no longer limited to unsafe text generation. Untrusted content may redirect control flow, misuse tool privileges, corrupt persistent state, leak sensitive information, or trigger harmful external actions. At the same time, research on LLM agent security is expanding quickly but remains fragmented across attack families, defense layers, application domains, and evaluation settings. This paper synthesizes 247 papers through a lifecycle-based, systems-oriented framework that models agent security around the interaction of information flow, delegated authority, and persistent state. We organize the literature around four questions: how LLM agent security should be modeled, which threat surfaces and attack families dominate, what defenses have been proposed and with what tradeoffs, and how security claims are evaluated. We find that prompt injection and tool-mediated control-flow hijacking still dominate the field, while persistent state corruption and multi-agent propagation are becoming central emerging concerns. We further find that current defenses provide useful building blocks but remain weakly compositional, and that existing benchmarks still underrepresent long-horizon, stateful, and deployment-sensitive risks. We argue that secure LLM agents require explicit trust boundaries, principled privilege control, provenance-aware state management, and evaluation practices aligned with realistic operational settings.

</details>

---

### [[20_Research/Papers/强化学习/Event-Driven_Reinforcement_Learning_Enables_Long-Horizon_Control_in_Semiconductor_Fabrication|Event-Driven Reinforcement Learning Enables Long-Horizon Control in Semiconductor Fabrication]]

![[assets/2606.10705_first_page.png|800]]

- **arXiv**: [2606.10705](https://arxiv.org/abs/2606.10705)
- **PDF**: https://arxiv.org/pdf/2606.10705
- **详细分析**: [[20_Research/Papers/强化学习/Event-Driven_Reinforcement_Learning_Enables_Long-Horizon_Control_in_Semiconductor_Fabrication|Event-Driven Reinforcement Learning Enables Long-Horizon Control in Semiconductor Fabrication]]
- **作者**: Yavar Yeganeh, Mahsa Shekari, Nicla Frigerio, Daniele Pagano, Andrea Matta
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.2，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Event-Driven Reinforcement Learning Enables Long-Horizon Control in Semiconductor Fabrication》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning promises to optimize sequential decisions in large-scale systems. Semiconductor manufacturing systems are stochastic and highly constrained environments where heterogeneous wafers traverse hundreds of processing steps across extensive equipment networks. These characteristics yield complex, high-dimensional decision problems with delayed feedback and long-horizon requirements, complicating production planning and control. We propose a deep reinforcement learning framework for multi-objective policy optimization at this scale. Specifically, we formulate control as a centralized-agent problem, where a core policy coordinates system-wide decisions, while system evolution is represented as an interconnected temporal process driven by discrete events. Accordingly, we develop a tailored event-driven temporal-difference formulation that remains general and can be integrated with various policy optimization methods under relevant training settings. We investigate several core model-free algorithms incorporated into this framework and evaluate their effectiveness using high-fidelity simulations of diverse, industry-real operating scenarios. Across extensive validation experiments, agents trained in both offline and online settings show significant and consistent gains in throughput and utilization. We further evaluate performance and generalization across training phases, clarifying the relative strengths of alternative reinforcement learning formulations and algorithms. Overall, the results support the scalability, generality, and transferability of the proposed framework for controlling event-driven complex adaptive systems.

</details>

---

### [[20_Research/Papers/机器人/UniDexTok_A_Unified_Dexterous_Hand_Tokenizer_from_Real_Data|UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data]]

![[assets/2606.10683_figure.png|800]]

- **arXiv**: [2606.10683](https://arxiv.org/abs/2606.10683)
- **PDF**: https://arxiv.org/pdf/2606.10683
- **详细分析**: [[20_Research/Papers/机器人/UniDexTok_A_Unified_Dexterous_Hand_Tokenizer_from_Real_Data|UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data]]
- **作者**: Dong Fang, Youjun Wu, Yuanxin Zhong, Rui Zhang, Yunlong Wang, Xiaosong Jia, Yu-Gang Jiang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DexGraspNet, LinkerHand-Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous hands are essential for fine-grained manipulation, but their hardware designs vary substantially across embodiments. Differences in kinematics, joint definitions, and degrees of freedom make it difficult to define a shared state representation compared with parallel grippers. As a result, dexterous-hand data remains fragmented and difficult to use for joint training. In this work, we propose the Unified Dexterous Hand Model (UDHM), which maps human and robot hand states into a shared 22-DoF semantic interface. Based on UDHM, we introduce UniDexTok, a retargeting-free state tokenizer that learns embodiment-conditioned discrete tokens from standardized real joint states. UniDexTok provides a unified representation for heterogeneous dexterous hands without relying on retargeting or simulation data. Compared with the recent baseline UniHM, UniDexTok reduces MPJAE from 15.63 degrees to 0.16 degrees and MPJPE from 18.51 mm to 0.18 mm, corresponding to error reductions of 98.98% and 99.03%, respectively. These results improve reconstruction from centimeter-scale to sub-millimeter accuracy. Experiments further show that data from other embodiments improves target-embodiment reconstruction accuracy, demonstrating the benefit of cross-embodiment tokenization. UniDexTok also shows strong zero-shot and few-shot reconstruction ability when new dexterous hands are introduced.

</details>

---

### [[20_Research/Papers/大模型/Infini_Memory_Maintainable_Topic_Documents_for_Long-Term_LLM_Agent_Memory|Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory]]

![[assets/2606.10677_figure.png|800]]

- **arXiv**: [2606.10677](https://arxiv.org/abs/2606.10677)
- **PDF**: https://arxiv.org/pdf/2606.10677
- **详细分析**: [[20_Research/Papers/大模型/Infini_Memory_Maintainable_Topic_Documents_for_Long-Term_LLM_Agent_Memory|Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory]]
- **作者**: Suozhao Ji, Baodong Wu, Zehao Wang, Lei Xia, Qingping Li, Ruisong Wang, Wenbo Ding, Zhenhua Zhu, Boxun Li, Guohao Dai, Yu Wang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

</details>

---

### [[20_Research/Papers/强化学习/Fast_and_Highly_Expressive_Policy_Learning_for_Offline_Reinforcement_Learning_via_Bootstrapped_Flow_Q-Learning|Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning]]

![[assets/2606.10613_figure.png|800]]

- **arXiv**: [2606.10613](https://arxiv.org/abs/2606.10613)
- **PDF**: https://arxiv.org/pdf/2606.10613
- **详细分析**: [[20_Research/Papers/强化学习/Fast_and_Highly_Expressive_Policy_Learning_for_Offline_Reinforcement_Learning_via_Bootstrapped_Flow_Q-Learning|Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning]]
- **作者**: Thanh Nguyen, Tri Ton, Hongbin Choe, Tung M. Luu, Chang D. Yoo
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Fast and Highly Expressive Policy Learning for Offline Reinforcement Learning via Bootstrapped Flow Q-Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based Q-learning has emerged as a powerful paradigm for offline reinforcement learning, but its reliance on multi-step denoising makes both training and inference computationally expensive and brittle. Recent efforts to accelerate diffusion Q-learning toward single-step action generation typically introduce auxiliary networks, policy distillation, or multi-phase training, which frequently compromise simplicity, stability, or performance. To address these limitations, we introduce Bootstrapped Flow Q-Learning (BFQ), a novel framework that enables accurate single-step action generation during both training and inference, without auxiliary networks or distillation procedures. BFQ adopts a divide-and-conquer view of the displacement vector along the flow path: it begins by learning short-range displacements that can be accurately estimated from the Flow Matching marginal velocity, and bootstraps these components to directly learn a noise-to-action mapping in a single step. This formulation eliminates multi-step denoising, resulting in a learning procedure that is substantially faster, simpler, and more robust. Extensive D4RL evaluations show that BFQ improves performance while significantly reducing computational cost compared to multi-step diffusion baselines, demonstrating that single-step action generation suffices for high-performance offline Reinforcement Learning.

</details>

---

### [[20_Research/Papers/大模型/Causal_Ensemble_Agent_Hierarchical_Causal_Discovery_with_LLM-guided_Expert_Reweighting|Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting]]

![[assets/2606.10607_figure.png|800]]

- **arXiv**: [2606.10607](https://arxiv.org/abs/2606.10607)
- **PDF**: https://arxiv.org/pdf/2606.10607
- **详细分析**: [[20_Research/Papers/大模型/Causal_Ensemble_Agent_Hierarchical_Causal_Discovery_with_LLM-guided_Expert_Reweighting|Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting]]
- **作者**: Xinyu Li, Yuanyuan Wang, Haoxuan Li, Chuan Zhou, Erdun Gao, Bo Han, Tongliang Liu, Kun Zhang, Howard Bondell, Mingming Gong
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Causal Ensemble Agent: Hierarchical Causal Discovery with LLM-guided Expert Reweighting》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Causal discovery aims to uncover causal structures from observational data, which is crucial for real-world decision-making. However, different causal discovery algorithms can produce divergent results that conflict with each other, complicating the identification of accurate causal graphs. Traditional approaches rely on numerical values and statistical assumptions, often ignoring rich domain-specific information, such as feature descriptions, which could also help structure learning. While recent works explore using Large Language Models (LLMs) to infer causal relations via direct queries, such methods can be unreliable due to a lack of alignment with the actual data. To address these limitations, we propose Causal Ensemble Agent (CEA), a novel framework that aggregates structural insights from statistical discovery experts across different graph levels via linear opinion pooling, and uses an LLM as a meta-referee to dynamically reweight experts when the aggregated confidence is close to the decision boundary, thereby composing an improved and more complete causal graph. Extensive experiments on both synthetic and real-world datasets demonstrate that CEA achieves the strongest overall performance across a wide range of causal discovery methods, highlighting the effectiveness of using LLMs for meta-analysis in causal discovery.

</details>

---

### [[20_Research/Papers/强化学习/Dmsh_A_Multi-Agent_Reinforcement_Learning_Framework_for_All-Quad_Mesh_Generation|Dmsh: A Multi-Agent Reinforcement Learning Framework for All-Quad Mesh Generation]]

![[assets/2606.10601_figure.png|800]]

- **arXiv**: [2606.10601](https://arxiv.org/abs/2606.10601)
- **PDF**: https://arxiv.org/pdf/2606.10601
- **详细分析**: [[20_Research/Papers/强化学习/Dmsh_A_Multi-Agent_Reinforcement_Learning_Framework_for_All-Quad_Mesh_Generation|Dmsh: A Multi-Agent Reinforcement Learning Framework for All-Quad Mesh Generation]]
- **作者**: Anirudh Kalyan, Cosmin Anitescu, Xiaoying Zhuang, Timon Rabczuk, Somdatta Goswami, Sundararajan Natarajan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Dmsh: A Multi-Agent Reinforcement Learning Framework for All-Quad Mesh Generation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MeshingNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating high-quality meshes for arbitrary geometries remains a fundamental bottleneck in computational engineering, often demanding heuristic tuning and semi-manual workflows. In this paper, we introduce Dmsh, a first fully automated reinforcement learning pipeline that unifies geometric decomposition and quadrilateral mesh generation within a single learning-based framework. Dmsh decomposes the problem through three coordinated agents handling topology simplification, geometric regularization, and mesh generation. The meshing process is formulated as a Markov Decision Process and solved using a parametric Soft Actor-Critic architecture with decoupled critics, enabling efficient exploration of a hybrid discrete-continuous action space. A curriculum learning strategy ensures scalability from simple domains to highly complex geometries, suppressing seed variance. By design, the recursive decomposition enables parallel meshing of subregions, yielding globally conforming all-quadrilateral meshes without post hoc correction. Across a wide range of benchmarks, Dmsh consistently outperforms existing methods in automation, robustness, and mesh quality, establishing a new paradigm for learning-based mesh generation.

</details>

---

### [[20_Research/Papers/大模型/HIPIF_Hierarchical_Planning_and_Information_Folding_for_Long-Horizon_LLM_Agent_Learning|HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning]]

![[assets/2606.10507_figure.png|800]]

- **arXiv**: [2606.10507](https://arxiv.org/abs/2606.10507)
- **PDF**: https://arxiv.org/pdf/2606.10507
- **详细分析**: [[20_Research/Papers/大模型/HIPIF_Hierarchical_Planning_and_Information_Folding_for_Long-Horizon_LLM_Agent_Learning|HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning]]
- **作者**: Juncheng Diao, Zhicong Lu, Peiguang Li, Yongwei Zhou, Changyuan Tian, Qingbin Li, Rongxiang Weng, Jingang Wang, Xunliang Cai
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.1（加权：大模型 0.9，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, STEP-HRL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Models (LLMs) have demonstrated strong capabilities as autonomous agents across a wide range of tasks, their performance often degrades in multi-turn long-horizon agentic tasks. Existing methods have made progress through fine-grained credit assignment to alleviate long-horizon sparse rewards and hierarchical reinforcement learning to decompose tasks and reduce long-term dependency. However, these methods still do not directly address long-context interference, in which continuously growing histories weaken the agent's ability to track the global task state and impair subsequent reasoning and decision-making. Inspired by the way humans handle complex tasks through subgoal decomposition and completed progress summarization, we propose Hierarchical Planning and Information Folding (HIPIF) for long-horizon LLM agent learning. HIPIF trains the agent end-to-end to organize long-horizon execution around explicit subgoals while folding completed subgoal histories to reduce long-context interference. Furthermore, to stabilize subgoal-based planning and execution, HIPIF combines hierarchical reflection and subgoal-oriented process rewards to guide subgoal generation, transition, and execution, without relying on costly auxiliary models or task-specific expert trajectories. Extensive experiments on three publicly available agentic benchmarks demonstrate the validity of our method.

</details>

---

### [[20_Research/Papers/大模型/Decoupling_Thought_from_Speech_Knowledge-Grounded_Counterfactual_Reasoning_for_Resilient_Multi-Agent_Argumentation|Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent Argumentation]]

![[assets/2606.10475_figure.png|800]]

- **arXiv**: [2606.10475](https://arxiv.org/abs/2606.10475)
- **PDF**: https://arxiv.org/pdf/2606.10475
- **详细分析**: [[20_Research/Papers/大模型/Decoupling_Thought_from_Speech_Knowledge-Grounded_Counterfactual_Reasoning_for_Resilient_Multi-Agent_Argumentation|Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent Argumentation]]
- **作者**: Jakub Masłowski, Jarosław A. Chudziak
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent Argumentation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent debate frameworks have been shown to improve large language model performance in convergent tasks, but they are currently optimized in a way that heavily favors final output accuracy rather than stability of the process. During long-horizon exchanges reactive systems under sustained perturbations often experience logic degradation, argument repetition, and role drift. To structurally prevent the identity loss and maintain the process fidelity, we introduce Knowledge-Grounded Counterfactual Reasoning (KG-CFR), a dual-stage architecture that enforces a strict separation of concerns between a private, retrieval-augmented planning buffer, and a public execution layer. We assess this system in Dynamic Resource Allocation under Uncertainty (DRAU), a dedicated 1v1v1 environment, introducing diversity as distinct from standard debate settings. Over 270 completely factorial crisis simulation trajectories with stochastic environmental shocks, KG-CFR prevents judge-detected critical post-shock degradation (defined as a quality shift, $Δ\le -0.20$) in more than 95% of perturbed runs, increasing the overall argument quality from 0.694 to 0.822. Our primary contribution is the demonstration of architectural decoupling being an important factor of systemic resilience enhancement under sustained pressure without quality loss. Furthermore, we introduce custom vector metrics for discourse divergence and plan-execution alignment that provide strong, directionally consistent evidence of operational stability. Our ablation experiments suggest that the proper doctrinal grounding can be an equally important factor for argument quality, as the prospective planning. KG-CFR, according to our initial metric evaluations, reduces semantic looping, by preserving the agent's consistency with the original plan.

</details>

---

### [[20_Research/Papers/强化学习/Mitigating_Bias_in_Low-SNR_Financial_Reinforcement_Learning_via_Quantum_Representations|Mitigating Bias in Low-SNR Financial Reinforcement Learning via Quantum Representations]]

![[assets/2606.10448_figure.png|800]]

- **arXiv**: [2606.10448](https://arxiv.org/abs/2606.10448)
- **PDF**: https://arxiv.org/pdf/2606.10448
- **详细分析**: [[20_Research/Papers/强化学习/Mitigating_Bias_in_Low-SNR_Financial_Reinforcement_Learning_via_Quantum_Representations|Mitigating Bias in Low-SNR Financial Reinforcement Learning via Quantum Representations]]
- **作者**: Zeyu Liu, Xuanzhi Feng, Sing Kwong Lai, Yuanchen Gao, Xiaoyi Pang, Hualei Zhang, Jingcai Guo, Jie Zhang, Song Guo
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Mitigating Bias in Low-SNR Financial Reinforcement Learning via Quantum Representations》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, FinRL, Pre-Net, QRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The financial market is a typical low signal-to-noise ratio (SNR) setting, which often destabilizes off-policy maximum-entropy methods like Soft Actor-Critic (SAC). Specifically, noisy state representations may produce unreliable Q-value estimates, and bootstrapping amplifies these errors, forming a failure mode we call the "Financial Entropy Trap". In this paper, we propose FPQC-SAC, an efficient and plug-and-play SAC variant that places a compact and bounded Parameterized Quantum Circuit (PQC) before the actor and critic networks to constrain feature propagation at the representation level, rather than filtering raw inputs or regularizing Q-values after bootstrapping. Notably, FPQC-SAC reduces the impact of extreme market fluctuations on Bellman target estimation, while trainable quantum entanglement preserves flexible cross-asset interactions. Empirical evaluations on real-world portfolio management tasks demonstrate that FPQC-SAC substantially enhances out-of-sample stability and cumulative returns by achieving a 66.89% relative gain in cumulative return over standard unconstrained SAC and outperforms the best continuous-control deep reinforcement learning baseline by approximately 27%. Open-source code is available at https://github.com/ZeyuLIU-UST/FPQC-SAC-main.

</details>

---

### [[20_Research/Papers/大模型/Agentic_Hybrid_RAG_for_Evidence-Grounded_Muon_Collider_Analysis|Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis]]

![[assets/2606.10381_figure.png|800]]

- **arXiv**: [2606.10381](https://arxiv.org/abs/2606.10381)
- **PDF**: https://arxiv.org/pdf/2606.10381
- **详细分析**: [[20_Research/Papers/大模型/Agentic_Hybrid_RAG_for_Evidence-Grounded_Muon_Collider_Analysis|Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis]]
- **作者**: Ruobing Jiang, Dawei Fu, Cheng Jiang, Tianyi Yang, Zijian Wang, Youpeng Wu, Yong Ban, Yajun Mao, Qiang Li
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Agentic Hybrid RAG for Evidence-Grounded Muon Collider Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Muon collider research spans accelerator physics, detector instrumentation, and high-energy phenomenology, with relevant evidence scattered across a rapidly expanding and heterogeneous body of scientific literature. As high-energy physics (HEP) increasingly explores agent-assisted analysis workflows, efficiently locating, integrating, and verifying scientific evidence becomes an essential capability. While retrieval-augmented generation (RAG) offers a promising framework for scientific question answering, integrating agentic reasoning without compromising retrieval precision remains a key challenge. In this work, we present agentic hybrid RAG, an evidence-grounded RAG framework for muon collider research. The framework combines a hybrid retriever, integrating sparse lexical and dense semantic retrieval, with an agentic reasoning module for query decomposition, evidence expansion, and grounded answer generation. To enable systematic evaluation, we construct the first benchmark for retrieval-augmented scientific question answering in the muon collider domain, comprising a curated literature corpus together with dedicated retrieval and answer-generation benchmarks covering major detector and physics research topics. Extensive evaluation shows that hybrid retrieval provides the strongest retrieval backbone, while agentic reasoning is most effective for controlled evidence expansion and answer synthesis. Built on this principle, agentic hybrid RAG consistently outperforms representative retrieval and RAG baselines in retrieval effectiveness, answer quality, evidence coverage, and factual grounding. Together, the benchmark and framework provide a foundation for evidence-grounded scientific question answering and future HEP analysis agents operating over large-scale scientific literature.

</details>

---

### [[20_Research/Papers/具身智能/Test-time_Adversarial_Takeover_A_Real-time_Hijacking_Interface_against_Robotic_Diffusion_Policies|Test-time Adversarial Takeover: A Real-time Hijacking Interface against Robotic Diffusion Policies]]

![[assets/2606.10371_figure.png|800]]

- **arXiv**: [2606.10371](https://arxiv.org/abs/2606.10371)
- **PDF**: https://arxiv.org/pdf/2606.10371
- **详细分析**: [[20_Research/Papers/具身智能/Test-time_Adversarial_Takeover_A_Real-time_Hijacking_Interface_against_Robotic_Diffusion_Policies|Test-time Adversarial Takeover: A Real-time Hijacking Interface against Robotic Diffusion Policies]]
- **作者**: Zi Yin, Peilin Chai, Siyuan Huang, Zhanhao Hu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Test-time Adversarial Takeover: A Real-time Hijacking Interface against Robotic Diffusion Policies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EfficientNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based action generation has become a foundational component of embodied AI, but its reliance on visual conditioning leaves deployed visuomotor policies vulnerable to adversarial manipulation. Most prior attacks focus on disruption: they perturb the observation stream to reduce task success or induce erratic behavior. We study a stronger threat, Test-time Adversarial Takeover (TAKO), in which an attacker obtains a real-time steering interface over a frozen robot policy and turns it into a remotely piloted instrument. TAKO learns a small vocabulary of reusable universal patches through differentiable diffusion inference; at test time, the attacker switches among these patches in the camera stream to compose attacker-chosen trajectories. This works because the perturbation acts on the visual conditioning pathway, where the induced bias can persist through iterative generative inference. We further show that the natural targeted baseline, target-policy matching, fails because the victim policy cannot reliably supervise itself on out-of-distribution target shifts. Across four tasks (2D manipulation, simulated aerial delivery, simulated ground navigation, and physical-world ground navigation), two visual encoders (ResNet-18 and EfficientNet-B0 + Transformer), and three generative inference families (DDPM, DDIM, and flow matching), human operators achieve 100\% takeover success on attacker-defined objectives in every evaluated setting. The project page is available at https://tako-attack.github.io.

</details>

---

### [[20_Research/Papers/具身智能/A_Practical_Recipe_Towards_Improving_Sim-and-Real_Correlation_for_VLA_Evaluation|A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation]]

![[assets/2606.10366_figure.png|800]]

- **arXiv**: [2606.10366](https://arxiv.org/abs/2606.10366)
- **PDF**: https://arxiv.org/pdf/2606.10366
- **详细分析**: [[20_Research/Papers/具身智能/A_Practical_Recipe_Towards_Improving_Sim-and-Real_Correlation_for_VLA_Evaluation|A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation]]
- **作者**: Shuo Wang, Hanyuan Xu, Yingdong Hu, Fanqi Lin, Yang Gao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, Isaac-Sim, ManipBench, RLBench, Real-World, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation has become an essential tool for evaluating and improving vision-language-action (VLA) policies, offering scalable, reproducible, and controllable alternatives to costly real-world robot evaluation. Recent simulation benchmarks have made substantial progress on realism and diversity, yet these platforms have not been widely adopted as reliable proxies for real-world policy evaluation. In this work, we investigate this issue through the lens of sim-and-real correlation. We conduct a systematic study across multiple simulation platforms, VLA policies, tasks, and perturbation factors, measuring whether simulated evaluation preserves real-world conclusions in terms of policy ranking consistency, performance correlation, and perturbation-wise failure patterns. This analysis allows us to characterize the limitations of existing simulators and identify what kinds of simulation signals are more aligned with real-world deployment. We further examine how users should exploit simulation for policy improvement, including when simulator-based finetuning is beneficial and how the amount of post-training data affects sim-and-real alignment. Overall, our work provides a unified framework for measuring, interpreting, and improving the usefulness of simulation for VLA policies, offering guidance both for simulator designers and for practitioners who use simulation as part of the policy development pipeline.

</details>

---

### [[20_Research/Papers/大模型/ReflectiChain_Epistemic_Grounding_in_LLM-Driven_World_Models_for_Supply_Chain_Resilience|ReflectiChain: Epistemic Grounding in LLM-Driven World Models for Supply Chain Resilience]]

![[assets/2606.10359_figure.png|800]]

- **arXiv**: [2606.10359](https://arxiv.org/abs/2606.10359)
- **PDF**: https://arxiv.org/pdf/2606.10359
- **详细分析**: [[20_Research/Papers/大模型/ReflectiChain_Epistemic_Grounding_in_LLM-Driven_World_Models_for_Supply_Chain_Resilience|ReflectiChain: Epistemic Grounding in LLM-Driven World Models for Supply Chain Resilience]]
- **作者**: Jia Luo
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 0.2，世界模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《ReflectiChain: Epistemic Grounding in LLM-Driven World Models for Supply Chain Resilience》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ARL, Semi-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents in supply chains face a fundamental epistemic gap: large language models (LLMs) interpret policies but lack physical grounding, while reinforcement learning (RL) optimizes flows but is semantically blind to unstructured constraints. We introduce REFLECTICHAIN, bridging this gap through a Generative Supply Chain World Model (SC-WM) - encoding heterogeneous supply networks into a 6-dim graph-latent space with physical conservation - and Double-Loop Learning that separates epistemic uncertainty (KL-trust-region-bounded policy adaptation) from aleatoric uncertainty (stochastic latent rollouts). On Semi-Sim, a 10-node semiconductor benchmark with SIR risk propagation, 6 perturbation types, and 10 policy constraint templates, REFLECTICHAIN improves Rationale Consistency Score by 33.0% (p &lt; 0.0001, d = 2.78), maintains 82.3% operability under adversarial shocks, and exhibits anti-fragile behavior (+40.2% gain under moderate pressure). We identify three operational epistemic mechanisms - uncertainty separation, knowledge-boundary detection, and empirical Bayesian policy updating - and discuss five limitation categories.

</details>

---

### [[20_Research/Papers/大模型/Reasoning_or_Memorization_Direction-Aware_Diversity_Exploration_in_LLM_Reinforcement_Learning|Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning]]

![[assets/2606.10346_figure.png|800]]

- **arXiv**: [2606.10346](https://arxiv.org/abs/2606.10346)
- **PDF**: https://arxiv.org/pdf/2606.10346
- **详细分析**: [[20_Research/Papers/大模型/Reasoning_or_Memorization_Direction-Aware_Diversity_Exploration_in_LLM_Reinforcement_Learning|Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning]]
- **作者**: Jiangnan Xia, Yucheng Shi, Yu Yang, Kishan Panaganti, Zhenwen Liang, Ninghao Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.3，强化学习 1）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Reasoning or Memorization? Direction-Aware Diversity Exploration in LLM Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DiRL, EVOL-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has become a key paradigm for eliciting reasoning abilities in large language models, where exploration is crucial for discovering effective solution trajectories. Existing exploration methods typically encourage diversity in semantic or gradient spaces, without distinguishing what drives this diversity. A trajectory may appear novel because it follows a new reasoning process, or because it varies memorized patterns and shortcuts. Rewarding both cases equally may steer exploration toward memorization rather than genuine reasoning improvement. In this paper, we propose DiRL, a Direction-Aware Reinforcement Learning framework that anchors exploration to an internal reasoning-memorization direction of the policy. Specifically, DiRL extracts this direction from model representations, constructs direction-weighted gradient features to characterize rollout updates, and shapes rewards to amplify reasoning-aligned exploration while suppressing memorization-aligned variations. DiRL integrates seamlessly into standard Group Relative Policy Optimization (GRPO). Extensive experiments on mathematical and general reasoning benchmarks demonstrate the effectiveness of DiRL, showing significant improvements over various existing exploration methods.

</details>

---

### [[20_Research/Papers/大模型/Baseline-Free_Policy_Optimization_for_Neural_Combinatorial_Optimization|Baseline-Free Policy Optimization for Neural Combinatorial Optimization]]

![[assets/2606.10321_figure.png|800]]

- **arXiv**: [2606.10321](https://arxiv.org/abs/2606.10321)
- **PDF**: https://arxiv.org/pdf/2606.10321
- **详细分析**: [[20_Research/Papers/大模型/Baseline-Free_Policy_Optimization_for_Neural_Combinatorial_Optimization|Baseline-Free Policy Optimization for Neural Combinatorial Optimization]]
- **作者**: Carlos S. Sepúlveda, Gonzalo A. Ruz
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Baseline-Free Policy Optimization for Neural Combinatorial Optimization》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Neural combinatorial optimization (NCO) trains autoregressive policies to solve routing problems. The standard training algorithm, REINFORCE with a rollout baseline, requires maintaining and periodically updating a frozen copy of the policy for variance reduction. This baseline introduces a structural vulnerability: on harder instances, a poor baseline produces noisy gradient estimates that can destabilize training. We evaluate Group Relative Policy Optimization (GRPO), an algorithm from large language model alignment that eliminates the baseline entirely by normalizing advantages within groups of sampled trajectories. In a controlled comparison of five RL algorithms on TSP and CVRP benchmarks within the RL4CO framework, we find that: (i) GRPO avoids the training collapse observed with REINFORCE on TSP-100, where performance degrades from cost 9.8 to 52.1 immediately after the warmup phase and does not recover under extended training; (ii) at matched gradient updates, GRPO achieves solution quality within 2% of POMO, a strong AM-based multi-start baseline, while requiring no external baseline; and (iii) P3O, a pairwise preference algorithm also from the alignment literature, is competitive on TSP but shows higher variability on CVRP. These results identify GRPO as a promising baseline-free alternative for NCO, particularly in settings where baseline-dependent training becomes fragile.

</details>

---

### [[20_Research/Papers/大模型/Catching_One_in_Five_LLM-as-Judge_Blind_Spots_in_Production_Multi-Turn_Transaction_Agents|Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents]]

![[assets/2606.10315_figure.png|800]]

- **arXiv**: [2606.10315](https://arxiv.org/abs/2606.10315)
- **PDF**: https://arxiv.org/pdf/2606.10315
- **详细分析**: [[20_Research/Papers/大模型/Catching_One_in_Five_LLM-as-Judge_Blind_Spots_in_Production_Multi-Turn_Transaction_Agents|Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents]]
- **作者**: Sawyer Zhang, Alexander Wang, Sophie Lei
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-as-judge is the default instrument for evaluating conversational agents, yet its reliability is almost always reported as agreement with human ratings, not recall of real defects. We study a deployed multi-turn food-and-beverage ordering agent and measure how many genuine quality problems its built-in LLM judge catches, using exhaustive human transcript review as ground truth. Across three batches the judge surfaces well under a quarter of human-confirmed systematic problems -- 2 of 9 patterns (22%) in one batch, and its operational gate flagged zero of 100 rounds in a batch where humans confirmed 23 distinct defects and 7 new cross-cutting patterns. Our blind-spot taxonomy shows the failure is structured, not random: the judge catches turn-local issues (a fabricated statistic, a wrong language) but misses cross-turn state issues (confirm-gate lockout, cart hallucination, escalation lockout, stale referents). The mechanism: the scoring rubric exposes only three coarse axes (intent, brand-voice, personalization) and has no category for the behavioural dimensions -- state-tracking, guardrails, recovery -- where most defects cluster. The failure is routing, not perception: 113 of 114 rounds whose raw judge note describes a confirm-gate or cart-state defect are scored "brand voice", and none reach an operational failure -- the gate is wired to hangs and hard assertions, not the rubric -- so the 0% is a routing-and-wiring failure, not blindness. The consequence for prevalence estimation is sharp: when the apparent defect rate is zero the Rogan-Gladen correction degenerates -- no signal can recover the true rate -- while where the gate reports a nonzero rate the same estimator implies a 3-6x undercount under our measured sensitivity. For production multi-turn agents, automated judging is a regression floor, not a substitute for human review.

</details>

---

### [[20_Research/Papers/大模型/The_Confident_Liar_Diagnosing_Multi-Agent_Debate_with_Log-Probabilities_and_LLM-as-Judge|The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge]]

![[assets/2606.10296_figure.png|800]]

- **arXiv**: [2606.10296](https://arxiv.org/abs/2606.10296)
- **PDF**: https://arxiv.org/pdf/2606.10296
- **详细分析**: [[20_Research/Papers/大模型/The_Confident_Liar_Diagnosing_Multi-Agent_Debate_with_Log-Probabilities_and_LLM-as-Judge|The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge]]
- **作者**: Ali Keramati, Justin Cheok, Jacob Horne, Mark Warschauer
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ChatEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent debate systems are typically evaluated only on whether the final answer is correct, overlooking the quality of the intermediate reasoning that debate is designed to produce. This paper studies the relationship between three signals in multi-agent debate: token-level log-probability distributions over reasoning tokens, LLM-as-judge rubric scores assigned to those tokens, and final task accuracy. We examine whether internal confidence signals predict externally evaluated reasoning quality, and whether either signal aligns with task correctness, across three domains: rubric-based scoring, mathematical reasoning, and factual question answering. Our framework pairs a two-agent debate architecture -- a Constructor and an Auditor -- with an LLM-as-judge that scores each agent's reasoning along instruction following, justification quality, and evidence grounding, together with a critical-failure flag. Experiments in the rubric-scoring domain reveal a consistent four-phase confidence trajectory and a substantial role asymmetry: confidence aligns with judged reasoning quality roughly twice as strongly for the Constructor as for the Auditor, and confidence-based detection of critical reasoning failures is markedly more reliable for the Constructor (AUROC 0.804) than for the Auditor (0.634). These findings motivate the broader cross-domain investigation proposed in this paper.

</details>

---

### [[20_Research/Papers/强化学习/Hierarchical_Policies_from_Verbal_and_Egocentric_Human_Signals_for_Natural_Human-Robot_Interaction|Hierarchical Policies from Verbal and Egocentric Human Signals for Natural Human-Robot Interaction]]

![[assets/2606.10276_figure.png|800]]

- **arXiv**: [2606.10276](https://arxiv.org/abs/2606.10276)
- **PDF**: https://arxiv.org/pdf/2606.10276
- **详细分析**: [[20_Research/Papers/强化学习/Hierarchical_Policies_from_Verbal_and_Egocentric_Human_Signals_for_Natural_Human-Robot_Interaction|Hierarchical Policies from Verbal and Egocentric Human Signals for Natural Human-Robot Interaction]]
- **作者**: Dongjun Lee, Juheon Choi, Dong Kyu Shin, Sinjae Kang, Kimin Lee
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Hierarchical Policies from Verbal and Egocentric Human Signals for Natural Human-Robot Interaction》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For natural human-robot interaction, a robot must understand human intent expressed not only through language but also through nonverbal signals such as gestures and gaze. However, current robot policies rely on language instructions as the sole interface for conveying intent, leaving nonverbal signals unused and placing the full burden of communication. In this work, we present EDITH, a robot framework that captures the human's nonverbal signals through continuous streams of first-person view and gaze from smart glasses, and uses them alongside language instructions as inputs to the robot policy. Our hardware system streams the human's first-person view, gaze, and speech to the robot in real time, transcribing the speech into language instructions. To handle these rich but noisy signals, we design a hierarchical policy in which a high-level policy infers the human's intent and produces a sequence of subtasks, where each subtask is represented as a fine-grained instruction paired with a keyframe that grounds the intent in the scene (e.g., the frame where the human points at the target object). A low-level policy then executes these subtasks. In our experiments on human-robot interactive tasks, EDITH enables the robot to act on the human's nonverbal signals even when intent is expressed only briefly, and significantly reduces user effort to convey intent compared to using language instructions alone. Visit our project page for source code and real-robot demo videos.

</details>

---

### [[20_Research/Papers/具身智能/What_Matters_in_Orchestrating_Robot_Policies_A_Systematic_Study_of_Hierarchical_VLA_Agents|What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents]]

![[assets/2606.10267_first_page.png|800]]

- **arXiv**: [2606.10267](https://arxiv.org/abs/2606.10267)
- **PDF**: https://arxiv.org/pdf/2606.10267
- **详细分析**: [[20_Research/Papers/具身智能/What_Matters_in_Orchestrating_Robot_Policies_A_Systematic_Study_of_Hierarchical_VLA_Agents|What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents]]
- **作者**: Jiaheng Hu, Mohit Shridhar, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang, Jie Tan, Annie Xie
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.7（加权：具身智能 2.1，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Hi-VLA, HiVLA, Humanoid-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical vision-language-action (Hi-VLA) systems have emerged as a promising paradigm for complex robot manipulation, by using high-level VLM planners to decompose tasks into language subgoals executed by low-level VLA controllers. Despite recent empirical progress, there is a lack of unified design principles for these systems: existing Hi-VLA systems differ in how they choose and connect planners, controllers, mechanisms to switch between the two, and how observations and memory are represented in the planner. In this paper, we present a systematic study of Hi-VLA design for robot manipulation. We unify representative Hi-VLA agents under an options-style control framework and benchmark core design choices across short-horizon, long-horizon, and reasoning-intensive tasks. Our analysis distills practical principles for building Hi-VLA systems, showing how model choices and interface mechanisms jointly shape performance. Applying these principles yields a substantially stronger system than either flat VLA control or a naively designed hierarchy, across experiments both in simulation and on a real ALOHA robot. Overall, our results provide a foundation for building more capable, robust, and principled hierarchical VLA agents. More information and video at jiahenghu.github.io/hi-vla.

</details>

---

### [[20_Research/Papers/强化学习/YUBI_Yielding_Universal_Bidigital_Interface_for_Bimanual_Dexterous_Manipulation_at_Scale|YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale]]

![[assets/2606.10244_figure.png|800]]

- **arXiv**: [2606.10244](https://arxiv.org/abs/2606.10244)
- **PDF**: https://arxiv.org/pdf/2606.10244
- **详细分析**: [[20_Research/Papers/强化学习/YUBI_Yielding_Universal_Bidigital_Interface_for_Bimanual_Dexterous_Manipulation_at_Scale|YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale]]
- **作者**: Takehiko Ohkawa, Jumpei Arima, Yuki Noguchi, Masatoshi Tateno, Makoto Sugiura, Takuya Okubo, Kengo Ikeuchi, Yuma Shin, Hiroki Nishizawa, Naoaki Kanazawa, Yuki Wakayama, Daiki Fukunaga...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《YUBI: Yielding Universal Bidigital Interface for Bimanual Dexterous Manipulation at Scale》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Yielding Universal Bidigital Interface (YUBI), a finger-aligned gripper designed to enable intuitive, ergonomic, and scalable data collection for bimanual dexterous manipulation. While handheld data collection systems such as Universal Manipulation Interface (UMI) enable affordable data collection, their bulky pistol-grip designs can pose ergonomic and usability challenges for fine-grained, dexterous manipulation tasks. To address this, YUBI presents a distinct design principle: yielding, finger-driven actuation that directly maps human finger movements to gripper jaw motion. Using the YUBI devices, we set up a data collection system with integrated VR-based 6 DoF tracking of the gripper, ensuring high-fidelity trajectory data acquisition. We curate a UMI-based dataset of unprecedented scale: 8,434 hours across 1.20M episodes and 119 tasks. Experiments show that YUBI offers advantages over the UMI gripper in versatility for complex bimanual tasks, dexterity, and operational efficiency. A single policy trained on the YUBI dataset transfers across multiple bimanual robots (UR, Franka, and ELEY) simply by mounting the gripper on each platform, confirming that the collected data are directly executable as policy supervision. We release the gripper hardware, data-collection software, and dataset as one integrated stack, offering the open community a reproducible path to large-scale data acquisition for advancing robotic foundation models.

</details>

---

### [[20_Research/Papers/强化学习/SHAPO_Sharpness-Aware_Policy_Optimization_for_Safe_Exploration|SHAPO: Sharpness-Aware Policy Optimization for Safe Exploration]]

![[assets/2606.10228_figure.png|800]]

- **arXiv**: [2606.10228](https://arxiv.org/abs/2606.10228)
- **PDF**: https://arxiv.org/pdf/2606.10228
- **详细分析**: [[20_Research/Papers/强化学习/SHAPO_Sharpness-Aware_Policy_Optimization_for_Safe_Exploration|SHAPO: Sharpness-Aware Policy Optimization for Safe Exploration]]
- **作者**: Kaustubh Mani, Yann Pequignot, Vincent Mai, Liam Paull
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SHAPO: Sharpness-Aware Policy Optimization for Safe Exploration》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Safety-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe exploration is a prerequisite for deploying reinforcement learning (RL) agents in safety-critical domains. In this paper, we approach safe exploration through the lens of epistemic uncertainty, where the actor's sensitivity to parameter perturbations serves as a practical proxy for regions of high uncertainty. We propose Sharpness-Aware Policy Optimization (SHAPO), a sharpness-aware policy update rule that evaluates gradients at perturbed parameters, making policy updates pessimistic with respect to the actor's epistemic uncertainty. Analytically we show that this adjustment implicitly reweighs policy gradients, amplifying the influence of rare unsafe actions while tempering contributions from already safe ones, thereby biasing learning toward conservative behavior in under-explored regions. Across several continuous-control tasks, our method consistently improves both safety and task performance over existing baselines, significantly expanding their Pareto frontiers.

</details>

---

### [[20_Research/Papers/具身智能/Exploration_of_Foundation_Model-Based_Robots_in_Patient_and_Elderly_Care|Exploration of Foundation Model-Based Robots in Patient and Elderly Care]]

![[assets/2606.10208_figure.png|800]]

- **arXiv**: [2606.10208](https://arxiv.org/abs/2606.10208)
- **PDF**: https://arxiv.org/pdf/2606.10208
- **详细分析**: [[20_Research/Papers/具身智能/Exploration_of_Foundation_Model-Based_Robots_in_Patient_and_Elderly_Care|Exploration of Foundation Model-Based Robots in Patient and Elderly Care]]
- **作者**: Zhiwen Qiu, Wei Liu, Yuexing Hao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.6，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Exploration of Foundation Model-Based Robots in Patient and Elderly Care》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Demand for older-adult and patient care is growing rapidly as populations age worldwide. Foundation models are increasingly being integrated into robots and interactive agents, with the promise of more flexible communication and personalized assistance. However, care settings require reliable and workflow-compatible systems with accountable human oversight, and it remains unclear whether current embodied systems can translate technical advances into clinical impact. This Perspective synthesizes foundation model-based care robots across three areas: design features, user experience, and evidence for care-related outcomes. Current systems most commonly use foundation models as conversational and reasoning layers within voice-centered socially assistive embodiments, while multimodal grounding and physical autonomy remain limited. Empirical evaluations report positive usability and engagement benefits, but reliability failures persist across the interaction pipeline such as hallucinations and conversational breakdowns. Evidence for care impact remains concentrated in proximal outcomes such as cognitive engagement and participation, with limited evidence for validated clinical or care-related changes. We argue that future research should transition toward care-specific evaluation standards, accountable autonomy, and integration into care workflows to support more responsive and responsible care technologies.

</details>

---

### [[20_Research/Papers/具身智能/Flow_Control_Steering_Vision-Language-Action_Models_with_Simple_Real-Time_Inputs|Flow Control: Steering Vision-Language-Action Models with Simple Real-Time Inputs]]

![[assets/2606.10180_figure.png|800]]

- **arXiv**: [2606.10180](https://arxiv.org/abs/2606.10180)
- **PDF**: https://arxiv.org/pdf/2606.10180
- **详细分析**: [[20_Research/Papers/具身智能/Flow_Control_Steering_Vision-Language-Action_Models_with_Simple_Real-Time_Inputs|Flow Control: Steering Vision-Language-Action Models with Simple Real-Time Inputs]]
- **作者**: Jonathan C. Kao, Jason Chan, Andy Wang
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Flow Control: Steering Vision-Language-Action Models with Simple Real-Time Inputs》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce flow control of vision-language-action (VLA) models, a simple and effective way to steer VLA actions in real-time through generic inputs, such as a keyboard. This method can be used out-of-the-box and does not require retraining or fine-tuning VLAs. It enables relatively crude user inputs to steer a VLA to align with user intent. The VLA transforms these inputs into action samples drawn from the VLA expert action distribution learned during training, so that the generated actions are high quality (conformity to the action expert distribution) and high fidelity (reflecting the user's intent). We demonstrate that flow control has many desirable properties: (1) flow control accurately and responsively steers robot actions with user inputs, (2) it is robust to suboptimal user inputs, (3) it enables users to steer VLAs to achieve significantly higher success rates and faster task completion, and (4) fine-tuning a VLA on flow control trajectories improves the autonomous policy. Together, these results provide a simple and intuitive way for users to help steer VLA actions, increasing task performance.

</details>

---

### [[20_Research/Papers/世界模型/BiWM_Advancing_Open-Source_Interactive_Video_World_Models_with_Bidirectional_Autoregression|BiWM: Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression]]

![[assets/2606.10135_figure.png|800]]

- **arXiv**: [2606.10135](https://arxiv.org/abs/2606.10135)
- **PDF**: https://arxiv.org/pdf/2606.10135
- **详细分析**: [[20_Research/Papers/世界模型/BiWM_Advancing_Open-Source_Interactive_Video_World_Models_with_Bidirectional_Autoregression|BiWM: Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression]]
- **作者**: Shaohao Rui, Xiaofeng Mao, Zhanyu Zhang, Peijia Lin, Yansong Zhu, Yibo Zhang, Haibin Wan, Weijie Ma
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《BiWM: Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transitioning bidirectional video diffusion models into an autoregressive paradigm improves the interactivity of video world models, but existing causal pipelines need many stages (control fine-tuning, autoregressive training, causal initialization, few-step distillation) and still trail bidirectional models in quality due to error accumulation. Recent world models such as Yume-1.5 and Matrix-Game-3.0 instead adopt a bidirectional autoregressive approach, gaining fidelity and stable long-horizon rollout from self-correcting error propagation, yet open-source frameworks (e.g., minWM) support only causal models. We present BiWM, the first full-stack framework for interactive video world models under the bidirectional autoregressive paradigm, jointly optimizing generation quality and inference speed. From a pretrained video backbone, BiWM injects camera control by fine-tuning, then runs a few-step Distribution Matching Distillation (DMD) stage that turns the backbone into an action/camera-controllable world model: just two training stages instead of four in minWM, converging in a few hundred steps on 8xH200 GPUs. A single recipe spans Wan2.1-1.3B, Wan2.2-5B, HunyuanVideo-1.5-8B, and LTX-2.3-22B, and also supports secondary fine-tuning of existing bidirectional models. BiWM enables real-world camera control where minWM loses controllability, integrates pluggable history compression (FramePack-style and PackForcing-style) for long rollouts, and offers an optional NVFP4 4-bit training/inference pipeline. To counter DMD's mode-seeking degradation, we add GAN and mass-covering forward-KL objectives that preserve scene dynamics. We open-source BiWM for resource-constrained research and high-fidelity environment simulation.

</details>

---

### [[20_Research/Papers/大模型/MetaPlate_Counterfactual-Guided_RAG-LLM_Tool_for_Personalized_Food_Recommendation_and_Hyperglycemia_Prevention|MetaPlate: Counterfactual-Guided RAG-LLM Tool for Personalized Food Recommendation and Hyperglycemia Prevention]]

![[assets/2606.10120_figure.png|800]]

- **arXiv**: [2606.10120](https://arxiv.org/abs/2606.10120)
- **PDF**: https://arxiv.org/pdf/2606.10120
- **详细分析**: [[20_Research/Papers/大模型/MetaPlate_Counterfactual-Guided_RAG-LLM_Tool_for_Personalized_Food_Recommendation_and_Hyperglycemia_Prevention|MetaPlate: Counterfactual-Guided RAG-LLM Tool for Personalized Food Recommendation and Hyperglycemia Prevention]]
- **作者**: Asiful Arefeen, Carol Johnston, Hassan Ghasemzadeh
- **cs 子类**: cs.AI, cs.HC, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《MetaPlate: Counterfactual-Guided RAG-LLM Tool for Personalized Food Recommendation and Hyperglycemia Prevention》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Postprandial hyperglycemia is a key risk factor for metabolic disorders; however, existing dietary guidance is often static, impractical, and insufficiently personalized, providing recommendations that are difficult to follow or not impactful. While recent advances leverage continuous glucose monitoring (CGM) and machine learning to predict glycemic responses, these approaches are largely predictive and lack actionable guidance. Moreover, recommendation systems are often misaligned with user goals and require extensive input. We present MetaPlate, a counterfactual explanation (CF) guided, context-aware decision-support framework that generates personalized meal recommendations to mitigate postprandial glucose excursions in healthy adults. MetaPlate integrates multimodal data, including CGM readings, wearable-derived physiological signals, and user-provided meal inputs from $25$ individuals to model pre-meal context. A machine learning model predicts glucose response, while a CF optimization module adjusts meal composition modifying macronutrient amounts to maintain glucose levels within a target range ($\leq 140$ mg/dL). An LLM-based retrieval-augmented generation (RAG) layer enhances interpretability by producing human-readable recommendations using constrained search of the USDA food database. We evaluate MetaPlate via a structured expert-in-the-loop assessment with registered dietitians (RDs), comparing performance before and after prompt refinement. Results show improvements in meal realism, portion suitability, and recommendation likelihood, with expert feedback indicating a shift from clinically implausible outputs to actionable, contextually appropriate recommendations. Our findings emphasize the importance of domain knowledge and structured constraints in LLM-driven systems and highlight the potential of MetaPlate as a real-time personalized dietary decision-support tool.

</details>

---

### [[20_Research/Papers/世界模型/Business_World_Model|Business World Model]]

![[assets/2606.10044_first_page.png|800]]

- **arXiv**: [2606.10044](https://arxiv.org/abs/2606.10044)
- **PDF**: https://arxiv.org/pdf/2606.10044
- **详细分析**: [[20_Research/Papers/世界模型/Business_World_Model|Business World Model]]
- **作者**: Cecil Pang, Hiroki Sayama
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Business World Model》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Businesses are increasingly adopting AI-enabled tools to improve productivity, reduce costs, and enhance products and services. However, the transformative potential of AI extends beyond automating predefined tasks: it lies in enabling intelligent systems to plan, optimize, and execute business initiatives from high-level strategic objectives. This paper introduces the concept and architecture of a business world model (BWM), a world model specialized for business and organizational environments. Inspired by world models in artificial intelligence, cognitive science, and control theory, a BWM encodes business states, dynamics, constraints, objectives, and feasible action space to support autonomous decision-making. We propose a business-semantics-centric formulation in which business states, dynamics and actions are linked to key business entities. Within this framework, agents can simulate alternative action sequences, estimate their effects on future business outcomes, and evaluate trade-offs under uncertainty. The proposed architecture integrates semantic data representations, probabilistic machine learning models, deterministic business rules, and explicit action space into a coherent structure for planning and counterfactual reasoning. Although its individual components are not new, the contribution of BWM lies in organizing them as an executable internal simulator for business initiatives. This work establishes a conceptual foundation for autonomous business systems capable of moving from instruction-based execution toward goal-driven planning and execution.

</details>

---

### [[20_Research/Papers/大模型/3SPO_State-Score-Supervised_Policy_Optimization_for_LLM_Agents|3SPO: State-Score-Supervised Policy Optimization for LLM Agents]]

![[assets/2606.09961_figure.png|800]]

- **arXiv**: [2606.09961](https://arxiv.org/abs/2606.09961)
- **PDF**: https://arxiv.org/pdf/2606.09961
- **详细分析**: [[20_Research/Papers/大模型/3SPO_State-Score-Supervised_Policy_Optimization_for_LLM_Agents|3SPO: State-Score-Supervised Policy Optimization for LLM Agents]]
- **作者**: Yu Han, Kailing Li, Yang Jiao, Yulin Dai, Yuqian Fu, Linhai Zhuo, Tianwen Qian
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.12（加权：大模型 0.8，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《3SPO: State-Score-Supervised Policy Optimization for LLM Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training large language models (LLMs) as autonomous agents via reinforcement learning (RL) has enabled frontier models to achieve superhuman performance in long-horizon tasks. However, existing RL algorithms operate at the trajectory level, performing policy optimization only after collecting complete episode rollouts. This coarse-grained approach faces fundamental challenges in multi-turn agent settings where rewards are sparse, delayed, and credit assignment across individual steps is critical. In this work, we propose \textbf{State-Score-Supervised Policy Optimization (3SPO)}, a novel RL algorithm that performs post-step policy optimization with dynamic state score supervision. At each step, 3SPO computes the state score based on historical success rates, supervising step-wise credit assignment, adaptive rollout and post-step policy optimization without requiring value function estimation or additional auxiliary models. Theoretically, under a per-state bandit abstraction, we show that the proposed score-supervised allocation mechanism achieves logarithmic allocation regret and provide sample-complexity guarantees for action identification, score distinguishability, and filtering stability. Experiments on ALFWorld and WebShop with Qwen2.5-1.5B/7B-Instruct show that 3SPO consistently outperforms GRPO by $+22.6\%$ on ALFWorld and $+15.6$ points on WebShop, while using comparable resources to achieve $2.4\times$ more state exploration and $1.8\times$ faster convergence. Code is available at https://github.com/genalyu/3SPO.

</details>

---

### [[20_Research/Papers/强化学习/Uncertainty-Aware_Motion_Planning_for_Autonomous_Driving_in_Mixed_Traffic_Environment|Uncertainty-Aware Motion Planning for Autonomous Driving in Mixed Traffic Environment]]

![[assets/2606.09958_figure.png|800]]

- **arXiv**: [2606.09958](https://arxiv.org/abs/2606.09958)
- **PDF**: https://arxiv.org/pdf/2606.09958
- **详细分析**: [[20_Research/Papers/强化学习/Uncertainty-Aware_Motion_Planning_for_Autonomous_Driving_in_Mixed_Traffic_Environment|Uncertainty-Aware Motion Planning for Autonomous Driving in Mixed Traffic Environment]]
- **作者**: Ming Cheng, Hao Chen, Ziyi Yang, Ziluowen Luo, Senzhang Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Uncertainty-Aware Motion Planning for Autonomous Driving in Mixed Traffic Environment》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In mixed-traffic environments where autonomous and human-driven vehicles may co-exist, motion planning for autonomous vehicles requires anticipating the future behaviors of surrounding human drivers. Existing reinforcement learning-based methods generally directly incorporate the predicted human intents into the observation to enable a proactive planning. However, human intent is inherently uncertain due to the behavioral diversity, perception noise, and partial observability. Treating predicted intends as deterministic states can result in unsafe decisions for autonomous vehicles. To address this problem, we propose Uncertainty-Aware Motion Planning (UAMP), which incorporates uncertainty in human intent prediction for AV decision-making. Specifically, UAMP first introduces a proximity-aware uncertainty estimator to quantify the interaction-conditioned intent uncertainty and constructs an uncertainty-guided joint intent distribution over surrounding human-driven vehicles. Within this uncertainty set, UAMP further introduces Uncertainty-Calibrated Value Learning (UCVL) to correct value function learning biases arising from directly incorporating uncertain human intent predictions into the observation. Extensive experiments in various mixed-traffic scenarios show that UAMP significantly improves safety and driving comfort, while maintaining traffic efficiency compared with existing approaches. The code is released at https://anonymous.4open.science/r/UAMP-5638.

</details>

---

### [[20_Research/Papers/大模型/One_Lens,_Many_Worlds_A_Capability-Typed_Interface_for_World-Model_Interpretability|One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability]]

![[assets/2606.09936_first_page.png|800]]

- **arXiv**: [2606.09936](https://arxiv.org/abs/2606.09936)
- **PDF**: https://arxiv.org/pdf/2606.09936
- **详细分析**: [[20_Research/Papers/大模型/One_Lens,_Many_Worlds_A_Capability-Typed_Interface_for_World-Model_Interpretability|One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability]]
- **作者**: Bhavith Chandra Challagundla, Sanskar Pandey, Param Thakkar, Rishikesh Mallagundla, Yugandhar Reddy Gogireddy, Wenhao Lu, Hindol Roy Choudhury, Shravani Challagundla, Mohamed Deraz Nasr, Spursh Deshpande
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.16，世界模型 0.56）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are now built on substantially different computational substrates. Latent recurrent state-space models such as PlaNet and the Dreamer family compress observations into recurrent states; token-based models such as IRIS quantize observations into a learned codebook and predict autoregressively with a transformer; and joint-embedding predictive architectures such as I-JEPA predict in a learned latent space with no pixel decoder. The interpretability methods applied to these models, including probing, activation patching, sparse autoencoders, and surprise analysis, share a common set of primitives, yet they are re-implemented from scratch for each architecture because existing hook-and-cache tooling assumes a transformer language model with no notion of actions, environment steps, or imagined rollouts. We argue that this fragmentation reflects the tooling rather than the models, and that the shared structure of world models is captured by a small typed interface. We present WorldModelLens, an open-source interpretability substrate organized around a capability-typed adapter: every model implements four required methods (encode, transition, initial state, sample) and declares a set of optional heads (decode, reward, continue, actor, critic) through an explicit capability descriptor, so that reinforcement-learning and self-supervised world models are first-class without either imitating the other. A single hook and cache layer exposes time-indexed activations, imagination rollouts, and intervention replay over this interface, allowing each analysis to be written once.

</details>

---

### [[20_Research/Papers/大模型/When_RL_Fails_after_SFT_Rejuvenating_Model_Plasticity_for_Robust_SFT-to-RL_Handoff|When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff]]

![[assets/2606.09932_figure.png|800]]

- **arXiv**: [2606.09932](https://arxiv.org/abs/2606.09932)
- **PDF**: https://arxiv.org/pdf/2606.09932
- **详细分析**: [[20_Research/Papers/大模型/When_RL_Fails_after_SFT_Rejuvenating_Model_Plasticity_for_Robust_SFT-to-RL_Handoff|When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff]]
- **作者**: Runze Liu, Jiashun Liu, Xu Wan, Yuqian Fu, Ling Pan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SFT-then-RL, SFT-to-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL) has become a standard pipeline for Large Language Model (LLM) post-training. SFT is expected to provide a useful behavioral prior for RL to further enhance model capabilities. However, checkpoints with excessive SFT often show limited improvement during RL. We attribute this failure to the loss of model plasticity: the reduced ability of an SFT-initialized policy to be effectively reshaped by subsequent RL. To better understand this phenomenon, we conduct detailed analysis from multiple perspectives, including parameter changes, output spaces, and RL optimization dynamics. Our results show that models from excessive SFT tend to produce over-confident token distributions and exhibit sharp parameter landscapes, which make them harder to optimize in the RL stage. To enable a more robust SFT-to-RL handoff, we propose \texttt{Rejuvenation}, a simple yet effective method that restores plasticity while preserving useful SFT-acquired priors. Rejuvenation leverages base-anchored model fusion to reduce excessive SFT-induced drift with targeted neuron reset to mitigate model rigidity. Experimental results on both math reasoning tasks and agentic tasks demonstrate that our approach consistently improves RL performance on over-trained SFT models, while also enhancing generalization to out-of-distribution tasks.

</details>

---

### [[20_Research/Papers/大模型/Co-GLANCE_Uncertainty-Aware_Active_Perception_for_Heterogeneous_Robot_Teaming|Co-GLANCE: Uncertainty-Aware Active Perception for Heterogeneous Robot Teaming]]

![[assets/2606.09919_figure.png|800]]

- **arXiv**: [2606.09919](https://arxiv.org/abs/2606.09919)
- **PDF**: https://arxiv.org/pdf/2606.09919
- **详细分析**: [[20_Research/Papers/大模型/Co-GLANCE_Uncertainty-Aware_Active_Perception_for_Heterogeneous_Robot_Teaming|Co-GLANCE: Uncertainty-Aware Active Perception for Heterogeneous Robot Teaming]]
- **作者**: Michal P. Podolinsky, Neel P. Bhatt, Pranay Samineni, Rohan Siva, Christian Ellis, Ufuk Topcu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Co-GLANCE: Uncertainty-Aware Active Perception for Heterogeneous Robot Teaming》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perceptual uncertainty is a central challenge for heterogeneous robot teams operating in unstructured outdoor environments, where no single viewpoint affords reliable scene understanding. Perceptual uncertainty, arising from sources such as occlusions, manifests differently across robot viewpoints depending on scene structure. Detecting and resolving sources of perceptual uncertainty requires both scene-based contextual reasoning and capability-aware robot allocation. While vision-language models provide strong semantic priors for both, they are computationally prohibitive for onboard inference and lack calibrated uncertainty quantification. We introduce Co-GLANCE, a real-time onboard perception and decision-making system for uncertainty resolution in heterogeneous robot teams. Co-GLANCE distills the semantic reasoning capabilities of a vision-language model into an end-to-end model for occlusion segmentation and robot allocation, eliminating the need for cloud-based inference. To quantify perceptual uncertainty, Co-GLANCE combines conformal prediction with selective abstention to provide statistically valid coverage guarantees for segmentation, robot allocation, and detection outputs. These calibrated uncertainty estimates directly trigger active perception, dispatching the most appropriate robot to acquire informative viewpoints and resolve uncertainty. Across real-world scenarios, Co-GLANCE outperforms cloud-based vision-language model baselines in occlusion segmentation and robot allocation accuracy by 25% and 36%, respectively, while reducing per-frame inference latency 350x. We also release an air-ground dataset for future research. Code, videos, and dataset available at https://co-glance.github.io/ .

</details>

---

### [[20_Research/Papers/大模型/Less_Context,_More_Accuracy_A_Bi-Temporal_Memory_Engine_for_LLM_Agents_Where_a_Lean_Retrieved_Context_Beats_the_Full_History|Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History]]

![[assets/2606.09900_figure.png|800]]

- **arXiv**: [2606.09900](https://arxiv.org/abs/2606.09900)
- **PDF**: https://arxiv.org/pdf/2606.09900
- **详细分析**: [[20_Research/Papers/大模型/Less_Context,_More_Accuracy_A_Bi-Temporal_Memory_Engine_for_LLM_Agents_Where_a_Lean_Retrieved_Context_Beats_the_Full_History|Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History]]
- **作者**: Liuyin Wang
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory is the missing layer for LLM agents: across sessions they forget, and the common workaround -- replaying the whole history into the prompt -- is expensive, slow, and, as distractors accumulate, less accurate. Most memory systems win on cost or latency but still lose to the full-context baseline on accuracy, and benchmark numbers are reported on inconsistent, non-reproducible harnesses, so one system appears at wildly different scores across sources. We present Engram, an open-source, dual-process memory engine on a bi-temporal data model. A fast write path appends lossless episodes with no LLM on the critical path; an asynchronous path extracts atomic (subject, predicate, object) facts, builds a bi-temporal knowledge graph, and resolves contradictions without an LLM call per fact -- invalidating, never deleting, so every fact keeps provenance and a supersession chain. A hybrid read path fuses dense, lexical, graph, and recency/salience signals, applies a point-in-time ("as-of") filter, and assembles a compact, provenance-tagged context. On the full 500-question LongMemEval_S, graded by the official category-specific judge, Engram's lean configuration -- answering from a ~9.6k-token retrieved slice, never the full history -- scores 83.6% vs. 73.2% for full-context (+10.4 points, McNemar p &lt; 10^-6) at ~8x fewer tokens (9.6k vs. 79k), with 0/500 errored. The gain needs a hybrid read path: facts alone lose recall, while facts plus retrieved chunks recover detail. We also contribute a neutral, in-repo evaluation harness with the official judge baked in and the full-context baseline in every table, publish the raw per-question logs, and document the measurement-integrity pitfalls (truncation, home-grown judges, full-history leaks) that silently distort memory benchmarks. Every number ships with a command to reproduce it.

</details>

---

### [[20_Research/Papers/强化学习/SocraticPO_Policy_Optimization_via_Interactive_Guidance|SocraticPO: Policy Optimization via Interactive Guidance]]

![[assets/2606.09887_figure.png|800]]

- **arXiv**: [2606.09887](https://arxiv.org/abs/2606.09887)
- **PDF**: https://arxiv.org/pdf/2606.09887
- **详细分析**: [[20_Research/Papers/强化学习/SocraticPO_Policy_Optimization_via_Interactive_Guidance|SocraticPO: Policy Optimization via Interactive Guidance]]
- **作者**: Zirui Liu, Jie Ouyang, Qi Liu, Xianquan Wang, Jiayu Liu, Tingyue Pan, Qingchuan Li, Jing Sha, Zhenya Huang, Shijin Wang, Enhong Chen
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SocraticPO: Policy Optimization via Interactive Guidance》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SciKnowEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) for large language models usually supervises reasoning with scalar outcome rewards, such as binary correctness. Such rewards provide an optimization direction but rarely explain how a model should revise its mistaken reasoning, which can encourage shortcut learning and brittle policies. We propose \textbf{SocraticPO} (Socratic Policy Optimization), a policy-optimization framework that augments RL rollouts with Socratic-style natural-language guidance. During rollout, the student first answers independently; if the answer is incorrect, a teacher diagnoses the attempt and provides concise corrective guidance, after which the student continues under the expanded context. Crucially, this guidance is paired with reward decay: correct answers obtained after teacher intervention only receive decayed rewards, preventing the policy from treating teacher help as a free path to reward. Since SocraticPO only modifies the rollout process while leaving the standard expected-reward objective intact, it can be plugged into existing policy-gradient backends such as Reinforce++. Moreover, because the teacher provides only text-level guidance, SocraticPO can leverage stronger black-box teacher models without requiring access to logits or distribution matching. On undergraduate-level scientific reasoning benchmarks from SciKnowEval, SocraticPO improves over strong RL and self-distillation baselines. Ablations show that both targeted guidance and reward decay are necessary, with reward decay mitigating reliance on assisted correction.

</details>

---

### [[20_Research/Papers/强化学习/Failure_Modes_of_Deep_Multi-Agent_RL_in_Asynchronous_Pricing_Reproducible_Triggers,_Trace_Diagnostics,_and_a_Partial_Fix|Failure Modes of Deep Multi-Agent RL in Asynchronous Pricing: Reproducible Triggers, Trace Diagnostics, and a Partial Fix]]

![[assets/2606.09884_first_page.png|800]]

- **arXiv**: [2606.09884](https://arxiv.org/abs/2606.09884)
- **PDF**: https://arxiv.org/pdf/2606.09884
- **详细分析**: [[20_Research/Papers/强化学习/Failure_Modes_of_Deep_Multi-Agent_RL_in_Asynchronous_Pricing_Reproducible_Triggers,_Trace_Diagnostics,_and_a_Partial_Fix|Failure Modes of Deep Multi-Agent RL in Asynchronous Pricing: Reproducible Triggers, Trace Diagnostics, and a Partial Fix]]
- **作者**: Shree Murthy, Rohan Pandey
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Failure Modes of Deep Multi-Agent RL in Asynchronous Pricing: Reproducible Triggers, Trace Diagnostics, and a Partial Fix》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CT-MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study two reproducible failure modes of deep multi-agent reinforcement learning in continuous-time pricing markets: (i) tacit cartel formation between competing DDPG agents, and (ii) actor--critic instability at high event rates. We instantiate both inside a single CT-MARL benchmark (Poisson-clocked price updates, observation latency $δ$, interior-optimum logit demand), show that synchronous DDPG agents reliably trigger Failure Mode 1 with collusion index $Δ= 0.69 \pm 0.11$, and quantify a partial microstructure fix: asynchrony alone cuts collusion by 48\% and adding latency drives it to a minimum of $Δ= 0.28$. The fix has clearly documented costs: it is partial ($Δ$ remains supra-Bertrand), it is non-monotone in $δ$, and it does not survive Failure Mode 2, which emerges as DDPG critic divergence at $λ= 5$ and corrupts the phase-diagram cell at $(λ{=}5, δ{=}1)$. We accompany the scalar collusion index with trajectory-level trace diagnostics that expose the within-episode signalling collapse and the post-shock non-recovery.

</details>

---

### [[20_Research/Papers/强化学习/QSplitFL_Capability_Aware_Deep_Q-Learning_for_Optimal_Split_Point_Selection_in_Split_Federated_Learning|QSplitFL: Capability Aware Deep Q-Learning for Optimal Split Point Selection in Split Federated Learning]]

![[assets/2606.09869_figure.png|800]]

- **arXiv**: [2606.09869](https://arxiv.org/abs/2606.09869)
- **PDF**: https://arxiv.org/pdf/2606.09869
- **详细分析**: [[20_Research/Papers/强化学习/QSplitFL_Capability_Aware_Deep_Q-Learning_for_Optimal_Split_Point_Selection_in_Split_Federated_Learning|QSplitFL: Capability Aware Deep Q-Learning for Optimal Split Point Selection in Split Federated Learning]]
- **作者**: Nazmus Shakib Shadin, Xinyue Zhang, Jingyi Wang, Miao Pan
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Security, Systems

#### 研究背景与动机

《QSplitFL: Capability Aware Deep Q-Learning for Optimal Split Point Selection in Split Federated Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated Learning (FL) combined with Split Learning (SL) is a privacy preserving paradigm that enables training deep neural networks (DNNs) on resource constrained devices while reducing overall training cost. However, determining the optimal split point, meaning the layer where the model is divided still remains a critical challenge, especially when clients have heterogeneous hardware capabilities. Fixed split points can overload weak devices and increase the communication and server load, which slows convergence and reduces stability. This paper introduces QSplitFL, a novel capability-aware Deep Q-Network (DQN) framework for optimal split point selection in Split learning based Federated Learning (SFL) environments. Unlike existing approaches that rely on high-dimensional model weight representations, QSplitFL employs a lightweight state representation derived directly from client hardware metrics, including CPU utilization, memory, battery level, and network latency. The proposed framework incorporates a decayed loss-drop reward function that prioritizes early convergence, and a committee-based DQN architecture with majority voting to mitigate reward hacking. Extensive experiments on MNIST, Fashion-MNIST, CIFAR-10, and CIFAR-100 datasets using CNN, ResNet50, MobileNetV4, and ConvNeXt architectures demonstrate that our approach achieves better convergence and higher accuracy compared to existing methods, while effectively adapting to heterogeneous device resources. The source code is publicly available at https://github.com/AIPO-Lab/QSplitFL.

</details>

---

### [[20_Research/Papers/大模型/Can_Multi-Agent_LLMs_Identify_Their_Peers_Stylometric_Fingerprinting_in_Role-Constrained_Political_Analysis|Can Multi-Agent LLMs Identify Their Peers? Stylometric Fingerprinting in Role-Constrained Political Analysis]]

![[assets/2606.09854_figure.png|800]]

- **arXiv**: [2606.09854](https://arxiv.org/abs/2606.09854)
- **PDF**: https://arxiv.org/pdf/2606.09854
- **详细分析**: [[20_Research/Papers/大模型/Can_Multi-Agent_LLMs_Identify_Their_Peers_Stylometric_Fingerprinting_in_Role-Constrained_Political_Analysis|Can Multi-Agent LLMs Identify Their Peers? Stylometric Fingerprinting in Role-Constrained Political Analysis]]
- **作者**: Juergen Dietrich
- **cs 子类**: cs.AI, cs.CL, cs.CY, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Can Multi-Agent LLMs Identify Their Peers? Stylometric Fingerprinting in Role-Constrained Political Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent large language model (LLM) pipelines for political statement analysis are vulnerable to peer-preservation bias: models tend to protect peer models from deactivation and show identity-dependent scoring distortions. Prompt-level anonymization was proposed as a mitigation, but prior work simultaneously documented that stylometric fingerprints survive anonymization in role-constrained outputs - raising the question of whether this mitigation is sufficient. This paper provides the first systematic investigation of whether LLMs can identify the model family behind political analysis texts under anonymization conditions. We evaluate three classifier approaches - LLM zero-shot and few-shot (Claude Sonnet 4.6 and Llama-3.3-70B) and a fine-tuned T5-base model - on a five-class attribution task covering four commercial LLM families and an open-world 'unknown' class. We introduce a statement-disjoint cross-validation protocol (SD-CV; defined in Section 3.5) that guarantees no content overlap between training and validation data, and contrast it with a run-disjoint baseline (RD-CV). T5 achieves Macro F1 = 0.991 (+-0.008) under SD-CV and F1 = 0.978 on 24 completely held-out statements - robust despite a 2.1x increase in train-test content distance versus RD-CV (0.767 vs. 0.366, p&lt;0.001), demonstrating genuine stylometric generalization. A fractional SD-CV analysis identifies a performance knee at 40% of training data (~440 texts). Our findings confirm that prompt-level anonymization alone cannot neutralize model identity signals, with direct implications for EU AI Act compliance (Articles 13, 14, 26) and for computer system validation (CSV) in quality-critical multi-agent deployments.

</details>

---
