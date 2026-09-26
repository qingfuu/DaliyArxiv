# cs.GR | Graphics | 2026-09-25

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/TAPESIM_Efficient_Simulation_of_Adhesive_Tape_Dispensing_for_Robotic_Manipulation|TAPESIM: Efficient Simulation of Adhesive Tape Dispensing for Robotic Manipulation]]

![[assets/2609.28766_figure.png|800]]

- **arXiv**: [2609.28766](https://arxiv.org/abs/2609.28766)
- **PDF**: https://arxiv.org/pdf/2609.28766
- **详细分析**: [[20_Research/Papers/具身智能/TAPESIM_Efficient_Simulation_of_Adhesive_Tape_Dispensing_for_Robotic_Manipulation|TAPESIM: Efficient Simulation of Adhesive Tape Dispensing for Robotic Manipulation]]
- **作者**: Zhaofeng Luo, Xinyu Lu, jaehoon Choi, Zhehuan Chen, Trinity Chung, Xiaowen Qiu, Hugh Nicholas Perkins, Gianna Calderon, Alexis Duburcq, Sanghyun Son, Tsun-Hsuan Wang, Yi-Ling Qiao...
- **cs 子类**: cs.GR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《TAPESIM: Efficient Simulation of Adhesive Tape Dispensing for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：TapeSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Applying adhesive tape to secure wire harnesses or seal packages requires robots to coordinate a flexible strip, a moving roll, and surfaces that attach and detach. Simulation could make these interactions repeatable for robot development and evaluation, but resolving every adhesive layer is expensive and can suppress roll motion at practical solver tolerances, while a permanently rigid roll cannot release material. We present TapeSim, a tape simulator that concentrates deformation near the unwinding region and along the released strip. We will release the source code. A rigid cluster represents most wound material, while an advancing deformable collar enables payout and leaves released tape flexible and reattachable. Optional releasable bonds simplify adhesive interfaces and reduce mean step times for smaller rolls. Controlled swing tests show improved roll rotation. At 32 turns, clustering gives 3.2-3.4x mean physics-step speedups at a fixed Newton tolerance and 4.5-8.4x for comparable roll motion. Across five real-motion Stick replays, the clustered variants reduce mean image-plane core-landmark error by 23-29% relative to the full-shell cohesive baseline. On 100 paired Peel cases, they improve balanced accuracy from 50% to 72.9-76.3%, with interface rankings varying across tasks. A teleoperated box-sealing sequence demonstrates attachment, dispensing, cutting, and sealing in a continuous workflow.

</details>

---
