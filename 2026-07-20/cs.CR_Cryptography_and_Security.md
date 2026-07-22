# cs.CR | Cryptography and Security | 2026-07-20

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Refusal_is_Not_Safety!_Benchmarking_Latent_Safety_Risks_of_LLM-Driven_Content_Humorization|Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization]]

![[assets/2607.15977_figure.png|800]]

- **arXiv**: [2607.15977](https://arxiv.org/abs/2607.15977)
- **PDF**: https://arxiv.org/pdf/2607.15977
- **详细分析**: [[20_Research/Papers/大模型/Refusal_is_Not_Safety!_Benchmarking_Latent_Safety_Risks_of_LLM-Driven_Content_Humorization|Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization]]
- **作者**: Yu Cui, Ruiqing Yue, Tingyu Li, Sicheng Pan, Zhuoyu Sun, Xufeng Zhang, Baohan Huang, Haibin Zhang, Cong Zuo
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Refusal is Not Safety! Benchmarking Latent Safety Risks of LLM-Driven Content Humorization》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety defenses for large language models (LLMs) have been extensively studied, with existing approaches focusing on attack detection and refusal mechanisms. Such fixed-form direct refusal strategies may introduce the risk of prefix injection attacks. Recent work has explored a new direction that leverages humor as an indirect refusal mechanism to mitigate over-refusal in jailbreak scenarios and reduce prefix injection risks. However, this approach implicitly assumes that humorous responses are safe. Whether humorization itself introduces safety risks remains unexplored. To address this issue, we conduct an exploratory study involving over 30,000 real-world agent interaction records and 45 stand-up comedians, revealing practical safety concerns in LLM-based content humorization. Motivated by these findings, we propose \textsc{HumorSafe}, a novel framework for evaluating latent safety risk propagation during humorization. \textsc{HumorSafe} enables LLMs to learn harmful humorization patterns and use them to transform benign content into humorous content with safety risks. Across five frontier LLMs, we find that LLMs can introduce stereotypes and toxicity during humorization. We further propose \textsc{HumorPIA}, a prompt injection attack that exploits latent risks in humor-based defenses. \textsc{HumorPIA} preserves the appearance of safe humorous refusal while covertly injecting harmful content, allowing latent risks to evade existing detection mechanisms. Experiments show that it increases toxicity by 3.14$\times$ while maintaining an apparent safety rate of 97.8\% even under defense settings. Our findings highlight a gap in existing LLM safety evaluations under humorized settings.

</details>

---

### [[20_Research/Papers/大模型/Do_Agents_Dream_of_False_Memories_Black-box_Visual_Attacks_on_Long-term_Memory_in_Multimodal_AI_Agents|Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents]]

![[assets/2607.15657_figure.png|800]]

- **arXiv**: [2607.15657](https://arxiv.org/abs/2607.15657)
- **PDF**: https://arxiv.org/pdf/2607.15657
- **详细分析**: [[20_Research/Papers/大模型/Do_Agents_Dream_of_False_Memories_Black-box_Visual_Attacks_on_Long-term_Memory_in_Multimodal_AI_Agents|Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents]]
- **作者**: Halima Bouzidi, Mboutidem Ekemini Mkpong, Mohammad Abdullah Al Faruque
- **cs 子类**: cs.CR, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distinct failure modes based on the availability of historical context: (1) Memory poisoning, an in-context attack where the adversarial image replaces a benign one whose content is reinforced by prior textual context, reliably corrupting visual recall and steering the agent toward attacker-chosen narratives; (2) Memory injection, an out-of-context attack where the adversarial image replaces a benign one in a conversation turn devoid of prior textual grounding, causing the agent to generate attacker-influenced responses with no corrective signal from memory. We evaluate Lucid across various conversation domains and five black-box memory architectures, including graph-structured, LLM-summarized, and commercially deployed systems. Lucid achieves 61.6% ASR on poisoning and 58.4% ASR on injection, exposing a structural vulnerability in multimodal memory pipelines.

</details>

---
