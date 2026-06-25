# cs.SE | Software Engineering | 2026-06-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/WebCQ_Cooperative_Multi-Agent_Deep_Reinforcement_Learning_for_Scalable_Web_GUI_Testing|WebCQ: Cooperative Multi-Agent Deep Reinforcement Learning for Scalable Web GUI Testing]]

![[assets/2606.22502_figure.png|800]]

- **arXiv**: [2606.22502](https://arxiv.org/abs/2606.22502)
- **PDF**: https://arxiv.org/pdf/2606.22502
- **详细分析**: [[20_Research/Papers/强化学习/WebCQ_Cooperative_Multi-Agent_Deep_Reinforcement_Learning_for_Scalable_Web_GUI_Testing|WebCQ: Cooperative Multi-Agent Deep Reinforcement Learning for Scalable Web GUI Testing]]
- **作者**: Yujia Fan, Sinan Wang, Zebang Fei, Yao Qin, Huaxuan Li, Yepang Liu
- **cs 子类**: cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.5，强化学习 1.4）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《WebCQ: Cooperative Multi-Agent Deep Reinforcement Learning for Scalable Web GUI Testing》归入 强化学习、大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reinforcement learning (MARL)-based techniques have shown promise for GUI testing. However, as the complexity of modern GUI software increases, existing MARL-based approaches (e.g., MARG and Fastbot) struggle to scale due to the inherent limitations of their underlying tabular reinforcement learning algorithms. This limits their applicability to large-scale commercial GUI software, especially web applications with vast state spaces and many interactive elements. To fill this gap, we propose WebCQ, a novel MARL-based approach for scalable web GUI testing. WebCQ incorporates QTRAN for multi-agent coordination and a lightweight synchronization mechanism, allowing it to work under asynchronous web testing scenarios. It extracts semantic and exploration features for each UI event to form an action vector. This vector is concatenated with the current state vector and fed into the policy network, enabling DQN-based decision making within a dynamic action space. We evaluated WebCQ on eight large-scale commercial websites. Under the same time budget and agent count, WebCQ explored 33.3% more states and executed 42.2% more unique actions than MARG, while triggering more failures on six of the eight websites under test. It also demonstrated strong scalability, maintaining higher action throughput during 20-hour experiments, and achieving greater performance improvements as the number of agents increased. These results show that WebCQovercomes key limitations of existing MARL-based approaches, providing a scalable and effective solution for enhancing modern web GUI testing.

</details>

---
