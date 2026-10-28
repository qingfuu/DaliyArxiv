# cs.SE | Software Engineering | 2026-10-26

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/StateMirror_Pre-Execution_Detection_of_Hallucinated_Tool_Calls_in_Coding_Agents|StateMirror: Pre-Execution Detection of Hallucinated Tool Calls in Coding Agents]]

![[assets/2610.32648_figure.png|800]]

- **arXiv**: [2610.32648](https://arxiv.org/abs/2610.32648)
- **PDF**: https://arxiv.org/pdf/2610.32648
- **详细分析**: [[20_Research/Papers/大模型/StateMirror_Pre-Execution_Detection_of_Hallucinated_Tool_Calls_in_Coding_Agents|StateMirror: Pre-Execution Detection of Hallucinated Tool Calls in Coding Agents]]
- **作者**: Shiwen Shan, Yintong Huo, Zhiying Wu, Yuxin Su
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《StateMirror: Pre-Execution Detection of Hallucinated Tool Calls in Coding Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based coding agents may propose invalid actions that are not applicable in the execution environment, such as accessing non-existent paths or missing packages. We term this mismatch hallucinated tool use. A preliminary study of 4,398 agent trajectories reveals that these hallucinations are pervasive and costly, requiring a median of 3 additional interaction steps and 22.4K tokens to recover. Existing frameworks rely on reactive, post-execution feedback, wasting runtime resources. Nevertheless, since an agent's execution environment is grounded in concrete codebase and harness components, many action prerequisites can be extracted and validated prior to execution. To this end, we introduce StateMirror, a lightweight pre-execution detector. StateMirror intercepts actions at the harness boundary, extracts state predicates via AST and command analysis, and deterministically validates them against the live repository. By pinpointing exact environment mismatches before execution, StateMirror preempts invalid actions and subsequent recovery cycles. Evaluation on 2,508 actions shows StateMirror achieves 0.940 precision and 0.817 F1 in detecting such hallucinations, surpassing the strongest LLM judge by 35.3% in F1 while reducing median detection latency from 17.73 s to 1.50 ms with zero token consumption. For practical mitigation, StateMirror's pre-execution feedback enables agents to rectify over 95% of hallucinated tool calls. During live mitigation on 79 tasks, StateMirror reduces agent execution time by 15.8% and token consumption by 11.8% while maintaining task resolution.

</details>

---

### [[20_Research/Papers/大模型/WaitLens_Temporal_VLM-Based_Adaptive_Waiting_for_Industrial_GUI_Testing_Agents|WaitLens: Temporal VLM-Based Adaptive Waiting for Industrial GUI Testing Agents]]

![[assets/2610.32482_figure.png|800]]

- **arXiv**: [2610.32482](https://arxiv.org/abs/2610.32482)
- **PDF**: https://arxiv.org/pdf/2610.32482
- **详细分析**: [[20_Research/Papers/大模型/WaitLens_Temporal_VLM-Based_Adaptive_Waiting_for_Industrial_GUI_Testing_Agents|WaitLens: Temporal VLM-Based Adaptive Waiting for Industrial GUI Testing Agents]]
- **作者**: Shika Ikeura, Xuan Wang, Ziyi Kuang, Jianping Xu, Chao Kang, Yongxiang Hu, Xiaoyu Wang, Juxing Yuan, Yangfan Zhou
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《WaitLens: Temporal VLM-Based Adaptive Waiting for Industrial GUI Testing Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Improving the efficiency of GUI testing agents is important for industrial deployment. Beyond LLM inference, fixed waiting between consecutive interactions introduces substantial overhead. Our industrial study reveals that fixed waiting accounts for 42.3% of the time within the sampled interaction intervals, comparable to the 54.8% spent on model calls. Moreover, 62.9% of the waiting time is spent after the GUI has already finished loading. Although prior studies have proposed adaptive waiting strategies, their reliance on app-specific data or platform-specific information limits their applicability across diverse industrial environments. To this end, we propose WaitLens, which fine-tunes a lightweight VLM on GUI loading trajectories annotated with waiting end times. We introduce temporal resampling to construct diverse training examples, enabling the model to learn varying GUI loading behaviors from temporal observations. Experiments show that WaitLens achieves 86.08% accuracy in deciding whether to keep waiting, compared with 54.13% for the backbone VLM. Our evaluation using recordings from Meituan's industrial testing pipeline shows that WaitLens reduces mean extra waiting after the interface is ready by 94.98% compared with a 20-second fixed wait.

</details>

---

### [[20_Research/Papers/大模型/From_Faulty_Claims_to_Incorrect_Patches_An_Empirical_Study_of_Task-Grounded_Reasoning_in_Coding_Agents|From Faulty Claims to Incorrect Patches: An Empirical Study of Task-Grounded Reasoning in Coding Agents]]

![[assets/2610.32338_figure.png|800]]

- **arXiv**: [2610.32338](https://arxiv.org/abs/2610.32338)
- **PDF**: https://arxiv.org/pdf/2610.32338
- **详细分析**: [[20_Research/Papers/大模型/From_Faulty_Claims_to_Incorrect_Patches_An_Empirical_Study_of_Task-Grounded_Reasoning_in_Coding_Agents|From Faulty Claims to Incorrect Patches: An Empirical Study of Task-Grounded Reasoning in Coding Agents]]
- **作者**: You Wang, Jinjun Huang, Zhonghao Jiang, Jialun Cao, Jiachi Chen, Zhongxin Liu
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Faulty Claims to Incorrect Patches: An Empirical Study of Task-Grounded Reasoning in Coding Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based coding agents increasingly resolve real-world software engineering tasks, yet still fail on many of them. Prior trajectory studies characterize these failures through task-agnostic patterns of agent behavior, such as repeated actions. However, an agent may follow a sound workflow yet act on a faulty understanding of the existing code, the task requirements, or a candidate fix. Reasoning models, which power most state-of-the-art coding agents, reveal this understanding in their native chain-of-thought (CoT), whose claims about the task can be checked against the facts. Yet it remains unclear how many such checkable claims the CoT contains, how many are faulty, and whether faulty claims actually cause incorrect patches. We present the first empirical study of such claims, which we term task-grounded reasoning, analyzing 400 trajectories of four open-weight reasoning models on SWE-bench Pro. We extract atomic claims from the CoT with an LLM, assess them against evidence gathered by an LLM agent, and manually trace the defects of incorrect patches back to faulty claims, confirming each link with a claim-corrected replay. Task-grounded reasoning covers only 18.5% of the CoT tokens, yet yields 191 atomic claims per trajectory, at least 9.6% of which are faulty. Faulty claims also occur in 96.7% of the resolved trajectories, so their mere presence is a weak signal of failure. Yet two thirds of the 188 incorrect patches trace back to faulty claims. Correcting such a claim makes the agent fix the linked defect in 89.0% of the cases, and correcting all such claims resolves 11.7% of the failed tasks. Our findings show that the CoT carries task-specific signals for diagnosing and repairing agent failures, but exploiting them requires pinpointing the few faulty claims that actually cause patch defects.

</details>

---
