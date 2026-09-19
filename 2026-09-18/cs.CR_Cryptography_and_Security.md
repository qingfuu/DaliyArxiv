# cs.CR | Cryptography and Security | 2026-09-18

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Your_Robot_Was_Trained_on_a_Lie_Collision_Mesh_Poisoning_Attacks_on_Robotic_Manipulation|"Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation]]

![[assets/2609.18122_figure.png|800]]

- **arXiv**: [2609.18122](https://arxiv.org/abs/2609.18122)
- **PDF**: https://arxiv.org/pdf/2609.18122
- **详细分析**: [[20_Research/Papers/具身智能/Your_Robot_Was_Trained_on_a_Lie_Collision_Mesh_Poisoning_Attacks_on_Robotic_Manipulation|"Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation]]
- **作者**: Gengyang Xu, Dongwei Xiao, Yiteng Peng, Yanbo Dai, Ruochen Zhou, Shing-Chi Cheung, Xiaoyu Ji, Wenyuan Xu, Shuai Wang
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 1.5，机器人 1.9）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《"Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation》归入 机器人、具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Poisoned-Sim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-enabled robotic manipulation increasingly relies on robot simulators for policy training and evaluation before real-world deployment. Inside a simulator, a 3D asset contains two separate geometries: a visual mesh used for rendering and a collision mesh used for physical interaction. For computational efficiency, the collision mesh is deliberately a coarse approximation that need not have the same geometry as the visual mesh, a legitimate and pervasive discrepancy we call the Visual--Collision Gap (V--C Gap). We show that the V--C Gap opens a new and practical attack surface, and propose Collision Mesh Poisoning (CMP), the first poisoning attack against robotic manipulation delivered through the 3D asset supply chain. An attacker modifies only the collision mesh of a 3D asset, leaving the visual mesh and all other components unchanged. A policy trained and evaluated with the poisoned asset behaves normally throughout simulation, yet degrades, fails, or creates physical safety risks once deployed in the real world. Since current asset review practices cover malware, copyright, and format compliance, but not visual--collision consistency, poisoned assets can be distributed through legitimate supply chain channels. We evaluate several defenses and our results show that they are insufficient to defend against CMP, highlighting the need for new defenses.

</details>

---
