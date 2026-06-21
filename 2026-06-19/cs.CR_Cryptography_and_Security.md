# cs.CR | Cryptography and Security | 2026-06-19

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/A_Measurement_Study_of_Cryptographic_Misuse_in_Embodied_AI_Mobile_Applications|A Measurement Study of Cryptographic Misuse in Embodied AI Mobile Applications]]

![[assets/2606.19983_figure.png|800]]

- **arXiv**: [2606.19983](https://arxiv.org/abs/2606.19983)
- **PDF**: https://arxiv.org/pdf/2606.19983
- **详细分析**: [[20_Research/Papers/具身智能/A_Measurement_Study_of_Cryptographic_Misuse_in_Embodied_AI_Mobile_Applications|A Measurement Study of Cryptographic Misuse in Embodied AI Mobile Applications]]
- **作者**: Junchao Li, Xuelei Wang, Yuhang Huang, Qi Wang, Boyang Ma, Xuelong Dai, Minghui Xu, Yue Zhang
- **cs 子类**: cs.CR
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 2.4（加权：具身智能 2.4）
- **关联关键词**: EmbodiedAI, Security, Systems

#### 研究背景与动机

《A Measurement Study of Cryptographic Misuse in Embodied AI Mobile Applications》归入 具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied AI (EAI) mobile applications are evolving from auxiliary user interfaces into active control-path components, directly linking mobile-side cryptographic security to cyber-physical trust. Despite this shift, existing security research predominantly focuses on embodied AI devices and cloud infrastructures, leaving the mobile control layer largely unexplored as a critical attack surface. To bridge this gap, we present the first large-scale measurement study of cryptographic misuse within the EAI mobile ecosystem. We construct EAIAppZoo, a benchmark of 507 real-world applications across six EAI domains, and employ an automated semantic-aware analysis pipeline to measure the prevalence and characteristics of five major cryptographic failure modes. Our measurement yields 12,975 misuse findings (with an evaluated precision of 80.74\%), revealing that these cryptographic failures are driven by EAI-specific engineering constraints rather than random developer errors. We uncover structural security trade-offs: latency-sensitive control paths systematically weaken transport protection, while the heavy reliance on offline device provisioning and legacy IoT SDKs exacerbates the local hardcoding of authentication credentials. Through real-world case studies, we demonstrate how these mobile-side cryptographic flaws bypass nominal network protections, enabling adversaries to intercept command channels and hijack the physical control of EAI entities. Ultimately, our findings highlight that mobile applications have become a fragile, yet overlooked, cryptographic trust boundary in cyber-physical systems.

</details>

---
