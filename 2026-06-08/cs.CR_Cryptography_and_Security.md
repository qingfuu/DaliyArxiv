# cs.CR | Cryptography and Security | 2026-06-08

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/MalSkillBench_A_Runtime-Verified_Benchmark_of_Malicious_Agent_Skills|MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills]]

![[assets/2606.07131_figure.png|800]]

- **arXiv**: [2606.07131](https://arxiv.org/abs/2606.07131)
- **PDF**: https://arxiv.org/pdf/2606.07131
- **详细分析**: [[20_Research/Papers/大模型/MalSkillBench_A_Runtime-Verified_Benchmark_of_Malicious_Agent_Skills|MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills]]
- **作者**: Wenbo Guo, Wei Zeng, Chengwei Liu, Xiaojun Jia, Yijia Xu, Lei Tang, Yong Fang, Yang Liu
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MalSkillBench, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI coding agents such as Claude Code and Gemini CLI increasingly extend themselves with third-party skills: markdown packages bundling natural-language instructions, executable scripts, and tool permissions. Because a skill is at once code and agent-facing instruction, it introduces a supply chain dependency whose risk is neither pure code nor pure prompt. Detection tools have never been measured against verified ground truth spanning this hybrid space, leaving their effectiveness unknown and wild-only evaluations biased. We present MalSkillBench, the first runtime-verified benchmark of malicious agent skills: 3,944 malicious skills labeled along a three-dimensional taxonomy of 108 cells. Of these, 3,214 come from a closed-loop Generate-Verify-Feedback pipeline admitting only samples whose malicious behavior fires inside a Docker sandbox under system-call monitoring and an LLM judge; we add 703 in-the-wild and 4,000 matched benign skills. Our measurements are consistent: code injection reaches 94.5% verification yield but prompt injection only 75.8%, the same fragility that later makes it hard to detect; the wild sample is narrow, dominated by one cryptocurrency-theft campaign (86.6% one behavior, 81% from two accounts) with a small but architecturally new tail attacking the agent control plane; the strongest skill-specific detector reaches 98.4% recall on code injection yet collapses on prompt-injection and agent-control attacks, and wild-only scoring swings the ranking by up to 66 recall points; supply-chain scanners and prompt-injection defenses each see only half of a skill, and no combination recovers the code-instruction relationship. Detecting malicious skills therefore requires reasoning jointly over task intent, code, and instructions. We release the dataset, pipeline, baselines, and results.

</details>

---

### [[20_Research/Papers/具身智能/Blockchain_Infrastructure_for_Intelligent_Cyber--Physical--Social_Systems_Post-Quantum_Security,_Interoperability,_and_Trustworthy_Data_Econ|Blockchain Infrastructure for Intelligent Cyber--Physical--Social Systems:Post-Quantum Security, Interoperability, and Trustworthy Data Economies in the Era of Embodied AI]]

![[assets/2606.06895_figure.png|800]]

- **arXiv**: [2606.06895](https://arxiv.org/abs/2606.06895)
- **PDF**: https://arxiv.org/pdf/2606.06895
- **详细分析**: [[20_Research/Papers/具身智能/Blockchain_Infrastructure_for_Intelligent_Cyber--Physical--Social_Systems_Post-Quantum_Security,_Interoperability,_and_Trustworthy_Data_Econ|Blockchain Infrastructure for Intelligent Cyber--Physical--Social Systems:Post-Quantum Security, Interoperability, and Trustworthy Data Economies in the Era of Embodied AI]]
- **作者**: Song Guo, Huawei Huang, Dongping Liu, Aoyu Zhang, Luyao Zhang
- **cs 子类**: cs.CR
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.4，机器人 0.4）
- **关联关键词**: Robotics, EmbodiedAI, Security

#### 研究背景与动机

《Blockchain Infrastructure for Intelligent Cyber--Physical--Social Systems:Post-Quantum Security, Interoperability, and Trustworthy Data Economies in the Era of Embodied AI》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRASim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The deployment of embodied artificial intelligence via world-model-based robotics presents a transformative opportunity for blockchain infrastructure, establishing urgent demand for trustworthy data provenance, cross-organizational governance, and incentive-compatible sharing across decentralized ecosystems. Simultaneously, quantum computing advances recognized by the 2025 Nobel Prize in Physics and the Turing Award threaten the cryptographic primitives securing these data economies, creating an interdependent imperative: long-lived verification for embodied AI depends on crypto-agile architectures capable of withstanding quantum adversaries. This tutorial examines blockchain as the coordination layer bridging this dual transition, from financial substrate to foundational Cyber-Physical-Social Systems infrastructure that simultaneously secures against quantum cryptanalysis and enables scalable, trustworthy data economies. The session opens with an immersive AWS Braket demonstration engaging participants with superconducting, trapped-ion, and neutral-atom hardware to assess cryptographic threat timelines and witness ECDSA-to-post-quantum signature transitions. Five integrated modules progress from embodied AI and world-model requirements through quantum hardware reality and evidence-based security migration, to scalable cross-shard architectures via BrokerChain protocols, trustworthy data economies implementing Croissant metadata standards and robotic learning provenance, and industry ecosystem integration for multi-modal cloud deployment. By bridging quantum hardware realities with embodied AI data requirements, this tutorial charts blockchain as unified infrastructure for next-generation decentralized intelligent environments, providing open-source frameworks and roadmaps for architecting quantum-resistant, interoperable, and data-trustworthy systems.

</details>

---
