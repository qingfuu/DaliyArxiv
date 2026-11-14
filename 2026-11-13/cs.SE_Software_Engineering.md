# cs.SE | Software Engineering | 2026-11-13

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Where_LLM_Agents_Get_Stuck_Debugging_Databases_Access_More_Than_Reasoning|Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning]]

![[assets/2611.17304_first_page.png|800]]

- **arXiv**: [2611.17304](https://arxiv.org/abs/2611.17304)
- **PDF**: https://arxiv.org/pdf/2611.17304
- **详细分析**: [[20_Research/Papers/大模型/Where_LLM_Agents_Get_Stuck_Debugging_Databases_Access_More_Than_Reasoning|Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning]]
- **作者**: Gustavo Pinto
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Where LLM Agents Get Stuck Debugging Databases: Access More Than Reasoning》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) coding agents are increasingly asked not only to write code but to debug running systems from live runtime data. We report a field observation of one such agent (Claude Code) as it diagnosed eight database incidents in a production message-dispatch engine. In every incident whose root cause depended on runtime concurrency, the agent announced a cause, shipped a fix, and later walked it back, and each wrong guess cost a deploy-and-observe cycle. Mapping each incident to what the agent lacked, we find that access to production state was the most pervasive bottleneck. The missing access included live lock views, untruncated deadlock reports, read-only execution, and an explicit environment context. An access gap was present in all five concurrency-dependent incidents: alone in one, and in four combined with a reasoning error such as anchoring on an early cause, incomplete exploration of the configuration, or a misreading of the code's transaction semantics. The three incidents that did not depend on concurrency needed nothing beyond what the agent already had. Within the incidents, the agent's wrong hypotheses were consistent with the evidence it could see; they were not fabrications. We argue that the next step for production-debugging agents is a forensics layer that gives the agent the access it lacks inside existing security controls. Such a layer would combine a safe interrogation API, a lock-and-deadlock flight recorder, and a production replay harness.

</details>

---
