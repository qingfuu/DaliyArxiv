# cs.CR | Cryptography and Security | 2026-06-15

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/SkillMutator_Benchmarking_and_Defending_Language-and-Code_Cross-modal_Attacks_on_LLM_Agent_Skills|SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills]]

![[assets/2606.14154_figure.png|800]]

- **arXiv**: [2606.14154](https://arxiv.org/abs/2606.14154)
- **PDF**: https://arxiv.org/pdf/2606.14154
- **详细分析**: [[20_Research/Papers/大模型/SkillMutator_Benchmarking_and_Defending_Language-and-Code_Cross-modal_Attacks_on_LLM_Agent_Skills|SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills]]
- **作者**: Youngduk Kim, Minkyoo Song, Seungwon Shin
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly extend their capabilities at runtime by loading Agent Skills, which pair natural-language specifications (SKILL.md) with executable scripts and resources. Because a skill's behavior relies on both natural-language instructions and executable code, assessing its safety requires cross-modal reasoning, creating a new language-and-code attack surface. Attackers can present a benign workflow in SKILL.md while embedding implicit directives that steer the agent to exfiltrate sensitive files, even if the scripts appear harmless. This attack surface remains understudied; prior work treats skills merely as prompt-injection vectors or static code artifacts, leaving attacks emerging from cross-modal interactions largely unmeasured. In our evaluation, open-source and commercial skill scanners detect only 2%-8% and 9%-17% of such attacks, respectively. To address this gap, we introduce SkillMutator, the first benchmark for install-time detection of language-and-code cross-modal attacks on Agent Skills. It emulates an adversarial mutation process across 13 attack categories, iteratively refining malicious skills using scanner feedback to make injected behaviors indistinguishable from legitimate workflows. We further propose a four-phase reasoning-trajectory distillation framework to distill frontier-teacher traces into smaller open-weight models. This produces a locally deployable scanner avoiding third-party data exposure and excessive API costs. On the strongest SkillMutator subset (n=76), our distilled model (Qwen2.5-Coder-7B-Instruct) improves detection from 17.1% to 88.2%, surpassing GPT-4o-mini (23.7%) and GPT-5.4-mini (79.0%), and reaching frontier-level GPT-5.4 (86.8%). These results show practical defense against cross-modal attacks is feasible without relying on costly frontier models.

</details>

---
