# cs.CR | Cryptography and Security | 2026-07-31

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Cybersecurity_Detection_Classification_with_Reasoning-enabled_Language_Models|Cybersecurity Detection Classification with Reasoning-enabled Language Models]]

![[assets/2607.28460_figure.png|800]]

- **arXiv**: [2607.28460](https://arxiv.org/abs/2607.28460)
- **PDF**: https://arxiv.org/pdf/2607.28460
- **详细分析**: [[20_Research/Papers/大模型/Cybersecurity_Detection_Classification_with_Reasoning-enabled_Language_Models|Cybersecurity Detection Classification with Reasoning-enabled Language Models]]
- **作者**: Amol Khanna, Manu Nandan, Cristian Viorel Popa, Joan Pujol-Roig, Diana Bolocan, Laura Vasilie, Alexandru Apostu, Chase Helwig, Mihaela Gaman, Michael Brautbar, Edward Raff, Chase Midler...
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

《Cybersecurity Detection Classification with Reasoning-enabled Language Models》归入 强化学习、世界模型、大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A major issue in Security Operations Centers (SOCs) is alert fatigue, as the number of detections reported is more than staff can triage in a given day. Prior work prompts or fine-tunes large language models (LLMs) to emit a triage label directly, but does not train them to reason about whether a detection is a genuine threat. We train a chain-of-thought (CoT) reasoning-enabled triage classifier on real, human-labeled Windows endpoint detections by combining automated prompt optimization, self-training, and reinforcement learning with verifiable rewards. We find that CoT reasoning also degrades the label-token probabilities that automated triage relies on, so we separately train a calibrator that reads the full reasoning trace and estimates the probability that the verdict is correct. Our system reaches 82.6% test accuracy and, at the high-confidence operating point that governs automated triage, improves benign recall by 43.0% and malicious recall by 18.3% over a direct-label LLM classifier. We further show that the trained calibrator is necessary - an untrained confidence judge collapses high-confidence recall to zero - and that a finetuned 30B model significantly outperforms frontier general-purpose models, motivating targeted training over scale.

</details>

---

### [[20_Research/Papers/大模型/Piggybacking_on_Perception_Stealthy_Concurrent_Audio_Prompt_Injections_against_Multimodal_LLM_Agents|Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents]]

![[assets/2607.28165_figure.png|800]]

- **arXiv**: [2607.28165](https://arxiv.org/abs/2607.28165)
- **PDF**: https://arxiv.org/pdf/2607.28165
- **详细分析**: [[20_Research/Papers/大模型/Piggybacking_on_Perception_Stealthy_Concurrent_Audio_Prompt_Injections_against_Multimodal_LLM_Agents|Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents]]
- **作者**: Mingxiao Liu, Yitong Li, Haoren Zhao, Yaoxiang Bian, Jianan Ma, Jian Zhang, Jialuo Chen, Xinhao Deng, Zhen Wang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Piggybacking on Perception: Stealthy Concurrent Audio Prompt Injections against Multimodal LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, SACRED-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-driven multimodal agents are increasingly deployed to execute autonomous tasks via continuous audio interaction. While this paradigm enhances interaction naturalness, it introduces a critical yet under-explored attack surface, as audio inputs inevitably contain environmental noise beyond user control. In this paper, we investigate concurrent audio prompt injection attacks targeting multimodal agents. Distinct from traditional acoustic attacks on voice devices, we propose novel techniques for instruction augmentation and scenario concealment. These methods allow malicious audio instructions to imperceptibly "piggyback" onto user speech, thereby hijacking agents to execute malicious actions. To systematically quantify this threat, we construct AudioAgentSecurity, the first comprehensive benchmark for audio instruction injection attacks, encompassing 8 real-world task scenarios and 10 distinct attack patterns. We evaluate 11 state-of-the-art agents, including Gemini 3 Pro and GPT-4o-audio. Notably, our methods achieve an average Attack Success Rate (ASR) of 69.10\% against the advanced Gemini 3 Pro. To counter this threat, we further introduce Cascaded Audio Decoupling and Verification (CADV), a defense mechanism based on source separation and consistency analysis. Compared with existing prompt-level defenses, CADV leverages acoustic source separation and cross-modal consistency analysis to detect audio instruction injections more robustly, achieving over 90\% detection success across diverse attack vectors. Finally, real-world experiments with human volunteers on Doubao AI Smartphone in diverse dynamic real-world scenarios confirm the attacks' high stealth and efficacy, while demonstrating that our defense reliably mitigates these vulnerabilities.

</details>

---
