# cs.SE | Software Engineering | 2026-10-21

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/InterWebCoder_Learning_Interactive_Webpage_Generation_from_Executable_Tests_via_Reinforcement_Learning|InterWebCoder: Learning Interactive Webpage Generation from Executable Tests via Reinforcement Learning]]

![[assets/2610.28610_figure.png|800]]

- **arXiv**: [2610.28610](https://arxiv.org/abs/2610.28610)
- **PDF**: https://arxiv.org/pdf/2610.28610
- **详细分析**: [[20_Research/Papers/大模型/InterWebCoder_Learning_Interactive_Webpage_Generation_from_Executable_Tests_via_Reinforcement_Learning|InterWebCoder: Learning Interactive Webpage Generation from Executable Tests via Reinforcement Learning]]
- **作者**: Jingyu Xiao, Dasen Dai, Yuxuan Wan, Jen-tse Huang, Yintong Huo, Hongyu Zhang, Michael R. Lyu
- **cs 子类**: cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《InterWebCoder: Learning Interactive Webpage Generation from Executable Tests via Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IWR-Bench, TDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive webpages underpin modern applications, but reproducing both their visual appearance and multi-step behavior remains challenging for multimodal large language models (MLLMs). Scalable training data must capture user actions, state transitions, and expected outcomes, while real-world webpage code is often entangled with irrelevant scripts and external dependencies. Moreover, existing GUI-agent-based verification provides slow and potentially unstable functional feedback. To address these challenges, we propose InterWebCoder, an efficient framework for interactive webpage code generation. InterWebCoder introduces a Test-Specification-Guided and Execution-Verified Data Synthesis pipeline that records real-world interaction trajectories and synthesizes self-contained webpage code with executable test scripts. A failureattributed repair mechanism uses runtime evidence to locate and iteratively fix errors in either the webpage code or test script. We then combine test-ID-weighted supervised fine-tuning with group-relative policy optimization, directly optimizing functional correctness and visual fidelity using test pass rates and state-level visual similarity. This replaces costly GUI-agent verification with fast, reproducible executable feedback. Our pipeline produces 1,736 verified samples from 2,058 tasks, achieving an 84.35% synthesis success rate. On IWR-Bench and Vision2Web, InterWebCoder achieves final scores of 48.54 and 48.42 with a 9B backbone, outperforming 30B-level models and Gemini-3.7-Flash while remaining competitive with Claude-Sonnet-5. It reduces reward-computation latency by over 97%, eliminates external MLLM verification costs, and accelerates end-to-end training by up to 1.4x.

</details>

---

### [[20_Research/Papers/大模型/AgenTest_Mining_Business_Rules_to_Test_LLM_Agents_for_Business_Logic_Bugs|AgenTest: Mining Business Rules to Test LLM Agents for Business Logic Bugs]]

![[assets/2610.28116_figure.png|800]]

- **arXiv**: [2610.28116](https://arxiv.org/abs/2610.28116)
- **PDF**: https://arxiv.org/pdf/2610.28116
- **详细分析**: [[20_Research/Papers/大模型/AgenTest_Mining_Business_Rules_to_Test_LLM_Agents_for_Business_Logic_Bugs|AgenTest: Mining Business Rules to Test LLM Agents for Business Logic Bugs]]
- **作者**: Lili Quan, Longtian Wang, Yuelin Wang, Mingfei Cheng, Chao Shen, Sen Chen, Xiaofei Xie
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《AgenTest: Mining Business Rules to Test LLM Agents for Business Logic Bugs》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly execute business operations through tools and interact directly with application data and services. Beyond completing user requests, these agents must obey domain-specific business rules that constrain when actions are permitted and what data or resources may be affected. Violating such rules can lead to business logic bugs, even when a task appears successful. Detecting these bugs is difficult because the rules are rarely available as explicit, testable specifications. They are distributed across system prompts and tool definitions, while others remain implicit in domain knowledge. Existing agent testing approaches typically evaluate task success, predefined policies, or known attack scenarios. This limits their ability to systematically uncover previously unspecified business-rule violations. We present AgenTest, which mines business rules from system prompts, tool definitions, and domain knowledge, refines them into Given-When-Then specifications, and systematically tests each specification. For each extracted specification, AgenTest instantiates its Given conditions by constructing a satisfying environment state and simulated user, exercises the agent through multi-turn interactions, and checks its Then conditions over messages, tool calls, and state changes using a hybrid oracle. On the airline, retail, and telecom agents of tau2-bench with two underlying models, AgenTest produces 551 refined specifications, and detects violations of 89 and 121 distinct specifications, respectively -- 3.4X and 2.5X as many as all baselines combined. Only AgenTest detects cases where an agent improperly accesses or modifies another user's data. Moreover, about 60% of bug-triggering runs cannot be detected from the final state alone, highlighting the need to check the full interaction against explicit business rules.

</details>

---
