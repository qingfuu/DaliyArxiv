# cs.CR | Cryptography and Security | 2026-11-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/FlipVLA_Backdoor_Attacks_on_Vision-Language-Action(VLA)_Models_Only_Through_Bit_Flips|FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips]]

![[assets/2611.33810_figure.png|800]]

- **arXiv**: [2611.33810](https://arxiv.org/abs/2611.33810)
- **PDF**: https://arxiv.org/pdf/2611.33810
- **详细分析**: [[20_Research/Papers/具身智能/FlipVLA_Backdoor_Attacks_on_Vision-Language-Action(VLA)_Models_Only_Through_Bit_Flips|FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips]]
- **作者**: Zexi Zhao, Zizhen Liu, Jing Justin Ye, Huawei Li
- **cs 子类**: cs.CR, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.4，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《FlipVLA: Backdoor Attacks on Vision-Language-Action(VLA) Models Only Through Bit Flips》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FlipVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models generate robot actions from visual observations and language instructions in real-world environments, making malicious model tampering a potential threat to physical safety. We study whether object-triggered backdoors can be implanted through a small, fixed set of parameter bit flips without retraining. The central challenge is to make persistent weight modifications disrupt trigger-present behavior while preserving performance on non-trigger inputs. We propose FlipVLA, a two-stage selector-amplifier method that exploits existing visual features within an FC-GELU-FC structure. The selector constructs a trigger-dependent response in a selected channel, using GELU to attenuate background activity. The amplifier modifies a connected downstream weight to convert this response into an action-relevant perturbation. Channel screening and discrete bit search construct both components under a limited modification budget. Experiments on OpenVLA-OFT and GR00T N1.7 across four LIBERO suites achieve attack success rates of 90.22% to 100%, with task success decreasing by at most 1.5 percentage points on clean scenes.

</details>

---
