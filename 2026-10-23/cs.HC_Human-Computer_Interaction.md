# cs.HC | Human-Computer Interaction | 2026-10-23

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/CARL_Chat_Assisted_Reinforcement_Learning|CARL: Chat Assisted Reinforcement Learning]]

![[assets/2610.31014_figure.png|800]]

- **arXiv**: [2610.31014](https://arxiv.org/abs/2610.31014)
- **PDF**: https://arxiv.org/pdf/2610.31014
- **详细分析**: [[20_Research/Papers/强化学习/CARL_Chat_Assisted_Reinforcement_Learning|CARL: Chat Assisted Reinforcement Learning]]
- **作者**: Sanjiv Das, Harshad Khadilkar, Sukrit Mittal, Daniel Ostrov, Jacob Sisk
- **cs 子类**: cs.HC
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《CARL: Chat Assisted Reinforcement Learning》归入 强化学习 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Failure of applied Reinforcement Learning (RL) to solve a given problem predominantly stems from unaddressed specification gaps, where the intent of human experts in the problem's domain is inaccurately or incompletely translated by AI into mathematical objectives, constraints, and reward functions. Failure can also stem from unaddressed performance gaps, where human domain experts are unable to determine the validity of the RL based solution or where parameters (i.e., hyperparameters or weights on the reward terms comprising the reward) are poorly chosen. Chat Assisted Reinforcement Learning (CARL) bridges these gaps through a human-AI co-design interface architecture that enforces interactive specification prior to code generation and then enables subsequent verification and parameter alterations via iteration. More specifically, CARL leads domain experts through a structured ten-step workflow for each iteration using step-specific skill files, domain-aware suggestions via an assistant persona (called Trillian), and compact decision summaries that maintain context across iterations without context overload. Once the domain expert confirms the Markov decision process (MDP) specified by this procedure, CARL's autonomous tool-use loop generates, tests, executes, and debugs an end-to-end RL training pipeline, followed by an interactive post-training diagnosis and revisit step that allows for verification and parameter alteration before running a new iteration if desired.

</details>

---

### [[20_Research/Papers/具身智能/PATH_Preference-Aware_Traversability_Estimation_for_Robotic_Teleoperation_in_Off-Road_Navigation|PATH: Preference-Aware Traversability Estimation for Robotic Teleoperation in Off-Road Navigation]]

![[assets/2610.30605_figure.png|800]]

- **arXiv**: [2610.30605](https://arxiv.org/abs/2610.30605)
- **PDF**: https://arxiv.org/pdf/2610.30605
- **详细分析**: [[20_Research/Papers/具身智能/PATH_Preference-Aware_Traversability_Estimation_for_Robotic_Teleoperation_in_Off-Road_Navigation|PATH: Preference-Aware Traversability Estimation for Robotic Teleoperation in Off-Road Navigation]]
- **作者**: Xianghao Meng, Wenshuo Wang, Cheng Shao, Lewei Feng, Qingxiao Liu, Canyu Wang, Junqiang Xi
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.4（加权：具身智能 0.3，强化学习 0.2，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PATH: Preference-Aware Traversability Estimation for Robotic Teleoperation in Off-Road Navigation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRL, PATH-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traversability estimation is critical for ground vehicle teleoperation, yet existing methods often neglect the human operator's preferences for speed and risk tolerance. To address this gap, we propose PATH-Net, a Preference-Aware Traversability estimation Hierarchical Network that adaptively generates preference-conditioned traversability cost maps and speed profiles for off-road teleoperation. Our framework integrates visual and geometric bird's-eye-view features with short-term historical vehicle states through a multi-head shared-backbone architecture. Our PATH-Net infers traversability cost maps while optimizing speed recommendations by using maximum entropy inverse reinforcement learning and sparse speed supervision. Our method incorporates operator preference via an asymmetric feature aggregation mechanism, splitting inference into a cost branch that prioritizes high-risk traversability regions and a speed branch that outputs preference-adjusted recommended speeds. Experiments with 15 operators across 225 teleoperated trajectories show alignment with user-specific navigation strategies, achieving modified Hausdorff distance of 0.17 m (aggressive) and 0.15 m (conservative). In the questionnaire assessment, participants reported lower NASA-TLX workload scores with PATH-Net recommendations than without recommendations, decreasing from 34.7 to 22.2. These results support preference-conditioned trajectory and speed recommendation for off-road teleoperation.

</details>

---
