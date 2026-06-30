# cs.CR | Cryptography and Security | 2026-06-29

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/其他/How_Humans,_Bots,_and_Agents_Communicate_About_Vulnerabilities_in_Pull_Requests|How Humans, Bots, and Agents Communicate About Vulnerabilities in Pull Requests]]

![[assets/2606.28125_figure.png|800]]

- **arXiv**: [2606.28125](https://arxiv.org/abs/2606.28125)
- **PDF**: https://arxiv.org/pdf/2606.28125
- **详细分析**: [[20_Research/Papers/其他/How_Humans,_Bots,_and_Agents_Communicate_About_Vulnerabilities_in_Pull_Requests|How Humans, Bots, and Agents Communicate About Vulnerabilities in Pull Requests]]
- **作者**: Pien Rooijendijk, Christoph Treude, Mairieli Wessel
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《How Humans, Bots, and Agents Communicate About Vulnerabilities in Pull Requests》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Developers may reference vulnerabilities in pull request discussions through both explicit identifiers, such as CVEs or GHSAs, and implicit security-related language (e.g., "unauthorized access" or "SQL injection"). Prior work has primarily focused on explicit identifiers, potentially overlooking vulnerability discussions that lack formal references. Bots and coding agents are becoming more common in pull requests, raising new questions about how different accounts communicate about vulnerabilities. In this registered report, we describe our planned study of vulnerability communication in pull requests by humans, bots, and coding agents. Building on the AIDev-pop dataset, we analyze explicit vulnerability references and implicit security-related signals across pull request titles, descriptions, review comments, commit messages, and timeline discussions. We further investigate whether these references are associated with vulnerabilities introduced or fixed in the modified code and how they relate to pull request review activity and outcomes. This study contributes a large-scale empirical investigation of vulnerability communication practices in modern software development.

</details>

---

### [[20_Research/Papers/大模型/AdvancedShelLM_A_Stateful_Multi-Agent_LLM_Honeypot_for_SSH_Deception|AdvancedShelLM: A Stateful Multi-Agent LLM Honeypot for SSH Deception]]

![[assets/2606.27990_figure.jpg|800]]

- **arXiv**: [2606.27990](https://arxiv.org/abs/2606.27990)
- **PDF**: https://arxiv.org/pdf/2606.27990
- **详细分析**: [[20_Research/Papers/大模型/AdvancedShelLM_A_Stateful_Multi-Agent_LLM_Honeypot_for_SSH_Deception|AdvancedShelLM: A Stateful Multi-Agent LLM Honeypot for SSH Deception]]
- **作者**: Muris Sladić, Eman Alibalić, Veronica Valeros, Carlos Catania, Sebastian Garcia
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AdvancedShelLM: A Stateful Multi-Agent LLM Honeypot for SSH Deception》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based SSH honeypots can generate believable interactions, but evaluations indicate they remain somewhat identifiable to determined attackers, indicating the need for a better scaffolding. We present a new LLM-based honeypot design that uses a multi-agent, multi-LLM architecture to address the limitations of the previous shelLM LLM honeypot. Our honeypot, called AdvancedShelLM, uses two LLM agents, a Manager and a Worker, that better understand the commands while reducing incorrect responses and increasing deception. It implements an advanced permanent filesystem, allowing many simultaneous attackers to see the same changing files for the first time. It was evaluated with: (i) unit tests for generative capabilities, (ii) an AI attacker (ARACNE) to assess realism and deception, (iii) human attackers to assess its deceptive capability, and (iv) an Internet deployment to evaluate deception in real-world attacks. In unit test results, AdvancedShelLM achieved a pass rate of up to 99.02%. The AI attacker ARACNE had issues making a decision if the system is honeypot or not, but showed slight bias towards saying honeypot, even for a real Ubuntu shell. With human attackers, AdvancedShelLM deceived more humans than Cowrie, but had similar results as shelLM. The Internet deployment showed concrete evidence that the output of AdvancedShelLM can influence the behaviour of real-life attackers.

</details>

---

### [[20_Research/Papers/大模型/When_the_Aggregator_Cheats_Data-Free_Backdoors_in_Federated_LLM-based_QA_Systems|When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems]]

![[assets/2606.27511_figure.png|800]]

- **arXiv**: [2606.27511](https://arxiv.org/abs/2606.27511)
- **PDF**: https://arxiv.org/pdf/2606.27511
- **详细分析**: [[20_Research/Papers/大模型/When_the_Aggregator_Cheats_Data-Free_Backdoors_in_Federated_LLM-based_QA_Systems|When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems]]
- **作者**: Chenqing Zhu, Yanbo Dai, Yulong Tian, Qingming Li, Songze Li
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-based question-answering (QA) systems are increasingly deployed in sensitive domains such as healthcare, mental health counseling, and legal consultation. Federated learning (FL) enables collaborative training without sharing raw client data, for which locally trained models are aggregated at a central server (i.e., a cloud service provider) to obtain a global model. In this paper, we explore the potential vulnerability where a malicious aggregator, who may collude with a third-party vendor, stealthily implants advertisement-type backdoors into federated QA models, without ever accessing client data. The attacker's goals are twofold: (1) preserve clean QA fidelity (i.e., the poisoned model behaves like a clean model on non-triggered queries); and (2) generate highly natural, contextually relevant responses with target advertisements when a trigger appears. Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. Motivated by this, we propose to leverage clients' uploaded gradients during training, and develop a two-stage framework for data-free and stealthy poisoning: (1) recover representative training samples from client gradients, and (2) construct poisoning datasets utilizing recovered samples and trigger phrases to inject backdoors into the global model. Experiments across representative QA datasets and LLM families under full fine-tuning and LoRA settings demonstrate that, our method achieves nearly 100% Attack Success Rate (ASR) while incurring negligible degradation on clean tasks. Crucially, reconstructing only 5-20% of gradients suffices to mount a reliable attack, exposing a practical blind spot in the pipeline of federated training of QA LLMs.

</details>

---
