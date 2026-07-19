# cs.HC | Human-Computer Interaction | 2026-07-17

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Catch,_Throw,_Repeat_Planning_for_Human-Robot_Partner_Juggling|Catch, Throw, Repeat: Planning for Human-Robot Partner Juggling]]

![[assets/2607.15129_figure.png|800]]

- **arXiv**: [2607.15129](https://arxiv.org/abs/2607.15129)
- **PDF**: https://arxiv.org/pdf/2607.15129
- **详细分析**: [[20_Research/Papers/机器人/Catch,_Throw,_Repeat_Planning_for_Human-Robot_Partner_Juggling|Catch, Throw, Repeat: Planning for Human-Robot Partner Juggling]]
- **作者**: Jonathan Rainer Lippert, Kai Ploeger, Abir Chowdhury, Hermann Müller, Jan Peters, Alap Kshirsagar
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Catch, Throw, Repeat: Planning for Human-Robot Partner Juggling》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic object exchange between humans and robots remains a challenging problem due to uncertainty in perception, timing, and contact-rich interaction. Human-robot juggling represents a particularly demanding instance of this problem, requiring precise real-time coordination, predictive motion planning with feedback control, and robustness to variability in human motion. Enabling such skills is of interest for advancing physical human-robot interaction and shared autonomy. We present a real-time planning and control architecture for human-robot partner juggling that enables a robot to reliably catch and throw balls in synchronized multi-ball patterns with a human partner. The system integrates predictive ball tracking, adaptive online trajectory optimization using a multiple-shooting formulation, and a state-machine-based coordination logic to enable synchronized multi-ball human-robot partner juggling. In a user study with 8 participants of varying juggling skill from beginner to expert, we demonstrate that our system can achieve three-ball cascades shared between the robot and the human. All participants exceeded previously reported best-case results within a 10-minute test session, with one participant extending the previous record for shared three-ball cascade juggling fivefold to 20 consecutive robot catches, and another participant achieving a 100% success rate with 40 consecutive catches in a single-ball catch-and-return setting. Video documentation can be found at https://kai-ploeger.com/partner-juggling

</details>

---
