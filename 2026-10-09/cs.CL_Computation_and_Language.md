# cs.CL | Computation and Language | 2026-10-09

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Do_LLMs_Learn_from_Rewards_in_Context_Rethinking_the_role_of_reward_in_In-Context_Reinforcement_Learning|Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning]]

![[assets/2610.11152_figure.png|800]]

- **arXiv**: [2610.11152](https://arxiv.org/abs/2610.11152)
- **PDF**: https://arxiv.org/pdf/2610.11152
- **详细分析**: [[20_Research/Papers/大模型/Do_LLMs_Learn_from_Rewards_in_Context_Rethinking_the_role_of_reward_in_In-Context_Reinforcement_Learning|Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning]]
- **作者**: Minchan Kwon, Seunghee Koh, Sunghyun Baek, Minsung Bae, Junmo Kim
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.45，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Do LLMs Learn from Rewards in Context? : Rethinking the role of reward in In-Context Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval, ICRL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly improve at inference time by accumulating experience in context rather than by updating parameters. This process is often described as in-context reinforcement learning (ICRL). Whether in-context learning (ICL) can actually play the role of RL, however, has not been tested. We study this question in its simplest form, direct ICRL, where the model conditions directly on raw trajectory-reward pairs, and ask whether the reward acts as a learning signal. Through controlled experiments on four benchmarks across six models, we find that the reward is read, but its effect is small: flipping, randomizing, or removing the reward leaves the improvement curve almost unchanged, and this holds even under meta-prompts that explicitly instruct the model to explore, exploit, or reason over rewards. Trajectories drive improvement, but not through their semantic content: shuffled or corrupted trajectories work as well as real ones. These patterns closely mirror those known in ICL, suggesting that direct ICRL is better understood as a special case of ICL than as inference-time RL. This reframing has implications for agent memory design: ICL factors such as input distribution and demonstrations may matter more than RL elements such as reward shaping and exploration.

</details>

---

### [[20_Research/Papers/大模型/Conversational_Voice_Aesthetic_Model_with_Reinforcement_Learning_from_Human_Listeners|Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners]]

![[assets/2610.10868_figure.png|800]]

- **arXiv**: [2610.10868](https://arxiv.org/abs/2610.10868)
- **PDF**: https://arxiv.org/pdf/2610.10868
- **详细分析**: [[20_Research/Papers/大模型/Conversational_Voice_Aesthetic_Model_with_Reinforcement_Learning_from_Human_Listeners|Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners]]
- **作者**: Xilin Jiang, Shun Zhang, Tejas Jayashankar, Yinghao Aaron Li, Osama Hanna
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.35，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MOSNet, POLQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Conversational Voice Aesthetic Model, a speech large language model for describing the voice aesthetics of real or synthetic speech responses in natural conversational contexts. Given a context and a response speech, CVAM describes salient moments that characterize the voice and predicts nine categorical attributes spanning gender, pitch, pacing, emotion, and delivery. The key challenge lies in perceptual fields such as emotion and delivery, which are inherently subjective and lack definitive ground truth. Therefore, we collect ~10 human annotations for each of 3k real and synthetic responses derived from the CANDOR corpus. CVAM is supervised finetuned on synthesized aesthetic descriptions and labels, then optimized with Group Relative Policy Optimization on human judgments. Experiments show that CVAM better agrees with human listeners than Gemini 3.1 Pro and open-source speech LLMs, and outperforms single-human-vs.-rest agreement. Together, we demonstrate the importance of grounding voice aesthetics in human perception and propose a principled framework for human alignment.

</details>

---
