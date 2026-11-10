# cs.NI | Networking and Internet Architecture | 2026-11-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/5G-NetBotSim_A_Synchronized_Co-Simulation_Framework_for_Connected_Robots_over_ROS_and_srsRAN-based_5G_Network|5G-NetBotSim: A Synchronized Co-Simulation Framework for Connected Robots over ROS and srsRAN-based 5G Network]]

![[assets/2611.09735_figure.png|800]]

- **arXiv**: [2611.09735](https://arxiv.org/abs/2611.09735)
- **PDF**: https://arxiv.org/pdf/2611.09735
- **详细分析**: [[20_Research/Papers/机器人/5G-NetBotSim_A_Synchronized_Co-Simulation_Framework_for_Connected_Robots_over_ROS_and_srsRAN-based_5G_Network|5G-NetBotSim: A Synchronized Co-Simulation Framework for Connected Robots over ROS and srsRAN-based 5G Network]]
- **作者**: Narges Golmohammadi, Bhaskara Venkata Raju Garuda, Ayan Joshi, Sabur Baidya
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.2（加权：机器人 1.2）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《5G-NetBotSim: A Synchronized Co-Simulation Framework for Connected Robots over ROS and srsRAN-based 5G Network》归入 机器人 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BotSim, EdgeSim, NetBotSim, NetSim, SynchroSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Connected robotic applications increasingly rely on wireless communication for teleoperation, coordination, and distributed autonomy. However, robotic simulators often use ideal links or abstract delay models that do not capture cellular scheduling and protocol processing effects. We present 5G NetBotSim, a realtime co simulation framework integrating ROS/Gazebo workloads with an executable, full stack srsRAN 5G network emulator. The framework provides isolated User Equipment (UE) robot contexts and stage level timing across the host, gNB, UE, ROS, and robot execution stages. We evaluate human to robot teleoperation and robot to robot leader follower coordination under controlled channel quality conditions. Results show how CQI and MCS variations propagate to throughput, communication latency, and robot performance. In leader follower coordination, higher channel quality reduces mean tracking error from 0.558 m to 0.460 m, a 17.6% reduction. These results demonstrate protocol stack in the loop co simulation for joint network and robotic-application evaluation.

</details>

---
