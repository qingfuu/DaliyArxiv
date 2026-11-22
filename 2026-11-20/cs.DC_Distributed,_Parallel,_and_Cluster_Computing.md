# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-20

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Held_While_Waiting_What_LLM_Agent_Sessions_Reserve_on_Serverless_and_Agent_Runtimes|Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes]]

![[assets/2611.26480_first_page.png|800]]

- **arXiv**: [2611.26480](https://arxiv.org/abs/2611.26480)
- **PDF**: https://arxiv.org/pdf/2611.26480
- **详细分析**: [[20_Research/Papers/大模型/Held_While_Waiting_What_LLM_Agent_Sessions_Reserve_on_Serverless_and_Agent_Runtimes|Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes]]
- **作者**: Mekhala Hithyshini Sreenivasa
- **cs 子类**: cs.DC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents spend nearly all their time waiting for the model. On Amazon Bedrock AgentCore, our agents waited a median of 2.7 seconds for each model reply, then computed for an estimated 5 to 40 milliseconds. AgentCore does not charge for CPU during the wait. But it reserves a separate environment, a virtual machine with its own memory, for every conversation, and keeps it reserved until the conversation is closed. So 1,000 conversations reserve 1,000 environments to do the work of 2 to 15 processor cores. A service runs out of environments long before it runs out of processing power. The shortage has two causes, and each has a fix. An environment stays reserved after its conversation ends: in the customer-service benchmark we ran, a conversation lasts 33 seconds on average, but its environment is held for 15 minutes more unless the client closes it. And an environment serves only one conversation, which is mostly waiting: in our simulation, 64 conversations sharing one environment need 59 times fewer environments, and 99 of every 100 replies are delayed by at most 40 milliseconds. The milliseconds are an estimate because they are hard to measure: a stubbed model, a timer around the model call, and steps run back to back each gave a plausible number that was too low. We show how to avoid all three. Of the two fixes, closing needs only the client. Sharing needs the platform, and of the agent runtimes we surveyed only one allows it, in part. They keep conversations apart because an agent runs tools, and sometimes code, chosen by a model. The open problem is to keep them apart without reserving an environment for each while it waits.

</details>

---
