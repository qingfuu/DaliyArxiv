# cs.LG | Machine Learning | 2026-07-07

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/大模型/CompactionRL_Reinforcement_Learning_with_Context_Compaction_for_Long-Horizon_Agents|CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents]]

![[assets/2607.05378_figure.png|800]]

- **arXiv**: [2607.05378](https://arxiv.org/abs/2607.05378)
- **PDF**: https://arxiv.org/pdf/2607.05378
- **详细分析**: [[20_Research/Papers/大模型/CompactionRL_Reinforcement_Learning_with_Context_Compaction_for_Long-Horizon_Agents|CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents]]
- **作者**: Yujiang Li, Zhenyu Hou, Yi Jing, Jie Tang, Yuxiao Dong
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CompactionRL, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon agentic LLMs are increasingly limited by finite context windows, as extended interaction trajectories can exceed the maximum context length before a task is completed. Context compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement learning remains underexplored. We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs with context compaction. Our approach jointly optimizes task execution and summary generation with token-level loss normalization and cross-trajectory generalized advantage estimation. This design enables the LLM agents to learn from compacted long-horizon trajectories. We train CompactionRL on top of open models and observe consistent performance gains on agentic coding tasks. CompactionRL enables the open GLM-4.5-Air model (106B-A30B) to achieve Pass@1 scores of 66.8% on SWE-bench Verified and 24.5% on Terminal-Bench 2.0, with absolute gains of 7.0 and 3.1 points, respectively. Built upon GLM-4.7-Flash (30B-A3B), CompactionRL improves Pass@1 by 5.5 and 6.8 points, reaching 56.0% on SWE-bench Verified and 20.2% on Terminal-Bench 2.0, respectively. CompactionRL is thus deployed in the RL pipeline for training the open GLM-5.2 model (750B-A40B).

</details>

---

### [[20_Research/Papers/强化学习/RL-Ballast_Ship_Ballast_Water_Path_Planning_and_Clog_Prediction_via_Reinforcement_Learning|RL-Ballast: Ship Ballast Water Path Planning and Clog Prediction via Reinforcement Learning]]

![[assets/2607.04906_first_page.png|800]]

- **arXiv**: [2607.04906](https://arxiv.org/abs/2607.04906)
- **PDF**: https://arxiv.org/pdf/2607.04906
- **详细分析**: [[20_Research/Papers/强化学习/RL-Ballast_Ship_Ballast_Water_Path_Planning_and_Clog_Prediction_via_Reinforcement_Learning|RL-Ballast: Ship Ballast Water Path Planning and Clog Prediction via Reinforcement Learning]]
- **作者**: Ming-Kuan Lin, Yi-Chung Lai, Ming-Hsin Chiang, Tsung-Wei Pan, Jung-Hua Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型, 大模型
- **相关性评分**: 2.42（加权：大模型 0.1，强化学习 1.36，世界模型 0.16，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RL-Ballast: Ship Ballast Water Path Planning and Clog Prediction via Reinforcement Learning》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Under the Shipping 4.0 paradigm, autonomous and reduced-crew vessels require intelligent internal systems to maintain operational safety and structural stability. Ballast-water control is essential for ship trim and integrity, but conventional rule-based or manual approaches have limited adaptability to hydraulic anomalies such as valve failures and pipe blockages, and often depend on dense pressure or flow sensors for diagnosis. To address these limitations, this paper proposes RL-Ballast, a graph-based deep reinforcement learning framework for adaptive ballast-water path planning and sensor-frugal blockage candidate scoring. The valve-permutation problem is transformed into 54 feasible fluid-transfer routes generated using graph theory and depth-first search. The partially observable ballast environment is approximated with frame-stacked tank levels and action outcomes, allowing the agent to infer hidden blockage effects without explicitly modeling a high-dimensional POMDP. During deterministic inference, episode-level failed-action memory and dynamic action masking prevent repeated ineffective actions and support immediate rerouting. Failed transfer histories are further accumulated to rank suspicious valves or pipe segments without dense instrumentation. Monte Carlo simulations show that RL-Ballast completes all unexpected single-blockage scenarios and reduces average decision steps from 61.0 to 41.5 compared with a Dijkstra rule-based baseline. For diagnostic support, the failure-history scoring scheme achieves a 100% Top-3 hit rate, a 66.7% strict Top-1 hit rate, and an 83.3% Top-1 tie-hit rate under serially indistinguishable blockage conditions. These results suggest that RL-Ballast enables adaptive rerouting and maintenance-oriented blockage diagnosis under limited sensing conditions.

</details>

---

### [[20_Research/Papers/世界模型/Learning_Task-Sufficient_World_Models_by_Synergizing_Agentic_Exploration_and_Structured_Modeling|Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling]]

![[assets/2607.04409_first_page.png|800]]

- **arXiv**: [2607.04409](https://arxiv.org/abs/2607.04409)
- **PDF**: https://arxiv.org/pdf/2607.04409
- **详细分析**: [[20_Research/Papers/世界模型/Learning_Task-Sufficient_World_Models_by_Synergizing_Agentic_Exploration_and_Structured_Modeling|Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling]]
- **作者**: Fan Feng, Yujia Zheng, Minghao Fu, Yongqiang Chen, Guangyi Chen, Kevin Murphy, Biwei Huang, Kun Zhang
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 机器人, 强化学习
- **相关性评分**: 1.72（加权：大模型 0.2，强化学习 0.16，世界模型 1.16，机器人 0.2）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling》归入 世界模型、大模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning and planning in imagination using world models provides an effective paradigm for training agents for decision-making. However, existing approaches often rely on high-dimensional latent spaces or generic visual embeddings that retain many factors irrelevant to control, limiting efficiency and generalization across tasks. To this end, we study how agents can learn world models with representations that are task-specific, minimal, and sufficient for decision-making. We achieve this via a closed-loop synergy between the agent and the world model, in which structured world-model learning distills task-sufficient representations from informative interaction data. On the agent side, agents actively probe the environment to collect informative trajectories that expose task-relevant latent factors, guided by an adaptive curriculum. On the world-model side, we learn structured representations over observations to distill compact, task-sufficient latent states from the collected interaction data. This synergy enables the empirical recovery of task-sufficient latent representations that capture all control-relevant factors. Leveraging these representations, the resulting policies achieve improved sample efficiency and generalization, including generalization across skills, object-skill compositions, and previously unseen tasks on standard continuous-control and robotic-manipulation benchmarks.

</details>

---

### [[20_Research/Papers/大模型/RL_Forgets!_Towards_Continual_Policy_Optimization|RL Forgets! Towards Continual Policy Optimization]]

![[assets/2607.04364_figure.png|800]]

- **arXiv**: [2607.04364](https://arxiv.org/abs/2607.04364)
- **PDF**: https://arxiv.org/pdf/2607.04364
- **详细分析**: [[20_Research/Papers/大模型/RL_Forgets!_Towards_Continual_Policy_Optimization|RL Forgets! Towards Continual Policy Optimization]]
- **作者**: Mao-Lin Luo, Zhe-Xu Wang, Zi-Hao Zhou, Bo Ye, Jian Zhao, Min-Ling Zhang, Tong Wei
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《RL Forgets! Towards Continual Policy Optimization》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MedBookVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual post-training is becoming a central paradigm for adapting vision-language models to evolving tasks. Recent work has increasingly favored reinforcement learning over supervised fine-tuning, driven by the belief that reinforcement learning is inherently less prone to forgetting. However, the belief remains insufficiently validated, as existing evidence is largely drawn from outdated or homogeneous benchmarks. To revisit this assumption, we introduce MRCL, a Multimodal Reasoning Continual Learning benchmark built from diverse and recently released multimodal datasets. Experiments on MRCL show that reinforcement learning can still suffer from severe catastrophic forgetting during continual post-training. To address this challenge, we propose Continual Policy Optimization (CPO), a replay-free framework grounded in the prior-task behavioral KL objective. CPO uses a theoretically justified parameter-movement regularization to limit policy drift on previous tasks. Extensive experiments across multiple model scales demonstrate that CPO consistently reduces forgetting while preserving, and in some cases improving, pretrained model capabilities. On Qwen3-VL-8B, CPO reduces forgetting by 13.7\% and improves pretrained capability by 7.0\%. The implementation code is available at https://github.com/MaolinLuo/CPO.

</details>

---

### [[20_Research/Papers/大模型/On_the_effectiveness_of_reward_functions_in_reinforcement_learning_for_confidence_calibration_of_large_language_models|On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models]]

![[assets/2607.04332_figure.png|800]]

- **arXiv**: [2607.04332](https://arxiv.org/abs/2607.04332)
- **PDF**: https://arxiv.org/pdf/2607.04332
- **详细分析**: [[20_Research/Papers/大模型/On_the_effectiveness_of_reward_functions_in_reinforcement_learning_for_confidence_calibration_of_large_language_models|On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models]]
- **作者**: Chee Heng Tan, Zhuoyi Lin, Mehul Motani, Wee Sun Lee
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《On the effectiveness of reward functions in reinforcement learning for confidence calibration of large language models》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we consider the setting where large language models (LLMs) are trained using reinforcement learning (RL) to simultaneously improve reasoning accuracy and verbalize its confidence. Our reward scheme uses two functions for rewarding confidence verbalized by the LLM: one when the LLM is correct and a different one when the LLM is incorrect. With a poorly designed reward scheme, the LLM may be incentivized to answer incorrectly so that it can be confident that its answer is indeed incorrect, a phenomenon that we call confidence reward hacking. We propose the concept of non-hackable confidence reward schemes and define a spectrum of such reward schemes for RL confidence calibration training in LLMs. We demonstrate that selective confidence reward hacking can occur in practical datasets with reward schemes that are not designed to be non-hackable. We also demonstrate that the reward scheme with the best calibration to accuracy tradeoff depends on the dataset and the application, and propose using the reward scheme as a hyperparameter to optimize the tradeoffs in accordance to what is important for the application. The code of our experiments is available in https://anonymous.4open.science/r/rl-confidence-calibration-9ED4/README.md.

</details>

---

### [[20_Research/Papers/具身智能/XS-VLA_Coupling_Coarse-grained_Spatial_Distillation_with_Latent_Flow_Matching_for_Lightweight_Robotic_Control|XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control]]

![[assets/2607.04171_figure.png|800]]

- **arXiv**: [2607.04171](https://arxiv.org/abs/2607.04171)
- **PDF**: https://arxiv.org/pdf/2607.04171
- **详细分析**: [[20_Research/Papers/具身智能/XS-VLA_Coupling_Coarse-grained_Spatial_Distillation_with_Latent_Flow_Matching_for_Lightweight_Robotic_Control|XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control]]
- **作者**: Lei Iok Tong, Qingchen Xie, Wei Huang, Ying Jie Yap, Yujie Zhang, Qianzhi Li, Xiaolong Liu, Zhidong Deng
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FPC-VLA, OpenVLA, Real-World, SmolVLA, SpatialVLA, TraceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Vision-Language Models (LVLMs) have shown strong multimodal understanding and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability. Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to highly diverse behaviors. To address these limitations, we propose XS-VLA, a two-stage framework for efficient and spatially grounded robotic manipulation. First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B backbone by fine-tuning on curated coarse-grained spatial descriptions, turning the lightweight model into a spatially grounded engine. Second, we use this enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic controllers, our policy combines a Conditional Variational Autoencoder (CVAE) with Flow Matching dynamics to model complex multimodal action distributions. On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among models with fewer than 0.5B parameters. It improves average success rates by up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over the SmolVLA 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show that spatial tuning and generative latent flow control substantially improve lightweight VLA performance, delivering a 3.2 times speedup in mission execution over the previous lightweight flow matching policy.

</details>

---

### [[20_Research/Papers/具身智能/ACE_Agentic_Control_for_Embodied_Manipulation_via_Zero-shot_Workflow_Reasoning|ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning]]

![[assets/2607.04162_figure.png|800]]

- **arXiv**: [2607.04162](https://arxiv.org/abs/2607.04162)
- **PDF**: https://arxiv.org/pdf/2607.04162
- **详细分析**: [[20_Research/Papers/具身智能/ACE_Agentic_Control_for_Embodied_Manipulation_via_Zero-shot_Workflow_Reasoning|ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning]]
- **作者**: Iok Tong Lei, QianZhi Li, Ying Jie Yap, Yujie Zhang, Rui Zhong, Haichao Gui, Xiaolong Liu, Zhidong Deng
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-ended tabletop manipulation requires agents to not only understand natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills: a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning and physical control, the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask specifies the target object and destination, is tracked over time, exposed for human verification, and ultimately passed to a task-agnostic downstream policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale memory. After an action is executed, the system automatically verifies whether the intended sub-goal succeeded, using the outcome to advance, retry, repair, or replan. This enables online adaptation to user corrections, scene changes, and physical failures. We evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation formation with number cubes and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization on novel semantic constraints and randomized tabletop scenes without task-specific retraining. Specifically, while standard end-to-end baselines struggle to complete these logically demanding tasks, ACE achieves a 50% success rate in equation formation and a 70% success rate in constraint retrieval. This contrast demonstrates that explicit workflow reasoning and mask-mediated control offer a robust, practical route toward adaptable robotic manipulation.

</details>

---

### [[20_Research/Papers/强化学习/CDCP_Conditional_Diffusion_Model_with_Contextual_Prompts_for_Multi-task_Offline_Safe_Reinforcement_Learning|CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning]]

![[assets/2607.03903_figure.png|800]]

- **arXiv**: [2607.03903](https://arxiv.org/abs/2607.03903)
- **PDF**: https://arxiv.org/pdf/2607.03903
- **详细分析**: [[20_Research/Papers/强化学习/CDCP_Conditional_Diffusion_Model_with_Contextual_Prompts_for_Multi-task_Offline_Safe_Reinforcement_Learning|CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning]]
- **作者**: Jiayi Guan, Tianle Zhang, Li Shen, Ruiqi Zhang, Ao Zhou, Lusong Li, Guai Chen, Mengjie Li, Alois Knoll, Xiaodong He, Changjun Jiang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《CDCP: Conditional Diffusion Model with Contextual Prompts for Multi-task Offline Safe Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-task offline safe reinforcement learning (RL) promises to learn a shared optimal safe policy from offline data across multiple tasks. This paradigm provides an effective means for the widespread application of RL in multi-task scenarios with high risk and interaction costs. However, the triple challenges of multi-tasking, safety constraints, and out-of-distribution (OOD) actions pose a significant hurdle for existing methods to ensure safety while maximizing reward returns. In this work, we propose a Conditional Diffusion model with Contextual Prompts (CDCP) to address these challenges. Concretely, we first rethink the requirements and challenges in current multi-task decision-making and control scenarios and establish the objectives of multi-task offline safe RL. Subsequently, we transform the multi-task constrained optimization problem into a conditional generation problem using the diffusion model. Based on this, we design a classifier-free guided cost-constraint strategy to provide flexible cost constraints and eliminate extrapolation errors from OOD actions via supervised learning. Additionally, we introduce a novel contextual prompting method to enhance multi-task representation accuracy and adaptability to unseen tasks. A gradient loss synchronization strategy is also introduced to eliminate gradient interference, improving training stability. Finally, extensive experiments demonstrate that the CDCP algorithm exhibits higher performance and safety in multi-task scenarios than the current state-of-the-art baseline methods. It meets different cost constraints without further training, providing a more flexible cost-constraint solution for the multi-task safe RL.

</details>

---

### [[20_Research/Papers/具身智能/ADP_Adversarial_Dynamics_Priors_for_Physically_Grounded_Humanoid_Locomotion|ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion]]

![[assets/2607.03454_figure.jpg|800]]

- **arXiv**: [2607.03454](https://arxiv.org/abs/2607.03454)
- **PDF**: https://arxiv.org/pdf/2607.03454
- **详细分析**: [[20_Research/Papers/具身智能/ADP_Adversarial_Dynamics_Priors_for_Physically_Grounded_Humanoid_Locomotion|ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion]]
- **作者**: Seokju Lee, Jeongtae Lee, Jeonghyeok Lim, Jeonguk Kang, Byungwook Lee, Seungho Han, Keun Ha Choi, Dongil Park, Kyung-Soo Kim
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《ADP: Adversarial Dynamics Priors for Physically Grounded Humanoid Locomotion》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose Adversarial Dynamics Priors (ADP) for perturbation-resilient humanoid locomotion control. Existing motion prior-based methods induce natural motion styles by imitating kinematic motion features, but they do not directly regularize dynamics features, such as CoM motion, centroidal momentum, contact forces, and contact states. To address this limitation, we replace kinematic motion-style feature with selected dynamics features extracted from locomotion trajectories as the target of adversarial regularization.To this end, we use trajectory optimization to construct a reference dataset and train a discriminator to evaluate whether policy-induced temporal windows are consistent with the resulting reference distribution.Without explicit motion tracking, ADP encourages policy rollouts to remain close to the reference support, even after perturbations. Experimental results show that, compared with AMP, the strongest baseline in our evaluation, ADP improves the $80\%$-success impulse threshold ($J_{80}$) by $16.7\%$, while reducing direction-averaged recovery time and velocity tracking error by $47.9\%$ and $35.4\%$, respectively.

</details>

---

### [[20_Research/Papers/世界模型/Reduced-Order_Models_The_Mother_of_World_Models|Reduced-Order Models: The Mother of World Models]]

![[assets/2607.03198_first_page.png|800]]

- **arXiv**: [2607.03198](https://arxiv.org/abs/2607.03198)
- **PDF**: https://arxiv.org/pdf/2607.03198
- **详细分析**: [[20_Research/Papers/世界模型/Reduced-Order_Models_The_Mother_of_World_Models|Reduced-Order Models: The Mother of World Models]]
- **作者**: Rajat Ghosh
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.52（加权：强化学习 0.16，世界模型 1.36）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Reduced-Order Models: The Mother of World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models -- compressed latent representations of an environment that support action-conditioned prediction and planning -- are typically presented as a product of modern self-supervised learning. This paper argues that the functional anatomy of a world model was independently developed, deployed, and formally analyzed decades earlier in the model-order-reduction (MOR) and control literature, under different names and for a different purpose: the real-time operation of physical systems. We trace the anatomy across three communities. Low-dimensional models of turbulence built on proper orthogonal decomposition (POD) supplied latent dynamics learned from data of a chaotic environment; eigenface methods in early computer vision supplied the encoder-decoder half, including a primitive runtime validity check; and measurement-based POD frameworks for facility thermal control assembled the complete loop -- POD coefficients as latent state, parametric dependence on actuator setpoints as action conditioning, modal reconstruction as decoding, and, critically, a priori analytical error bounds as a verification layer that certified when the model's predictions could be trusted in closed loop. We then examine what each tradition possesses that the other lacks: MOR contributes verification, physical grounding, and extreme data efficiency; learned world models contribute nonlinear representation, transferability, and horizon. We argue that the outstanding obstacle to deploying world models in systems that cannot fail -- power, thermal, process control -- is not predictive fidelity but verifiability, and we outline a research agenda for physics-grounded, verifiable world models that unifies the two lineages.

</details>

---

### [[20_Research/Papers/强化学习/Anticipatory_Reinforcement_Learning_for_Trajectory_Tracking|Anticipatory Reinforcement Learning for Trajectory Tracking]]

![[assets/2607.03132_figure.png|800]]

- **arXiv**: [2607.03132](https://arxiv.org/abs/2607.03132)
- **PDF**: https://arxiv.org/pdf/2607.03132
- **详细分析**: [[20_Research/Papers/强化学习/Anticipatory_Reinforcement_Learning_for_Trajectory_Tracking|Anticipatory Reinforcement Learning for Trajectory Tracking]]
- **作者**: Georg Schäfer, Jakob Rehrl, Stefan Huber, Simon Hirlaender
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.42（加权：具身智能 0.6，强化学习 1.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: RL

#### 研究背景与动机

《Anticipatory Reinforcement Learning for Trajectory Tracking》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) in industrial control often suffers from lag and overshoot due to purely reactive control based on the current tracking error. To achieve anticipatory control without high computational overhead, we introduce a predictive formulation that augments the DRL state space with target velocities and future reference horizons. Evaluating eight configurations using proximal policy optimization (PPO) on a 1-degree-of-freedom (1-DoF) helicopter testbed, simulation results showed a 9-fold error reduction, lowering the mean absolute deviation from 2.73° to 0.31°. However, zero-shot transfer to physical hardware revealed a sim-to-real gap. Interestingly, a simpler configuration using a single, further look-ahead horizon matched the real-world top performance of the most complex model (1.11°). Overall, evaluating various combinations of prediction horizons and target velocities demonstrated that highly granular predictive data is not necessarily required for physical transfer.

</details>

---

### [[20_Research/Papers/强化学习/Integrating_Physics-Informed_Neural_Networks_for_Safe_Reinforcement_Learning_in_a_1-DoF_Helicopter_System|Integrating Physics-Informed Neural Networks for Safe Reinforcement Learning in a 1-DoF Helicopter System]]

![[assets/2607.03125_figure.png|800]]

- **arXiv**: [2607.03125](https://arxiv.org/abs/2607.03125)
- **PDF**: https://arxiv.org/pdf/2607.03125
- **详细分析**: [[20_Research/Papers/强化学习/Integrating_Physics-Informed_Neural_Networks_for_Safe_Reinforcement_Learning_in_a_1-DoF_Helicopter_System|Integrating Physics-Informed Neural Networks for Safe Reinforcement Learning in a 1-DoF Helicopter System]]
- **作者**: Georg Schäfer, Jakob Rehrl, Stefan Huber
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Integrating Physics-Informed Neural Networks for Safe Reinforcement Learning in a 1-DoF Helicopter System》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) offers powerful control for industrial cyber-physical systems (ICPSs), but its "black-box" exploration risks violating strict hardware safety limits. Typically, these constraints are managed through complex reward shaping. In this work-in-progress paper, we embed a differentiable physics model directly into the proximal policy optimization (PPO) actor loss function. By simulating short-horizon future trajectories during training, the policy is penalized for anticipated safety violations independent of the task-reward signal. Evaluated on a simulated 1-degree-of-freedom helicopter testbed with strict pitch constraints, our physics-informed soft regularizations substantially reduce constraint violations while maintaining reliable target tracking.

</details>

---
