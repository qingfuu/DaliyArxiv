# cs.CR | Cryptography and Security | 2026-08-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/PromptShield_Home_Ambient_Multimodal_Prompt_Injection_Defense_for_Smart-Home_Agents|PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents]]

![[assets/2608.05495_figure.png|800]]

- **arXiv**: [2608.05495](https://arxiv.org/abs/2608.05495)
- **PDF**: https://arxiv.org/pdf/2608.05495
- **详细分析**: [[20_Research/Papers/大模型/PromptShield_Home_Ambient_Multimodal_Prompt_Injection_Defense_for_Smart-Home_Agents|PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents]]
- **作者**: He Zhang, Feilong Li, Dingning Long, Yilin Cui, Peijun Zhang, Yuewen Zhang, Qianyao Xu, Xinyi Fu
- **cs 子类**: cs.CR, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《PromptShield Home: Ambient Multimodal Prompt Injection Defense for Smart-Home Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Smart-home assistants increasingly use multimodal large language models (MLLMs) that perceive video and audio directly. This raises a safety question specific to the home: can the agent tell a genuine user command from ambient or externally-sourced content, television speech, on-screen text, or an overheard conversation, that merely looks like a command? We introduce PromptShield-Home, a pilot benchmark of realistic smart-home scenarios spanning addressee ambiguity, screen/audio injection, health-monitor false triggers, mixed occupancy, and a legitimate-command floor, and use it to compare three abstraction layers: traditional detectors (L0), a single MLLM agent (L1; vision, vision+ASR, and audio-visual), and multi-agent mediation (L2; voting, role specialists, cross-model arbitration). Because the label distribution is skewed toward inaction, aggregate accuracy is misleading, a constant always-block predictor scores 82%, so we report unsafe-execution and safe-completion rates separately. The two paradigms fail in opposite ways: detectors act on everything, while every MLLM configuration over-refuses, completing almost no genuine command and missing a true fall in every case. Crucially, their correct sets are disjoint: an oracle that always picks the right layer reaches 94.1%, against 76.5% for the best single layer. We report this as an upper bound, not a system - no router is implemented - and argue that home-agent safety is best served by learned routing and sensor fusion, not by replacing detectors with an MLLM.

</details>

---
