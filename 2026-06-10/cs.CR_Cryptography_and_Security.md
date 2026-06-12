# cs.CR | Cryptography and Security | 2026-06-10

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/MemVenom_Triggered_Poisoning_of_Multimodal_Memories_in_Web_Agents|MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents]]

![[assets/2606.10742_figure.png|800]]

- **arXiv**: [2606.10742](https://arxiv.org/abs/2606.10742)
- **PDF**: https://arxiv.org/pdf/2606.10742
- **详细分析**: [[20_Research/Papers/大模型/MemVenom_Triggered_Poisoning_of_Multimodal_Memories_in_Web_Agents|MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents]]
- **作者**: Yv Zhang, Hao Sun, Hao Fang, Kuofeng Gao, Fan Mo, Bin Chen, Shu-Tao Xia, Yaowei Wang
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

</details>

---
