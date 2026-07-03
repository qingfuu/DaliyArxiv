# cs.SE | Software Engineering | 2026-07-01

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Failure-Based_Testing_for_Deep_Reinforcement_Learning_Agents|Failure-Based Testing for Deep Reinforcement Learning Agents]]

![[assets/2606.31372_figure.png|800]]

- **arXiv**: [2606.31372](https://arxiv.org/abs/2606.31372)
- **PDF**: https://arxiv.org/pdf/2606.31372
- **详细分析**: [[20_Research/Papers/强化学习/Failure-Based_Testing_for_Deep_Reinforcement_Learning_Agents|Failure-Based Testing for Deep Reinforcement Learning Agents]]
- **作者**: Weibin Lin, Jiangtao Meng, Zheng Zheng
- **cs 子类**: cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人
- **相关性评分**: 2.3（加权：大模型 0.5，强化学习 1.6，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Failure-Based Testing for Deep Reinforcement Learning Agents》归入 强化学习、大模型、机器人 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep Reinforcement Learning (DRL) agents have been widely adopted across diverse domains to address challenging decision-making problems, such as autonomous driving and robotic control. Given that many of these applications are safety- and security-critical, rigorous testing of DRL agents is indispensable. Existing testing methods are typically guided by reward signals to detect failures. However, for well-trained agents, whose performance approaches optimal levels in standard operating conditions, reward signals remain generally high, making current methods ineffective at uncovering critical failures. To address these challenges, we propose a novel failure-based method that leverages task-induced failure insights to enhance failure detection capability while reducing the number of tests required. Since DRL agents are inherently designed with human-defined tasks, they provide valuable cues about task difficulty. Intuitively, a DRL agent is more likely to fail when confronted with a more difficult task; therefore, PRT prioritizes these tasks. Building on this foundation, we propose Prior Random Testing, a black-box failure-based testing method that enables targeted prioritization while preserving the diversity of generated test cases. Guided by task-induced failure insights, PRT prioritizes failure-prone regions of the input domain, thereby facilitating efficient failure detection. PRT is evaluated on four widely used benchmarks and compared with different state-of-the-art methods including fuzzing, search-based and generative-based methods. PRT ranks among the top performers in terms of both the cost of finding the first failure and the diversity of test cases. Notably, compared to random testing, PRT achieves better diversity and reduces the testing cost by over 50%.

</details>

---
