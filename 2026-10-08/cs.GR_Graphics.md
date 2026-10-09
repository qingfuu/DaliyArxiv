# cs.GR | Graphics | 2026-10-08

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/End-to-End_Autonomous_Generation_of_Human_Assembly_Plans|End-to-End Autonomous Generation of Human Assembly Plans]]

![[assets/2610.09781_first_page.png|800]]

- **arXiv**: [2610.09781](https://arxiv.org/abs/2610.09781)
- **PDF**: https://arxiv.org/pdf/2610.09781
- **详细分析**: [[20_Research/Papers/大模型/End-to-End_Autonomous_Generation_of_Human_Assembly_Plans|End-to-End Autonomous Generation of Human Assembly Plans]]
- **作者**: Faustin Arion von Arx, Millicent Schlafly, Mark D. Fuge
- **cs 子类**: cs.GR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《End-to-End Autonomous Generation of Human Assembly Plans》归入 机器人、大模型、具身智能 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Turning a CAD design into an assembly plan is still largely done by hand, requiring engineers to reason about geometric feasibility, tool access, stability, and the ergonomics of human assembly. In this work, we encode long-established design for assembly (DfA) principles into a contained, end-to-end approach for generating assembly plans. Our approach takes only a mesh assembly and produces either a step-by-step assembly manual or a structured failure report, requiring no joint metadata, fastener annotations, or additional information. Four major components of a manufacturing plan are addressed autonomously: an assembly tool list, the assembly sequence and subassemblies, an assembly manual, and design feedback for improving assemblability. For determining the sequence plan, we systematically disassemble the object in a physics simulator and apply a cost function that encodes DfA principles. Manual generation, tool labelling, and assembly feedback rely primarily on multimodal large language models. Compared with a baseline that always removes the outermost part first from Tian et al., DfA-aware sequence planning reduces simulated assembly time, measured with a robot-arm assembly-time proxy, by 35% on 136 assemblies of 5 to 30 parts. The correct tool is selected for 88.6% of assembly steps. A vision-language model judge compares the generated manuals against ablated variants, identifying which page elements carry the information a reader needs. The presented approach and open-source code are available for use by engineers or AI agents looking to rapidly accelerate the creation of manufacturing plans for a given product design.

</details>

---
