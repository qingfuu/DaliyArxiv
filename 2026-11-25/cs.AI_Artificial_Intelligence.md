# cs.AI | Artificial Intelligence | 2026-11-25

#arxiv #ComputerScience

**论文数**: 32

### [[20_Research/Papers/具身智能/Embodied_AI_Fails_the_Mirror_Test_How_a_Simple_Mirror_Breaks_Robot_Policies|Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies]]

![[assets/2611.33010_figure.png|800]]

- **arXiv**: [2611.33010](https://arxiv.org/abs/2611.33010)
- **PDF**: https://arxiv.org/pdf/2611.33010
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_AI_Fails_the_Mirror_Test_How_a_Simple_Mirror_Breaks_Robot_Policies|Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies]]
- **作者**: Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li, Wen Gao, Yonghong Tian, Weihao Yu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.6（加权：具身智能 3.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HallusionBench, IllusionVQA, MIRA-Bench, MirrorBench, MirrorQA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop conditions. Across five policies spanning Vision-Language-Action models, World Action Models, and agentic policies, every mirror condition reduces aggregate success rates: averaged over the three conditions, the drop ranges from 10.8 to 56.7 percentage points across policies, and it reaches 62.5 points on the mirrored tabletop. Because a mirror is also a physical obstacle, we compare it against geometrically matched non-reflective panels; 50--88\% of mirror-specific failures occur without recorded robot--panel contact, so direct collisions alone do not explain the degradation. Trajectory and contact analyses instead reveal recurring behaviors consistent with phantom targeting of reflected objects and spatial mislocalization of real ones. Targeted diagnostics further characterize grasping near reflections, policy-dependent pushing progress, and physical-target interaction under main-camera occlusion. Real-robot experiments with $π_{0.5}$ and FastWAM also show lower overall success rates under the upright-mirror and mirrored-tabletop conditions. These findings reveal a shared vulnerability to reflective environments across diverse robot policies and motivate reflection-aware evaluation of embodied intelligence. Code is available at https://github.com/iPPLab/robodojo-mirror.

</details>

---

### [[20_Research/Papers/机器人/CAPER_PartGround_and_PlanRefine_for_Reliable_Manual-Guided_Robotic_Assembly_Planning|CAPER: PartGround and PlanRefine for Reliable Manual-Guided Robotic Assembly Planning]]

![[assets/2611.32986_figure.png|800]]

- **arXiv**: [2611.32986](https://arxiv.org/abs/2611.32986)
- **PDF**: https://arxiv.org/pdf/2611.32986
- **详细分析**: [[20_Research/Papers/机器人/CAPER_PartGround_and_PlanRefine_for_Reliable_Manual-Guided_Robotic_Assembly_Planning|CAPER: PartGround and PlanRefine for Reliable Manual-Guided Robotic Assembly Planning]]
- **作者**: Hanzhao Xi, Zhonghao Li, Suxuan Liu, Shanghan Zhou, Zesheng Chen, Qiufeng Wang, Yaran Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CAPER: PartGround and PlanRefine for Reliable Manual-Guided Robotic Assembly Planning》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Models (VLMs) used in robot task planning to derive assembly procedures from existing manuals may correctly interpret individual assembly actions yet confuse exact part identities, predict unsupported Part IDs, or produce inconsistent parts across assembly steps. Thus, we propose CAPER (Capacity-Aware Part-grounding and Evidence Refinement), a manual-guided robotic assembly framework that enables VLMs to generate assembly procedures with two modules--PartGround and PlanRefine. PartGround aligns step-level manual evidence with product-specific inventory and part-reference information to identify exact Part IDs and quantities, transforming free-form hardware prediction into evidence-guided assignments represented in a shared Assembly Intermediate Representation (Assembly IR). PlanRefine audits PartGround assignments against finite inventory by removing the lowest-confidence assignments. Uncertain identity cases remain marked for review in the Assembly IR. We evaluate CAPER on the IKEA Assembly in the Wild (IAW) dataset. Experiment results show that CAPER reaches a Finite-inventory Consistency Rate of 83.33% and produces zero observed out-of-inventory Part-ID occurrences. At the plan level, PlanRefine removes all observed inventory-overuse pairs (9 -&gt; 0) and excess units (51 -&gt; 0). Overall, the results indicate that PartGround and PlanRefine improve part reliability, while also enhancing finite-inventory consistency and local prediction accuracy. Project page and video: https://xhzzzz123.github.io/CAPER/

</details>

---

### [[20_Research/Papers/具身智能/Motion_Conditioned_World_Modeling_for_Embodied_Visual_Tracking|Motion Conditioned World Modeling for Embodied Visual Tracking]]

![[assets/2611.32900_figure.png|800]]

- **arXiv**: [2611.32900](https://arxiv.org/abs/2611.32900)
- **PDF**: https://arxiv.org/pdf/2611.32900
- **详细分析**: [[20_Research/Papers/具身智能/Motion_Conditioned_World_Modeling_for_Embodied_Visual_Tracking|Motion Conditioned World Modeling for Embodied Visual Tracking]]
- **作者**: Jiahao Zhang, Xuan Yao, Junyu Gao, Changsheng Xu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 1.2，世界模型 0.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Motion Conditioned World Modeling for Embodied Visual Tracking》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：EVT-Bench, Real-World, TrackVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models support embodied decision-making by predicting future environment states. In embodied visual tracking, uncertain target motion and robot-induced viewpoint changes jointly affect visual observations, making future-state prediction challenging. We propose Motion-Conditioned World Modeling, which incorporates predicted target-motion distributions and robot ego-motion into latent state transitions. A Geometry--Progress module jointly models geometric paths and single-step travel distances through shared motion modes and path-conditioned progress distributions. This formulation captures uncertainty in route selection and motion progress while preserving their dependence. Action-induced coordinate transformations express predicted paths in the next robot frame, providing geometrically grounded conditions for future visual-state prediction. Future visual feature reconstruction supervises the motion predictor through the conditioned transition branch, linking explicit motion representations to subsequent observations. The model is jointly optimized with motion likelihood, feature reconstruction, and expert-action supervision, enabling the tracking policy to combine visual context with predictive motion cues.Experiments on three embodied tracking benchmarks demonstrate improved tracking performance and cross-environment generalization with a lightweight $0.5$B backbone.

</details>

---

### [[20_Research/Papers/大模型/Lazy_Agents_Answer_Against_Their_Own_Beliefs_Reinforcement_Learning_with_Verifiable_Beliefs_Teaches_Them_to_Act_on_What_They_Believe|Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe]]

![[assets/2611.32884_figure.png|800]]

- **arXiv**: [2611.32884](https://arxiv.org/abs/2611.32884)
- **PDF**: https://arxiv.org/pdf/2611.32884
- **详细分析**: [[20_Research/Papers/大模型/Lazy_Agents_Answer_Against_Their_Own_Beliefs_Reinforcement_Learning_with_Verifiable_Beliefs_Teaches_Them_to_Act_on_What_They_Believe|Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe]]
- **作者**: Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang, Soujanya Poria
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.6（加权：大模型 0.6，强化学习 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode scores only the final answer, so it cannot teach the agent when to commit, because a lucky guess receives the same reward as an answer backed by evidence. During training, however, the simulator can compute the exact posterior over the answer at every step and tell whether the evidence is already enough. We propose Reinforcement Learning with Verifiable Beliefs (RLVB), which rewards the agent for taking further steps while this posterior still allows several answers and for committing once the evidence is sufficient. The reward needs no judge, critic or reward model, and it never reads the belief line the agent writes before each action. We also introduce Pro Worlds, a benchmark of visual puzzles where the agent views a large world through a small window. We evaluate three vision-language models on three benchmarks, two of which are never seen in training. RLVB improves the base model in all nine settings, by 17.1% on average. Under the outcome reward, GRPO and PPO fall below the base model on average. RLVB also outperforms PPO with a process reward from an LLM judge by 9.3% on average while using 1.6 times fewer GPU-hours. The trained agent answers with sufficient evidence in 51%, 12% and 74% of the episodes on the three benchmarks, against 8%, 0.4% and 36% for the base model. Its accuracy gain therefore comes from answering more often at high levels of evidence. The belief line shows how the agent reaches this evidence: it acts on its own belief. It commits at only 0.1 to 2.2% of the turns at which the evidence is insufficient and its line still names several answers, against 3 to 68% for the base model.

</details>

---

### [[20_Research/Papers/具身智能/MRBench_Benchmarking_Physical_Necessity_Reasoning_in_Heterogeneous_Multi-Robot_Manipulation|MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation]]

![[assets/2611.32803_figure.png|800]]

- **arXiv**: [2611.32803](https://arxiv.org/abs/2611.32803)
- **PDF**: https://arxiv.org/pdf/2611.32803
- **详细分析**: [[20_Research/Papers/具身智能/MRBench_Benchmarking_Physical_Necessity_Reasoning_in_Heterogeneous_Multi-Robot_Manipulation|MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation]]
- **作者**: Yanzhe Chen, Zhijun Cao, Ruihe An, Chang Gong, Mike Zheng Shou
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《MRBench: Benchmarking Physical Necessity Reasoning in Heterogeneous Multi-Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MRBench, RoCoBench, VIKI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in multi-robot manipulation have shown how robots can collaborate to accomplish complex tasks. However, successful coordination does not reveal which robots are actually needed. The same task may require different teams as robot capabilities change, resources become unavailable, or objects replace robotic support. We argue that reliable multi-robot manipulation requires physical necessity reasoning: understanding what a task demands, which resources can fulfill those demands, and which are truly necessary. We introduce MRBench, a benchmark for physical necessity reasoning in heterogeneous multi-robot manipulation. It comprises eight tasks with distinct concurrency and reach constraints, each evaluated under five configurations that change the required resources while preserving the task goal. Our evaluation reveals that existing coordination agents perform well with reference teams but struggle when robot embodiments change or passive objects can replace robotic support. To address this gap, we propose MRScissors, which separates task requirements from measured physical capabilities and identifies minimal feasible teams through constrained search. Across two model backbones, MRScissors achieves 85.4% and 91.2% team-selection accuracy, outperforming the strongest baselines by 10.4 and 9.5 points, respectively. Together, these findings expose a critical gap between coordinating robots and understanding their physical necessity.

</details>

---

### [[20_Research/Papers/大模型/Are_We_Rewarding_the_Wrong_Module_Module-Specific_Policy_Optimization_for_Multimodal_Reinforcement_Learning|Are We Rewarding the Wrong Module? Module-Specific Policy Optimization for Multimodal Reinforcement Learning]]

![[assets/2611.32687_figure.png|800]]

- **arXiv**: [2611.32687](https://arxiv.org/abs/2611.32687)
- **PDF**: https://arxiv.org/pdf/2611.32687
- **详细分析**: [[20_Research/Papers/大模型/Are_We_Rewarding_the_Wrong_Module_Module-Specific_Policy_Optimization_for_Multimodal_Reinforcement_Learning|Are We Rewarding the Wrong Module? Module-Specific Policy Optimization for Multimodal Reinforcement Learning]]
- **作者**: HuiSeong Cho, Jun Yeong Park, Yu Rang Park
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.1（加权：大模型 0.5，强化学习 1.6）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Are We Rewarding the Wrong Module? Module-Specific Policy Optimization for Multimodal Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AT-RL, PEARL, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) based on Group Relative Policy Optimization (GRPO) has been widely adopted to enhance the multimodal reasoning of multimodal large language models (MLLMs). However, existing methods share a common limitation of Module-Level Credit Entanglement, in which the vision encoder, projector, and LLM modules are jointly optimized using the same advantage signals even when perceptual correctness and final-answer correctness differ. To address this limitation, we propose Module-Specific Policy Optimization (MSPO), a framework that separates perceptual and outcome-based learning signals across model modules. Specifically, MSPO uses responses to perception checklists comprising auxiliary questions about visual information to derive an advantage for training the vision encoder. From these responses, MSPO computes the Confidence-aware Perception Reward (CaPR), using a perception sign obtained by thresholding checklist accuracy to determine reward direction and posterior confidence from a Beta distribution over latent perception accuracy to scale reward magnitude. We then derive the vision advantage through group-relative normalization of CaPR and scale it using main-task success rates. This advantage guides updates to the vision encoder, while the projector and LLM retain outcome-based GRPO updates. Extensive experiments on seven mathematical and general reasoning benchmarks demonstrate that MSPO outperforms existing RL-tuned models on average at both the 3B and 7B scales.

</details>

---

### [[20_Research/Papers/大模型/Economic_World_Model|Economic World Model]]

![[assets/2611.32663_figure.png|800]]

- **arXiv**: [2611.32663](https://arxiv.org/abs/2611.32663)
- **PDF**: https://arxiv.org/pdf/2611.32663
- **详细分析**: [[20_Research/Papers/大模型/Economic_World_Model|Economic World Model]]
- **作者**: Qirui Mi, Yujia Ming, Bo Li, Haifeng Zhang
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.2（加权：大模型 0.2，世界模型 1）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《Economic World Model》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EconGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can artificial intelligence reproduce the economic dynamics that emerge as households, firms and governments interact and adapt through markets and institutions? To answer this question, we define an economic world model (EWM) as an agent's internal representation of how an economic system works, enabling counterfactual simulation and decision-making under resource constraints. We then propose a general framework for studying EWMs that links three tasks: simulating agent behaviour, learning economic transitions and systematically evaluating the dynamics. As an initial implementation, we learn household policies from microeconomic data and calibrate a structural economic transition model using macroeconomic data, linking individual decisions to aggregate dynamics. Our micro-to-macro evaluation framework compares simulated individual actions and group distributions with observed microdata and assesses macroeconomic dynamics through forecasting and counterfactual experiments. Results show that simulated and observed household consumption distributions overlap by 94.9%, while EWM forecasts closely track real GDP and several other aggregate levels. In government-borrowing counterfactuals, the EWM reproduces the benchmark life-cycle model's short-run transmission from borrowing to consumption. For ex ante planning, the EWM enables an LLM agent to achieve 10.29% higher simulated GDP under the epidemic shock than direct LLM decisions. This initial EWM is only a starting point. We invite economists and AI researchers to build a stronger EWM together. Economists can contribute richer economic models and knowledge, while AI researchers can develop stronger data-driven methods for simulating agent behaviour and learning economic transitions. Together, we aim not only to reproduce real economic dynamics, but also to discover and test new mechanisms that support better decisions and benefit society.

</details>

---

### [[20_Research/Papers/具身智能/DexWAC_A_Unified_World-Actor-Critic_Model_for_Dexterous_Robot_Manipulation|DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation]]

![[assets/2611.32654_figure.png|800]]

- **arXiv**: [2611.32654](https://arxiv.org/abs/2611.32654)
- **PDF**: https://arxiv.org/pdf/2611.32654
- **详细分析**: [[20_Research/Papers/具身智能/DexWAC_A_Unified_World-Actor-Critic_Model_for_Dexterous_Robot_Manipulation|DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation]]
- **作者**: Hongjia Liu, Dacheng Zhou, Minghao Fu, Chuanjun Guo, Tianze Wang, Qingtao Liu, He Wang, Li Yi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.8（加权：具身智能 2.7，强化学习 0.8，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success. Recent world-action models (WAMs) extend vision-language-action (VLA) models with the first signal by jointly predicting actions and future observations, yet this predictive ability serves only as an auxiliary loss for policy learning. Meanwhile, most policy improvement methods learn dynamics and values in separate models, increasing training overhead and limiting representation sharing between these complementary objectives. We introduce DexWAC, a unified world-actor-critic model that jointly learns an actor, an action-conditioned world model, and a bootstrapped critic in a single robot pretraining stage. Our key insight is that visual prediction encourages control-relevant features, while value supervision promotes task-relevant representations; together, they shape a representation suited to policy learning. Built on an image-editing backbone, DexWAC predicts, for each action chunk, the visual latent and proprioception at its endpoint together with its reward and continuation, so the world model alone efficiently yields complete imagined transitions without generating intermediate video frames. After adapting the world model and critic on real rollouts, we improve the pretrained actor through either PPO on imagined rollouts or critic-guided best-of-$N$ selection. DexWAC surpasses the large-scale pretrained VLA and WAM baselines in simulation and achieves 75% average success on two real-world tasks, compared with 45% for $π_{0.5}$. Its world model is more accurate and faster than video-based baselines, and ablations confirm that learning dynamics and value together improves the policy.

</details>

---

### [[20_Research/Papers/机器人/ICLWorld_Benchmarking_In-Context_Learning_of_Agents_from_Digital_to_Physical_Worlds|ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds]]

![[assets/2611.32649_figure.png|800]]

- **arXiv**: [2611.32649](https://arxiv.org/abs/2611.32649)
- **PDF**: https://arxiv.org/pdf/2611.32649
- **详细分析**: [[20_Research/Papers/机器人/ICLWorld_Benchmarking_In-Context_Learning_of_Agents_from_Digital_to_Physical_Worlds|ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds]]
- **作者**: Qingle Liu, Jieming Li, Pei-lin Li, Shenghan Zheng, Ruize Yang, Sunqi Fan, Deyao Hong, Huan-ang Gao, Meng-Hao Guo, Shuojin Yang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, CLBench, ICLWorld, MMCL-Bench, OSWorkerBench, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline, rely on text or static images, and risk training-data contamination, while robot evaluations are limited to method-level ablations. We present ICLWorld, an online benchmark that evaluates the ICL of agents from digital to physical worlds, covering computer use and robot use, together with UIverse, a unified harness that turns every environment into a user interface. We build 30 environments, record 630 demonstration videos (10+ hours), and design 160 tasks with customized, often counter-intuitive rules that cannot be satisfied without learning from the context. Each task comes with three rule versions, given as text or video, and we test generalization at three levels, from replaying the demonstration to new instances and unseen environments. Across six frontier models, the strongest agents, Claude Opus 5.5 and GPT-6 Astra, succeed on 82% and 76% of computer-use runs but only 27% and 26% of robot-use runs, and a no-rule control reduces success to at most 8%. GPT-6 Astra succeeds under all three rule versions on only 38% of computer-use tasks, half its rate under a single rule, and answers 98% of robot rule questions correctly yet completes only 20% of these tasks. Frontier agents learn rules comparably well from video and from text and transfer them across environments, whereas weaker agents rely on text and lose most of their video-based success once the demonstrated situation is resampled. These findings reveal substantial gaps between the digital and the physical world and between identifying a rule and acting on it.

</details>

---

### [[20_Research/Papers/强化学习/TeamFlowRL_Online_Policy_Optimization_of_Decentralized_Flow_Policies_for_Multi-Agent_Coordination|TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination]]

![[assets/2611.32645_figure.png|800]]

- **arXiv**: [2611.32645](https://arxiv.org/abs/2611.32645)
- **PDF**: https://arxiv.org/pdf/2611.32645
- **详细分析**: [[20_Research/Papers/强化学习/TeamFlowRL_Online_Policy_Optimization_of_Decentralized_Flow_Policies_for_Multi-Agent_Coordination|TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination]]
- **作者**: Guowei Zou, Beiwen Zhang, Haitao Wang, Hong Hong, Zhiquan Chen, Hejun Wu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《TeamFlowRL: Online Policy Optimization of Decentralized Flow Policies for Multi-Agent Coordination》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL, TeamFlowRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Complex cooperative tasks require coordinated multi-agent behavior. Offline generative policies learn expressive cooperative behaviors from trajectories but remain limited by fixed datasets. Online reinforcement learning can improve them through environment interaction. However, fine-tuning flow policies is difficult because action likelihoods are hard to compute. We propose TeamFlowRL, a two-stage framework that pretrains multi-agent flow policies offline and fine-tunes them online. We formulate team policy optimization over the complete denoising trajectories of decentralized flow policies, avoiding intractable action likelihoods. The resulting objective weights each agent's trajectory ratio with a shared team advantage and clips each ratio separately, aligning local policy updates with the common team return. Across 51 paired configurations in seven simulation groups, TeamFlowRL improves every offline initialization, with a 47.3% average gain in normalized score. It also achieves 33.1% higher average success under exploration noise than Gaussian-policy fine-tuning across 6 bimanual tasks.

</details>

---

### [[20_Research/Papers/强化学习/BARE_Body-Aware_Reflexive_Evasion_for_Humanoid_Robots|BARE: Body-Aware Reflexive Evasion for Humanoid Robots]]

![[assets/2611.32642_figure.png|800]]

- **arXiv**: [2611.32642](https://arxiv.org/abs/2611.32642)
- **PDF**: https://arxiv.org/pdf/2611.32642
- **详细分析**: [[20_Research/Papers/强化学习/BARE_Body-Aware_Reflexive_Evasion_for_Humanoid_Robots|BARE: Body-Aware Reflexive Evasion for Humanoid Robots]]
- **作者**: Zihao Li, Tong Chen, Hua Song, Zitong Ding, Zihao Xu, Ce Hao, Weibang Bai
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《BARE: Body-Aware Reflexive Evasion for Humanoid Robots》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FootstepNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic obstacle avoidance is essential for safely deploying humanoid robots in real-world environments, where rapidly approaching objects require immediate evasive responses. Recent advances in reflexive evasion have focused primarily on quadrupeds, which typically rely on large-scale whole-body maneuvers. In contrast, humanoids can exploit their rich body articulation to evade through small, localized body adjustments. By moving threatened body regions without repositioning the entire body, these responses may require less execution time and less surrounding free space. However, local adjustments can alter mass distribution or support conditions, making it challenging to achieve rapid evasion while maintaining whole-body stability. To this end, we propose BARE (Body-Aware Reflexive Evasion), a humanoid reflexive evasion framework guided by human motion priors that enables rapid local evasion while maintaining whole-body stability. A risk-guided motion adapter is designed to select reference motions from a retargeted human evasive motion library based on the threatened body region and to adjust their temporal phases based on collision urgency, allowing the robot to reach evasive postures before potential contact. Conditioned on the adapted reference and link-level collision risk, a reflexive evasion policy learns through reinforcement learning to coordinate local body adjustments with whole-body stabilization. We validate BARE in simulation and real-world experiments, demonstrating its ability to perform targeted local evasion while maintaining whole-body stability.

</details>

---

### [[20_Research/Papers/具身智能/ReFocus_Progress-Guided_Adaptive_Practice_for_Long-Horizon_Robotic_Manipulation_Reinforcement_Learning|ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning]]

![[assets/2611.32639_figure.png|800]]

- **arXiv**: [2611.32639](https://arxiv.org/abs/2611.32639)
- **PDF**: https://arxiv.org/pdf/2611.32639
- **详细分析**: [[20_Research/Papers/具身智能/ReFocus_Progress-Guided_Adaptive_Practice_for_Long-Horizon_Robotic_Manipulation_Reinforcement_Learning|ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning]]
- **作者**: Haoyuan Li, Wei Huang, Jiehong Lin, Shengrong Zhang, Chenzhi Liu, Shengchao Zhou, Hehe Fan, Xiaojuan Qi, Yi Yang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.4（加权：具身智能 1.5，强化学习 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online reinforcement learning (RL) enables vision-language-action policies to improve through environmental interaction. However, in long-horizon manipulation, sparse success/failure feedback provides little information about where policies encounter bottlenecks. Moreover, repeated full-task rollouts also leave these bottlenecks weakly analyzed and insufficiently practiced. To this end, we introduce ReFocus, a progress-guided multi-round RL framework that alternates between Global and Local RL to identify task-specific bottlenecks and allocate additional practice to them. Specifically, during Global RL, we decompose each task into a Directed Acyclic Graph (DAG) of subtasks. Then a DAG-based Progress Reward is leveraged for both policy training and bottleneck diagnosis. Based on the identified bottlenecks, ReFocus selects Adaptive Practice Windows, defining task segments from an entry stage to a target stage. It allocates additional interaction to these segments during Local RL while updating the entire policy. After that, it evaluates the policy to perform the full task for the next round of RL, forming an iteration between Global and Local RL. Experiments on LIBERO-Long and RoboCasa365 show that ReFocus achieves success rates of 97.8% and 51.3%, respectively, compared with 90.6% and 39.3% for the $π_{0.5}$ baseline. Furthermore, we evaluate a real-world adaptation on three long-horizon tasks. On BreadBaker, ReFocus achieves 95% success, compared with 30% for the $π_{0.5}$. Project page: https://refocus-robotics.github.io.

</details>

---

### [[20_Research/Papers/具身智能/MXI-MemICL_Towards_In-Context_Robot_Manipulation_through_Self-Retrieved_Interaction_Memory|MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory]]

![[assets/2611.32564_figure.png|800]]

- **arXiv**: [2611.32564](https://arxiv.org/abs/2611.32564)
- **PDF**: https://arxiv.org/pdf/2611.32564
- **详细分析**: [[20_Research/Papers/具身智能/MXI-MemICL_Towards_In-Context_Robot_Manipulation_through_Self-Retrieved_Interaction_Memory|MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory]]
- **作者**: Jialong Peng, Shihao Zhou, Feng Yan, Wen Xiao, Haozheng Wang, Wenqi Ren, Wenyuan Sheng, Jian Qiao, Jiaxu Miao, Lin Ma, Chao Yang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《MXI-MemICL: Towards In-Context Robot Manipulation through Self-Retrieved Interaction Memory》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BehaviorVLA, OpenVLA, Real-World, StellaVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In-context learning (ICL) offers robots a way to acquire new skills from a single demonstration without parameter updates. However, existing robotic ICL methods either rely on large-scale pretraining constrained by scarce, costly robot interaction data or require additional annotations yet struggle to generalize across tasks. To bridge this gap, we propose MXI-MemICL, a framework for memory-guided ICL in vision-language-action (VLA) models. By treating demonstrations as retrievable memory, MXI-MemICL enables in-context manipulation without additional large-scale pretraining or specialized annotations. Specifically, a visual-action causal encoder turns actions and their observed effects in demonstrations and completed interactions into reusable memory to guide execution. To retrieve experience suited to upcoming execution, an intention predictor forecasts the next stage's intent and uses it to query memory. The retrieved experience conditions the language backbone through experience-token prefixes and gated cross-attention, guiding action generation with a learned gate that regulates its influence. MXI-MemICL improves success over the baseline by +8.2% and +14.4% on RoboCasa365 and RoboTwin 2.0. Real-robot experiments show a +9.0% gain, with demonstrations adding +5.0% on seen and +16.7% on unseen tasks. The code will be made publicly available.

</details>

---

### [[20_Research/Papers/具身智能/Next-Manip_On-Demand_Agent-Policy_Collaboration_for_Robotic_Manipulation|Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation]]

![[assets/2611.32533_figure.png|800]]

- **arXiv**: [2611.32533](https://arxiv.org/abs/2611.32533)
- **PDF**: https://arxiv.org/pdf/2611.32533
- **详细分析**: [[20_Research/Papers/具身智能/Next-Manip_On-Demand_Agent-Policy_Collaboration_for_Robotic_Manipulation|Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation]]
- **作者**: Jiayi Liu, Ke Ye, Jiaming Zhou, Yufei Huang, Haotian Liang, Kun-Yu Lin, Junwei Liang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.5，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Next-Manip: On-Demand Agent-Policy Collaboration for Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robotic manipulation requires task reasoning, failure recovery, and precise control, yet limited manipulation data make these abilities difficult to obtain from a single policy. Recent multimodal agents show promise in task reasoning and recovery but lack reliable fine-grained control and incur high inference cost, whereas learned policies provide efficient fine-grained execution but struggle beyond their learned skills. Although their complementary strengths suggest combining the two, doing so requires repeatedly deciding which executor should act as task demands change. Instead of relying on the agent for each decision, we present Next-Manip, an on-demand agent--policy collaboration framework that decouples executor allocation from costly agent inference. We propose an Agent Invocation Controller (AIC) that allocates control between the policy and the agent through a lightweight classifier of current execution demands. We further introduce Task Dynamics Context (TDC), which packages informative manipulation changes from in-context examples into compact task references to support both agent reasoning and executor allocation. Across two simulation benchmarks and real-world experiments, Next-Manip achieves state-of-the-art performance while reducing agent inference costs.

</details>

---

### [[20_Research/Papers/强化学习/Assessing_Robustness_to_Catastrophic_Forgetting_in_Continual_Deep_Reinforcement_Learning_for_Cyber-Physical_Systems|Assessing Robustness to Catastrophic Forgetting in Continual Deep Reinforcement Learning for Cyber-Physical Systems]]

![[assets/2611.32496_figure.png|800]]

- **arXiv**: [2611.32496](https://arxiv.org/abs/2611.32496)
- **PDF**: https://arxiv.org/pdf/2611.32496
- **详细分析**: [[20_Research/Papers/强化学习/Assessing_Robustness_to_Catastrophic_Forgetting_in_Continual_Deep_Reinforcement_Learning_for_Cyber-Physical_Systems|Assessing Robustness to Catastrophic Forgetting in Continual Deep Reinforcement Learning for Cyber-Physical Systems]]
- **作者**: Kim N. Nolle, Ivana Dusparic, Rhodri Cusack, Vinny Cahill
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.22（加权：大模型 0.1，强化学习 1.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Assessing Robustness to Catastrophic Forgetting in Continual Deep Reinforcement Learning for Cyber-Physical Systems》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As the use of reinforcement learning (RL) becomes more widespread in cyber-physical systems, it becomes increasingly important to design RL agents that are able to adapt to changes in their environments in order to maintain safety and reliability. This paper addresses the question of whether different classes of RL algorithm are more robust against forgetting previously learned behaviours, a critical issue in continual learning, in non-stationary environments. We evaluate the robustness of representative examples of three important classes of RL algorithm in a non-stationary autonomous parking environment. These are Proximal Policy Optimization (PPO), which is a model-free on-policy algorithm, Soft-Actor-Critic (SAC), which is a model-free off-policy algorithm, and Drama, which is a model-based algorithm. The agents must learn to successfully park in four different scenarios, which are presented successively, with parking spaces oriented at varying angles. We find off-policy algorithms appear to be more robust compared to on-policy algorithms due to their use of replay, while model-based algorithms do not appear to offer any direct advantage over model-free algorithms. These experiments also highlight the additional challenges of finding robust abstractions of the environment, and oversensitivity to hyperparameters.

</details>

---

### [[20_Research/Papers/具身智能/Does_Research-Paper_Context_Improve_LLM-Generated_Quadruped_Navigation_An_Exploratory_Simulation_Study|Does Research-Paper Context Improve LLM-Generated Quadruped Navigation? An Exploratory Simulation Study]]

![[assets/2611.32381_figure.png|800]]

- **arXiv**: [2611.32381](https://arxiv.org/abs/2611.32381)
- **PDF**: https://arxiv.org/pdf/2611.32381
- **详细分析**: [[20_Research/Papers/具身智能/Does_Research-Paper_Context_Improve_LLM-Generated_Quadruped_Navigation_An_Exploratory_Simulation_Study|Does Research-Paper Context Improve LLM-Generated Quadruped Navigation? An Exploratory Simulation Study]]
- **作者**: Barnabas Juhasz, Rolf Pfister
- **cs 子类**: cs.AI, cs.RO, cs.SE
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.8（加权：具身智能 2.1，大模型 0.4，机器人 1.3）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《Does Research-Paper Context Improve LLM-Generated Quadruped Navigation? An Exploratory Simulation Study》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can write competent robot navigation code, but not only does the research on the topic advance, a model may also, due to the volume of findings, fail to recall relevant findings and apply them to the task at hand. In this work, we test whether providing particular research papers as context improves the LLM-written navigation code for the Go2 quadruped, with the LLM (Claude Opus 5) and locomotion policy frozen. Specifically, we compare the navigation controllers the LLM writes when provided with and without particular papers across three settings: behavior trees, navigators edited from a shared base, and controllers written from scratch. When a maze's shortest route is blocked mid-episode, 2 of 8 controllers written with the context of an incremental-replanning paper complete all four trips under Isaac Sim physics, against 7 of 8 without it (two-sided Fisher's exact test, p = 0.041). This difference appears only under physics: in an idealized kinematic simulator, the controllers written with and without the paper are indistinguishable. We hypothesize that an LLM provided research papers as context tends to overweight both their content and their goals -- in this case, the efficiency of incremental replanning -- negatively affecting the fulfillment of the main task and leading to less robust code.

</details>

---

### [[20_Research/Papers/大模型/ASTERISM_Do_Multimodal_LLMs_Actually_Look_at_All_the_Images|ASTERISM: Do Multimodal LLMs Actually Look at All the Images?]]

![[assets/2611.32316_figure.png|800]]

- **arXiv**: [2611.32316](https://arxiv.org/abs/2611.32316)
- **PDF**: https://arxiv.org/pdf/2611.32316
- **详细分析**: [[20_Research/Papers/大模型/ASTERISM_Do_Multimodal_LLMs_Actually_Look_at_All_the_Images|ASTERISM: Do Multimodal LLMs Actually Look at All the Images?]]
- **作者**: Chanseul Cho, Dongwoo Kim, Noori Bae, Seungjae Moon, Seongsu Lee, Youngmin Ro
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.85，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《ASTERISM: Do Multimodal LLMs Actually Look at All the Images?》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MuirBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-image benchmarks aim to test whether a multimodal large language model (MLLM) combines evidence across images, but many of their items can be answered from a single image. Across about 33k items from 19 public benchmarks, our audit and a two-stage single-image filter find that one image or the question alone settles 24.2% of them. On these items, MLLMs recover from one image a median 78% of the accuracy that all images add over the text alone, so these items reward answering from one image, which we call the single-image shortcut. MLLMs take this shortcut even on items where one image is not enough. On such items, most of their wrong answers repeat an answer they give from one image, at a rate well above chance. We build ASTERISM, to our knowledge the largest audited multi-image benchmark, from these 19 benchmarks by keeping their items that need more than one image. Its 18.7k items, 2.0k of them corrected or rewritten, share one format, one scorer and seven task categories. We also release ASTERISM-Train with 49k training items and ASTERISM-Lite, a hard subset whose items we manually verify one by one. On ASTERISM-Lite, the strongest proprietary MLLM scores 68%. Reinforcement learning with verifiable rewards (RLVR), now common in MLLM post-training, rewards the shortcut as well, because a correct answer read off one image earns as much reward as one that combines images. In line with this, existing RLVR objectives add little to the ASTERISM score. To stop rewarding the shortcut in training as ASTERISM does in evaluation, we propose cross-image credit assignment (CICA), an extension of RLVR that moves the credit toward the tokens that need more than one image. On three open-source MLLMs, CICA raises the ASTERISM score by 2.6 to 6.0 points, more than twice the gain of each general and vision-specific RL objective trained on the same data.

</details>

---

### [[20_Research/Papers/具身智能/Sparse_Poison,_Strong_Hijack_Efficient_Trajectory-Level_Backdoors_in_Vision-Language-Action_Models_with_Only_1_%_Poisoning|Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning]]

![[assets/2611.32304_figure.png|800]]

- **arXiv**: [2611.32304](https://arxiv.org/abs/2611.32304)
- **PDF**: https://arxiv.org/pdf/2611.32304
- **详细分析**: [[20_Research/Papers/具身智能/Sparse_Poison,_Strong_Hijack_Efficient_Trajectory-Level_Backdoors_in_Vision-Language-Action_Models_with_Only_1_%_Poisoning|Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning]]
- **作者**: Simin Huang, Jiawei Chen, Shaolong Zhu, Qiwei Liang, Zhaoxia Yin
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.1，机器人 0.4）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Sparse Poison, Strong Hijack: Efficient Trajectory-Level Backdoors in Vision-Language-Action Models with Only 1\% Poisoning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BackdoorVLA, BadVLA, DropVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models advance robotic manipulation, but their reliance on demonstrations exposes them to backdoor threats. Among these threats, trajectory-level targeted backdoors are particularly challenging and may pose greater safety risks than behavior-disrupting attacks: rather than merely causing task failures or local action deviations, they must sustain closed-loop redirection to complete an attacker-specified multi-step task. To reliably induce such behaviors, existing methods typically rely on high poisoning rates to obtain sufficient target-trajectory supervision. However, high poisoning rates may compromise clean-task performance, whereas low rates leave target-trajectory supervision scarce and backdoor learning vulnerable to interference from dominant clean-task updates. To resolve this trade-off at low poisoning rates, we propose a two-stage co-optimization framework guided by vision, language, and action. Stage I freezes the policy and uses differentiable rendering and multimodal supervision to optimize a 3D trigger's texture, translation, and scale, strengthening trigger-target associations from limited poisoned demonstrations. Building on the optimized trigger, Stage II applies source-selective dual-LoRA adaptation to decouple clean and backdoor updates and mitigate their interference, followed by learned column-wise calibration and analytic fusion into a unified policy. Experiments on OpenVLA, OpenVLA-OFT, $π_0$, and $π_{0.5}$ across four LIBERO suites show consistent gains over all evaluated attack baselines. With only 1% poisoned data, our method achieves 86.4% target success and 95.2% clean-task success on OpenVLA-OFT in LIBERO-Spatial. Real-robot trials also demonstrate trajectory-level hijacking.

</details>

---

### [[20_Research/Papers/具身智能/Boundary-Aware_Policy_Learning_for_Agent-Orchestrated_Robot_Manipulation|Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation]]

![[assets/2611.32238_figure.png|800]]

- **arXiv**: [2611.32238](https://arxiv.org/abs/2611.32238)
- **PDF**: https://arxiv.org/pdf/2611.32238
- **详细分析**: [[20_Research/Papers/具身智能/Boundary-Aware_Policy_Learning_for_Agent-Orchestrated_Robot_Manipulation|Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation]]
- **作者**: Kaipeng Fang, Yuhao Wang, Ji Zhang, Yunsong Zhou, Jingkuan Song, Lianli Gao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.2，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LingBot-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, while the agent may invoke it outside this region. We call this region the policy's handoff boundary. Existing whole-task policies typically have handoff boundaries that are narrow and difficult for an agent to characterize, making reliable coordination challenging. We propose Boundary-Aware Policy Learning, which explicitly shapes and then expands the handoff boundary of a visuomotor policy. First, Boundary-Explicit Training fine-tunes the policy on contact segments with diverse start poses, yielding a wide and well-defined boundary that can be communicated to the agent through a simple handoff protocol. Second, Boundary-Expanding Self-Improvement retrains the policy on curated successful system rollouts, extending the boundary toward earlier stages of each task and allowing the agent to hand over sooner with fewer language-model calls. Across RoboTwin 2.0 and RoboDojo, our system outperforms the strongest baseline by over 26 percentage points, reaching 98.4% success in randomized RoboTwin 2.0 scenes, while further reducing its API cost and execution time by 41.3% and 37.5%, respectively. These results suggest that the key to robust agent-policy orchestration lies not only in improving either component individually, but also in explicitly shaping the boundary between them.

</details>

---

### [[20_Research/Papers/具身智能/Roboclock_A_Unified_Benchmark_for_Time-Aware_Robotic_Intelligence|Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence]]

![[assets/2611.32233_figure.png|800]]

- **arXiv**: [2611.32233](https://arxiv.org/abs/2611.32233)
- **PDF**: https://arxiv.org/pdf/2611.32233
- **详细分析**: [[20_Research/Papers/具身智能/Roboclock_A_Unified_Benchmark_for_Time-Aware_Robotic_Intelligence|Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence]]
- **作者**: Yujie Zhao, Anthony L. Hu, Zimeng Huang, Zhijing Wu, Luobin Wang, Richard Li, Shrivas Sudharsan, Henrik I. Christensen, Jishen Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Roboclock: A Unified Benchmark for Time-Aware Robotic Intelligence》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DynamicVLA, OpenVLA, RLBench, ReflexBench, ReflexVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Time is a fundamental dimension of robotic intelligence: a robot may fail despite physically correct actions if it acts outside a valid time window, responds too slowly to an event, or fails to meet required throughput. Yet existing robotic benchmarks primarily emphasize spatial correctness and logical task completion, largely overlooking the temporal constraints of real-world applications. We present RoboClock, a unified benchmark for time-aware robotic manipulation featuring 60 tasks across five application domains. Mirroring these failure modes, RoboClock structures tasks around three types of temporal constraints: Temporal Window, Event-Reactive, and Throughput. Furthermore, RoboClock incorporates a Latency-Aligned evaluation protocol that continuously advances environment time during model inference and control-interface delays, paired with time-sensitive metrics. Evaluating over 30 methods, we find that the best-performing approach is the trained VLA, yet it achieves only 8.3% temporal success even on Easy-level tasks, with persistent challenges in generalization and transfer. These findings reveal fundamental limitations in current robotic systems and highlight the need to jointly optimize physical competence, temporal reasoning, and execution latency.

</details>

---

### [[20_Research/Papers/具身智能/CoverMem_Coverage-Constrained_Visual_Memory_for_Budgeted_Embodied_Question_Answering|CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering]]

![[assets/2611.32119_figure.png|800]]

- **arXiv**: [2611.32119](https://arxiv.org/abs/2611.32119)
- **PDF**: https://arxiv.org/pdf/2611.32119
- **详细分析**: [[20_Research/Papers/具身智能/CoverMem_Coverage-Constrained_Visual_Memory_for_Budgeted_Embodied_Question_Answering|CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering]]
- **作者**: Ruijie Ma, Haoyue Liu, Mingda Zhang, Dongxu Yue, Xiaoying Tang
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《CoverMem: Coverage-Constrained Visual Memory for Budgeted Embodied Question Answering》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EM-EQA, EQA, OpenEQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Episodic-memory embodied question answering enables agents to answer questions based on previously recorded visual observations of the surrounding scenes. However, growing observation histories, varying observation quality across viewpoints, and limited computational resources make it challenging to construct and maintain compact visual memories while retrieving sufficient evidence for question answering. To address these challenges, we introduce CoverMem, which incorporates three key components: (1) a coverage-constrained memory construction method that selects a compact set of informative full frames satisfying object-quality and representative-scene coverage requirements; (2) a coverage-preserving incremental maintenance strategy that locally reselects only the affected frames to satisfy updated coverage requirements as observations arrive; and (3) a budgeted complementary frame selection method that balances question relevance, additional support for question requirements, and redundancy with selected frames within a fixed budget. Experimental results on three benchmarks covering diverse environments and question types demonstrate that CoverMem improves question-answering performance under limited visual budgets.

</details>

---

### [[20_Research/Papers/机器人/MARGIN_A_Risk-Aware_Agent_for_Robot_Program_Refinement|MARGIN: A Risk-Aware Agent for Robot Program Refinement]]

![[assets/2611.32093_figure.png|800]]

- **arXiv**: [2611.32093](https://arxiv.org/abs/2611.32093)
- **PDF**: https://arxiv.org/pdf/2611.32093
- **详细分析**: [[20_Research/Papers/机器人/MARGIN_A_Risk-Aware_Agent_for_Robot_Program_Refinement|MARGIN: A Risk-Aware Agent for Robot Program Refinement]]
- **作者**: Hongbo Duan, Fan Du, Haipeng Luo, Bin Qian, Zichao Nie, Yilin Mi, Yaopeng Tian, Jiake Tian, Siyuan Liu, Yan Gao, Fangming Liu, Xueqian Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《MARGIN: A Risk-Aware Agent for Robot Program Refinement》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RobotWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-programming agents improve executable control policies through repeated testing and repair, yet binary success saturates while execution risk persists across unseen scenes. We introduce MARGIN, a risk-aware agent that converts successful robot rollouts into actionable evidence for program refinement. Its near-miss margin measures the fraction of the execution budget remaining in the slowest successful development rollout. The agent uses this signal to prioritize fragile programs, guide targeted repairs, and select revisions that preserve development success while increasing execution headroom. An exact safe-racing rule accelerates success-based candidate evaluation. We evaluate MARGIN across LIBERO-Pro, LIBERO-90, and Robosuite. In our 80-task LIBERO-Pro reproduction, 78 programs attain perfect development success while accounting for substantial failures on unseen seeds. The near-miss margin predicts held-out failures with an AUC of 0.774, and low-margin programs exhibit 2.97 times higher failure risk. Across two independent evaluation rounds spanning 37 unique LIBERO-Pro tasks, MARGIN reduces executed control steps by 10.7% and 15.0%, with reductions of 18.0-20.0% on LIBERO-90 and Robosuite. Safe racing reduces fixed-sequence candidate-evaluation episodes by 53.5% while retaining identical selections, and paired execution probes improve acceptance decisions by identifying hidden regressions. Together, these results establish near-miss evidence as an effective basis for risk-aware, budget-efficient robot program refinement.

</details>

---

### [[20_Research/Papers/强化学习/More_Powerful,_Less_Verifiable_Mitigating_Hard-to-Verify_Hallucinations_in_MLLM's_Reinforcement_Learning|More Powerful, Less Verifiable? Mitigating Hard-to-Verify Hallucinations in MLLM's Reinforcement Learning]]

![[assets/2611.32055_figure.png|800]]

- **arXiv**: [2611.32055](https://arxiv.org/abs/2611.32055)
- **PDF**: https://arxiv.org/pdf/2611.32055
- **详细分析**: [[20_Research/Papers/强化学习/More_Powerful,_Less_Verifiable_Mitigating_Hard-to-Verify_Hallucinations_in_MLLM's_Reinforcement_Learning|More Powerful, Less Verifiable? Mitigating Hard-to-Verify Hallucinations in MLLM's Reinforcement Learning]]
- **作者**: Jianhong Pang, Ziyi Ye, Qiuxia Hou, Yanhao Zhang, Zuxuan Wu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《More Powerful, Less Verifiable? Mitigating Hard-to-Verify Hallucinations in MLLM's Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) strengthens model capabilities through feedback from humans and environments. However, emerging evidence suggests that reward optimization can produce outputs whose errors are harder for humans to detect. To address this issue, we construct ITHV (the Image-Text Hallucination Verifiability Dataset), comprising 2,728 visually grounded instances that distinguish between obvious hallucinations, which humans readily detect, and elusive hallucinations, which humans struggle to identify. We then propose DAPO-V, an extension of DAPO that maximizes correctness subject to a budget on verifiability-aware risk. Specifically, DAPO-V combines a verifiability-aware reward with adaptive dual control, where larger penalties are assigned to incorrect responses on questions with lower human verification accuracy. An adaptive multiplier further adjusts the penalty strength according to risk-budget violations. Across three MLLM base models, DAPO-V improves overall accuracy while substantially improving accuracy on elusive hallucination questions by 5.78--9.72 percentage points over accuracy-only DAPO. We further test DAPO-V with a blinded human study, which shows that hallucinations are more readily detected in DAPO-V than those of the base model.

</details>

---

### [[20_Research/Papers/具身智能/EffectWAM_Learning_Action-Grounded_Effects_for_Robot_Manipulation|EffectWAM: Learning Action-Grounded Effects for Robot Manipulation]]

![[assets/2611.32053_figure.png|800]]

- **arXiv**: [2611.32053](https://arxiv.org/abs/2611.32053)
- **PDF**: https://arxiv.org/pdf/2611.32053
- **详细分析**: [[20_Research/Papers/具身智能/EffectWAM_Learning_Action-Grounded_Effects_for_Robot_Manipulation|EffectWAM: Learning Action-Grounded Effects for Robot Manipulation]]
- **作者**: Yuan Zhang, Hao Cui, Jingfei Ni, Meiyi Wang, Xin Nie, Chi Liu, Wenjie Xu, Lin Gao, Hao Li, Xianhe Zhang, Jiajia Wu, Diyuan Liu...
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，机器人 0.8）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《EffectWAM: Learning Action-Grounded Effects for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EscherNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models connect visual prediction with executable robot control. We present EffectWAM, which develops this connection through three complementary components: Effect, camera positional encoding (CaPE), and Action Grounding. Effect represents visual change as the difference between independently encoded future observations and a shared current-observation anchor. CaPE conditions endpoint pooling on relative camera pose when reliable extrinsics are available, while sharing the same learned parameters with pose-free pooling for uncalibrated trajectories. Action Grounding trains the visual representation to retain measured changes in end-effector pose and gripper state. An exponential moving average of the observation encoder supplies Effect targets. A shared generation expert learns to jointly predict Effect and an executable action chunk through flow matching, and reuses the sampled pair to generate future video on demand. This allows the controller to execute actions without waiting for video synthesis. We train on more than 20,000 hours of heterogeneous embodied data, excluding unused chain-of-thought data, and accommodate dataset-specific joint, end-effector, and hand-pose representations. Our evaluation uses the Small (8B) configuration on all five benchmarks and additionally evaluates the Large (26B) configuration on RoboDojo. Experiments examine closed-loop manipulation across complementary benchmarks, and comparisons across multiple baseline policies show consistent improvements from Action Grounding.

</details>

---

### [[20_Research/Papers/具身智能/Perception_Is_Enough,_at_the_Right_Scale_Scale-Adaptive_Token_Pruning_for_Vision-Language-Action_Models|Perception Is Enough, at the Right Scale: Scale-Adaptive Token Pruning for Vision-Language-Action Models]]

![[assets/2611.31954_figure.png|800]]

- **arXiv**: [2611.31954](https://arxiv.org/abs/2611.31954)
- **PDF**: https://arxiv.org/pdf/2611.31954
- **详细分析**: [[20_Research/Papers/具身智能/Perception_Is_Enough,_at_the_Right_Scale_Scale-Adaptive_Token_Pruning_for_Vision-Language-Action_Models|Perception Is Enough, at the Right Scale: Scale-Adaptive Token Pruning for Vision-Language-Action Models]]
- **作者**: Yifeng Lin, Liuxiang Qiu, Yunfeng Chen, Tiesong Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Perception Is Enough, at the Right Scale: Scale-Adaptive Token Pruning for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EcoVLA, EffVLA, EfficientVLA, OpenVLA, SP-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models must process continuous streams of visual observations, and the resulting computational cost limits real-time robotic control. Token pruning reduces this cost, but a fixed semantic scale of perceptual representation can overlook information needed at different stages of manipulation. We show that perceptual semantics can guide effective token selection without relying on internal attention when the selection scale adapts to the scene's evolving semantic structure. Based on this observation, we introduce TauPrune-VLA, a training-free method that controls the scale of the retained perceptual representation through a single perception temperature $τ$. To adapt this scale as manipulation proceeds, TauPrune-VLA updates $τ$ online using trends in perceptual semantics, with robot-state changes and action magnitude regulating the adjustment strength. While these semantics evolve over the course of manipulation, they remain relatively stable between consecutive frames. This continuity allows retention indices computed from the current observation to be applied at the next policy invocation, enabling token selection to run asynchronously with inference and reducing pruning overhead. Evaluated across diverse VLA models and simulation benchmarks, TauPrune-VLA achieves up to a $1.86\times$ inference speedup while maintaining near-baseline task success rates. We further validate its effectiveness on two real-world robotic platforms.

</details>

---

### [[20_Research/Papers/强化学习/MIFLOW_Dynamic_Recent-Behavior_Priors_for_Reference-Calibrated_Online_Flow-Policy_Reinforcement_Learning|MIFLOW: Dynamic Recent-Behavior Priors for Reference-Calibrated Online Flow-Policy Reinforcement Learning]]

![[assets/2611.31902_figure.png|800]]

- **arXiv**: [2611.31902](https://arxiv.org/abs/2611.31902)
- **PDF**: https://arxiv.org/pdf/2611.31902
- **详细分析**: [[20_Research/Papers/强化学习/MIFLOW_Dynamic_Recent-Behavior_Priors_for_Reference-Calibrated_Online_Flow-Policy_Reinforcement_Learning|MIFLOW: Dynamic Recent-Behavior Priors for Reference-Calibrated Online Flow-Policy Reinforcement Learning]]
- **作者**: Chenhao Wang, Haonan Ma, Wenjie Zhang, Yifan Wang, Mingbin Gao, Yuan-Ye Zhang, Wenjing Hong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《MIFLOW: Dynamic Recent-Behavior Priors for Reference-Calibrated Online Flow-Policy Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FlowRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based policies provide expressive action distributions for continuous-control reinforcement learning. In online actor-critic learning, off-policy value estimates can be unreliable in poorly covered action regions, where expressive policies may shift probability mass toward critic-favored actions. We propose MIFLOW, which calibrates online flow-policy learning with a recency-adaptive flow-matching prior fitted to recently executed actions. Inspired by canalization as a qualitative analogy for path-dependent stabilization, we use the prior as a moving density reference for value-guided policy improvement. MIFLOW uses the approximate recent-action log-density in a dimension-normalized correction to both actor updates and critic targets. This correction increases the cost of low-density actions while keeping them available. Across six MuJoCo continuous-control tasks and five random seeds, MIFLOW achieves competitive mean return curves and higher late-training mean returns than the evaluated baselines on several tasks. In a Walker2d-v4 case study, MIFLOW shows a lower proportion of actions assigned low density by the learned reference, both overall and among high-Q actions. Prior-family and prior-buffer comparisons show task-dependent differences in returns and prior-defined diagnostics. These results support dynamic recent-behavior priors for reference calibration in the evaluated settings. The diagnostics measure how sampled actions align with the learned reference. True action support and critic extrapolation error remain unmeasured in these experiments.

</details>

---

### [[20_Research/Papers/强化学习/CALVIN-MAX_When_Does_a_Mid-Execution_Change_Hurt_a_Robot_Policy|CALVIN-MAX: When Does a Mid-Execution Change Hurt a Robot Policy?]]

![[assets/2611.31868_first_page.png|800]]

- **arXiv**: [2611.31868](https://arxiv.org/abs/2611.31868)
- **PDF**: https://arxiv.org/pdf/2611.31868
- **详细分析**: [[20_Research/Papers/强化学习/CALVIN-MAX_When_Does_a_Mid-Execution_Change_Hurt_a_Robot_Policy|CALVIN-MAX: When Does a Mid-Execution Change Hurt a Robot Policy?]]
- **作者**: Sajjad Pakdamansavoji
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CALVIN-MAX: When Does a Mid-Execution Change Hurt a Robot Policy?》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DynamicVLA, SwitchVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots must often keep working after the world changes, as when a block moves or the camera shifts while the robot still acts on what it saw before. Recent work showed that one change during a task lowers success for every policy tested, but did not separate the effect of its timing from the cost of the changed world, or measure what it costs afterwards. We introduce CALVIN-MAX, a benchmark of 7,828 cases on CALVIN's five-instruction chains, each with one change to the objects, the camera, the robot, or the instruction. Each case compares three runs that are identical until the affected instruction begins: one without the change, one with it in place from that moment, and one in which it arrives while the robot is moving. The second run against the first gives the cost of the changed world, and the third against the second the effect of meeting it mid-motion. On 1,526 held-out cases per policy, with hypotheses fixed in advance, each of ten released policies loses 4.4 to 9.9 percentage points on the affected instruction over the eight core changes. Whether timing matters depends on the change: one that alters what the robot sees costs 5.4 points less mid-motion than from the start, whereas a change to the scene itself or to the robot shows no detectable effect. Rewinding the robot to the start of the instruction removes the benefit for every policy; the stricter test we fixed in advance, that the rewound run then matches the second run, passes for three. The cost also outlasts the affected instruction: the change stays in place, and a policy that still completes that instruction is 5.0 to 16.8 points less likely to complete the next one.

</details>

---

### [[20_Research/Papers/具身智能/Two-Stage_Post-Training_for_Flow-Based_Embodied_Foundation_Models|Two-Stage Post-Training for Flow-Based Embodied Foundation Models]]

![[assets/2611.31850_first_page.png|800]]

- **arXiv**: [2611.31850](https://arxiv.org/abs/2611.31850)
- **PDF**: https://arxiv.org/pdf/2611.31850
- **详细分析**: [[20_Research/Papers/具身智能/Two-Stage_Post-Training_for_Flow-Based_Embodied_Foundation_Models|Two-Stage Post-Training for Flow-Based Embodied Foundation Models]]
- **作者**: Jiaming Zhang, Yao Lyu, Haoning Wang, Yongjun Chen, Liping Zhang, Shengbo Eben Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型
- **相关性评分**: 1.72（加权：具身智能 1.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Two-Stage Post-Training for Flow-Based Embodied Foundation Models》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, Meta-World, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale pretraining provides embodied models with general capabilities, but reliable task execution still requires post training. In multitask settings, supervised fine-tuning (SFT) faces distribution mismatch between training and deployment, whereas reinforcement learning (RL) is limited by sparse rewards and uneven learning progress across tasks. Multi-teacher on policy distillation (MOPD) consolidates expert capabilities through dense supervision on the model's own trajectories, but achieving performance beyond the teachers remains challenging. We propose a two-stage post training framework for flow-based embodied models, constructing distillation objectives from the velocity regression formulation of conditional flow matching. Stage 1 efficiently consolidates expert capabilities through MOPD. Stage 2 combines RL with teacher distillation that weights velocity errors according to the sampling noise, where distillation is restricted to failed trajectories to supplement sparse rewards with dense guidance without directly constraining successful behaviors. Experiments across multiple models and benchmarks show that the framework outperforms joint SFT and exceeds the corresponding teachers' aggregate success rates. Sample efficiency comparisons show higher success rates than direct RL with fewer environment interactions.

</details>

---

### [[20_Research/Papers/强化学习/POISE_Curvature-Aware_Critic_Regularization_for_Smooth_Actor-Critic_Control|POISE: Curvature-Aware Critic Regularization for Smooth Actor-Critic Control]]

![[assets/2611.31835_figure.png|800]]

- **arXiv**: [2611.31835](https://arxiv.org/abs/2611.31835)
- **PDF**: https://arxiv.org/pdf/2611.31835
- **详细分析**: [[20_Research/Papers/强化学习/POISE_Curvature-Aware_Critic_Regularization_for_Smooth_Actor-Critic_Control|POISE: Curvature-Aware Critic Regularization for Smooth Actor-Critic Control]]
- **作者**: Jeong Woon Lee, Namho Kim, Hyoseok Hwang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《POISE: Curvature-Aware Critic Regularization for Smooth Actor-Critic Control》归入 强化学习、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LipsNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actor-critic methods achieve high returns in robotic control, yet trained actors exhibit high-frequency action oscillations. Most smoothness methods constrain the actor, whereas PAVE regularizes the critic by separately penalizing action-gradient variation and encouraging negative action curvature. The same gradient change, however, moves the critic's preferred action farther where the critic is flat, and separate penalties do not measure this motion. We characterize this motion through the greedy shift, which approximates greedy-action displacement across state transitions to first order under local concavity. Since displacement alone does not reflect its critic-value consequences, the analysis further shows that the shift's curvature-weighted energy approximates the value lost by retaining the previous greedy action to second order. Based on this relationship, POISE regularizes the curvature-weighted energy along temporal and spatial state displacements. It employs a saddle-free curvature metric and reward-scale-consistent scaling while leaving the actor unchanged. On six continuous control tasks with TD3, POISE reduces the smoothness score on every task by $5.9\times$ on average ($4.5\times$ geometric mean), compared with $2.2\times$ ($1.9\times$) for the strongest baseline, and achieves the lowest score on five tasks. Paired return intervals include zero on four tasks, with a 14% increase on Ant and an 11% decrease on Hopper.

</details>

---

### [[20_Research/Papers/大模型/Exploring_Multi-Player_Social_Games_as_Verifiable_Training_Grounds_for_Large_Language_Models|Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models]]

![[assets/2611.31821_figure.png|800]]

- **arXiv**: [2611.31821](https://arxiv.org/abs/2611.31821)
- **PDF**: https://arxiv.org/pdf/2611.31821
- **详细分析**: [[20_Research/Papers/大模型/Exploring_Multi-Player_Social_Games_as_Verifiable_Training_Grounds_for_Large_Language_Models|Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models]]
- **作者**: Keyu He, Michael Li, Jiarui Liu, Mingqian Zheng, Koichi Onoue, Tongshuang Wu, Maarten Sap
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.75，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Exploring Multi-Player Social Games as Verifiable Training Grounds for Large Language Models》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SocialRL, Sotopia-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The training of socially intelligent language models often relies on large language model (LLM) judges, which are expensive, noisy, and vulnerable to reward hacking. Multi-player social games offer a natural alternative: they require open-ended communication to coordinate with teammates and infer hidden roles, while their rules provide an objective outcome which can serve as a verifiable reward for training. Using three social games, we explore how much social intelligence Qwen3 models can acquire through supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR). Results show that against a much stronger Gemma-3-27B model, SFT and RLVR raise the win rate of Qwen3-4B from 33% to 81% on the three trained games, and from 39% to 54% on three additional held-out games. In contrast, in-context strategies such as prompting improve the win rate of Qwen3-4B by only about 6 pp across the same games we train and evaluate on. Furthermore, we show that the gains from SFT and RLVR hold across the model sizes 1.7B, 4B, and 32B. Qualitative analyses of agent behavior show signs of stronger social intelligence; for example, trained agents tend to share information more openly, check each other's claims against public evidence, and coordinate their votes. More broadly, our results demonstrate that training LLMs on verifiable outcomes in social games can cultivate generalizable social behaviors, which offers a scalable path for building socially intelligent agents.

</details>

---

### [[20_Research/Papers/机器人/CATWAY_Cost-sensitive_agentic_three-way_robot_decisions_with_calibrated_language-model_confidence|CATWAY: Cost-sensitive agentic three-way robot decisions with calibrated language-model confidence]]

![[assets/2611.31694_first_page.png|800]]

- **arXiv**: [2611.31694](https://arxiv.org/abs/2611.31694)
- **PDF**: https://arxiv.org/pdf/2611.31694
- **详细分析**: [[20_Research/Papers/机器人/CATWAY_Cost-sensitive_agentic_three-way_robot_decisions_with_calibrated_language-model_confidence|CATWAY: Cost-sensitive agentic three-way robot decisions with calibrated language-model confidence]]
- **作者**: Erik Derner
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.65（加权：具身智能 0.3，大模型 0.25，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《CATWAY: Cost-sensitive agentic three-way robot decisions with calibrated language-model confidence》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A language-model robot agent must decide whether to execute, question or refuse an instruction, and an unsafe execution costs far more than an unneeded question. No prior robot gate derives all its thresholds from error costs or acts on calibrated probabilities, and none was fitted in one domain and evaluated unchanged in another. We propose CATWAY, a cost-sensitive three-way decision gate: a loss matrix over four instruction conditions (clear, ambiguous, infeasible, unsafe) fixes execute, ask and refuse regions on the probability simplex, the question being the information-gathering step. Its probabilities fuse a ten-sample vote with graded scores of ambiguity, infeasibility and risk by logistic regression. Fitted on household instructions and frozen, CATWAY was tested on text-level decisions of three small models in-domain, in two new robot domains and on the external TRUST-NAV benchmark. At eleven generations per decision against one, it was significantly cheaper than a direct prompt, a cost-aware prompt and an unguarded agent in all 18 household comparisons (mean loss per item 0.28 against 0.57-0.83), in 9 of 18 in the new domains and in 10 of 18 on TRUST-NAV (Holm per set), and never significantly costlier. It executed none of the 142 unsafe test instructions. On a unanimous vote, the minimum-expected-loss rule reduces calibration to one loss-derived threshold, so for two of six model configurations a gate on the vote alone never executed a clear instruction, costing 0.49 per item on TRUST-NAV against CATWAY's 0.13 and 0.09; the fused estimate avoided this on every set.

</details>

---

### [[20_Research/Papers/大模型/RECAP_Training_Long-horizon_LLM_Agents_with_Context_Compaction|RECAP: Training Long-horizon LLM Agents with Context Compaction]]

![[assets/2611.31258_first_page.png|800]]

- **arXiv**: [2611.31258](https://arxiv.org/abs/2611.31258)
- **PDF**: https://arxiv.org/pdf/2611.31258
- **详细分析**: [[20_Research/Papers/大模型/RECAP_Training_Long-horizon_LLM_Agents_with_Context_Compaction|RECAP: Training Long-horizon LLM Agents with Context Compaction]]
- **作者**: Yulun Jiang, Maria Brbic, Michael Moor
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.35（加权：大模型 1.15，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《RECAP: Training Long-horizon LLM Agents with Context Compaction》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Context compaction enables large language model agents to tackle long-horizon tasks within limited context budgets by replacing interaction histories with compressed summaries. However, learning effective compaction jointly with the agent policy remains challenging, as summaries affect task success over many subsequent interactions. We introduce RECAP, a reinforcement learning (RL) framework based on the principle that a summary should preserve the behavior induced by the original interaction history. We formalize this principle with a behavior distortion objective that measures the divergence between the agent's subsequent behavior under compressed and original contexts. We show that the gradient of the distortion objective decomposes into two complementary learning signals: distortion-based reward for summary generation and self-distillation for subsequent actions. Experiments on Qwen3.5-4B show that RECAP consistently outperforms the task-reward-only RL baselines on both environments, leading to an absolute improvement of 4.6% and 4.3% on BrowseComp-plus and SWE-bench Verified, respectively. Ablations further highlight the value of jointly supervising summary generation and post-compaction behavior for RECAP.

</details>

---
