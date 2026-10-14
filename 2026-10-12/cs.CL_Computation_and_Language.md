# cs.CL | Computation and Language | 2026-10-12

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/SOAR_Source-Aware_Reinforcement_Learning_with_Precise_Credit_Assignment_for_Search_Agents|SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents]]

![[assets/2610.13157_first_page.png|800]]

- **arXiv**: [2610.13157](https://arxiv.org/abs/2610.13157)
- **PDF**: https://arxiv.org/pdf/2610.13157
- **详细分析**: [[20_Research/Papers/强化学习/SOAR_Source-Aware_Reinforcement_Learning_with_Precise_Credit_Assignment_for_Search_Agents|SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents]]
- **作者**: Shengze Huang, Zihao Tang, Jinluan Yang, Xin Yu, Zhenghao Lin, Xiao Liu, Zengxuan Wen, Yeyun Gong, Haizhen Huang, Weiwei Deng, Feng Sun, Qi Zhang...
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.55，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for Search Agents》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) for search agents often suffers from evidence fabrication, a failure mode where agents bypass external information ($E_{ext}$) and fabricate an incorrect answer. We argue that this fabrication arises from an over-reliance on unreliable internal knowledge ($E_{int}$) as shortcuts due to the inherent opacity of reasoning trajectories. To address this, we propose SOAR (SOurce-Aware Reinforcement learning), a paradigm that transforms monolithic reasoning into source-explicit trajectories. SOAR (i) disentangles $E_{ext}$ and $E_{int}$ into parallel, observable streams via a Source-Aware Workflow, and (ii) incorporates Source-Consistent Reward to guide the policy evolution. By making information-source attribution explicit, SOAR enables precise credit assignment between different knowledge streams. Evaluations show that SOAR outperforms baselines on 3B and 7B backbones by 7.3% and 5.4%, while reducing evidence fabrication by 74.8%. These confirm that SOAR significantly improves performance on knowledge-intensive benchmarks while effectively mitigating evidence fabrication, fostering more faithful and grounded reasoning with enhanced robustness.

</details>

---

### [[20_Research/Papers/强化学习/MADS_Multi-Agent_Dialog_Simulation_for_Robust_Conversational_Agents|MADS: Multi-Agent Dialog Simulation for Robust Conversational Agents]]

![[assets/2610.12757_figure.png|800]]

- **arXiv**: [2610.12757](https://arxiv.org/abs/2610.12757)
- **PDF**: https://arxiv.org/pdf/2610.12757
- **详细分析**: [[20_Research/Papers/强化学习/MADS_Multi-Agent_Dialog_Simulation_for_Robust_Conversational_Agents|MADS: Multi-Agent Dialog Simulation for Robust Conversational Agents]]
- **作者**: Arkajyoti Chakraborty, Adam Zernik, Ishika Kulkarni, Mudit Arora, Hugo Lin, Justin Chiu, Alessandro Di Bari, Neha Gupta, Andreas Stolcke
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.15（加权：大模型 0.95，强化学习 0.2）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《MADS: Multi-Agent Dialog Simulation for Robust Conversational Agents》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ComplexFuncBench, MADS-Bench, ToolBench, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task-oriented conversational agents remain fragile under realistic conditions, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present MADS (Multi-Agent Dialog Simulation), a synthetic data generation pipeline that produces structured, diverse dialogue trajectories. We inject adversarial conversation, producing validated conversation trajectories that capture realistic, unhappy paths. Using MADS, we construct MADS-Bench: a benchmark spanning six domains, 55 personas, and 1095 conversations, with approximately 66% of conversations containing failure-prone conversation scenarios. We evaluate the robustness of the trained models using a two-stage training approach that combines supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR).

</details>

---
