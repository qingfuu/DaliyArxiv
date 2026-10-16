# cs.LG | Machine Learning | 2026-10-14

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/具身智能/LADDER_A_Long-Horizon_Robot_Manipulation_Benchmark|LADDER: A Long-Horizon Robot Manipulation Benchmark]]

![[assets/2610.18053_figure.png|800]]

- **arXiv**: [2610.18053](https://arxiv.org/abs/2610.18053)
- **PDF**: https://arxiv.org/pdf/2610.18053
- **详细分析**: [[20_Research/Papers/具身智能/LADDER_A_Long-Horizon_Robot_Manipulation_Benchmark|LADDER: A Long-Horizon Robot Manipulation Benchmark]]
- **作者**: Petko Petkov, Giuliano Albanese, Nikolay Nikolov, Luc Van Gool, Jonathan Tremblay, Danda Pani Paudel
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《LADDER: A Long-Horizon Robot Manipulation Benchmark》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robot manipulation policies learn short-horizon skills effectively, but degrade rapidly on long-horizon tasks. Existing benchmarks cannot isolate failures because task horizon is either too short or entangled with scene and object variations. We propose LADDER, a long-horizon robot manipulation benchmark scaling from 1 to 10 subgoals within the same environment over three suites (SimplerEnv-Long, RobotArena-$\infty$-Long, and RoboLab-Long), 145 tasks, eight categories, two embodiments, and 2,024 simulated episodes per system. We evaluate two orchestration paradigms: text subgoals for learned low-level policies (VoLo) and tool selection orchestration (CaP-X, GPT-Policy, PSP-Agent, TiPToP). Given the full instruction directly, low-level policies achieve 85.4% on single-subgoal tasks, but drop to near zero on extended tasks. While orchestration remedies this, it remains bounded by physical execution errors of the low-level policy rather than high-level planning and achieves only ~25%. Tool selection orchestration with GPT-Policy on GPT-6 Astra significantly outperforms learned-policy methods, but incurs significant time and cost budget and succeeds only ~62%. Real-world experiments across two embodiments confirm the collapse of the low-level policy and the gain from orchestration. Project website: https://ladder.insait.ai

</details>

---

### [[20_Research/Papers/具身智能/DR-APO_Decoupled-Representation_Advantage-Guided_Policy_Optimization_from_Continuous_Control_to_Embodied_Navigation|DR-APO: Decoupled-Representation Advantage-Guided Policy Optimization from Continuous Control to Embodied Navigation]]

![[assets/2610.16618_figure.png|800]]

- **arXiv**: [2610.16618](https://arxiv.org/abs/2610.16618)
- **PDF**: https://arxiv.org/pdf/2610.16618
- **详细分析**: [[20_Research/Papers/具身智能/DR-APO_Decoupled-Representation_Advantage-Guided_Policy_Optimization_from_Continuous_Control_to_Embodied_Navigation|DR-APO: Decoupled-Representation Advantage-Guided Policy Optimization from Continuous Control to Embodied Navigation]]
- **作者**: Runhua Zhang, Yingjie Niu, Chao Li
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.12（加权：具身智能 1.5，强化学习 1.16，世界模型 0.16，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《DR-APO: Decoupled-Representation Advantage-Guided Policy Optimization from Continuous Control to Embodied Navigation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policy representations in reinforcement learning have expanded beyond Gaussian policies to diffusion and flow-matching based generative policies. However, existing RL methods remain representation-specific, lacking a unified optimization interface for emerging generative policies. In particular, extending likelihood-based objectives to multi-step generative policies couples optimization to their internal generation process, where accumulated likelihood ratios can weaken the update signal. Meanwhile, generative-policy-specific methods often rely on multi-candidate generation and critic-based selection, improving overall return while providing limited improvement to the policy itself. We introduce DR-APO (Decoupled-Representation Advantage-Guided Policy Optimization), which decouples policy improvement from policy representation through advantage-guided target improvement and representation-compatible direct action fitting, providing a shared optimization principle for Gaussian, diffusion, and flow policies. Across five MuJoCo-v5 tasks, DR-APO remains competitive with SAC for Gaussian policies and achieves the best aggregate policy-only performance for both diffusion and flow-matching policies. NavDP post-training improves the Success Rate (SR) from 70.33% to 89.55% in simulation and from 25% to 65% in real-world navigation. These results demonstrate a unified policy-improvement principle across Gaussian, diffusion, and flow policies, from continuous-control learning to embodied-policy post-training.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Reachability-Based_Safety_Representations_for_Real-Time_Robot_Navigation_in_Unknown_and_Dynamic_Environments|Learning Reachability-Based Safety Representations for Real-Time Robot Navigation in Unknown and Dynamic Environments]]

![[assets/2610.16522_figure.png|800]]

- **arXiv**: [2610.16522](https://arxiv.org/abs/2610.16522)
- **PDF**: https://arxiv.org/pdf/2610.16522
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Reachability-Based_Safety_Representations_for_Real-Time_Robot_Navigation_in_Unknown_and_Dynamic_Environments|Learning Reachability-Based Safety Representations for Real-Time Robot Navigation in Unknown and Dynamic Environments]]
- **作者**: Bojan Derajić
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning Reachability-Based Safety Representations for Real-Time Robot Navigation in Unknown and Dynamic Environments》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CoRL, Failure-Set, Safe-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe robot navigation in unknown, dynamic environments requires more than geometric collision checking: a robot still far from an obstacle may be unable to avoid it because of its speed, orientation, or the obstacle's motion. Hamilton--Jacobi (HJ) reachability analysis captures this in a value function whose sign separates states that admit a safe continuation from those where collision is unavoidable, but computing it online for every newly observed environment is too expensive. This dissertation trains neural implicit representations offline on reachability solutions to give optimization-based controllers this information in real time. Since the value function never exceeds the constraint, it equals a directly computed constraint, such as a signed distance, minus a nonnegative dynamics correction. Learning only this correction keeps represented obstacles outside the predicted safe set despite approximation errors. The first two of five methods use the learned function as a terminal constraint in model predictive control, for static local environments and predicted obstacle motion. The next two use it as a barrier candidate in control barrier function safety filters, for static environments and, through pairwise barriers in relative coordinates, for a varying number of moving obstacles. Simulations and hardware experiments on ground and aerial robots show better collision avoidance than geometric and hand-designed baselines, especially for short horizons and moving obstacles. The fifth method replaces the grid-based offline solver, which limits the first four to low-dimensional models. For control-affine dynamics with polytopic inputs, the HJ Hamiltonian is maximized at a vertex, so a parallelizable tree search over vertex inputs can generate training labels. With a loss from the HJ variational inequality, these labels yield barrier candidates for systems with up to 13 states.

</details>

---

### [[20_Research/Papers/具身智能/Trust-Calibrated_VLA_Policy_Post-Training_with_Evolving_Imagination|Trust-Calibrated VLA Policy Post-Training with Evolving Imagination]]

![[assets/2610.16517_figure.png|800]]

- **arXiv**: [2610.16517](https://arxiv.org/abs/2610.16517)
- **PDF**: https://arxiv.org/pdf/2610.16517
- **详细分析**: [[20_Research/Papers/具身智能/Trust-Calibrated_VLA_Policy_Post-Training_with_Evolving_Imagination|Trust-Calibrated VLA Policy Post-Training with Evolving Imagination]]
- **作者**: Wenzhan Li, Yiran Qin, Heng Zhou, Huirui Wang, Yulan Guo, Ruimao Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.22（加权：具身智能 1.8，强化学习 0.56，世界模型 0.36，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Trust-Calibrated VLA Policy Post-Training with Evolving Imagination》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MBRL, MERL, MFRL, MeRL, Static-MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are often pretrained via imitation learning, making reinforcement learning (RL) post-training important when deployment moves beyond demonstration coverage. Existing refinement paradigms expose a reliability--efficiency tension: model-free refinement avoids simulator bias but is interaction-intensive, whereas model-based refinement can exploit unreliable imagination even as its simulator adapts. We propose Model-Evolving Reinforcement Learning (MERL), a trust-calibrated framework that couples policy optimization with an online-updated simulator comprising a world model and a reward proxy head. Across stages, simulator reliability controls the imagined-data ratio and rollout horizon; within rollouts, chunk-level trust controls replay selection and optimization weight. For recursive imagination without exact grounded continuations, a residual predictor estimates trust without querying future ground truth. On perturbed LIBERO-PRO tasks, MERL reaches 79.7% average success, improves high-threshold learning speed by 10.9% over the matched model-free control, and outperforms same-protocol external baselines across three training seeds. Fixed-data adaptation from 50 demonstrations per task achieves 80.0% average success on two physical-robot tasks.

</details>

---

### [[20_Research/Papers/具身智能/Vision-Predictor-Action_Towards_Efficient_Embodied_AI_via_Neuro-Symbolic_JEPA_Predictors|Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors]]

![[assets/2610.15556_first_page.png|800]]

- **arXiv**: [2610.15556](https://arxiv.org/abs/2610.15556)
- **PDF**: https://arxiv.org/pdf/2610.15556
- **详细分析**: [[20_Research/Papers/具身智能/Vision-Predictor-Action_Towards_Efficient_Embodied_AI_via_Neuro-Symbolic_JEPA_Predictors|Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors]]
- **作者**: Yeonseok Lee
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.5（加权：具身智能 2.7，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Vision-Predictor-Action: Towards Efficient Embodied AI via Neuro-Symbolic JEPA Predictors》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NS-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models commonly generate robot actions token by token through Large Language Model (LLM) decoders, causing inference latency to grow with action sequence length and limiting closed-loop control frequency. We present Goal-Conditioned Vision-Predictor-Action (VPA), which replaces autoregressive decoders with a lightweight latent control loop. A shared vision encoder and a frozen text encoder embed observations, goal images, and instructions; a neuro-symbolic selector chooses a discrete skill; a Joint-Embedding Predictive Architecture (JEPA) predictor forecasts the next latent state; and a flow-matching solver generates an entire action chunk in a few integration steps, so that sequential network evaluations per decision step do not depend on the action horizon. We analyze inference complexity, regularization against representation collapse, and conditions under which latent sub-goal thresholding limits error accumulation across task phases. As an initial proof of concept, we evaluated VPA on the LIBERO-10 suite. The trainable model has under 20M parameters (checkpoint under 75 MB, excluding a frozen 63.4M-parameter CLIP text encoder); a decision step of a single-camera reference configuration takes 10-14 ms on an Apple M4; and trained only on LIBERO-10 demonstrations in under three hours on a single GPU, a two-camera policy succeeded in 40.0% of 200 evaluation episodes. These preliminary results from a single training run suggest the approach is workable. Code and weights are available at https://github.com/ylee-sling/Vision-Predictor-Action and https://huggingface.co/ylee-sling/vpa-libero10, and archived at https://doi.org/10.5281/zenodo.22960920.

</details>

---

### [[20_Research/Papers/具身智能/Harnessing_VLM_in_Embodied_RL_From_Reward_Regressor_to_Success_Detector_via_Exploration-Augmented_Key-Observation_Gating|Harnessing VLM in Embodied RL: From Reward Regressor to Success Detector via Exploration-Augmented Key-Observation Gating]]

![[assets/2610.15401_figure.png|800]]

- **arXiv**: [2610.15401](https://arxiv.org/abs/2610.15401)
- **PDF**: https://arxiv.org/pdf/2610.15401
- **详细分析**: [[20_Research/Papers/具身智能/Harnessing_VLM_in_Embodied_RL_From_Reward_Regressor_to_Success_Detector_via_Exploration-Augmented_Key-Observation_Gating|Harnessing VLM in Embodied RL: From Reward Regressor to Success Detector via Exploration-Augmented Key-Observation Gating]]
- **作者**: Xin Liu, Yutong Jiang, Jian Su, Ziheng Wang, Chuang Wang, Haoran Li, Dongbin Zhao
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《Harnessing VLM in Embodied RL: From Reward Regressor to Success Detector via Exploration-Augmented Key-Observation Gating》归入 具身智能、大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HIL-SERL, MetaWorld, Real-World, ResNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

VLMs provide promising solutions to embodied reward design. Most current methods that train VLMs as reward regressors not only require extensive annotations but are also primarily designed for finetuning pretrained policies, and perform less well in the more challenging from-scratch RL setting. This issue stems from a fundamental mismatch: regressing precise rewards is misaligned with what VLMs naturally excel at. We posit that it is more aligned with VLMs' inherent multi-modal VQA capabilities for the models to function as success detectors, and propose VLM success reward via Exploration-Augmented Key-Observation Gating (VLMeg) to well harness VLM for embodied reward design. As the core of VLMeg, the proposed exploration-augmented key-observation gating first determines whether the current RL episode is judgment-worthy based on its similarity to a generated success trajectory. Then, the key observation with the lowest confusion from the judgment-worthy episode will be selected for VLM evaluation as episodic reward. This gating mechanism not only avoids redundant calls but also enables higher detection accuracy of VLM. Considering the sparsity of judgment-worthy episodes, the advanced exploration incentives based on the generated trajectory are introduced, enabling more efficient exploration toward judgment-worthy trajectories for more VLM reward triggers and thus gaining higher RL efficiency. Extensive experiments in MetaWorld demonstrate VLMeg achieves state-of-the-art from-scratch RL, outperforming advanced VLM-based baselines on 12 challenging reward-free tasks. Furthermore, VLMeg also enables effective RL without any ground-truth reward in 3 challenging real-world experiments. Code will be open after acceptance at https://github.com/Raina915/VLMeg.

</details>

---

### [[20_Research/Papers/强化学习/ANTE_Anticipate,_Then_Execute_--_Learning_Internal_World_Models_for_Coding_Agents_from_Verified_Beliefs|ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs]]

![[assets/2610.15368_figure.png|800]]

- **arXiv**: [2610.15368](https://arxiv.org/abs/2610.15368)
- **PDF**: https://arxiv.org/pdf/2610.15368
- **详细分析**: [[20_Research/Papers/强化学习/ANTE_Anticipate,_Then_Execute_--_Learning_Internal_World_Models_for_Coding_Agents_from_Verified_Beliefs|ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs]]
- **作者**: Yi Ge, Kangrui Ruan, Jifan Chen, Manish Prajapat, Christian Bock, Xiaoyang Wang, Rein Houthooft, Aritra Sengupta, Varun Kumar
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 2.22（加权：大模型 0.5，强化学习 0.56，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ANTE-RL, PatchWorld, SWE-World, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. However, most existing coding agents never look ahead: their policies do not anticipate the consequences of actions, and the terminal reward barely attributes a failure to certain earlier steps, so an ill-judged edit can corrupt the repository state irreversibly before any signal arrives. Recent code world models aim to address these challenges, but they are either trained and then frozen before reinforcement learning (RL), or reduced to an auxiliary next-token loss on the environment's outputs. We present ANTE (Anticipate, Then Execute), an agentic RL framework that verifies the policy's pre-action predictions by real execution and turns them into per-step credit for its actions and trust-or-abstain decisions. With an internal belief stated before each action, Belief-Anchored Policy Optimization (BAPO) turns the settled predictions into per-step advantages by anchoring credit on the policy's own forecasts. To turn the trained forecasts into better actions at inference, thereby facilitating effective test-time scaling, ANTE-TTO (test-time optimization) selects among candidate actions without an external scorer. ANTE raises Qwen3-32B from 25.0% to 57.2% pass@1 on SWE-bench Verified, 6.2% above a matched GRPO baseline trained without the belief state; its world model's accuracy climbs from 44% to 69% during RL, and the learned foresight capability transfers across harnesses and out-of-distribution domains. In summary, we aim to build a code world model that knows what has happened, what holds now, and what the next action will achieve.

</details>

---

### [[20_Research/Papers/具身智能/CoLA_Multi-VLA_Coordination_via_Learned_Adapters|CoLA: Multi-VLA Coordination via Learned Adapters]]

![[assets/2610.15337_figure.png|800]]

- **arXiv**: [2610.15337](https://arxiv.org/abs/2610.15337)
- **PDF**: https://arxiv.org/pdf/2610.15337
- **详细分析**: [[20_Research/Papers/具身智能/CoLA_Multi-VLA_Coordination_via_Learned_Adapters|CoLA: Multi-VLA Coordination via Learned Adapters]]
- **作者**: Ahaskar Kashyap, Jiawen Zong, Boyu Ma, Chuhao Zhou, Jingliang Li, Stefano V. Albrecht, Jianfei Yang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《CoLA: Multi-VLA Coordination via Learned Adapters》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CommNet, MARL, Multi-VLA, TwinVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are typically deployed as isolated single-agent policies. When several such agents share a workspace, they can coordinate implicitly, by observing one another, or explicitly, by exchanging messages, but it remains unclear when explicit communication becomes necessary. We introduce CoLA (Coordination via Learned Adapters), which keeps each agent's VLA backbone frozen and trains a lightweight message channel and a per-arm diffusion action head on top, with fully decentralised execution. Across three tasks that differ in how much each agent can observe, the channel matters only when information is private. On an occluded tray handover, where the box's colour marker is visible to one agent only, CoLA reaches 76.0% success versus 1.3% with messages zeroed throughout training. On two-arm and three-arm handover tasks, removing messages has no measurable effect with a shared overhead camera (90.6% vs. 88.3% at two arms; 63.5% vs. 60.0% at three), but lowers success on the two-arm task's wrist-only variant (74.8% vs. 64.3%). This architecture generalises across different VLA backbones as well. With a frozen $π_{0.5}$ backbone on the same occluded tray task, CoLA matches the overall success rate of a LoRA-fine-tuned baseline (37.3% vs. 34.7%) using a fraction of the trainable parameters. When CoLA places the box, it selects the correct tray 71.8% of the time, whereas the independently fine-tuned baseline, whose placing arm never sees the marker, selects it at chance level (34.7% against 33.3%).

</details>

---

### [[20_Research/Papers/具身智能/Compositional_Average_Velocity_Modeling_for_Efficient_Diffusion_Offline_Reinforcement_Learning|Compositional Average Velocity Modeling for Efficient Diffusion Offline Reinforcement Learning]]

![[assets/2610.14941_figure.png|800]]

- **arXiv**: [2610.14941](https://arxiv.org/abs/2610.14941)
- **PDF**: https://arxiv.org/pdf/2610.14941
- **详细分析**: [[20_Research/Papers/具身智能/Compositional_Average_Velocity_Modeling_for_Efficient_Diffusion_Offline_Reinforcement_Learning|Compositional Average Velocity Modeling for Efficient Diffusion Offline Reinforcement Learning]]
- **作者**: Thanh Nguyen, Abu Hanif Muhammad Syarubany, Hwanhee Kim, Chang D. Yoo
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.02（加权：具身智能 0.3，强化学习 1.36，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Compositional Average Velocity Modeling for Efficient Diffusion Offline Reinforcement Learning》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based policies have recently emerged as a powerful paradigm for offline reinforcement learning, but their reliance on multi-step denoising introduces substantial computational overhead and requires backpropagation through time during training, limiting scalability and practical deployment. In this work, we propose \textbf{Instant Flow Q-Learning (InsQL)}, a single-step generative policy learning framework that retains the expressive capacity of diffusion models while eliminating iterative sampling and BPTT. InsQL builds on the flow-matching perspective of diffusion policies, but replaces marginal velocity parameterization with \emph{average-velocity} modeling and introduces a principled compositional mechanism, yielding a theoretically grounded objective that learns average velocity consistently across scales. This formulation provides a direct noise-to-action mapping and enables single-step action generation. InsQL further unifies compositional average-velocity modeling with behavior-regularized actor--critic optimization in a single framework, requiring only a single policy network and avoiding distillation, multi-stage procedures, and Jacobian computations during training. At inference time, actions are generated in a single forward pass and can be refined via value-guided candidate selection to improve performance. Extensive experiments on standard offline RL benchmarks and real-world robotic manipulation tasks show that InsQL matches or surpasses state-of-the-art diffusion-based methods while substantially reducing both training and inference time. Overall, these results establish compositional average-velocity modeling as an efficient and scalable alternative to multi-step generative policies for offline RL.

</details>

---

### [[20_Research/Papers/具身智能/CFG-Policy_Unified_Diffusion_Policy_Learning_Framework_via_Classifier-free_Guidance|CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance]]

![[assets/2610.14936_figure.png|800]]

- **arXiv**: [2610.14936](https://arxiv.org/abs/2610.14936)
- **PDF**: https://arxiv.org/pdf/2610.14936
- **详细分析**: [[20_Research/Papers/具身智能/CFG-Policy_Unified_Diffusion_Policy_Learning_Framework_via_Classifier-free_Guidance|CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance]]
- **作者**: Shutong Ding, Zhaoyang Liu, Yimiao Zhou, Jingya Wang, Jiayuan Gu, Ye Shi
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型, 世界模型
- **相关性评分**: 1.82（加权：具身智能 0.6，大模型 0.2，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CFG-Policy: Unified Diffusion Policy Learning Framework via Classifier-free Guidance》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CFGRL, RIPT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion policies are increasingly used in robotic control and manipulation, vision-language-action models, and world-model-based agents. Their ability to represent multimodal action distributions offers rich opportunities for exploration in reinforcement learning (RL). However, optimizing diffusion policies with RL can reduce the behavioral diversity and further limit their exploration capability. In RL post-training, directly fine-tuning a pretrained policy may also disrupt its acquired capabilities, while action-space residuals may lack the expressive power for multimodal exploration. Together, these issues reveal a common challenge across online and offline-to-online diffusion RL: improving task performance while retaining the behavioral diversity and capabilities needed for continued adaptation. We introduce CFG-Policy, a unified, plug-and-play framework that separates exploration and exploitation into two generative policies and combines their score or velocity fields during sampling through classifier-free guidance. For online RL, a frozen exploration branch sustains behavioral diversity while an exploitation branch learns from task rewards; for offline-to-online RL, a pretrained exploitation branch remains frozen while a trainable branch steers the composed behavior. CFG-Policy preserves the underlying RL objectives and improves performance with QSM and QVPO on 5 MuJoCo tasks and with Flow-SDE+PPO on 4 RoboTwin manipulation tasks. Project page is at https://zhy-liu.github.io/cfg-policy-page.

</details>

---

### [[20_Research/Papers/强化学习/Chunk-wise_Model-based_Policy_Optimization|Chunk-wise Model-based Policy Optimization]]

![[assets/2610.14564_figure.png|800]]

- **arXiv**: [2610.14564](https://arxiv.org/abs/2610.14564)
- **PDF**: https://arxiv.org/pdf/2610.14564
- **详细分析**: [[20_Research/Papers/强化学习/Chunk-wise_Model-based_Policy_Optimization|Chunk-wise Model-based Policy Optimization]]
- **作者**: Weixi Song, Donglin Wang, Yong-Lu Li
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型, 机器人
- **相关性评分**: 3.32（加权：具身智能 0.9，强化学习 0.96，世界模型 0.76，机器人 0.7）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Chunk-wise Model-based Policy Optimization》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HumanoidBench, MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based reinforcement learning has shown superior sample efficiency by leveraging the learned latent dynamics either in the form of derivative-free planning/imagined rollout training or dynamics gradient-based policy updates. While these approaches achieve comparatively fast learning, they all suffer, to varying degrees, from issues of recurrent compounding errors, high inference-time latency, and instability in backward propagation through time (BPTT). In this work, we propose a model-based RL approach that uses the chunk world model as a differentiable training-time evaluator to optimize the chunk actor without recurrent model invocation. Through the collaborative chunk-wise prediction of the world model and policy, we can generate H-step hypothetical rollouts in a single forward pass and directly optimize value expansion, avoiding the costly and unstable BPTT. We evaluate our method on 19 challenging high-dimensional humanoid tasks from HumanoidBench and deploy our method to the real-world for quadruped bipedal walking. Project Website: https://song-wx.github.io/cmpo.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Sparse-TD-JEPA_Improving_Zero-Shot_Reinforcement_Learning_With_Sparse_Latent_Task_Representations|Sparse-TD-JEPA: Improving Zero-Shot Reinforcement Learning With Sparse Latent Task Representations]]

![[assets/2610.14400_figure.png|800]]

- **arXiv**: [2610.14400](https://arxiv.org/abs/2610.14400)
- **PDF**: https://arxiv.org/pdf/2610.14400
- **详细分析**: [[20_Research/Papers/具身智能/Sparse-TD-JEPA_Improving_Zero-Shot_Reinforcement_Learning_With_Sparse_Latent_Task_Representations|Sparse-TD-JEPA: Improving Zero-Shot Reinforcement Learning With Sparse Latent Task Representations]]
- **作者**: Duaa Nakshbandi, Zhiyu An, Wan Du
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.6，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Sparse-TD-JEPA: Improving Zero-Shot Reinforcement Learning With Sparse Latent Task Representations》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Successor-feature-based zero-shot reinforcement learning methods pre-train a task encoder and successor-feature predictor on offline, reward-free data, then recover a policy at test time by solving a closed-form linear regression over a small labeled dataset. We identify an underexplored limitation of this approach: when the task encoder produces dense representations, the inferred reward signal becomes diffuse across the state space, reducing the contrast between goal-relevant states and the background and providing a weaker signal for the policy to follow. We address this limitation by introducing an l1 sparsity penalty that concentrates reward-predictive structure into a smaller effective subspace of the task encoder's latent space. The penalty is applied only during training and requires no architectural change or modification to the closed-form inference procedure. We instantiate this approach as Sparse-TD-JEPA, a single-line of code addition based on Temporal-Difference Joint-Embedding Predictive Architecture (TD-JEPA) that significantly improved its performance in zero-shot reinforcement learning. We evaluate Sparse-TD-JEPA on 65 tasks across the DeepMind Control (DMC) Suite and OGBench, covering locomotion, navigation, trajectory stitching, puzzle solving, and robotic manipulation. Sparse-TD-JEPA improves over TD-JEPA in all 13 domain-level comparisons. On DMC, it increases the average return from 661 +- 6 to 714 +- 3. On OGBench, it increases the average success rate from 38.0 +- 0.8 to 48.4 +- 2.3, with improvements of 13.4-18.0 percentage points on the evaluated antmaze navigation and stitching domains. Overall, Sparse-TD-JEPA achieves the highest mean performance among established zero-shot baselines in nine of the 13 domains. Analysis further shows that sparsity produces a sharper and more task-informative inferred reward landscape.

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_See_through_Action_Predictive_Curiosity_for_Robots|Learning to See through Action: Predictive Curiosity for Robots]]

![[assets/2610.14302_figure.png|800]]

- **arXiv**: [2610.14302](https://arxiv.org/abs/2610.14302)
- **PDF**: https://arxiv.org/pdf/2610.14302
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_See_through_Action_Predictive_Curiosity_for_Robots|Learning to See through Action: Predictive Curiosity for Robots]]
- **作者**: Stelios Zarifis, Panagiotis Filntisis, George Retsinas, Petros Maragos
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 大模型, 强化学习
- **相关性评分**: 2.02（加权：具身智能 0.6，大模型 0.2，强化学习 0.16，世界模型 0.36，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning to See through Action: Predictive Curiosity for Robots》归入 机器人、具身智能、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans and animals do not learn vision from a fixed set of data: they move, interact, and learn from the visual consequences of their actions. Motivated by this developmental view, we study whether robots can improve visual learning by actively collecting experience through curiosity-driven interaction. We introduce DySCOVER, a self-supervised framework for active robot visual learning. A robot observes RGB frames, learns a visual autoencoder that encodes and reconstructs them, and trains a recurrent world model to predict the next visual latent state conditioned on the current state and action. The agent's policy is trained only with intrinsic rewards: reconstruction error encourages visually novel observations, while the world model's error encourages transitions whose consequences are not yet predictable. This prediction error biases the policy toward more intricate trajectories that enrich the agent's set of experiences with observations beyond those encouraged by visual novelty alone. Our experiments conducted with robotic arms as the embodied agents show that adding predictive curiosity improves the vision model over using visual curiosity alone. Across variations in initial conditions, experience capacity, embodiment, and scene content, adding predictive curiosity consistently improved visual learning. These results show that predictive curiosity can improve active visual learning beyond reconstruction-based curiosity alone.

</details>

---
