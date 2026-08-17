# cs.CR | Cryptography and Security | 2026-08-14

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/InterSAGE_The_Secure_and_Verifiable_Interoperability_Protocol_for_An_Internet_of_Agents|InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents]]

![[assets/2608.13030_first_page.png|800]]

- **arXiv**: [2608.13030](https://arxiv.org/abs/2608.13030)
- **PDF**: https://arxiv.org/pdf/2608.13030
- **详细分析**: [[20_Research/Papers/大模型/InterSAGE_The_Secure_and_Verifiable_Interoperability_Protocol_for_An_Internet_of_Agents|InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents]]
- **作者**: Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu
- **cs 子类**: cs.CR, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The emerging Internet of Agents enables LLM-powered agents to discover peers, invoke tools, and delegate tasks across organizational boundaries. Existing protocols increasingly define how agents exchange messages, but not how an agent proves its identity, authorization, advertised capabilities, or accountability after delegation. We present InterSAGE, a trust-native protocol suite that supplies this missing security substrate alongside, rather than in place of, communication protocols. InterSAGE comprises four layers: Persistent Identity, Discovery, Trust Negotiation, and Accountability. Its four core primitives are: (1) Agent Identity Cards that bind developer, code package, operator, and deployment context; (2) capability-aware discovery using DID-bound Verifiable Credential manifests; (3) trust negotiation combining monotonic capability attenuation with two-tier access control; and (4) kernel-mediated cryptographic audit trails that bind usage, delegation, and execution traces to agent identity without a consensus ledger. InterSAGE is designed to complement MCP, A2A, ANP, and AG-UI, allowing communication protocols to evolve independently while keeping trust semantics explicit, portable, and verifiable. We compare InterSAGE with more than 50 efforts spanning agent protocols, decentralized identity, OAuth/OIDC extensions, zero-trust governance, delegation, and audit architectures. We show that no prior architecture jointly enforces persistent identity, capability-aware discovery, trust negotiation, and accountability as a unified four-layer trust substrate for secure agent interoperability.

</details>

---
