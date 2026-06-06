# cs.CR | Cryptography and Security | 2026-06-04

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Sequential_Data_Poisoning_in_LLM_Post-Training|Sequential Data Poisoning in LLM Post-Training]]

![[assets/2606.04929_figure.png|800]]

- **arXiv**: [2606.04929](https://arxiv.org/abs/2606.04929)
- **PDF**: https://arxiv.org/pdf/2606.04929
- **详细分析**: [[20_Research/Papers/大模型/Sequential_Data_Poisoning_in_LLM_Post-Training|Sequential Data Poisoning in LLM Post-Training]]
- **作者**: Jack Sanderson, Yihan Wang, Xiaoqian Lu, Gautam Kamath, Yiwei Lu
- **cs 子类**: cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Sequential Data Poisoning in LLM Post-Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM post-training proceeds through multiple stages, e.g., supervised fine-tuning (SFT) followed by reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO), where each stage draws data from different, potentially untrusted sources. Existing literature assumes data poisoning attacks may occur at each training stage, but neglects the possibility of multiple attackers. To study the trustworthiness of the entire post-training pipeline, we propose the threat model of sequential data poisoning, where multiple adversaries separately poison the SFT and preference datasets. Under this threat model, we identify the single-attacker illusion: each adversary, evaluated in isolation, appears to pose a negligible threat. Yet when adversaries collaborate across stages, the true vulnerability is revealed. In the SFT $\to$ DPO pipeline, their contributions are additive: splitting a fixed poison budget across stages outperforms concentrating it in either stage alone. In the SFT $\to$ PPO pipeline, their contributions are complementary: neither SFT nor reward model poisoning succeeds individually, yet their combination does. These findings show that security analyses of individual post-training stages systematically underestimate compound vulnerabilities that emerge only from their interaction. Code is available at this https URL .

</details>

---
