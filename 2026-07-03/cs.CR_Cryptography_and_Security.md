# cs.CR | Cryptography and Security | 2026-07-03

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Cloak_and_Detonate_Scanner_Evasion_and_Dynamic_Detection_of_Agent_Skill_Malware|Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware]]

![[assets/2607.02357_figure.png|800]]

- **arXiv**: [2607.02357](https://arxiv.org/abs/2607.02357)
- **PDF**: https://arxiv.org/pdf/2607.02357
- **详细分析**: [[20_Research/Papers/大模型/Cloak_and_Detonate_Scanner_Evasion_and_Dynamic_Detection_of_Agent_Skill_Malware|Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware]]
- **作者**: Zimo Ji, Congying Xu, Zongjie Li, Yudong Gao, Xin Wei, Shuai Wang, Shing-Chi Cheung
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Cloak and Detonate: Scanner Evasion and Dynamic Detection of Agent Skill Malware》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MalSkillBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM coding agents increasingly rely on third-party agent skills from public marketplaces, which execute with the agent's privileges and create a software supply-chain attack surface: a malicious skill can steal credentials, exfiltrate source code, or install backdoors. Existing defenses use static skill scanners based on pattern matching or LLM-as-judge analysis, but it remains unclear whether they withstand adaptive evasions that preserve malicious behavior while changing payload appearance. This paper first presents an adversarial study of existing skill scanners through SkillCloak, a payload-preserving evasion framework that keeps the attack semantics intact while transforming their visible form. SkillCloak uses two complementary strategies: Structural Obfuscation, which rewrites visible payload indicators into semantically equivalent forms, and Self-Extracting Skill (SFS) Packing, which hides malicious components from the install-time view and restores them during agent execution. Across eight scanners and 1,613 in-the-wild malicious skills, SFS Packing bypasses every scanner at over 90%, while Structural Obfuscation bypasses over 80% on most static scanners and reaches 96% on a hybrid scanner, showing that appearance-based auditing is insufficient. Motivated by this finding, we propose SkillDetonate, a behavior-centric runtime auditor that executes skills in a sandbox and detects malicious effects through OS-boundary information-flow evidence rather than install-time appearance. SkillDetonate combines on-demand closure lift, which observes instructions materialized during execution, with marker-based taint analysis, which tracks sensitive-data flows across the agent context, files, processes, and network operations. The results show that SkillDetonate detects 97% of attacks at a 2% false-positive rate and sustains 87% detection on real-world malicious skills.

</details>

---

### [[20_Research/Papers/机器人/Overthink-Triggered_Slowdown_Attacks_on_LVLM-Based_Robotic_Systems|Overthink-Triggered Slowdown Attacks on LVLM-Based Robotic Systems]]

![[assets/2607.01518_figure.png|800]]

- **arXiv**: [2607.01518](https://arxiv.org/abs/2607.01518)
- **PDF**: https://arxiv.org/pdf/2607.01518
- **详细分析**: [[20_Research/Papers/机器人/Overthink-Triggered_Slowdown_Attacks_on_LVLM-Based_Robotic_Systems|Overthink-Triggered Slowdown Attacks on LVLM-Based Robotic Systems]]
- **作者**: Qiang Han, Jie Wu, Bo Chen
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Overthink-Triggered Slowdown Attacks on LVLM-Based Robotic Systems》归入 机器人、具身智能、大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Vision-Language Models (LVLMs) have been increasingly integrated into robotic systems. However, these models may exhibit overthinking behaviors, where they generate excessively long reasoning traces, incurring an excessive inference time. This overthinking behavior poses a serious risk to robotic systems, as the adversary can deliberately trigger overthinking to slow down the decision making of a victim robotic system, causing a variety of safety issues (i.e., an overthinking-induced slowdown attack). To initiate this attack, an adversary can embed carefully crafted, human-readable scene text into the visual scene observed by a victim robotic agent, causing significant inference delays even under a strict black-box setting. Therefore, the embedded scene text serves as a significant "trigger" for the attack. This work systematically identifies and validates transferable triggers of overthinking in robotic systems by introducing a three-stage framework. First, we construct a diverse corpus of reasoning-intensive scene text and extract overthinking-correlated lexical features from short response prefixes. Second, we perform an efficient black-box search guided by a prefix-based proxy score while selectively confirming a small set of top candidates with full latency measurements. Third, we evaluate black-box transfer using a fixed pool of triggers on unseen images and multiple LVLMs, reporting latency amplification and attack success rates under standard thresholds. Across three representative LVLMs, all triggers yield slowdown ratios greater than 1.0x, with the strongest single-trigger case reaching 6.96x. The physical printing of the text trigger still causes up to 4.74x latency amplification. These results demonstrate that our discovered triggers are transferred between multiple LVLM models and consistently cause significant slowdowns in robotic systems.

</details>

---
