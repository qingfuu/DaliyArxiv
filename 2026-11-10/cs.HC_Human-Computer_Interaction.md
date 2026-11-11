# cs.HC | Human-Computer Interaction | 2026-11-10

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/ROS2MR_Connecting_ROS_2_Motion_Planning_to_Mixed-Reality_Trajectory_Visualization|ROS2MR: Connecting ROS 2 Motion Planning to Mixed-Reality Trajectory Visualization]]

![[assets/2611.11830_figure.png|800]]

- **arXiv**: [2611.11830](https://arxiv.org/abs/2611.11830)
- **PDF**: https://arxiv.org/pdf/2611.11830
- **详细分析**: [[20_Research/Papers/机器人/ROS2MR_Connecting_ROS_2_Motion_Planning_to_Mixed-Reality_Trajectory_Visualization|ROS2MR: Connecting ROS 2 Motion Planning to Mixed-Reality Trajectory Visualization]]
- **作者**: Santiago Berrezueta-Guzman, Habiba-Loai Khalil, Andrei Koshelev, Stefan Wagner
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，机器人 2.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《ROS2MR: Connecting ROS 2 Motion Planning to Mixed-Reality Trajectory Visualization》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Human-Computer Interaction 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mixed reality (MR) allows users to inspect planned robot motion within their physical surroundings, but displaying trajectories from robotics software requires converting their joint configurations and timing into a format the MR application can play back. This paper presents ROS2MR, an extension of the MR-Robotics LAB platform that converts YAML-serialized ROS 2 joint trajectories, including MoveIt motion plans, into the platform's existing JSON playback format. The converter validates the input, maps arm joints by name, and resamples the trajectory at a nominal rate of 30 Hz, using cubic Hermite interpolation when joint velocities are supplied and linear interpolation otherwise, while binary gripper commands are sampled separately using a zero-order hold. A Python export helper combines sequences of motion plans and gripper states into a single trajectory and checks positional agreement at segment boundaries. The MR application was also adapted for Apple Vision Pro in addition to Meta Quest 3. A technical evaluation showed that the converter preserved the normalized duration and endpoint configurations for dense, sparse, and irregularly timed inputs. With supplied velocities, the position RMSE was approximately 2.91x10^-5 degrees for all sampling patterns; without them, sparse input increased it to 0.85 degrees, and close positional agreement did not guarantee accurate velocity profiles. A pick-and-place sequence retained its open--closed--open gripper order, although off-grid transitions were shifted to the output sampling grid. The resulting file-based pathway enables inspection of ROS-generated trajectories in MR without a live ROS connection.

</details>

---

### [[20_Research/Papers/大模型/Building_Rapport_with_Self-Disclosure_in_Human-Robot_Interaction|Building Rapport with Self-Disclosure in Human-Robot Interaction]]

![[assets/2611.09905_figure.png|800]]

- **arXiv**: [2611.09905](https://arxiv.org/abs/2611.09905)
- **PDF**: https://arxiv.org/pdf/2611.09905
- **详细分析**: [[20_Research/Papers/大模型/Building_Rapport_with_Self-Disclosure_in_Human-Robot_Interaction|Building Rapport with Self-Disclosure in Human-Robot Interaction]]
- **作者**: Haritha Anupindi, Chayan Sarkar, Tapas Nayak, Marynel Vazquez
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Building Rapport with Self-Disclosure in Human-Robot Interaction》归入 机器人、具身智能、大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LLM-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As social robots become increasingly present in everyday environments, establishing rapport with users is critical for enabling sustained and meaningful human-robot interaction. In human-human communication, self-disclosure is a well-established mechanism for building rapport; however, its role and impact in human-robot interaction (HRI) are not yet well understood. Although recent advances in large language models (LLMs) have improved the linguistic competence of conversational robots, such systems are typically deployed as reactive information providers, offering limited social reciprocity and relational depth. In this article, we investigate the role of robot self-disclosure in fostering rapport during face-to-face human-robot interaction. We propose a dialogue system, called RADIA that leverages retrieval-augmented generation (RAG) to enable a robot to retrieve and reference simulated autobiographical memories, allowing first-person self-disclosure to be incorporated naturally into ongoing conversations. We evaluate the proposed approach through an in-person user study, comparing interactions with a self-disclosing robot against a baseline non-self-disclosing robot. Our results show that robot self-disclosure significantly influences conversational dynamics and enhances users' perceived rapport with the robot, suggesting that self-disclosure is a valuable social behavior for long-term and socially engaging human-robot interaction.

</details>

---
