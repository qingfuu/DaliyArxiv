# cs.IR | Information Retrieval | 2026-11-18

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/More_Than_a_Score_Reinforcement_Learning_with_Verbalized_Feedback_for_Generative_Recommendation|More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation]]

![[assets/2611.22410_figure.png|800]]

- **arXiv**: [2611.22410](https://arxiv.org/abs/2611.22410)
- **PDF**: https://arxiv.org/pdf/2611.22410
- **详细分析**: [[20_Research/Papers/强化学习/More_Than_a_Score_Reinforcement_Learning_with_Verbalized_Feedback_for_Generative_Recommendation|More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation]]
- **作者**: Zipeng Chen, Xinyu Lin, Yuliang Sun, Sheng Zhang, Zeyu Wang, Xiaowen Shi, Junwei Pan, Chengguo Yin
- **cs 子类**: cs.IR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《More Than a Score: Reinforcement Learning with Verbalized Feedback for Generative Recommendation》归入 强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly used for generative recommendation, where recommended items are generated directly from users' interaction histories. To further improve recommendation quality, reinforcement learning (RL) has been applied to align these models with recommendation objectives. However, existing RL methods rely on scalar rewards to implicitly guide exploration. These rewards do not specify which aspects of a candidate conflict with the user's preferences or how the next candidate should differ. To address this gap, we propose VerRec, a verbalized feedback-guided RL framework for generative recommendation. Specifically, a user simulator generates personalized verbalized feedback based on the user's historical preferences and the candidate item profile. The policy uses this feedback to produce refined recommendations. Original and refined candidates form an expanded group and are jointly optimized with group relative policy optimization. The user simulator is only required during training and is removed at inference time. Experiments on three Amazon review datasets with two generative recommendation backbones demonstrate that VerRec improves recommendation accuracy and ranking quality. Further analyses show that verbalized guidance encourages exploration of more diverse candidates and helps the policy discover more rewarding recommendations during training.

</details>

---
