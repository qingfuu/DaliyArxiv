# cs.AI | Artificial Intelligence | 2026-10-14

#arxiv #ComputerScience

**论文数**: 26

### [[20_Research/Papers/具身智能/ChunkAct_Action_Chunking_for_Agentic_Robotics|ChunkAct: Action Chunking for Agentic Robotics]]

![[assets/2610.18874_figure.png|800]]

- **arXiv**: [2610.18874](https://arxiv.org/abs/2610.18874)
- **PDF**: https://arxiv.org/pdf/2610.18874
- **详细分析**: [[20_Research/Papers/具身智能/ChunkAct_Action_Chunking_for_Agentic_Robotics|ChunkAct: Action Chunking for Agentic Robotics]]
- **作者**: Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang, Emilio Ferrara
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.75（加权：具身智能 0.9，大模型 0.55，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《ChunkAct: Action Chunking for Agentic Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.

</details>

---

### [[20_Research/Papers/具身智能/What_Matters_in_Quality-Aware_VLA_Pretraining_A_Benchmark_and_Empirical_Study|What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study]]

![[assets/2610.18869_figure.png|800]]

- **arXiv**: [2610.18869](https://arxiv.org/abs/2610.18869)
- **PDF**: https://arxiv.org/pdf/2610.18869
- **详细分析**: [[20_Research/Papers/具身智能/What_Matters_in_Quality-Aware_VLA_Pretraining_A_Benchmark_and_Empirical_Study|What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study]]
- **作者**: Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang, Wenqian Zhang, Hefeifei Jiang, Peihao Li, Jian Zhang, Mengfei Zhao, Yikai Tang, Hai Zhai...
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AXIS-Bench, Cross-VLA, OpenVLA, Real-World, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Across three VLAs, we find that approach-aware episode conditioning improves mean success over plain behavioral cloning; conditioning and filtering favor episode and chunk labels, respectively, on average, with model-dependent reversals; and constant-tag fine-tuning improves mean success after conditioned pretraining with either tagged or untagged inference. We introduce AXIS-Bench to support these controlled comparisons. Built on crowdsourced simulation demonstrations, it provides recorded object and contact states for recomputing quality labels on shared trajectories. Replayable trajectories support workspace-aligned rendering and user-defined real-world target tasks. In our real-world experiment, simulation pretraining raises success from 9.6\% to 31.7\%. Project page: https://axis-bench.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/LIBERO-RIG_A_Hardware-Setup_Robustness_Benchmark_for_Vision-Language-Action_Models|LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models]]

![[assets/2610.18843_figure.png|800]]

- **arXiv**: [2610.18843](https://arxiv.org/abs/2610.18843)
- **PDF**: https://arxiv.org/pdf/2610.18843
- **详细分析**: [[20_Research/Papers/具身智能/LIBERO-RIG_A_Hardware-Setup_Robustness_Benchmark_for_Vision-Language-Action_Models|LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models]]
- **作者**: Andrea Yaoyun Cui, Hanyu Wang, Xinyi Wang, Bangzheng Li, Lin Zhang, Zhenggang Tang, Shyamal Buch, Dejia Xu, Matthew Tancik
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL, OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task fixed. The benchmark spans eleven perturbation axes, including camera mounting and optics, camera-to-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height, and gripper pads. Each axis has five severity levels, yielding 210 conditions across the four LIBERO suites. We evaluate nine recent vision-language-action models using 500 episodes per condition and substantiate each finding with rigorous statistical tests. Pooled success falls from 0.932 to 0.767 at the middle severity and 0.509 at the highest severity. Performance degradation varies substantially across perturbation axes and action interfaces, and training on visual perturbations does not mitigate faults that leave camera images unchanged. We release the benchmark together with manifests specifying the fixed perturbation parameters for each episode.

</details>

---

### [[20_Research/Papers/具身智能/RoboSimStudio_An_Interactive_Toolkit_for_Rapid_Real2Sim_of_Robot_Manipulation_Tasks|RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks]]

![[assets/2610.18835_figure.png|800]]

- **arXiv**: [2610.18835](https://arxiv.org/abs/2610.18835)
- **PDF**: https://arxiv.org/pdf/2610.18835
- **详细分析**: [[20_Research/Papers/具身智能/RoboSimStudio_An_Interactive_Toolkit_for_Rapid_Real2Sim_of_Robot_Manipulation_Tasks|RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks]]
- **作者**: Kaiyuan Chen, Shuangyu Xie, Uksang Yoo, Xinyue Zhu, Cael Magner, Alvin Zhu, Daehwa Kim, Eric Heiden, Erwin Coumans, Miles Macklin, Spencer Huang, Ken Goldberg
- **cs 子类**: cs.AI, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Blox-Net, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

It is difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes choices of solver, contact model, and physical parameters explicit and editable, allowing both humans and coding agents to iteratively refine simulations based on observed physical behavior. We implement RSS with the open Newton physics simulation system and describe experiments with human-guided real2sim using (1) visual evaluation, (2) force-feedback and (3) agentic Real2Sim2Real. Code, video and additional information can be found on the project website.

</details>

---

### [[20_Research/Papers/具身智能/SEAR_Self-Evolving_Agentic_Robotics|SEAR: Self-Evolving Agentic Robotics]]

![[assets/2610.18792_figure.png|800]]

- **arXiv**: [2610.18792](https://arxiv.org/abs/2610.18792)
- **PDF**: https://arxiv.org/pdf/2610.18792
- **详细分析**: [[20_Research/Papers/具身智能/SEAR_Self-Evolving_Agentic_Robotics|SEAR: Self-Evolving Agentic Robotics]]
- **作者**: Xinyi Wang, Bangzheng Li, Hanyu Wang, Lin Zhang, Andrea Yaoyun Cui, Zhenggang Tang, Shyamal Buch, Dejia Xu
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.55（加权：具身智能 0.6，大模型 0.45，机器人 1.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SEAR: Self-Evolving Agentic Robotics》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier language-model agents can now improve robots on their own: they write control code, test it, and keep what works as skills and memories for the next task. We introduce SEAR (Self-Evolving Agentic Robotics), a framework and benchmark built around two questions. Is the agent really learning, or just trying more often? And does what it learns still help on new tasks, in a new simulator, and on a real robot? The framework runs an agent in three modes: it writes code that becomes the policy (code-as-policy), acts live in the control loop (agent-as-policy), or works as a researcher that fine-tunes a vision-language-action model (auto-research). The benchmark adds controls that separate retained experience from repeated attempts, familiar tasks, privileged simulator state, larger budgets, and luck. Across seven frontier language models, 330 simulated and five physical tasks, and over four years of agent runtime, we highlight three findings. First, the learning curve of a robotic agent depends both on the overall time budget and the task difficulty relative to model capability. Harder tasks make longer sessions worthwhile; on easier tasks, re-rolling short attempts does just as well. Second, control code and shared routines transfer across tasks and simulators, while task-specific solutions do not. On a real robot, we observe a performance gap between agent-designed practice and novel human-designed scenes. Third, different models evolve more effectively in different ways. Some do best acting live, others writing code first. And a text-only model keeps pace with a comparable multimodal one: perception helps with error assessment, but agentic reasoning and tool use can matter more. We release the benchmark and codebase to support future research.

</details>

---

### [[20_Research/Papers/大模型/Can_an_Agent_Learn_to_Predict_Its_Own_Failure_Outcome-Grounded_Confidence_Calibration_in_LLM_Agents|Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents]]

![[assets/2610.18614_first_page.png|800]]

- **arXiv**: [2610.18614](https://arxiv.org/abs/2610.18614)
- **PDF**: https://arxiv.org/pdf/2610.18614
- **详细分析**: [[20_Research/Papers/大模型/Can_an_Agent_Learn_to_Predict_Its_Own_Failure_Outcome-Grounded_Confidence_Calibration_in_LLM_Agents|Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents]]
- **作者**: Ashutosh Hathidara
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.82（加权：大模型 1.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Can an Agent Learn to Predict Its Own Failure? Outcome-Grounded Confidence Calibration in LLM Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Controlling an acting LLM agent means deciding, at each step of a long-horizon task, whether to trust its next action, abstain, or hand off to a human. That decision needs a per-step confidence signal predicting whether the current rollout will eventually succeed. The agent's own self-reported verbalized confidence is the natural candidate, but existing reinforcement learning methods calibrate it against the correctness of a decision at the current step. We propose a method to calibrate it against the eventual outcome of a multi-step episode: under GRPO, the group of rollouts for a task supplies success labels, and a proper scoring rule scores each step's confidence against the realized outcome. In offline RL on recorded trajectories of a Qwen2.5-7B agent in ALFWorld, TextWorld, and WebShop environments, the AUROC of step confidence against episode outcome rises from near chance to 0.68-0.85, and the top-10% of steps the agent is most confident about succeed ~4.3x more often than average. In online RL on the live ALFWorld agent, four calibration rewards improve early-step AUROC, expected calibration error goes from 0.42 to below 0.12, and selective execution improves over both the untrained agent and a format-only RL control, without degrading task success. We also introduce an evaluation protocol that separates episode depth, task difficulty, and attempt-level foresight, which shows where the gain lies: the trained agent recognizes from its first step which tasks it will fail, while telling a succeeding attempt from a failing one at the same task is harder, with some early-window signal emerging on TextWorld.

</details>

---

### [[20_Research/Papers/强化学习/ACCRUE_Continual_Off-Policy_Reinforcement_Learning_for_Robot_Foundation_Models|ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models]]

![[assets/2610.18596_figure.png|800]]

- **arXiv**: [2610.18596](https://arxiv.org/abs/2610.18596)
- **PDF**: https://arxiv.org/pdf/2610.18596
- **详细分析**: [[20_Research/Papers/强化学习/ACCRUE_Continual_Off-Policy_Reinforcement_Learning_for_Robot_Foundation_Models|ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models]]
- **作者**: Changyeon Kim, Kimin Lee, Yashraj Narang, Yijie Guo
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.52（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, whereas off-policy methods improve single-task sample efficiency without addressing learner persistence across tasks. We propose ACCRUE, a continual off-policy RL framework that carries lightweight actor and critic networks across tasks, allowing each stage to reuse behavioral and value knowledge acquired through prior RL. The inherited critic adapts only on current-task transitions and guides current-task actor learning, while prior behavior is preserved by distilling the actor toward cached targets on a small number of retained episodes. Fixed visual features keep the inherited learner and its replay compatible with base-policy updates. Across contact-rich assembly sequences in simulation and on real-robot hardware, ACCRUE accelerates subsequent-task learning with near-zero forgetting and significantly reduces real-robot training time by 31.0\% to 68.5\%.

</details>

---

### [[20_Research/Papers/具身智能/Thinker-WM_A_Unified_World_Model_with_Shared_Multimodal_Representations_for_Embodied_Intelligence|Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence]]

![[assets/2610.18447_figure.png|800]]

- **arXiv**: [2610.18447](https://arxiv.org/abs/2610.18447)
- **PDF**: https://arxiv.org/pdf/2610.18447
- **详细分析**: [[20_Research/Papers/具身智能/Thinker-WM_A_Unified_World_Model_with_Shared_Multimodal_Representations_for_Embodied_Intelligence|Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence]]
- **作者**: Thinker Team, Peng Gao, Jichao Jiao, Chen Liao, Daqin Luo, Yiming Ma, Baiyu Pan, Hailin Shi, Jiyuan Wang, Xiangming Xu, Xiongwei Zhao
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 3.9（加权：具身智能 1.8，大模型 0.4，世界模型 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EWMBench, PlaNet, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented and evolved within a shared dynamics model. In this work, we present Thinker-WM, a unified multimodal world model that jointly models and generates RGB, metric depth, and robot action through a shared intermediate Unified Dynamics Transformer with modality-specific encoders and decoders. The model performs multimodal unification at the representation level: appearance, geometry, and action are transformed into a common dynamic representation and jointly evolved by shared parameters, while their distinct output structures are preserved. The same parameterization supports multiple functions, including joint video-action generation, world prediction, policy inference, action-conditioned generation, video-to-action generation, and inverse dynamics. To examine whether the shared representation captures action-related information, we introduce a lightweight motion probe that shows the frozen visual representation contains recoverable motion information. Thinker-WM is trained on a heterogeneous corpus comprising approximately 20K hours of egocentric video, 10K hours of real-robot data, and 1K hours of simulation data, including approximately 4K hours of real-robot data with aligned depth supervision. Extensive experiments demonstrate strong performance across embodied world-model evaluations. Thinker-WM ranks first on EWMBench, WorldOlympiad and WorldArena, while controlled studies further demonstrate the benefits of action conditioning, geometric interaction, and multi-function training within the shared representation.

</details>

---

### [[20_Research/Papers/具身智能/Let_the_Mind_Conceive,_Let_the_Hand_Achieve_Following_Multimodal_Instructions_for_Long-Horizon_Robotic_Manipulation|Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation]]

![[assets/2610.18352_figure.png|800]]

- **arXiv**: [2610.18352](https://arxiv.org/abs/2610.18352)
- **PDF**: https://arxiv.org/pdf/2610.18352
- **详细分析**: [[20_Research/Papers/具身智能/Let_the_Mind_Conceive,_Let_the_Hand_Achieve_Following_Multimodal_Instructions_for_Long-Horizon_Robotic_Manipulation|Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation]]
- **作者**: Youpeng Wen, Gang Wang, Tianyu Huang, Weiwei Zhang, Zhijian Huang, Wei Chen, Xieyuanli Chen, Yunhui Liu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.2，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Let the Mind Conceive, Let the Hand Achieve: Following Multimodal Instructions for Long-Horizon Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HarnessVLA, RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot following a multi-step instruction needs to act on the right objects in the right order, even as the scene changes. It must also maintain awareness of task progress and determine when to advance. To address these challenges, we introduce Orchestra, an agent harness that separates task planning and execution management from action generation. Orchestra decomposes a complete multimodal instruction into ordered subtasks, tracks completed steps, and updates the locations of relevant objects and destinations during execution. It maintains a shared context containing the active subtask, spatial grounding, and recent observations. An action policy uses this context to generate actions, while a separately trained progress evaluator estimates when to advance to the next subtask. To evaluate whether robots trained on atomic instructions and short trajectories can execute longer subtask sequences, we introduce a benchmark named RMBench-Compose. Orchestra achieves a mean success rate of $68.22\%$ across nine RMBench tasks, outperforming Mem-0 by $26.22$ percentage points. On RMBench-Compose, it achieves an Average Success Length (ASL) of $7.35$ subtasks, $2.46$ times that of HarnessVLA. Across four real-world multi-step tasks, it improves mean ASL by $25.0\%$ over Orchestra using the base $π_{0.5}$ policy. These results show that Orchestra helps robots carry out longer sequences of subtasks while preserving the requested subtask order and acting on the specified objects. Our code and project page are available at https://youpengwen.github.io/Orchestra.

</details>

---

### [[20_Research/Papers/大模型/TSRL_Trigger-based_Supervised_Reinforcement_Learning_for_Continual_Agent_Training|TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training]]

![[assets/2610.17726_figure.png|800]]

- **arXiv**: [2610.17726](https://arxiv.org/abs/2610.17726)
- **PDF**: https://arxiv.org/pdf/2610.17726
- **详细分析**: [[20_Research/Papers/大模型/TSRL_Trigger-based_Supervised_Reinforcement_Learning_for_Continual_Agent_Training|TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training]]
- **作者**: Yuqian Fu, Kaiwen Jiang, Zijun Song, Jiawei Wang, Yuanheng Zhu, Dongbin Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.92（加权：大模型 0.8，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TSRL: Trigger-based Supervised Reinforcement Learning for Continual Agent Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, SFT-RL, ScienceWorld, TSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents excel at complex, multi-step tasks but suffer from catastrophic forgetting during continual learning--acquiring new skills often degrades previously mastered capabilities. Existing post-training paradigms face a fundamental trade-off: Supervised Fine-Tuning (SFT) is sample-efficient but prone to severe forgetting, while Reinforcement Learning (RL) preserves prior capabilities but converges slowly without expert guidance. To bridge this gap, we introduce Trigger-based Supervised Reinforcement Learning (TSRL), a framework that integrates the strengths of both paradigms through an adaptive, state-dependent expert supervision mechanism. TSRL employs RL as the optimization backbone, activating SFT selectively on "hard states" where the policy fails. Theoretically, we show that restricting supervision to failure states derives an upper bound on the cumulative parameter updates, thereby reducing forgetting compared to full SFT. Empirically, TSRL achieves consistent gains across three agent benchmarks (ALFWorld, WebShop, and Deep Search) at both 7B and 32B scales. In continual learning scenarios, our method retains up to 9.6 points more capability on prior tasks than SFT-&gt;RL baselines, while matching or exceeding target-task performance.

</details>

---

### [[20_Research/Papers/大模型/PrT-Flow_Probability-Tractable_Flow_Matching_for_Reinforcement_Learning|PrT-Flow: Probability-Tractable Flow Matching for Reinforcement Learning]]

![[assets/2610.17667_first_page.png|800]]

- **arXiv**: [2610.17667](https://arxiv.org/abs/2610.17667)
- **PDF**: https://arxiv.org/pdf/2610.17667
- **详细分析**: [[20_Research/Papers/大模型/PrT-Flow_Probability-Tractable_Flow_Matching_for_Reinforcement_Learning|PrT-Flow: Probability-Tractable Flow Matching for Reinforcement Learning]]
- **作者**: Congzhong Sun, Ning Tan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.1，强化学习 1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PrT-Flow: Probability-Tractable Flow Matching for Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion models and Flow Matching can represent flexible distributions over robot actions, but many reinforcement learning algorithms also require the probability of each action. We introduce PrT-Flow (Probability-Tractable Flow Matching), which computes probability density while retaining multimodal, multi-step action generation. Its Jacobian-Tractable Transformer (JTT) makes each sampling step invertible and enables efficient computation of its Jacobian determinant. We train these finite steps with Conditional Euler-step Training (CET), which supervises their displacement over one step during sampling rather than their instantaneous velocity. We prove that, under certain assumptions, CET has the same minimizers as fitting the Euler-solver updates of Flow Matching. PrT-Flow achieves 96% success on Robomimic Lift after 300 epochs of imitation learning, matching the diffusion policy reference, and 96% success on OGBench Cube-Triple after 600k online steps. These results demonstrate that invertible networks with tractable probability densities can learn effective robot policies and support SAC-style actor-critic training. Our code is available at https://github.com/Sunlight-zero/PrT-Flow .

</details>

---

### [[20_Research/Papers/具身智能/TacitVLA_Reasoning_Vision-Language-Action_Models_Without_Reasoning_Latency|TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency]]

![[assets/2610.17540_figure.png|800]]

- **arXiv**: [2610.17540](https://arxiv.org/abs/2610.17540)
- **PDF**: https://arxiv.org/pdf/2610.17540
- **详细分析**: [[20_Research/Papers/具身智能/TacitVLA_Reasoning_Vision-Language-Action_Models_Without_Reasoning_Latency|TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency]]
- **作者**: Jack Lu, Yurong You, Boyi Li, Yulong Cao, Thomas Tian, Chaowei Xiao, Xiangyu Chen, Wenjie Luo, Boris Ivanovic, Marco Pavone, Yan Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeepThinkVLA, ERVLA, OneTwoVLA, RMBench, TacitVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Textual reasoning before acting has improved vision-language-action (VLA) models, but at the cost of latency: every action conditioned on the reasoning text must wait for autoregressive decoding. We show that actions do not need to wait for or condition on the generated reasoning to benefit from it, because the reasoning supervision already improves the backbone representation. We introduce TacitVLA, a reasoning VLA whose action expert never attends to the reasoning it generates for the current call. On long-horizon tasks where the reasoning text also serves as episodic memory, it can generate each entry during action execution rather than before acting. We evaluate it in a controlled study on four benchmarks spanning manipulation and autonomous driving, memory and non-memory tasks: RoboMME, RMBench, LIBERO, and PhysicalAI-AV. On all four, TacitVLA matches the performance of its explicit-reasoning counterpart at up to 3.4x lower latency, and matches the latency of the same architecture trained without reasoning at up to +17.1% success. In absolute terms, it surpasses the best previously published results on the RoboMME Counting suite (82.7% vs. 66.8%) and RMBench (77.5% vs. 56.5%), and reaches 72.9% on LIBERO-Plus and a 52.5% scene score on the public split of the PhysicalAI-AV closed-loop driving challenge. Project page: https://tacitvla.github.io.

</details>

---

### [[20_Research/Papers/具身智能/Observe,_Share,_or_Predict_Disentangling_Partner_Information_in_Embodied_Multi-Agent_Collaboration|Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration]]

![[assets/2610.16895_figure.jpg|800]]

- **arXiv**: [2610.16895](https://arxiv.org/abs/2610.16895)
- **PDF**: https://arxiv.org/pdf/2610.16895
- **详细分析**: [[20_Research/Papers/具身智能/Observe,_Share,_or_Predict_Disentangling_Partner_Information_in_Embodied_Multi-Agent_Collaboration|Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration]]
- **作者**: Adrián Szlatincsán, Filippo Ziliotto, Bruno Lepri, Luciano Serafini, Massimiliano Luca, Tommaso Campari
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs are used as high-level controllers for embodied agents, but it remains unclear whether they support collaborative reasoning, such as anticipating a collaborator's actions in real-time teamwork without dialogue. We ask if observing the partner's state, exchanging object knowledge, and predicting the partner's next action, shape task outcomes and coordination when agents can share percepts but never intentions, plans, or task-level messages, and whether the two agents occupy symmetric roles. Using the Habitat-based PARTNR benchmark, we introduce a Decoupled Partial Observability regime that enforces strictly individual perception, and we augment decentralized zero-shot ReAct planners with Other Agent's State (OAS) observation, object Knowledge Exchange (KE) between co-located agents, and Other Agent's Next Action (OANA) prediction, evaluated on the full 2 x 2 x 2 grid with four planners on 1,000 validation tasks. OAS observation improves task quality, reducing extraneous effort for every planner, whereas KE primarily improves execution efficiency, cutting simulation steps by up to 25% with little change in success. The two are largely redundant for strong planners but complementary for the weakest, for which KE without the OAS is the worst configuration. OANA prediction lowers the success rate in 15 of 16 model x context pairs while raising explicit partner mentions to 55-100%, and its accuracy gains lie mainly in the coarse action type, partly because agents recognize the action the partner is already performing. The robot retrieves objects sooner and completes its tasks earlier than the simulated human. Shared context reduces total task time by shortening the remaining duration that the human works alone. Also, coordination benefits arise from responding to shared context, especially the OAS, rather than explicit anticipation, yielding shallow, planner-dependent partner modeling.

</details>

---

### [[20_Research/Papers/具身智能/LIBERO-Industry_Benchmarking_Robotic_Manipulation_under_Industrial_Process_Constraints|LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints]]

![[assets/2610.16782_figure.png|800]]

- **arXiv**: [2610.16782](https://arxiv.org/abs/2610.16782)
- **PDF**: https://arxiv.org/pdf/2610.16782
- **详细分析**: [[20_Research/Papers/具身智能/LIBERO-Industry_Benchmarking_Robotic_Manipulation_under_Industrial_Process_Constraints|LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints]]
- **作者**: Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang, Boning Tan, Liangna Fu, Chao Tan, Yafu Li, Yulong Chen, Chaoqun Wan, Zhen Huang, Shuxian Liang, Xian-Sheng Hua
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，机器人 0.8）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DynamicVLA, Evaluation-Set, Meta-World, OpenVLA, Real-World, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture these constraints when assessing generalist robot policies. To address this gap, we introduce LIBERO-Industry, a novel benchmark built on the widely used robot learning benchmark LIBERO, that translates the aforementioned industrial constraints into controllable task conditions and measurable success criteria. Specifically, LIBERO-Industry comprises three classic task scenarios: Static-to-Dynamic (S2D) loading, Dynamic-to-Static (D2S) unloading, and Dynamic-to-Dynamic (D2D) transfer. The suites contain 216 tasks in total that systematically vary object geometry, conveyor speed, interaction-window duration, and geometric acceptance region size. Extensive experiments across five generalist robot policies (including vision-language-action models and world-action models) show that performance progressively degrades as industrial constraints are introduced and combined. Under a shared fine-tuning and evaluation protocol, the LIBERO-Industry co-training condition achieved higher observed target-transfer completion than the original-LIBERO condition.

</details>

---

### [[20_Research/Papers/具身智能/VLA-GAUGE_Systematically_Evaluating_Generalization_and_Robustness_in_Vision-Language-Action_Models|VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models]]

![[assets/2610.16567_figure.png|800]]

- **arXiv**: [2610.16567](https://arxiv.org/abs/2610.16567)
- **PDF**: https://arxiv.org/pdf/2610.16567
- **详细分析**: [[20_Research/Papers/具身智能/VLA-GAUGE_Systematically_Evaluating_Generalization_and_Robustness_in_Vision-Language-Action_Models|VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models]]
- **作者**: Jun Xiao, Rui Ye, Dong Cao, Jinyu Gu, Ying Wang, Zhiliang Zhu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 2.7，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CronusVLA, DeepThinkVLA, OpenVLA, RIPT-VLA, SimpleVLA-RL, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level diagnosis and combinatorial perturbation coverage, often without connecting diagnosis to targeted model refinement. We introduce VLA-GAUGE, a diagnostic framework that unifies both evaluations under a shared executable task representation. It combines (1) paired in-distribution and out-of-distribution tasks across six capability suites, (2) single-factor sensitivity analysis with combinatorial perturbation screening and evaluation, and (3) diagnosis-driven refinement through targeted data augmentation and model fine-tuning. We evaluate 12 VLAs spanning different model sizes and action-modeling paradigms under a unified protocol. We find that (1) The mean Zero-Shot Score on VLA-GAUGE is only 22.3%, with SimpleVLA-RL scoring 8.0% and ranking second to last among the evaluated models. (2) Under three representative combinatorial perturbation configurations, the mean R-Score is 9.3. (3) Diagnosis-driven fine-tuning improves $π_{0.5}$'s zero-shot generalization and robustness under a selected perturbation combination on held-out scenarios by 72.4 and 31.8 scoring points, respectively; the latter exceeds the 10.9-point gain from LIBERO-Plus single-factor fine-tuning despite fewer successful training trajectories. These results show that high reported success rates on familiar manipulation tasks do not guarantee strong zero-shot generalization to unseen tasks or robustness to combinatorial perturbations, while diagnostic evaluation provides actionable signals for targeted model improvement.

</details>

---

### [[20_Research/Papers/强化学习/XAI-Guided_Fourier_Domain_Generalisation_for_Pure-Simulation_Sim-to-Real_Deep_Reinforcement_Learning|XAI-Guided Fourier Domain Generalisation for Pure-Simulation Sim-to-Real Deep Reinforcement Learning]]

![[assets/2610.16478_figure.png|800]]

- **arXiv**: [2610.16478](https://arxiv.org/abs/2610.16478)
- **PDF**: https://arxiv.org/pdf/2610.16478
- **详细分析**: [[20_Research/Papers/强化学习/XAI-Guided_Fourier_Domain_Generalisation_for_Pure-Simulation_Sim-to-Real_Deep_Reinforcement_Learning|XAI-Guided Fourier Domain Generalisation for Pure-Simulation Sim-to-Real Deep Reinforcement Learning]]
- **作者**: Wei Yao, Chuyao Wang, Ziwei Wang, Nabil Aouf
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能
- **相关性评分**: 2.8（加权：具身智能 1.2，强化学习 1.6）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《XAI-Guided Fourier Domain Generalisation for Pure-Simulation Sim-to-Real Deep Reinforcement Learning》归入 强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning has shown strong potential for vision-based autonomous driving, but policies trained in simulation often suffer severe performance degradation when deployed in the real world. Existing sim-to-real methods commonly address this gap through image-transfer-based domain adaptation or policy-agnostic domain randomisation. However, the former requires laborious acquisition of target-domain data and is often limited to the deployment domain, whereas the latter introduces unguided perturbations that may not reflect the underlying sim-to-real discrepancy, leading to suboptimal transfer performance. To overcome these limitations, we propose XFD, an explainable artificial intelligence (XAI)-guided Fourier domain generalisation framework for pure-simulation sim-to-real reinforcement learning. The proposed framework extracts explainability attribution maps from simulated observations, and converts these attributions into policy-conditioned Fourier-domain interventions. By perturbing appearance-sensitive spectral components while preserving task-defining spatial structures, XFD constructs robustness-enhancing visual domains entirely within simulation. Subsequently, the proposed robust policy optimisation guides the policy towards attending to task-critical features while suppressing sensitivity to irrelevant visual information. Extensive experiments in simulation and zero-shot real-world deployment demonstrate that XFD consistently improves traveled distance and reward over standard policy and randomly domain-randomised baseline, especially on unseen maps with cluttered backgrounds. Attribution-based analysis further proves that the proposed policy preserves more consistent task-relevant visual evidence across simulation and real-world observations.

</details>

---

### [[20_Research/Papers/大模型/SurgiCLAW_An_Interpretable_Atomic-Skill_Agent_for_Precision_Robotic_Micromanipulation|SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation]]

![[assets/2610.15766_figure.png|800]]

- **arXiv**: [2610.15766](https://arxiv.org/abs/2610.15766)
- **PDF**: https://arxiv.org/pdf/2610.15766
- **详细分析**: [[20_Research/Papers/大模型/SurgiCLAW_An_Interpretable_Atomic-Skill_Agent_for_Precision_Robotic_Micromanipulation|SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation]]
- **作者**: Angen Ye, junjie xie, Yujia Song, Junkai Huang, Dapeng Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.3，大模型 0.5，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning. In surgical robotics, however, end-to-end prediction of low-level actions remains limited by insufficient precision, opaque decisions, and scarce data. This paper presents SurgiCLAW, a hierarchical skill-based framework for precision surgical manipulation. SurgiCLAW confines an MLLM to intraoperative visual understanding, structured explanation, and atomic surgical-skill selection, while delegating physical execution to verifiable deterministic control programs. For brain--machine-interface implantation, a representative high-precision surgical task, we construct a state-to-skill invocation dataset and expand it through visual and state perturbations. The model first learns structured skill invocation through supervised fine-tuning and is then optimized using three rewards for action correctness, operation prerequisites, and format validity, improving action selection, operational safety, and output parseability. We evaluate subtask success, offline model comparison, real-robot performance, and ablations. On a fixed test set, SurgiCLAW achieves 94.6% skill-selection accuracy and 93.0% macro-averaged F1 (Macro-F1). Across 50 closed-loop real-robot implantation trials, it achieves an 88.0% task success rate.

</details>

---

### [[20_Research/Papers/世界模型/LeHami_Symplectic_Latent_Dynamics_for_World_Models|LeHami: Symplectic Latent Dynamics for World Models]]

![[assets/2610.15267_figure.png|800]]

- **arXiv**: [2610.15267](https://arxiv.org/abs/2610.15267)
- **PDF**: https://arxiv.org/pdf/2610.15267
- **详细分析**: [[20_Research/Papers/世界模型/LeHami_Symplectic_Latent_Dynamics_for_World_Models|LeHami: Symplectic Latent Dynamics for World Models]]
- **作者**: Romina Yalovetzky, Randall Balestriero, Yann LeCun
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.92（加权：强化学习 0.16，世界模型 1.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

《LeHami: Symplectic Latent Dynamics for World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over long rollouts. We introduce Symplectic Hamiltonian JEPA (LeHami), which replaces the standard predictor with an action-conditioned Hamiltonian flow over a structured latent state (q, p) integrated using an exactly symplectic leapfrog step. This construction preserves phase-space volume at every rollout step and rules out uniform contraction, asymptotically stable fixed points, and merging of distinct latent states, independently of the learned parameters or action sequence. We obtain the momentum-like component from temporal derivatives of the learned position-like representation, providing an explicit second-order state for prediction and control. On conservative and actuated visual pendulum environments, LeHami substantially improves long-horizon velocity prediction over an unconstrained JEPA world model and empirically maintains constant latent volume where the baseline contracts. The learned flow also supports accurate integration at unseen sub-frame step sizes and numerical time reversal. These results show how geometric structure can provide inference-time guarantees that are complementary to representation regularization in latent world models.

</details>

---

### [[20_Research/Papers/强化学习/DexCast_Learning_Real-World_Dexterous_Control_from_Human_Videos|DexCast: Learning Real-World Dexterous Control from Human Videos]]

![[assets/2610.14691_figure.png|800]]

- **arXiv**: [2610.14691](https://arxiv.org/abs/2610.14691)
- **PDF**: https://arxiv.org/pdf/2610.14691
- **详细分析**: [[20_Research/Papers/强化学习/DexCast_Learning_Real-World_Dexterous_Control_from_Human_Videos|DexCast: Learning Real-World Dexterous Control from Human Videos]]
- **作者**: Zihan Gao, Yuhong Zhang, Mengzhe Wang, Kaisheng Liu, Shengpeng Li, Siyao Xiao, Runqing Cheng, Xiao Lin, Zhifang Liu, Haoqian Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexCast: Learning Real-World Dexterous Control from Human Videos》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet, Real-World, XL-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in 3D hand-object interaction (HOI) perception have opened new opportunities for learning dexterous robotic skills from human videos. However, existing dexterous imitation learning methods often rely on costly and manually teleoperated robot demonstrations, requiring substantial human effort. Therefore, we build DEXCAST, a framework that learns dexterous robotic hand control directly from monocular RGB-D videos by leveraging joint HOI reconstructions, without requiring any teleoperation. Furthermore, how to model high-dimensional robotic hand motion and extract temporal context to inform future action generation remains a key challenge. To this end, we propose a DexHand Motion Perception Module (DMPM) to capture inter-joint coordination and temporal dependencies in compact latent representations that condition our diffusion policy. Extensive real-world experiments demonstrate that DEXCAST achieves exceptional performance across diverse dexterous manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/Memory_Without_Curation_Learning_Multi-Stream_Latent_Memory_for_Robot_Policies|Memory Without Curation: Learning Multi-Stream Latent Memory for Robot Policies]]

![[assets/2610.14406_figure.png|800]]

- **arXiv**: [2610.14406](https://arxiv.org/abs/2610.14406)
- **PDF**: https://arxiv.org/pdf/2610.14406
- **详细分析**: [[20_Research/Papers/具身智能/Memory_Without_Curation_Learning_Multi-Stream_Latent_Memory_for_Robot_Policies|Memory Without Curation: Learning Multi-Stream Latent Memory for Robot Policies]]
- **作者**: Yilin Wu, Rutav Shah, Shuaiyi Huang, Sumedh A. Sontakke, Homanga Bharadhwaj, Andrea Bajcsy, Max Simchowitz, Guanya Shi
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Memory Without Curation: Learning Multi-Stream Latent Memory for Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RMBench, ReMemBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

It is widely appreciated that robotic policies require long-term memory to perform complex tasks. However, directly conditioning policies on all past observations leaves policy learning susceptible to learning spurious shortcuts, and introduces large latency at policy deployment. As such, today's memory-augmented policies curate what to remember, either by retaining only recent frames, selected keyframes, or textual summaries, or by learning latent representations of the visual stream alone. In this work, we propose an alternative approach IMPRINT, a policy-agnostic latent memory framework that augments vision-language-action (VLA) models with multi-stream memory without explicitly constraining what the policy should remember. IMPRINT compresses different streams into a latent memory that is updated incrementally at inference, enabling low latency. To avoid shortcut learning, IMPRINT adopts a two-stage training procedure, first supervising memory to reconstruct multiple streams (observations, actions, proprioception) of past information, as well as estimate current task progress, followed by end-to-end finetuning, jointly with the policy, on action prediction. Across both simulation and real-world tasks demanding memory, IMPRINT improves average success over the base VLA by at least 26%, outperforming popular alternatives, and maintaining lowest inference latency among memory-augmented VLAs. Through careful ablations, we demonstrate the utility of incorporating diverse information streams into robotic memory, validating the advantages of foregoing history curation. Project website: https://yilin-wu98.github.io/imprint_website/.

</details>

---

### [[20_Research/Papers/机器人/Akule_Fast_and_Scalable_Multi-Robot_Motion_Planning_via_Sparse_Interaction_Diffusion|Akule: Fast and Scalable Multi-Robot Motion Planning via Sparse Interaction Diffusion]]

![[assets/2610.14248_figure.png|800]]

- **arXiv**: [2610.14248](https://arxiv.org/abs/2610.14248)
- **PDF**: https://arxiv.org/pdf/2610.14248
- **详细分析**: [[20_Research/Papers/机器人/Akule_Fast_and_Scalable_Multi-Robot_Motion_Planning_via_Sparse_Interaction_Diffusion|Akule: Fast and Scalable Multi-Robot Motion Planning via Sparse Interaction Diffusion]]
- **作者**: Manav Vora, Gokul Puthumanaillam, Aditya Penumarti, Jane Shin, Melkior Ornik
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Akule: Fast and Scalable Multi-Robot Motion Planning via Sparse Interaction Diffusion》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion models provide expressive trajectory priors for multi-robot motion planning (MRMP), but scaling them to large teams requires coordinating individual motions without expensive joint computation. We introduce Akule, a sparse interaction diffusion framework that augments a frozen single-robot prior with three learned modules: a reusable pairwise correction model $R_φ$, a contextual selector $U_ψ$ that determines which corrections to evaluate, and a composer $G_ω$ that combines their effects through context-dependent signed weights. This decomposition separates which interactions merit computation from how their effects should be combined into coordinated denoising updates. We train $R_φ$ using matched pairwise trajectory optimizations, then learn $G_ω$ and $U_ψ$ from physically optimized joint trajectories without requiring a prescribed ground-truth interaction graph. The resulting joint proposals are passed to a downstream search-based planner for validation and repair. Across diverse MRMP benchmarks, Akule achieves competitive planning success, complete-planner speedups of up to $25\times$, zero-shot population transfer, and successful planning with up to $256$ robots. Ablations further demonstrate that learned selection and composition reduce pre-repair conflicts and downstream repair effort relative to heuristic selection and uniform summation.

</details>

---

### [[20_Research/Papers/强化学习/Visualizing_the_World_Model_in_an_Agent's_Value_Function|Visualizing the World Model in an Agent's Value Function]]

![[assets/2610.14186_figure.png|800]]

- **arXiv**: [2610.14186](https://arxiv.org/abs/2610.14186)
- **PDF**: https://arxiv.org/pdf/2610.14186
- **详细分析**: [[20_Research/Papers/强化学习/Visualizing_the_World_Model_in_an_Agent's_Value_Function|Visualizing the World Model in an Agent's Value Function]]
- **作者**: Shawheen Naderi, Fatemeh Akherati, Yubei Chen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 2.02（加权：大模型 0.5，强化学习 0.56，世界模型 0.96）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Visualizing the World Model in an Agent's Value Function》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Could model-free reinforcement learning algorithms actually be learning a model of the environment? In this work, we apply counterfactual interventions which hold everything about a state fixed, besides a targeted change, to explore if the value function of a Proximal Policy Optimization agent forms a world model of the Crafter environment. Despite only being trained to optimize reward, we discover that the value function learns concepts such as the rules governing when a diamond is collectible, water and food having an impact on health, heuristics regarding inventory, and more. Finally, we discuss the safety implications of our visualizations and some shortcomings of current reinforcement learning agents that will prevent us from building truly advanced machine intelligence.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Zero-Shot_Task_Planning_via_Hardware-Aware_LLM-VLM_Integration_for_Grounded_Robotic_Manipulation|Embodied Zero-Shot Task Planning via Hardware-Aware LLM-VLM Integration for Grounded Robotic Manipulation]]

![[assets/2610.14106_figure.png|800]]

- **arXiv**: [2610.14106](https://arxiv.org/abs/2610.14106)
- **PDF**: https://arxiv.org/pdf/2610.14106
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Zero-Shot_Task_Planning_via_Hardware-Aware_LLM-VLM_Integration_for_Grounded_Robotic_Manipulation|Embodied Zero-Shot Task Planning via Hardware-Aware LLM-VLM Integration for Grounded Robotic Manipulation]]
- **作者**: Lonnie Tankersley, Noorbakhsh Amiri Golilarz, Soroush Korivand
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.5（加权：具身智能 2.1，大模型 1.1，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Embodied Zero-Shot Task Planning via Hardware-Aware LLM-VLM Integration for Grounded Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can translate natural-language instructions into plausible manipulation plans, but robotic execution requires physically grounded decisions that respect robot embodiment, workspace geometry, reachability, collision constraints, and grasp feasibility. This paper presents a hardware-aware large language model-vision-language model (LLM-VLM) manipulation framework for a simulated Franka Research 3 robot in NVIDIA Isaac Sim. The framework separates symbolic reasoning from metric execution: an API-hosted LLM planner receives a structured scene summary and generates only symbolic task information, including the object to manipulate, target relation, approach preference, and objects to avoid. A local Qwen3-VL 8B VLM verifier supports semantic confirmation of ambiguous objects and open-container surrogates. Both the LLM planner and the VLM verifier are prohibited from generating robot coordinates, grasp poses, keepout dimensions, gripper commands, trajectory waypoints, or success labels. Instead, these decisions are handled by deterministic grounding and execution modules that use the robot model, scene geometry, MoveIt 2 collision checking, inverse kinematics, grasp validation, release verification, and final visual assessment. Execution feedback is returned only as symbolic context for replanning. The framework is evaluated through simulated digital-twin trials involving pickup, occluded-source access, keepout reasoning, relation placement, and sequential manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_from_Real-Robot_Interaction_without_High-Quality_State_Estimates|Reinforcement Learning from Real-Robot Interaction without High-Quality State Estimates]]

![[assets/2610.14042_figure.png|800]]

- **arXiv**: [2610.14042](https://arxiv.org/abs/2610.14042)
- **PDF**: https://arxiv.org/pdf/2610.14042
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_from_Real-Robot_Interaction_without_High-Quality_State_Estimates|Reinforcement Learning from Real-Robot Interaction without High-Quality State Estimates]]
- **作者**: Ryan Gao, Ashvin Anilkumar, Nicholas Corrado, William Cong, Josiah Hanna
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Reinforcement Learning from Real-Robot Interaction without High-Quality State Estimates》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DVRL, HIL-SERL, PlaNet, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A longstanding goal for robot reinforcement learning (RL) is that robots learn from their own physical experience, as humans and animals do. A key obstacle to learning directly from physical experience, especially outside instrumented lab environments, is that the state of the world is usually unobservable to the learner and must be estimated from on-board sensing. Errors in that estimate corrupt both the policy input and potentially the reward signal. We study this challenge using the contact-rich task of a bipedal robot learning to score soccer goals. We estimate all key state variables on-board with an unscented Kalman filter (UKF) and no external instrumentation (e.g., motion capture or overhead cameras). Because the UKF may incorrectly estimate state when the ball is unobserved, we learn a new state representation with a recurrent state-space model (RSSM) that, critically, only corrects the RSSM's latent state when the ball is observed. Building on RLPD, we introduce RSSM-RLPD and apply it to the task of a NAO robot learning to dribble a soccer ball into a goal. We show that the robot learns to score from multiple starting positions after 30 minutes of real-world interaction, reaching 100% success against 0% for a feed-forward policy under the same training budget. We complement our physical robot experiments with a simulation study and show that RSSM-RLPD learns policies that achieve a higher success rate than behavior cloning, a feed-forward, and GRU baseline. Taken together, our results show that the addition of a learned state representation to existing on-robot learning methods enables RL from real-robot data even with a high degree of partial observability.

</details>

---

### [[20_Research/Papers/具身智能/RoboHarness_A_Simple_Harness_Outperforms_VLA_and_World_Actions_Models|RoboHarness: A Simple Harness Outperforms VLA and World Actions Models]]

![[assets/2610.14018_figure.png|800]]

- **arXiv**: [2610.14018](https://arxiv.org/abs/2610.14018)
- **PDF**: https://arxiv.org/pdf/2610.14018
- **详细分析**: [[20_Research/Papers/具身智能/RoboHarness_A_Simple_Harness_Outperforms_VLA_and_World_Actions_Models|RoboHarness: A Simple Harness Outperforms VLA and World Actions Models]]
- **作者**: Bince Qu, Wei Chen, Bo Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.4，大模型 0.2，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《RoboHarness: A Simple Harness Outperforms VLA and World Actions Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HarnessVLA, OpenVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rise of large language models (LLMs) has opened a path toward generalist embodied AI, raising the question of how LLMs can act in the physical world. One straightforward approach is training the model to generate actions: collect robot-action data and video demonstration, refine LLM architecture with an action head, and train a vision-language-action (VLA) model at scale. However, we argue that coding agents have the potential to realize generalist embodied manipulation. All they need is a simple yet effective robot harness. We present RoboHarness: a robotic harness that gives LLM agents a visual-geometric control panel so that they can directly understand and invoke embodied tasks. With RoboHarness, Qwen3.8-Flash-Next outperforms state-of-the-art VLA models on BEHAVIOR Challenge 2025 tasks. The implementation will be released as open source.

</details>

---

### [[20_Research/Papers/大模型/VH-GPO_Verified_Handoff_for_LLM_Agent_Reinforcement_Learning|VH-GPO: Verified Handoff for LLM Agent Reinforcement Learning]]

![[assets/2610.14000_figure.png|800]]

- **arXiv**: [2610.14000](https://arxiv.org/abs/2610.14000)
- **PDF**: https://arxiv.org/pdf/2610.14000
- **详细分析**: [[20_Research/Papers/大模型/VH-GPO_Verified_Handoff_for_LLM_Agent_Reinforcement_Learning|VH-GPO: Verified Handoff for LLM Agent Reinforcement Learning]]
- **作者**: Haoze Li, Peng Zhou, Peiyuan Wu, Weijie Zhao, Yinan Xin
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.32（加权：大模型 1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《VH-GPO: Verified Handoff for LLM Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ActGuide-RL, AgentGym, AgentGym-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group-relative reinforcement learning methods such as GRPO train large language model (LLM) agents by comparing rollouts for the same task. When every trajectory in a group fails with the same reward, relative advantages collapse toward zero, leaving no useful learning signal. A frozen teacher can recover from a student-visited state, but letting it complete the task makes the recovered suffix entirely teacher-generated. We ask: after repairing a student failure, when should control return to the student? We propose outcome-verified teacher-student handoff, instantiated in Verified Handoff for Group Policy Optimization (VH-GPO). The teacher provides enough support to reach a state from which the student can succeed, then returns control so that successful experience is again student-generated. Given an environment-verified teacher recovery, VH-GPO selects the earliest independently confirmed handoff point found within a bounded search budget. With Qwen2.5-1.5B, VH-GPO increases success rates over GRPO from 59.38% to 94.79% on ALFWorld and from 71.62% to 77.34% on WebShop. Improvements also hold with the 7B student, for which additional teacher and student output tokens amount to 1.77% and 2.61% of regular student rollout output tokens on ALFWorld and WebShop, respectively. Ablation studies demonstrate the effectiveness of the key components. These results support using verified teacher assistance to repair failures while reinforcing the student's ability to complete tasks independently.

</details>

---
