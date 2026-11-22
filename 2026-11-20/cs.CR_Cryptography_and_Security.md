# cs.CR | Cryptography and Security | 2026-11-20

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Verified_Netlist-to-RTL_Recovery_with_LLM_Agents|Verified Netlist-to-RTL Recovery with LLM Agents]]

![[assets/2611.25324_first_page.png|800]]

- **arXiv**: [2611.25324](https://arxiv.org/abs/2611.25324)
- **PDF**: https://arxiv.org/pdf/2611.25324
- **详细分析**: [[20_Research/Papers/大模型/Verified_Netlist-to-RTL_Recovery_with_LLM_Agents|Verified Netlist-to-RTL Recovery with LLM Agents]]
- **作者**: Ahmet Efe, Recep Bugra Uludag, Ulya R. Karpuzcu
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Verified Netlist-to-RTL Recovery with LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Gate-level netlists circulate among IP integrators and foundries and can be extracted from chips. Reverse engineering them into readable register-transfer-level (RTL) code would help an adversary understand and modify a design, but remains difficult because word-level operations are scattered across many gates. Large language models (LLMs) can write and optimize RTL, but often fail to recover it from a whole netlist. We propose LOCA (LOgic Cone Attack), an LLM-based attack that divides an anonymized netlist into logic cones, has parallel agents rewrite them, and assembles compact RTL. Each cone contains the complete next-state logic of a group of related registers, giving an agent a small, meaningful task. Of five partitioning methods tested, only grouped cones lead to recovery. LOCA keeps only RTL proven equivalent to the netlist and measures its quality by compression. Function-preserving obfuscation does not stop LOCA on the tested designs, whereas unknown keys or hidden cell functions prevent it from proving recovery of the original design. Across 21 model-design pairs, LOCA recovers 17, versus 6 with whole-netlist prompting. Per-run recovery across models rises from 5% to 74%, at a median cost below one dollar with a low-cost model.

</details>

---
