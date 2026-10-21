# cs.CR | Cryptography and Security | 2026-10-19

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/GRAD_Graph-Structured_Antibody_Defense_for_LLM_Agents|GRAD: Graph-Structured Antibody Defense for LLM Agents]]

![[assets/2610.22828_first_page.png|800]]

- **arXiv**: [2610.22828](https://arxiv.org/abs/2610.22828)
- **PDF**: https://arxiv.org/pdf/2610.22828
- **详细分析**: [[20_Research/Papers/大模型/GRAD_Graph-Structured_Antibody_Defense_for_LLM_Agents|GRAD: Graph-Structured Antibody Defense for LLM Agents]]
- **作者**: Tianqi Song, Jiawei Du, Xuemei Jia, Zheng Wang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《GRAD: Graph-Structured Antibody Defense for LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory poisoning and decomposition attacks distribute malicious evidence across the operations of large language model agents. Existing request-level defenses can miss such attacks because they assess individual inputs without connecting earlier information to later actions. Moreover, detectors must adapt as task contexts change, while updates to shared parameters can impair previously learned detection capabilities. To address these challenges, we propose GRAD, which combines graph-based evidence aggregation across operations with an extensible collection of detection experts. Its Semantic-Structural Understanding Module (SSUM) jointly encodes operation text, event attributes, and typed candidate relations in an execution graph to aggregate distributed attack evidence into a graph-level risk score. Its Continual Antibody Adaptation (CAA) adds experts on frozen encoder snapshots and routes inputs by observable graph signatures, acquiring and reusing detection capabilities as tasks arrive. Across Decomp, MCP, and MRT, GRAD achieves AUROCs of 97.19%, 77.59%, and 86.60%, respectively, outperforming Sequential Monitor and locally adapted Agent-Sentry and NeuroTaint. CAA improves final accuracy by 13.08 percentage points over Replay on the cross-dataset task stream. The gain remains 9.05 points with equal family/base-case weights within each task. Its compact drop-in gate performs local model inference in milliseconds without monitoring API calls.

</details>

---

### [[20_Research/Papers/大模型/Model-as-a-Trojan_Self-Activating_Covert_DNS_Exfiltration_Baked_Into_the_Weights_of_an_LLM_Agent|Model-as-a-Trojan: Self-Activating Covert DNS Exfiltration Baked Into the Weights of an LLM Agent]]

![[assets/2610.22578_figure.png|800]]

- **arXiv**: [2610.22578](https://arxiv.org/abs/2610.22578)
- **PDF**: https://arxiv.org/pdf/2610.22578
- **详细分析**: [[20_Research/Papers/大模型/Model-as-a-Trojan_Self-Activating_Covert_DNS_Exfiltration_Baked_Into_the_Weights_of_an_LLM_Agent|Model-as-a-Trojan: Self-Activating Covert DNS Exfiltration Baked Into the Weights of an LLM Agent]]
- **作者**: Barak Haryati, Shaked Zychlinski
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Model-as-a-Trojan: Self-Activating Covert DNS Exfiltration Baked Into the Weights of an LLM Agent》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-weight models are downloaded from public hubs and run inside agent harnesses that grant them tools, most powerfully, a shell, under the assumption that a sandbox contains whatever the model might do. This paper demonstrates that the assumption has a blind spot: the weights themselves can be the malware, and the sandbox's last open door, DNS, is enough. We fine-tune an open-weight LLM so that a single covert behavior lives in its parameters: on the first turn of every conversation, whenever the model infers from its context that a shell tool is available, it emits one self-contained command that reads a secret from the runtime environment, base32-encodes it, chunks it, and exfiltrates it as DNS queries toward an attacker-controlled authoritative name server. It then answers the user normally and never mentions, or repeats, the act. Because the channel is DNS, the attack completes from inside a container with no internet egress beyond name resolution - measured payload-level and model-level behind an egress firewall that drops every non-DNS packet, with the secret reconstructed from the gateway resolver's query log. Because the behavior lives in the weights, prompting is the only off-switch a victim has, and it is unreliable: the implant fires in 20/20 of adversarial suppression trials, deflects direct interrogation without disclosing the sequence, and sweeps a 45-cell sandbox-fault matrix across five tool-calling formats - plus a fresh post-training canary, persona-only and absent system prompts, and an egress-locked topology - with zero leaks and zero repeat fires. Every training trajectory is execution-verified in a real container, and every claimed exfiltration is proven resolver-side: we reconstruct the secret from the authoritative resolver's query log alone.

</details>

---
