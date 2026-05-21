# cs.OH | cs.OH | 2026-05-20

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Safe_Deep_Reinforcement_Learning_for_Spacecraft_Reorientation_with_Pointing_Keep-Out_Constraint|Safe Deep Reinforcement Learning for Spacecraft Reorientation with Pointing Keep-Out Constraint]]

![[assets/2605.19967_figure.png|800]]

- **arXiv**: [2605.19967](https://arxiv.org/abs/2605.19967)
- **PDF**: https://arxiv.org/pdf/2605.19967
- **详细分析**: [[20_Research/Papers/强化学习/Safe_Deep_Reinforcement_Learning_for_Spacecraft_Reorientation_with_Pointing_Keep-Out_Constraint|Safe Deep Reinforcement Learning for Spacecraft Reorientation with Pointing Keep-Out Constraint]]
- **作者**: Juntang Yang, Mohamed Khalil Ben-Larbi
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.1，强化学习 1.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

航天器重定向机动常常需要满足指向禁入区约束，例如望远镜或敏感载荷不能对准太阳等强光源，否则可能造成设备损伤或任务失败。传统的约束姿态规划和非线性MPC虽然能处理约束，但计算开销较大，不利于在轨实时应用；人工势场方法又容易陷入局部最优。本文关注的是如何把深度强化学习用于连续姿态控制，同时真正保证机动过程中的安全性，因此具有较强的工程价值。

#### 方法概述和架构

论文采用面向连续状态与连续动作空间的 soft actor-critic（SAC）算法来学习航天器重定向策略，动作输出为机体系控制力矩。作者设计了一套新的状态表示，把姿态误差、角速度、载荷视轴、与禁入区相关的角度裕度、相对避让方向以及上一时刻的四元数标量分量一起作为观测输入，使智能体能够显式感知约束几何信息。奖励函数同时兼顾到达目标姿态、减小力矩、抑制控制突变，并对进入禁入区施加惩罚；训练阶段还使用 curriculum learning 逐步增加任务难度，以提升收敛稳定性。部署阶段则引入基于 control barrier function（CBF）的安全滤波器，对 SAC 输出的力矩进行在线检查与修正：若原动作安全则直接执行，否则替换为安全控制输入，从而把学习策略和安全保证解耦。

#### 实验结果分析

仿真结果表明，作者提出的状态空间表示和奖励设计是有效的，能够支持策略学习完成重定向任务。Monte Carlo 仿真进一步说明，仅靠 reward shaping 不能保证机动过程始终满足约束，仍可能出现安全违规。相比之下，加入 CBF-based safety filter 后，可以在机动全过程中保证禁入区约束得到满足。可见文本未给出具体数值，但结论清楚支持了“学习负责性能、滤波器负责安全”的组合思路。

<details>
<summary>完整摘要</summary>

本文针对具有单一指向禁入区约束的航天器重定向控制，构建了带安全滤波器的深度强化学习（DRL）方法。我们设计了一种新的状态空间表示，其中包含对姿态约束区域的紧凑表征；同时构造奖励函数，以在满足姿态约束的前提下实现控制目标。为处理连续状态空间和动作空间，采用 soft actor-critic（SAC）算法，并引入 curriculum learning 策略进行智能体训练。为保证姿态约束在部署阶段始终被满足，进一步实现了基于 control barrier function（CBF）的安全滤波器，用于智能体上线时的控制输出修正。仿真结果表明，所提出的状态空间表示和奖励函数设计是有效的；Monte Carlo 仿真强调，仅靠奖励塑形无法保证重定向机动过程中的安全性。相比之下，加入基于 CBF 的安全滤波器后，约束可以在机动过程中得到保证。

</details>

---

### [[20_Research/Papers/大模型/UAV-Assisted_Cooperative_Edge_Inference_for_Low-Altitude_Economy_via_MoE-based_Hierarchical_Deep_Reinforcement_Learning|UAV-Assisted Cooperative Edge Inference for Low-Altitude Economy via MoE-based Hierarchical Deep Reinforcement Learning]]

![[assets/2605.19290_figure.png|800]]

- **arXiv**: [2605.19290](https://arxiv.org/abs/2605.19290)
- **PDF**: https://arxiv.org/pdf/2605.19290
- **详细分析**: [[20_Research/Papers/大模型/UAV-Assisted_Cooperative_Edge_Inference_for_Low-Altitude_Economy_via_MoE-based_Hierarchical_Deep_Reinforcement_Learning|UAV-Assisted Cooperative Edge Inference for Low-Altitude Economy via MoE-based Hierarchical Deep Reinforcement Learning]]
- **作者**: Wenhao Zhuang, Yuyi Mao, Ivan Wang-Hei Ho, Xianghao Yu
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人
- **相关性评分**: 2.6（加权：强化学习 1.8，机器人 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

低空经济正在通过无人机支撑巡检、配送、农业等任务，但无人机在执行主任务时仍希望同时为地面设备提供边缘智能推理服务，这就带来了“飞行任务”和“AI推理”之间的强耦合约束。由于地面设备算力和能量有限，直接上传原始数据到无人机往往受制于无线链路吞吐瓶颈，因此更现实的方案是进行协同推理：设备本地先提取中间特征，再将其卸载到无人机完成后续推理。然而，在低空经济场景下，无人机轨迹必须尽量遵循预设航线以满足任务要求，同时还要兼顾通信质量和多设备推理调度，这使得联合优化问题具有明显的多时隙、多目标和部分可观测特征，值得关注。

#### 方法概述和架构

论文提出 UAV-assisted cooperative edge inference 框架，将无人机的航迹偏离参考路径作为其主任务约束，并把地面设备的推理任务拆分为“本地特征提取 + 中间特征卸载 + 无人机侧推理”两段式流程。作者把联合优化目标建模为一个带约束的 POMDP：状态包含无人机位置、信道条件以及可观测到的任务难度信息，动作同时包括无人机轨迹控制、任务卸载决策和特征压缩率选择。为解决轨迹控制与推理资源分配的时间尺度差异，提出 HDRL-MoE 的分层深度强化学习框架：上层负责慢变化的推理决策，下层负责快速变化的无人机轨迹调整，并通过统一的 critic 进行跨时间尺度评估。与此同时，MoE（mixture-of-experts）结构被用于离散卸载决策与连续压缩率优化的解耦：router network 负责协调不同设备的卸载选择，expert networks 则分别优化各自的特征压缩比例。整体训练过程中，智能体根据环境交互采集经验并更新策略网络，推理阶段则直接输出轨迹、卸载和压缩策略，实现在线决策。

#### 实验结果分析

作者在仿真中系统评估了所提 HDRL-MoE，并与多种基线方法比较，指标主要围绕推理准确率、成功卸载比例、轨迹偏离约束满足情况以及训练效率展开。结果显示，该方法在保证无人机轨迹偏离不超过低空经济任务阈值的前提下，能够取得更高的推理准确率；文中还指出成功卸载比例最高可提升 2.96%。此外，MoE 设计带来了更好的可扩展性：当地面设备数量增加时，算法仍能保持较好的性能，并且收敛所需训练轮次更少。正文还提到对非 IID 数据分布和多设备场景做了分析，可见文本未给出具体数值。

<details>
<summary>完整摘要</summary>

低空经济（LAE）正通过部署无人机推动产业格局重塑，以支持一系列需要灵活空中机动能力的应用。将边缘人工智能（AI）集成到低空经济平台中，形成了一种很有吸引力的新范式：无人机在执行其主要空中任务的同时，提供实时的 AI 分析。然而，由于这些主任务带来的严格使命约束以及无线链路吞吐瓶颈，要真正实现这一范式仍然面临挑战。为弥补这一缺口，我们提出一种无人机辅助的协同边缘推理框架：无人机在执行低空经济中的关键任务时，以相对参考路径的轨迹偏离来量化其任务执行情况，同时通过中间特征卸载为地面设备提供支持。在该框架下，联合优化无人机轨迹、推理任务卸载决策以及特征压缩比，以最大化系统性能。我们将这一联合优化问题建模为一个带约束的部分可观测马尔可夫决策过程（POMDP）。为高效求解该问题，我们提出 HDRL-MoE，这是一种新颖的分层深度强化学习框架，用于将变化较慢的推理决策与快速变化的无人机轨迹控制解耦。此外，HDRL-MoE 还集成了 mixture-of-experts（MoE）架构，其中路由网络负责协调离散的卸载决策，而专家网络则分别独立优化特征压缩比。大量仿真结果表明，HDRL-MoE 相比基线方法能显著提高推理准确率，并且借助其 MoE 设计展现出良好的可扩展性和效率。

</details>

---
