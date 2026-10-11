# cs.LG | Machine Learning | 2026-10-09

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/具身智能/A_Balanced_Data_Diet_Addressing_the_Exploration_Bottleneck_in_Mega-Scale_RL_for_Robot_Control|A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control]]

![[assets/2610.12465_figure.jpg|800]]

- **arXiv**: [2610.12465](https://arxiv.org/abs/2610.12465)
- **PDF**: https://arxiv.org/pdf/2610.12465
- **详细分析**: [[20_Research/Papers/具身智能/A_Balanced_Data_Diet_Addressing_the_Exploration_Bottleneck_in_Mega-Scale_RL_for_Robot_Control|A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control]]
- **作者**: Octi Zhang, Mateo Guaman Castro, Patrick Yin, Ignacio Dagnino, Abhishek Gupta, Rosario Scalise, Byron Boots
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.12（加权：具身智能 1.5，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robots must perform a wide range of tasks from agile locomotion to dexterous manipulation. While sim-to-real reinforcement learning (RL) has proven to be a useful tool for this goal, current RL pipelines depend on engineering-heavy, per-task structural priors such as shaped rewards and demonstrations. Recent work has shown that diverse simulator resets, combined with massively parallel simulation, can alleviate much of this engineering burden on several manipulation problems. However, we find that naively scaling this paradigm to more precise or dynamic problems remains non-trivial. While simulator resets can help with exploration, uniformly sampling over this distribution wastes a growing fraction of learning experience on task configurations the policy has already mastered or cannot yet attempt. This makes it challenging to see the expected benefits of scaling parallel environments for RL, since much of the learning signal in a batch is wasted during learning. To mitigate this, we introduce Success Guided Sampling (SGS), a simple adaptive sampler that concentrates RL training on task configurations around the frontier of the policy's capabilities. Doing so allows large-scale simulated RL to make the most out of the experience in a batch, enabling much more effective scaling to large-scale parallel simulation. Across experiments using up to $2^{20}$ (over one million) parallel environments, SGS enables RL to solve challenging multi-terrain quadruped locomotion and contact-rich assembly tasks that prior methods fail to solve. Finally, we distill the learned manipulation policies into RGB-based policies and demonstrate zero-shot transfer to several challenging assembly tasks on real hardware. Project website: https://sgs-rl.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/VioLA_Learning_Generalist_Humanoid_Control_Policies_from_Human_Data|VioLA: Learning Generalist Humanoid Control Policies from Human Data]]

![[assets/2610.12435_figure.png|800]]

- **arXiv**: [2610.12435](https://arxiv.org/abs/2610.12435)
- **PDF**: https://arxiv.org/pdf/2610.12435
- **详细分析**: [[20_Research/Papers/具身智能/VioLA_Learning_Generalist_Humanoid_Control_Policies_from_Human_Data|VioLA: Learning Generalist Humanoid Control Policies from Human Data]]
- **作者**: Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black, Wieland Brendel, Andreas Krause, Georg Martius, Martin Riedmiller
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VioLA: Learning Generalist Humanoid Control Policies from Human Data》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EgoVLA, OpenVLA, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in far larger numbers, but a person's motion is not a robot command. We remove both obstacles by changing what the generalist policy predicts. We introduce VioLA, a generalist humanoid policy that predicts body and hand motion latents instead of joint commands. A pretrained body- and hand-controller execute these latents on the robot. Their corresponding motion encoders map human and robot motion into the same latent spaces. A human recording is therefore labeled in the policy's action space, and the training demonstration pool contains 140.6 million frames, 93.2% of them human. As a result, VioLA follows locomotion instructions on the real robot zero-shot, without task-specific fine-tuning, reaching 100% success where GR00T N1.7 and $Ψ_0$ reach 16.7% and 0%, respectively. It also reaches 88.6% manipulation success without task-specific fine-tuning. The same approach works across two VLA and one world-action model backbones. A generalist policy trained on human demonstrations alone performs locomotion tasks on the real robot zero-shot. Code and checkpoints will be released.

</details>

---

### [[20_Research/Papers/强化学习/FAITH_Feasibility-Aware_Safety-Filtered_RL_for_High-Dimensional_Systems|FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems]]

![[assets/2610.12432_figure.jpg|800]]

- **arXiv**: [2610.12432](https://arxiv.org/abs/2610.12432)
- **PDF**: https://arxiv.org/pdf/2610.12432
- **详细分析**: [[20_Research/Papers/强化学习/FAITH_Feasibility-Aware_Safety-Filtered_RL_for_High-Dimensional_Systems|FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems]]
- **作者**: Songyuan Zhang, Baljeet Singh, Sarthak Ranjeet Kaingade, Chuchu Fan, Bryan Trinh
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 1.82（加权：具身智能 0.6，强化学习 0.36，世界模型 0.36，机器人 0.5）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe reinforcement learning commonly places safety and task performance in the same policy objective, where they can introduce competing updates. Safety filters separate them at action execution, but classical designs require an analytic safety function and dynamics model, and standard minimal-intervention filters are myopic to long-horizon task return because they minimize only instantaneous action deviation. Hard projections are also undefined when no safe action exists. We present FAITH, a feasibility-aware, model-free framework that approximates the optimal state-action safety value and amortizes minimal-intervention filtering with a feedforward network. The task policy optimizes the task return through the filtered dynamics, which recovers the feasible constrained problem without a competing safety term in the task-policy update. When no action satisfies the learned safety condition, the same filter approaches the action with minimum predicted peak harm. On a double integrator example and a Safety Gym environment, FAITH achieves the highest return among methods with no feasible-start violations and matches the lowest harm from infeasible starts. On a 29-DoF humanoid, it reaches a 99.95% safety rate while retaining 97% of the unfiltered return in Walking-Avoid, and obtains the highest measured safety rate in Push-Avoid by learning to sacrifice balancing and fall away from the protected region. The same policies are also demonstrated on a real-world Unitree G1 humanoid.

</details>

---

### [[20_Research/Papers/强化学习/CausalDreamer_Learning_Predictive_World_Models_with_Latent_Disentanglement|CausalDreamer: Learning Predictive World Models with Latent Disentanglement]]

![[assets/2610.12016_figure.png|800]]

- **arXiv**: [2610.12016](https://arxiv.org/abs/2610.12016)
- **PDF**: https://arxiv.org/pdf/2610.12016
- **详细分析**: [[20_Research/Papers/强化学习/CausalDreamer_Learning_Predictive_World_Models_with_Latent_Disentanglement|CausalDreamer: Learning Predictive World Models with Latent Disentanglement]]
- **作者**: Prince Jha, Nils Lukas, Kun Zhang, Salem Lahlou
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.82（加权：大模型 0.1，强化学习 0.16，世界模型 1.56）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《CausalDreamer: Learning Predictive World Models with Latent Disentanglement》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models for control must capture which aspects of the environment respond to the agent's actions and which are relevant to reward. Generative world models such as Dreamer 4 consist of a video tokenizer, which encodes each frame into a latent, and a dynamics model, which is pretrained to predict future latents from past latents and actions. Yet the tokenizer is trained with a reconstruction objective, without action or reward supervision, so its latent provides no explicit mechanism to separate controllable, uncontrollable, reward-relevant, and reward-irrelevant information. We propose \textit{CausalDreamer}, which keeps the tokenizer frozen and re-encodes its latent into a factored representation of four groups along two axes: controllability, where only the two controllable groups receive the action, and reward relevance, learned by predicting the reward from the two reward-relevant groups. The pretrained dynamics model is then fine-tuned to predict the factored representation. We evaluate \textit{CausalDreamer} and the pretrained world model it starts from with model-predictive planning on 20 MMBench2 tasks: 10 clean tasks seen during training and 10 unseen tasks, of which 6 are manipulated variants of clean tasks with a changed background, object, or maze layout, and 4 are new environments. We normalize returns so that a policy taking uniformly random actions scores 0 and an expert scores 1. \textit{CausalDreamer} achieves a 14\% higher normalized score than the pretrained world model on the clean tasks (0.199 vs.\ 0.175) and a 25\% higher score on the manipulated variants (0.307 vs.\ 0.246), while neither model scores meaningfully above the random policy in the new environments. Additionally, our analysis shows that the factored representation separates reward-irrelevant changes, such as a changed background, from its reward-relevant groups.

</details>

---

### [[20_Research/Papers/具身智能/CAPABLE_Capability-Aware_Policy_Adaptation_via_Behavioral_Latent_Encoding|CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding]]

![[assets/2610.11971_figure.png|800]]

- **arXiv**: [2610.11971](https://arxiv.org/abs/2610.11971)
- **PDF**: https://arxiv.org/pdf/2610.11971
- **详细分析**: [[20_Research/Papers/具身智能/CAPABLE_Capability-Aware_Policy_Adaptation_via_Behavioral_Latent_Encoding|CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding]]
- **作者**: Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan, Jeroen Schafer, Andrew Melnik, Qing Yang, Michael Beetz
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 1.72（加权：具身智能 0.9，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NerveNet, RobustVLA, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that motion contributes to end-effector behavior, online from command-response history and kinematics using a temporal encoder shared across joints, Jacobian grounding, cross-joint attention, and self-supervised physical prediction. The resulting representation conditions a residual policy that adds bounded corrections to the VLA arm action without fault labels or faulty-joint identifiers. Across 28 LIBERO tasks, CAPABLE raises success on an actuator excluded from fault training from 24.8% to 59.3%, outperforming a parameter-matched global-history baseline by 17.4 points while preserving healthy performance. Leave-one-actuator-out experiments across six joints show that this transfer is not specific to one actuator, and additional evaluations characterize transfer to unseen fault families and demonstrate recovery on a physical Franka Panda. https://capable-vla.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Reliability-Aware_Future_Conditioning_for_Temporally_Robust_Robot_Manipulation|Reliability-Aware Future Conditioning for Temporally Robust Robot Manipulation]]

![[assets/2610.11956_figure.png|800]]

- **arXiv**: [2610.11956](https://arxiv.org/abs/2610.11956)
- **PDF**: https://arxiv.org/pdf/2610.11956
- **详细分析**: [[20_Research/Papers/具身智能/Reliability-Aware_Future_Conditioning_for_Temporally_Robust_Robot_Manipulation|Reliability-Aware Future Conditioning for Temporally Robust Robot Manipulation]]
- **作者**: Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Zhiyuan Gao, Deyuan Qu, Max Gandyra, Yanxiang Zhan, Mehreen Naeem, Andrew Melnik, Jeroen Schafer, Qing Yang, Michael Beetz
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Reliability-Aware Future Conditioning for Temporally Robust Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：XIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A generated video of a task the robot is about to perform is useful guidance only if it depicts the phase the robot is actually in. We show that temporal misalignment can turn a task-consistent generated future into actively harmful guidance. On CALVIN, a five-frame early shift nearly erases the benefit of generated futures, reducing success from 81.3% to 54.8% against 54.0% without futures; imposed timing shifts reduce it even further to 34.2%, 19.8 points below the future-free policy. We introduce Reliability-Aware Future Conditioning (RAFC), which treats this as a control problem rather than a generation problem. At every step, RAFC estimates how far to trust the received clip and which nearby temporal hypothesis to prefer, falling back toward a static branch when neither fits, and it learns both from task reward alone without shift labels or alignment supervision. RAFC sits on top of Future-Experience Conditioning (FEC), which builds the clip once from task grounding, a robot-free digital-twin rollout, and mask-free video diffusion. Under deliberately off-grid phase shifts and rate mismatch, RAFC substantially improves success under temporal mismatch. Candidate ensembling accounts for most of the recovery near alignment, while learned reliability adds a further 7.0 percentage points over uniform averaging of the identical candidate bank under off-grid shifts. The gain holds on the evaluated task sets and survives on a Franka under natural timing mismatch nobody imposed, where aggregate success rises from 26.7% to 56.7%. All resources will be made publicly available. https://future-condition.github.io/.

</details>

---

### [[20_Research/Papers/强化学习/TACROSS_An_Efficient_and_Low-Cost_Scalable_Human_Touch_System_Across_Heterogeneous_Tactile_Sensors_for_Dexterous_Robot_Learning|TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning]]

![[assets/2610.11945_figure.png|800]]

- **arXiv**: [2610.11945](https://arxiv.org/abs/2610.11945)
- **PDF**: https://arxiv.org/pdf/2610.11945
- **详细分析**: [[20_Research/Papers/强化学习/TACROSS_An_Efficient_and_Low-Cost_Scalable_Human_Touch_System_Across_Heterogeneous_Tactile_Sensors_for_Dexterous_Robot_Learning|TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning]]
- **作者**: Bo Chen, Huanzhang Hu, Junyang Ma, Bo Yue, Fangdi Yu, Haijier Chen, Xianxin Lai, Shuyu Pan, Zhen Yang, Xiaoquan Sun, Wenze Cui, Zhongliang Jiang...
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 1.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《TACROSS: An Efficient and Low-Cost Scalable Human Touch System Across Heterogeneous Tactile Sensors for Dexterous Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting tactile demonstrations on robots is costly and slow, motivating the use of lower-cost human tactile gloves for scalable data collection. However, human capacitive/piezoresistive gloves and robotic tactile sensors differ fundamentally in transduction principle, sensor layout, spatial resolution, and dynamic response, making alignment of raw sensor channels ill-posed. To address this problem, we present TACROSS, a scalable system for learning from human touch and transferring it to robots that bridges this heterogeneity by aligning tactile streams at the level of contact events rather than raw sensor values. The hardware component of TACROSS integrates a piezoresistive glove with five layers and a cost of USD 10.86 with 285 sensing points. To align contact semantics, we design canonicalizers and residual adapters that map heterogeneous signals into a shared tactile latent with 256 dimensions via a temporal Transformer with attention across fingers. We further introduce a robot-grounded policy learning scheme in which robot demonstrations provide the sole source of ground-truth action supervision, while human demonstrations support tactile representation learning and provide confidence-weighted auxiliary supervision through valid retargeted hand targets. We evaluate our system on four contact-rich manipulation tasks. Compared to conventional teleoperation, our proposed system achieves a 3.5-fold efficiency improvement while reducing demonstration acquisition equipment cost by 95.7%. We will open-source the TACROSS hardware and software system and publicly release a tactile dataset comprising over 150 hours of recordings. Project page: https://tacross-touch-project.github.io/.

</details>

---

### [[20_Research/Papers/强化学习/When_to_Intervene_State-Aware_Sparse_Manipulation_in_Federated_Reinforcement_Learning|When to Intervene? State-Aware Sparse Manipulation in Federated Reinforcement Learning]]

![[assets/2610.11523_figure.png|800]]

- **arXiv**: [2610.11523](https://arxiv.org/abs/2610.11523)
- **PDF**: https://arxiv.org/pdf/2610.11523
- **详细分析**: [[20_Research/Papers/强化学习/When_to_Intervene_State-Aware_Sparse_Manipulation_in_Federated_Reinforcement_Learning|When to Intervene? State-Aware Sparse Manipulation in Federated Reinforcement Learning]]
- **作者**: Shutong Zheng, Sijia Chen
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《When to Intervene? State-Aware Sparse Manipulation in Federated Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated reinforcement learning (FRL) enables distributed agents to collaboratively train decision-making policies, but its decentralized training process also exposes global policy learning to Byzantine manipulation. Existing poisoning attacks primarily focus on how to construct malicious updates, while trajectory-level intervention timing remains largely implicit. In sequential decision making, however, where an intervention is applied can alter subsequent trajectories and learning signals. Through controlled experiments, we find that changing the selected trajectory states materially alters attack efficacy even when the malicious-update construction is fixed. We therefore identify when as a distinct attack dimension and introduce the Viability-constrained Behavioral Steering Attack (V-BSA), which uses local policy uncertainty to select sparse intervention states and applies envelope-constrained behavioral steering. Across discrete-action benchmarks, V-BSA achieves substantial degradation against robust aggregators and ensemble defenses with only a fraction of the interventions used by dense poisoning, while revealing task- and aggregation-dependent boundaries. Overall, our results highlight intervention timing as a distinct dimension of sequential robustness in FRL. The code is available at https://github.com/Yodeesy/V-BSA

</details>

---

### [[20_Research/Papers/强化学习/DaCe-DT_Data-Centric_Offline_Multi-Task_Reinforcement_Learning_via_Adaptive_Prompts_and_Trajectory_Correction_for_Heterogeneous_Tasks|DaCe-DT: Data-Centric Offline Multi-Task Reinforcement Learning via Adaptive Prompts and Trajectory Correction for Heterogeneous Tasks]]

![[assets/2610.11085_figure.png|800]]

- **arXiv**: [2610.11085](https://arxiv.org/abs/2610.11085)
- **PDF**: https://arxiv.org/pdf/2610.11085
- **详细分析**: [[20_Research/Papers/强化学习/DaCe-DT_Data-Centric_Offline_Multi-Task_Reinforcement_Learning_via_Adaptive_Prompts_and_Trajectory_Correction_for_Heterogeneous_Tasks|DaCe-DT: Data-Centric Offline Multi-Task Reinforcement Learning via Adaptive Prompts and Trajectory Correction for Heterogeneous Tasks]]
- **作者**: Xinfei Wang, Shanchen Pang, Chenhao Zhang, Shudong Wang, Wenhao Ji, Haiyuan Gui, Meng Han, Xiaojian Liao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《DaCe-DT: Data-Centric Offline Multi-Task Reinforcement Learning via Adaptive Prompts and Trajectory Correction for Heterogeneous Tasks》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MTRL, Meta-World, MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline multi-task reinforcement learning (Offline MTRL) heavily depends on the quality and distribution of pre-collected data. However, existing methods mainly focus on algorithmic optimization, with less emphasis on data-level improvements to enhance learning ability and generalization performance. This paper, from a data perspective, reveals three key bottlenecks that limit Offline MTRL performance:(i) ineffective utilization of prompts length under diverse task complexities, and (ii) semantic irrelevance of randomly sampled prompt segments, (iii) misleading supervision induced by fragmented and discontinuous trajectories. To address these challenges, we propose DaCe-DT, a robust offline MTRL framework designed to be insensitive to heterogeneous task complexities and data quality, featuring length-gated prompt masking (LGPM), retrieval-augmented prompt construction (RAPC), and value-adaptive return calibration (VARC). Together, these mechanisms enable DaCe-DT to deliver data-centric prompt adaptation and trajectory refinement, resulting in robust multi-task generalization and stable policy learning amid heterogeneous offline data and tasks. Experimental results on Meta-World show that DaCe-DT consistently outperforms state-of-the-art methods, achieving an average improvement of 11.73% on optimal datasets and an improvement of 13.34% on suboptimal datasets, demonstrating its effectiveness in learning stably from imperfect data and improving overall multi-task performance.

</details>

---

### [[20_Research/Papers/具身智能/Higher-Order_Morphology_Priors_for_Quadruped_Reinforcement_Learning_Under_Actuator_Degradation|Higher-Order Morphology Priors for Quadruped Reinforcement Learning Under Actuator Degradation]]

![[assets/2610.10934_figure.png|800]]

- **arXiv**: [2610.10934](https://arxiv.org/abs/2610.10934)
- **PDF**: https://arxiv.org/pdf/2610.10934
- **详细分析**: [[20_Research/Papers/具身智能/Higher-Order_Morphology_Priors_for_Quadruped_Reinforcement_Learning_Under_Actuator_Degradation|Higher-Order Morphology Priors for Quadruped Reinforcement Learning Under Actuator Degradation]]
- **作者**: Derek You, Zafir Shamsi, Keqin Wang, Christine Allen-Blanchette
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.82（加权：具身智能 1.8，强化学习 0.76，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Higher-Order Morphology Priors for Quadruped Reinforcement Learning Under Actuator Degradation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：NerveNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actuator degradation turns quadruped locomotion into a coordination problem requiring joints to compensate for lost actuation. Prior work suggests that morphology-aware graph policies improve learning and generalization under body perturbations. We ask whether these benefits can be strengthened by explicitly modeling higher-order mechanical structure. We represent the Unitree Go1 as a cell complex with limb- and body-level rank-2 cells and apply Hodge-based message passing. Under degradation training, the node-edge-face Hodge actor achieves the highest return on unseen actuator degradations, with higher survival and lower velocity-tracking error. These results support higher-order morphology as a useful inductive bias for whole-body compensation under actuator degradation.

</details>

---

### [[20_Research/Papers/具身智能/World-Model_Policy_Arbiter_for_Goal-Conditioned_Reinforcement_Learning|World-Model Policy Arbiter for Goal-Conditioned Reinforcement Learning]]

![[assets/2610.10932_figure.png|800]]

- **arXiv**: [2610.10932](https://arxiv.org/abs/2610.10932)
- **PDF**: https://arxiv.org/pdf/2610.10932
- **详细分析**: [[20_Research/Papers/具身智能/World-Model_Policy_Arbiter_for_Goal-Conditioned_Reinforcement_Learning|World-Model Policy Arbiter for Goal-Conditioned Reinforcement Learning]]
- **作者**: Junwei Quan, Evgenii Opryshko, Nicholas Rhinehart, Igor Gilitschenski
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.36）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《World-Model Policy Arbiter for Goal-Conditioned Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GCRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning (GCRL) has produced a diverse set of goal-reaching algorithms, yet no single algorithm performs best across environments, goals, and even different phases of the same task. Rather than deploying only the best-performing policy, we ask whether a set of frozen goal-conditioned policies can be used collectively as a portfolio, deciding at every state which policy should act. Choosing a policy at each state is not straightforward. The policies' own value functions cannot be compared directly: they may use different scales, and some policies have no value function. We need to judge each policy by the states it is likely to reach, even though we can execute only one policy at a time. We also need to avoid switching so often that control becomes unstable. To address these challenges, we introduce World-Model Policy Arbiter (WMPA), a test-time framework that, given a set of frozen policies as input, rolls out each frozen policy in a learned state-space world model, evaluates the imagined futures with a shared goal-conditioned value function, and executes the highest-scoring policy for a short commitment interval before the next round of arbitration (policy selection). WMPA assumes access to a bank of frozen goal-conditioned policies and requires neither policy retraining nor privileged task-specific knowledge. Under the official OGBench evaluation protocol on 18 state-based datasets spanning maze navigation as well as cube, scene, and puzzle manipulation, WMPA improves the macro-average success rate from the 44% achieved by the best policy selected per dataset to 58%, with statistically significant gains on 12 datasets. These gains include +33 percentage points on cube-double-play and +36 percentage points on scene-play.

</details>

---

### [[20_Research/Papers/大模型/Similar_Predictive_Fit_but_Different_Latent_Dynamics_Characterizing_Learned_Dynamical_Structure_in_Personalized_Models_of_Brain_Disorders|Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders]]

![[assets/2610.10850_figure.png|800]]

- **arXiv**: [2610.10850](https://arxiv.org/abs/2610.10850)
- **PDF**: https://arxiv.org/pdf/2610.10850
- **详细分析**: [[20_Research/Papers/大模型/Similar_Predictive_Fit_but_Different_Latent_Dynamics_Characterizing_Learned_Dynamical_Structure_in_Personalized_Models_of_Brain_Disorders|Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders]]
- **作者**: Rita Huan-Ting Peng, Nhat Bui
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.16，世界模型 0.96）
- **关联关键词**: LLM, WorldModel

#### 研究背景与动机

《Similar Predictive Fit but Different Latent Dynamics: Characterizing Learned Dynamical Structure in Personalized Models of Brain Disorders》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As AI models move toward clinical decision-making and personalized treatment, understanding \emph{what} a model learns is important beyond predictive accuracy alone. We investigate whether personalized latent dynamics reveal clinically associated differences even when predictive fit is similar. A lightweight CNN--Transformer EEG foundation model pretrained on the Temple University EEG Corpus (TUEG) extracts segment-level representations. Using the Temple University Epilepsy Corpus (TUEP), representations are mapped to a shared latent-state space, and sparse multinomial logistic transition distributions (mLTD) are fit independently to each subject to obtain personalized transition-dependency graphs $W_n$. Analyses include $n{=}198$ subjects (99 epilepsy / 99 non-epilepsy). At $k{=}4$, epilepsy subjects exhibit substantially denser learned dependency structure ($p{=}1.1\times10^{-7}$), with the same pattern at $k{=}6$ (19.90 vs. 13.46; $p{=}5.2\times10^{-5}$). Graph-derived features provide moderate group discrimination under 5-fold subject-wise cross-validation (AUROC 0.68 at $k{=}4$; 0.65 at $k{=}6$). In contrast, held-out log-likelihood is nearly identical between groups at $k{=}4$ ($-0.992$ vs. $-0.991$; $p{=}0.95$), with similarly matched next-state prediction (AUROC 0.855 vs. 0.861; $p{=}0.54$). Thus, similar predictive fit does not imply similar learned dynamics: groups can be comparably predictable while differing substantially in the internal dynamical structure learned by personalized models. This distinction motivates evaluating learned structure alongside predictive performance in personalized clinical models.

</details>

---

### [[20_Research/Papers/具身智能/Diagnosing_and_Recovering_from_Observation-Space_Shift_at_Long-Horizon_Skill_Seams|Diagnosing and Recovering from Observation-Space Shift at Long-Horizon Skill Seams]]

![[assets/2610.10810_figure.png|800]]

- **arXiv**: [2610.10810](https://arxiv.org/abs/2610.10810)
- **PDF**: https://arxiv.org/pdf/2610.10810
- **详细分析**: [[20_Research/Papers/具身智能/Diagnosing_and_Recovering_from_Observation-Space_Shift_at_Long-Horizon_Skill_Seams|Diagnosing and Recovering from Observation-Space Shift at Long-Horizon Skill Seams]]
- **作者**: Pranav Wagh, Yu Fang, Yue Yang, Mingyu Ding
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Diagnosing and Recovering from Observation-Space Shift at Long-Horizon Skill Seams》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robotic manipulation is often built by chaining independently trained skills. Although each skill can be reliable in isolation, performance degrades sharply when skills are chained: each downstream skill must start from the state its predecessor leaves behind rather than from its training distribution. We study this failure mode, Observation-Space Shift (OSS), and ask what causes these skill-seam failures. Using privileged simulator resets, we find that the dominant shift comes from displaced scene state (e.g., an open drawer or secondary objects left behind by earlier skills), not from the robot's joint configuration or the object the downstream skill manipulates. To test this diagnosis, we build a fully learned detect-restore-resume system: a task-progress monitor detects the stall, a learned policy restores the displaced scene components, and seam-robust fine-tuning lets the skill resume. It recovers the seam where every tested alternative fails, which we treat as evidence for the diagnosis rather than as a general-purpose method. On the BOSS-44 benchmark, the system improves full-chain success from 7.6% to 26.5%, a 3.5x improvement over the base policy and 51% of a privileged restoration oracle, whereas best-of-K resampling, a Diffusion Policy, and world-model baselines fail to recover from the evaluated seam states. On a real Franka arm running a fine-tuned $π_{0.5}$ policy, the same monitor is limited by exterior-camera observability, yet closing the loop still recovers some otherwise-terminal failures, motivating wrist and gripper sensing. These results suggest that some long-horizon composition failures are better addressed by restoring the scene before resuming the policy than by retrying from an off-support state.

</details>

---

### [[20_Research/Papers/强化学习/Strategic_Investment_Decision_Making_for_Value_Creation_in_Energy_Transition_A_Reinforcement_Learning_Approach|Strategic Investment Decision Making for Value Creation in Energy Transition: A Reinforcement Learning Approach]]

![[assets/2610.10768_first_page.png|800]]

- **arXiv**: [2610.10768](https://arxiv.org/abs/2610.10768)
- **PDF**: https://arxiv.org/pdf/2610.10768
- **详细分析**: [[20_Research/Papers/强化学习/Strategic_Investment_Decision_Making_for_Value_Creation_in_Energy_Transition_A_Reinforcement_Learning_Approach|Strategic Investment Decision Making for Value Creation in Energy Transition: A Reinforcement Learning Approach]]
- **作者**: Yasaman Cheraghi, Reidar B. Bratvold, Aojie Hong, Ressi B. Muhammad, Sergey Alyaev
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Strategic Investment Decision Making for Value Creation in Energy Transition: A Reinforcement Learning Approach》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The global challenge of climate change has driven significant steps to reduce CO2 emissions, guided by international agreements like the Paris Agreement of 2015. Acting too slowly could result in future losses and reputational damage, while moving too quickly could jeopardize shareholder value due to the marginal profitability or potential losses due to technology immaturity of many renewable projects. To navigate this complex transition, energy companies must adopt Sequential Decision Making (SDM) strategies to maximize value creation from decision flexibility under uncertainties. To support this, we developed a custom simulation environment to model the dynamic energy landscape up to 2050. Building on this, we designed a multi-criteria SDM framework that explores various decision strategies related to different portfolios for allocating funds across three sectors: oil &amp; gas, renewables, and CO2 reduction. It aims to maximize value during the transition while accounting for uncertainties in productions, energy prices, and costs. This framework has three objectives: maximizing profit, minimizing CO2 social costs, and enhancing competitive advantage in the renewable energy sector. This research evaluates the use of Reinforcement Learning (RL) to identify optimal investment policies within the defined SDM framework. The agent's sequential decisions shape a virtual dynamic environment by influencing key variables such as oil and gas production, renewable energy output, CO2 emissions, and revenues. Through repeated interaction, the RL algorithm explores the state space and learns an optimal policy under uncertainty. We benchmark the RL strategy against a set of manually defined baseline policies and find it consistently outperforms them in adaptability and long-term value creation.

</details>

---
