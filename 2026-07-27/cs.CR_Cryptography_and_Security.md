# cs.CR | Cryptography and Security | 2026-07-27

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/大模型/Ethereum_NFT_Smart_Contracts_Knowledge-Guided_Vulnerability_Detection_with_LLM_and_Code_Slicing|Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing]]

![[assets/2607.21983_figure.png|800]]

- **arXiv**: [2607.21983](https://arxiv.org/abs/2607.21983)
- **PDF**: https://arxiv.org/pdf/2607.21983
- **详细分析**: [[20_Research/Papers/大模型/Ethereum_NFT_Smart_Contracts_Knowledge-Guided_Vulnerability_Detection_with_LLM_and_Code_Slicing|Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing]]
- **作者**: Deyu Yang, Rundong Wei, Xiaoqi Li
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Ethereum NFT Smart Contracts: Knowledge-Guided Vulnerability Detection with LLM and Code Slicing》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ethereum non-fungible tokens (NFTs) implement ownership, transfer, authorization, and metadata operations through smart contracts, making contract vulnerabilities a direct risk to digital assets. Existing static analyzers provide efficient rule-based screening but can struggle with application-specific logic, whereas unconstrained large language model analysis may be distracted by irrelevant code or produce inconsistent outputs. We present a vulnerability-detection method that combines vulnerability-focused code slicing, an ERC-721-oriented knowledge base, and constrained DeepSeek analysis. Regular-expression patterns locate candidate statements for reentrancy, integer overflow or underflow, and timestamp dependence. A structure-aware context-window algorithm then extracts line-numbered code slices. DeepSeek analyzes each slice using explicit decision rules and a fixed output schema, and the resulting records support automated batch processing. On 450 NFT contract samples, the full configuration produced 437 positive labels, corresponding to a reported positive-label rate of 97.1%. Removing the external knowledge base reduced this rate to 87.11%, while analyzing complete contracts without the knowledge base reduced it to 73.78%. These results indicate that focused code context and domain constraints materially affect the detector's reported output.

</details>

---

### [[20_Research/Papers/大模型/KaPilot_LLM-Assisted_Generation_of_Kani_Specifications_for_Unsafe_Rust_Verification|KaPilot: LLM-Assisted Generation of Kani Specifications for Unsafe Rust Verification]]

![[assets/2607.21957_figure.png|800]]

- **arXiv**: [2607.21957](https://arxiv.org/abs/2607.21957)
- **PDF**: https://arxiv.org/pdf/2607.21957
- **详细分析**: [[20_Research/Papers/大模型/KaPilot_LLM-Assisted_Generation_of_Kani_Specifications_for_Unsafe_Rust_Verification|KaPilot: LLM-Assisted Generation of Kani Specifications for Unsafe Rust Verification]]
- **作者**: Minghua Wang, Yuxi Ling, Mingzhi Gao, Yuwei Liu, Lin Huang
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《KaPilot: LLM-Assisted Generation of Kani Specifications for Unsafe Rust Verification》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GoldSet, ULSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rust's ownership and type system provide strong memory safety guarantees, but unsafe code still presents memory safety risks. Formal verification is crucial for ensuring memory safety, but writing precise specifications for unsafe Rust is challenging and largely manual. Large language models (LLMs) have shown promise in generating formal specifications but are often code-centric, prone to inheriting implementation flaws, and lack systematic quality assessment. In this paper, we present KaPilot, a multi-agent framework for automatically generating specifications to verify unsafe Rust memory safety using Kani. The process begins with lightweight program analysis and proof harness generation. The SafetyReq agent extracts a concise, refined list of safety requirements from the target Rust function's documentation, which guides the SpecGenerate agent in producing initial specifications that specify memory safety concerns. Then, the specifications are iteratively refined through a generate-precheck-verify loop involving SpecGenerate, SpecPrecheck, and SpecVerify agents, which assess quality and feed errors back. By executing this loop multiple times, KaPilot generates a set of candidate specifications. Finally, the shuffle-and-implication strategy is applied to systematically determine the best specification from these candidates. We evaluated KaPilot on 54 unsafe Rust functions with ground truth and 70 without. KaPilot achieved 88.9% and 71.4% specification generation success, respectively, with 57.4% of generated specifications equivalent to or stronger than the ground truth. Compared with AutoSpec, KaPilot produces 14.8% more verifiable specifications and 25.9% more equivalent-or-better specifications.

</details>

---

### [[20_Research/Papers/大模型/SIREN_(Luring_LLMs_onto_the_Rocks)_PAIR-Driven_Preference_Manipulation_in_Web-RAG_Recommenders|SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders]]

![[assets/2607.21951_first_page.png|800]]

- **arXiv**: [2607.21951](https://arxiv.org/abs/2607.21951)
- **PDF**: https://arxiv.org/pdf/2607.21951
- **详细分析**: [[20_Research/Papers/大模型/SIREN_(Luring_LLMs_onto_the_Rocks)_PAIR-Driven_Preference_Manipulation_in_Web-RAG_Recommenders|SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders]]
- **作者**: Evan Caville, Siamak Layeghy, Billy Sung, Sara Dolnicar, Marius Portmann
- **cs 子类**: cs.CR, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Robotics, Security

#### 研究背景与动机

《SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GEO-Bench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs). When an LLM answers a recommendation query by retrieving and reading live webpages, it acts as a recommender, and each retrieved page becomes a potential attack surface. Prior work has examined fabricated products, retrieval poisoning, and rank promotion. However, these studies do not compare how different edits to an already retrieved page change the model's final ranking while the surrounding source set remains unchanged. To address this gap, we propose SIREN, an automated attacker--judge method that adapts the PAIR jailbreaking loop to competitive rank manipulation, with the goal of moving a chosen entity to rank~1 in an LLM-generated recommendation. SIREN retrieves and captures webpages using Anthropic's web tools, then iteratively edits a retrieved source using an interpretable taxonomy of 23 content-poisoning techniques. The custom-RAG replay platform keeps the same sources in the same order, so changes in the model's ranking can be linked to changes in the supplied content rather than to differences in retrieval. Across two production Claude models, SIREN reaches rank~1 in 62 of 124 technique trials nested within eight query--model contexts. The payloads that reached rank~1 were then tested in fresh sessions, where they reproduced the result with a mean success rate of 0.805. Across the evaluated settings, declarative ranking claims and seeded lists were generally more effective than directive-form injections, although the strength of this difference depended on the target model. To the best of our knowledge, this is among the first controlled studies of competitive rank manipulation in production LLMs where the supplied source context is kept fixed.

</details>

---

### [[20_Research/Papers/大模型/CARE_Pre-Execution_Command_Verification_for_Shell-Executing_LLM_Agents|CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents]]

![[assets/2607.21642_figure.png|800]]

- **arXiv**: [2607.21642](https://arxiv.org/abs/2607.21642)
- **PDF**: https://arxiv.org/pdf/2607.21642
- **详细分析**: [[20_Research/Papers/大模型/CARE_Pre-Execution_Command_Verification_for_Shell-Executing_LLM_Agents|CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents]]
- **作者**: Wenxiao Zhang, Yu Liu, Zhiwei Yang, Zhongyi Zhang, Hanqi Feng, Xinyu Wang, Peng Qiu, Yanbing Liu, Barnabas Poczos, Jin B. Hong
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents are increasingly used for coding and terminal automation, making shell-command dispatch a high-stakes runtime control point. We study command-level pre-execution mediation for individual shell commands produced by LLM agents under bounded path context. Existing safeguards remain limited: generic guardrails do not model shell structure in sufficient detail, always-on LLM judges are relatively costly and variable, and shell parsers do not directly prevent harmful execution. We present CARE (Canonicalization, Attribution, and Resolution Engine), a shell-specific, static-first verifier for individual shell commands before execution. CARE canonicalizes generated commands into stable verification targets, derives deterministic evidence over syntax, command semantics, path context, and provenance-backed risk patterns, and escalates only underdetermined cases to an LLM judge. This design keeps the common case fast, reproducible, and auditable while reserving neural adjudication for borderline commands. On the balanced main split, CARE reaches 85.64% F1 with a 0.91% false-positive rate at 2.32 ms mean latency. When deployed in its static enforcement profile, CARE retains 84.99% F1 at 0.34 ms and reduces realised harm on RedCode-gen to 37.33%. Across external-generalization tests and controlled Docker-sandbox execution, these profiles expose a practical trade-off between benign recovery, false-positive burden, latency, and harm reduction. Overall, command-level shell mediation can reduce dispatch-boundary risk for LLM agents while preserving most benign workflows.

</details>

---
