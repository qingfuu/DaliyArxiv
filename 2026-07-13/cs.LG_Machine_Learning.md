# cs.LG | Machine Learning | 2026-07-13

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/大模型/LLM_for_EDA_in_Front-End_Design_Challenges_and_Opportunities|LLM for EDA in Front-End Design: Challenges and Opportunities]]

![[assets/2607.09616_figure.png|800]]

- **arXiv**: [2607.09616](https://arxiv.org/abs/2607.09616)
- **PDF**: https://arxiv.org/pdf/2607.09616
- **详细分析**: [[20_Research/Papers/大模型/LLM_for_EDA_in_Front-End_Design_Challenges_and_Opportunities|LLM for EDA in Front-End Design: Challenges and Opportunities]]
- **作者**: Kangwei Xu, Bing Li, Ulf Schlichtmann
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《LLM for EDA in Front-End Design: Challenges and Opportunities》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoBench, AutoEval, ConfiBench, CorrectBench, VerilogEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As chip complexity increases and time-to-market pressures grow, front-end design has become a critical bottleneck in chip development. Recently, Large Language Models (LLMs) have shown great potential in Electronic Design Automation (EDA). Beyond specification understanding, LLMs show the potential to serve as a unified intelligent interface for hardware description language (HDL) generation, testbench construction, and design space exploration. The rise of agentic AI, represented by pioneering systems such as OpenClaw, offers a strategic roadmap for the next generation EDA. From this perspective, this paper discusses the evolution of EDA from localized assistance to autonomous agentic execution. Then, we review representative advances of LLMs in front-end design, focusing on key tasks such as circuit and testbench generation from a shared specification, as well as design quality improvement in established workflows such as high-level synthesis. Finally, we discuss the key challenges and limitations of integrating LLMs into EDA, and outline future opportunities for advancing LLM-enabled front-end design, offering a systematic perspective for researchers interested in leveraging agentic AI technologies for EDA.

</details>

---

### [[20_Research/Papers/强化学习/Action-Factored_Multi-Agent_Reinforcement_Learning_for_Scalable_Quantum_Device_Tuning|Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning]]

![[assets/2607.09422_figure.png|800]]

- **arXiv**: [2607.09422](https://arxiv.org/abs/2607.09422)
- **PDF**: https://arxiv.org/pdf/2607.09422
- **详细分析**: [[20_Research/Papers/强化学习/Action-Factored_Multi-Agent_Reinforcement_Learning_for_Scalable_Quantum_Device_Tuning|Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning]]
- **作者**: Edwin De Nicolo, Rahul Marchand, Cornelius Carlsson, Pranav Vaidhyanathan, Natalia Ares
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HyperMARL, InforMARL, MARL, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-agent reinforcement learning is well suited to problems with large parameter spaces and exploitable local structure, such as the tuning of electrostatically-defined quantum-dot arrays. However, if parameter cross-talk is strong, a non-stationary environment from the perspective of any individual agent can destabilize learning - the same effect that plagues manual tuning of such systems. We propose using a factored representation of the action space, learned online, to decouple agents and minimize their interference. Our framework, QADAPT, uses this factorization to efficiently learn shared policies based on local measurements and rewards. With this modular strategy, we achieve zero-shot generalization to unseen quantum device sizes and maintain an approximately constant number of convergence steps to reach target regimes. This work provides a scalable route toward the rapid calibration of large-scale quantum processors.

</details>

---

### [[20_Research/Papers/具身智能/GenVid2Robot_From_Video_Generation_to_Robot_Manipulation_via_Rigid-Geometric_Consistency|GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency]]

![[assets/2607.09191_figure.jpg|800]]

- **arXiv**: [2607.09191](https://arxiv.org/abs/2607.09191)
- **PDF**: https://arxiv.org/pdf/2607.09191
- **详细分析**: [[20_Research/Papers/具身智能/GenVid2Robot_From_Video_Generation_to_Robot_Manipulation_via_Rigid-Geometric_Consistency|GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency]]
- **作者**: Haohui Huang, Xi Yuan, Panpan Liao, Tao Teng, Chenguang Yang, Jing Guo, Yi Guo
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generated videos provide useful visual motion priors for robot manipulation, but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry, grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction, GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.

</details>

---

### [[20_Research/Papers/大模型/Present_but_Rescaled_Chat-to-Agent_Transfer_of_Additive_Activation_Steering|Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering]]

![[assets/2607.09156_figure.png|800]]

- **arXiv**: [2607.09156](https://arxiv.org/abs/2607.09156)
- **PDF**: https://arxiv.org/pdf/2607.09156
- **详细分析**: [[20_Research/Papers/大模型/Present_but_Rescaled_Chat-to-Agent_Transfer_of_Additive_Activation_Steering|Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering]]
- **作者**: Lucas Pinto
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Additive activation steering (injecting a scaled residual-stream direction during generation) is calibrated almost entirely in single-turn chat, yet the models it targets are increasingly deployed as tool-using ReAct agents. We present the first systematic chat-to-agent transfer study of additive steering, coupling behavioral measurement with a representation read-out in a matched-information design: the same items rendered as plain chat or as a ReAct tool-use episode, with matched-norm random-direction controls and the transcript re-encoded every turn to exclude KV-cache contamination. Transfer is real but rescaled, and the right description is a dissociation: the injected direction reaches the late layers at near-full strength in every setting and model tested (install-site agent-over-chat ratios 0.83-1.16 across three families), while the behavioral coupling is reset per model and context. On Qwen2.5-7B a refusal bypass vector amplifies in the agent (T = 1.45, CI [1.20, 1.78], N = 300); across a powered uniform-protocol distribution the coupling spans amplification (Gemma-2-9B T = 2.00) to attenuation (Yi-1.5-9B T = 0.43, CI [0.29, 0.60]), with no universal constant and a single clean attenuator against a universal sign. Directional ablation of the same axis does not amplify (T = 0.93, CI including 1) while additive injection amplifies (T = 1.50), a 20.1-point gain difference (CI [13.4, 26.8]) that identifies an additive-specific mechanism. Two pre-registered instruments converge to localize the rescaling to the ReAct format scaffold, before any tool observation, rather than to the observation boundary where a dilution account would predict it. The safety implication is immediate and unpredictable: agentic deployment amplifies steering-based refusal bypass by up to 2.00x on some models while others attenuate, so a deployment cannot assume a given model is safe under additive steering.

</details>

---

### [[20_Research/Papers/具身智能/Learning_More_from_Less_Reinforcement_Learning_from_Hindsight|Learning More from Less: Reinforcement Learning from Hindsight]]

![[assets/2607.09042_figure.png|800]]

- **arXiv**: [2607.09042](https://arxiv.org/abs/2607.09042)
- **PDF**: https://arxiv.org/pdf/2607.09042
- **详细分析**: [[20_Research/Papers/具身智能/Learning_More_from_Less_Reinforcement_Learning_from_Hindsight|Learning More from Less: Reinforcement Learning from Hindsight]]
- **作者**: Iris Xu, Sunshine Jiang, John Marangola, Nitish Dashora, Richard Li, Thomas Liu, Zexue He, Yuheng Zhi, Alex Pentland, Pulkit Agrawal, Zhang-Wei Hong
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 大模型, 机器人, 世界模型
- **相关性评分**: 2.12（加权：具身智能 0.6，大模型 0.2，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Learning More from Less: Reinforcement Learning from Hindsight》归入 强化学习、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is increasingly used to post-train vision-language-action (VLA) models, but every update consumes robot rollouts that are slow and costly to collect, making sample efficiency a central concern. Manipulation tasks typically provide only sparse rewards, so a weak policy fails almost every rollout early in training and has little to learn from, even when those failures execute coherent behavior. Such a failure, however, is a success at a different task. We present Learning from Hindsight (LfH), which brings hindsight relabeling to RL post-training of VLAs by scoring failed rollouts against the tasks they actually achieved. A single vision-language model relabels both the instruction and the reward, proposing a hindsight instruction for a group of failed rollouts and scoring how well each satisfies it, and the policy trains on the relabeled and original rollouts jointly. Because VLAs generalize across language, relabeling in language lets the policy learn more from the same trajectories. On out-of-distribution LIBERO-PRO tasks, where standard RL improves only slowly, LfH achieves $5\times$ improvement in sample efficiency, and outperforms a dense progress-reward baseline. The gains hold across VLA backbones and on a physical Franka robot.

</details>

---

### [[20_Research/Papers/强化学习/SafeExplorer_An_Unbiased_Policy_Gradient_for_Reinforcement_Learning_with_Recovery_Interventions|SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions]]

![[assets/2607.08925_figure.png|800]]

- **arXiv**: [2607.08925](https://arxiv.org/abs/2607.08925)
- **PDF**: https://arxiv.org/pdf/2607.08925
- **详细分析**: [[20_Research/Papers/强化学习/SafeExplorer_An_Unbiased_Policy_Gradient_for_Reinforcement_Learning_with_Recovery_Interventions|SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions]]
- **作者**: Elham Daneshmand, Majid Khadiv, Glen Berseth, Hsiu-Chin Lin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.12（加权：大模型 0.2，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：JSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training reinforcement-learning agents directly on physical robots makes every fall costly, since a fall can damage the platform and cannot be undone like a simulator reset; the goal is therefore to minimize falls during training rather than trade them off against return, as constrained Markov decision process (MDP) formulations do. A standard mitigation hands control to a separate recovery policy whenever the agent leaves a designer-specified safe region (a subset of state space it should stay within), but the resulting mixed-policy rollouts silently bias every on-policy update, and the importance-sampling correction that would remove this bias is ill-defined whenever the recovery policy is deterministic. We address this bias with a drop-in modification of proximal policy optimization (PPO). Its core is an unbiased policy-gradient estimator that uses the score function only at safe timesteps and never evaluates the recovery policy's density, so it stays valid even when the recovery policy is deterministic, exactly where importance sampling breaks, and it empirically dominates importance sampling even when the recovery policy is stochastic. Because the recovery policy still makes credit assignment slow near the safe-region boundary, two further components accelerate learning: a closed-form value for recovery-triggering states when dynamics and recovery are deterministic, and an imitation loss that copies recovery actions only when recovery succeeds. On a three-environment, five-seed benchmark, the resulting algorithm reduces training-time falls by factors of 233x, 48x, and 26x on HalfCheetah, Ant, and Unitree Go1 over standard PPO, while matching or exceeding PPO's final reward, and on Ant, where the recovery policy is unreliable, it is the only method that reaches 80% of the best final reward.

</details>

---

### [[20_Research/Papers/强化学习/FlowDAgger_Human-in-the-Loop_Adaptation_of_Generative_Robot_Policies_in_Latent_Space|FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space]]

![[assets/2607.08877_figure.png|800]]

- **arXiv**: [2607.08877](https://arxiv.org/abs/2607.08877)
- **PDF**: https://arxiv.org/pdf/2607.08877
- **详细分析**: [[20_Research/Papers/强化学习/FlowDAgger_Human-in-the-Loop_Adaptation_of_Generative_Robot_Policies_in_Latent_Space|FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space]]
- **作者**: Michael Murray, Daphne Chen, Simran Bagaria, Dean Fortier, Tess Hellebrekers, Galen Mullins, Harshavardhan Gajarla, Oier Mees, Maya Cakmak, Andrey Kolobov
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space》归入 机器人、强化学习、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, HIL-SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained generative robot policies based on flow matching and diffusion have achieved impressive results across a wide range of manipulation tasks. Yet real-world deployments routinely expose failure modes outside the pretraining distribution. Closing these gaps typically requires large-scale data collection or online reinforcement learning on physical hardware, which is impractical for rapid and safe adaptation. We present FlowDAgger, a sample- and compute-efficient method for adapting frozen generative robot policies from human interventions in latent space. Our key idea is action inversion: each human expert action is mapped to the noise that would have produced it under the frozen base policy, using reverse-time integration followed by local refinement. The resulting inverted noise provides supervision for a lightweight latent policy that steers the base model at deployment time, enabling rapid skill acquisition while preserving its behavioral priors. We evaluate FlowDAgger in simulation and on real-world bimanual and single-arm manipulation, adapting both action-head VLAs and world-action models from a handful of interventions. FlowDAgger outperforms supervised fine-tuning and latent-space RL baselines and preserves pretrained skills on held-out tasks, offering a practical path for adapting robot foundation models in the real world. Website: https://microsoft.github.io/FlowDAgger

</details>

---
