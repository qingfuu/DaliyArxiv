# cs.CL | Computation and Language | 2026-11-20

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/具身智能/AgentRoboCritic_Understanding_the_Capability_of_Frontier_Agents_on_Direct_Robot_Control|AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control]]

![[assets/2611.26613_figure.png|800]]

- **arXiv**: [2611.26613](https://arxiv.org/abs/2611.26613)
- **PDF**: https://arxiv.org/pdf/2611.26613
- **详细分析**: [[20_Research/Papers/具身智能/AgentRoboCritic_Understanding_the_Capability_of_Frontier_Agents_on_Direct_Robot_Control|AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control]]
- **作者**: Yiyang Du, Yuxuan Kuang, Qitao Zhao, Yixuan Wang, Zhanqiu Guo, Yi Xu, Xin Li, Wenbin He, Liu Ren, Chenyan Xiong
- **cs 子类**: cs.CL, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.45（加权：具身智能 0.6，大模型 0.75，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control》归入 机器人、大模型、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FailBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succeed nor where they fail. In this paper, we present a systematic action-level analysis of frontier agents on direct robot control across 12 manipulation benchmarks. We introduce AgentRoboCritic, an intent-grounded critique framework in which the policy agent states a local intent alongside each action, and a critic evaluates the action's outcome and failure mode against this intent. Our action-level analysis demonstrates the promising capabilities of frontier agents on direct robot control, including closed-loop recovery from local execution failures, reliable semantic grounding across diverse scenes, and strong zero-shot manipulation without task-specific adaptation. It also identifies their current limitations, including task-relevant physical execution bottlenecks such as grasping and alignment, and uneven recovery across failure modes. Finally, we validate our critic on a 400-action human-annotated benchmark and release a dataset of 12,844 annotated actions alongside a fine-tuned open-source critic, Muse-Glimmer-30B, whose failure-mode accuracy rises from 32.58% to 74.24%, enabling low-cost action-level analysis.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Error_Detection_in_Chest_X-ray_Reports_A_Large_Language_Model_Reading_Image_Evidence|Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence]]

![[assets/2611.26492_first_page.png|800]]

- **arXiv**: [2611.26492](https://arxiv.org/abs/2611.26492)
- **PDF**: https://arxiv.org/pdf/2611.26492
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Error_Detection_in_Chest_X-ray_Reports_A_Large_Language_Model_Reading_Image_Evidence|Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence]]
- **作者**: Yanda Cheng, Bo Wen, Yuhao Lu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Multimodal Error Detection in Chest X-ray Reports: A Large Language Model Reading Image Evidence》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DenseNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rad-Linter checks chest X-ray reports against image-derived evidence to flag potential errors for review. A pretrained image classifier supplies scores for nine pathologies, and a 1.5B-parameter language model, fine-tuned with LoRA on 1,816 examples, checks their consistency with the report. We compare it with a keyword-and-negation rule baseline given the same reports and scores. Evaluation uses controlled report-score pairings from OpenI, with consistency labels derived from automatic report labels and score thresholds. Each counterfactual quad crosses two real reports with two real score vectors from other patients, creating two consistent and two inconsistent pairs. Every report and score vector occurs in both conditions, so either input alone permits only 50% accuracy. On 131 quads, Rad-Linter achieves 98.5% pair accuracy versus 80.5% for the rule baseline, and classifies all four pairs correctly in 94.4% of quads versus 56.5%. The checkers perform similarly on omission items, including unmentioned and negated findings; larger differences occur on the remaining item types, which require interpreting how findings are described. The same language model without fine-tuning remains near 50% accuracy. On a second set of 181 quads that also includes reports on which the automatic labelers disagree, pair accuracy is 93.4% versus 75.3%. These controlled results show that, given the same image-derived scores, a trained language model detects report-score inconsistencies more accurately than the tested rule baseline, with the advantage concentrated in interpreting how findings are worded.

</details>

---
