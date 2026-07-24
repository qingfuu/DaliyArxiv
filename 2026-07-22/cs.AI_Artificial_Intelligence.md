# cs.AI | Artificial Intelligence | 2026-07-22

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/强化学习/Copy_Less,_Ground_More_Overcoming_Repetitive_Copying_in_Long-Context_Reasoning_via_Evidence-Aware_Reinforcement_Learning|Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning]]

![[assets/2607.19345_figure.png|800]]

- **arXiv**: [2607.19345](https://arxiv.org/abs/2607.19345)
- **PDF**: https://arxiv.org/pdf/2607.19345
- **详细分析**: [[20_Research/Papers/强化学习/Copy_Less,_Ground_More_Overcoming_Repetitive_Copying_in_Long-Context_Reasoning_via_Evidence-Aware_Reinforcement_Learning|Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning]]
- **作者**: Lizhe Fang, Weizhou Shen, Tianyi Tang, Yisen Wang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.6（加权：强化学习 0.6）
- **关联关键词**: RL

#### 研究背景与动机

《Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GoLongRL, LongBench, LoongRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models that generate step-by-step reasoning traces have achieved strong performance on complex tasks, and extending them to long-context settings has emerged as an important frontier. However, we identify a critical failure mode in this regime: \emph{repetitive copying}, where models extensively copy text from the input into their reasoning traces rather than productively solving the problem. We show that this behavior is pervasive across frontier long-context LLMs and intensifies with context length. By separating each prompt into task-relevant key evidence and irrelevant distractor context, we further show that the root cause is insufficient grounding: models copy from the prompt indiscriminately, and those that fail to focus on key evidence are far more likely to answer incorrectly. Motivated by this diagnosis, we propose GEAR (Grounding Evidence-Aware Reward), a reward shaping method that augments the accuracy signal with a grounding reward for overlap with key evidence and a distractor penalty for overlap with irrelevant context. To enable GEAR on natural-language data, we develop an automated pipeline that constructs evidence-annotated training data from arbitrary documents. We validate GEAR across multiple model scales and benchmarks, showing consistent improvements of up to +4.6 average points over standard RL with accuracy-based rewards, with larger gains at longer contexts, while also reducing repetitive copying and thinking length. Our findings suggest that, even as long-context evaluation shifts from simple retrieval toward complex reasoning, accurate grounding in relevant evidence remains an indispensable capability with substantial room for improvement.

</details>

---

### [[20_Research/Papers/大模型/Agents_in_the_Wild_Where_Research_Meets_Deployment|Agents in the Wild: Where Research Meets Deployment]]

![[assets/2607.19336_first_page.png|800]]

- **arXiv**: [2607.19336](https://arxiv.org/abs/2607.19336)
- **PDF**: https://arxiv.org/pdf/2607.19336
- **详细分析**: [[20_Research/Papers/大模型/Agents_in_the_Wild_Where_Research_Meets_Deployment|Agents in the Wild: Where Research Meets Deployment]]
- **作者**: Grace Hui Yang, Pranav N. Venkit, Hooman Sedghamiz, Enrico Santus, Victor Dibia, Ioana Baldini
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agents in the Wild: Where Research Meets Deployment》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentSafetyBench, MobileSafetyBench, ST-WebAgentBench, ScienceAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic systems large language model (LLM) based architectures capable of reasoning, planning, acting, and coordinating with tools and other agents are rapidly transitioning from research prototypes to production scale deployments across domains such as software engineering, scientific discovery, and finance. While academic work has emphasized benchmarks and algorithmic innovation, deployment raises new challenges around robustness, safety, and reliability. This tutorial brings together researchers and practitioners to explore advances in reasoning and planning, multi agent coordination, and evaluation, highlighting open challenges arising from deployment experience. Through applied case studies in pharmaceutical discovery and financial systems, we analyze common design patterns that make agentic systems successful, and discuss practical mitigation strategies for failure modes, such as verification pipelines, fallback mechanisms, and human in the loop supervision. Attendees will gain a comprehensive view of the field along with concrete design patterns, evaluation checklists, and templates for safe and reliable deployment across industries.

</details>

---

### [[20_Research/Papers/机器人/From_Distances_to_Trajectories_Real-Time_Signed_Distance_Function_Mapping_and_Distance-Accelerated_Motion_Planning_for_UAVs|From Distances to Trajectories: Real-Time Signed Distance Function Mapping and Distance-Accelerated Motion Planning for UAVs]]

![[assets/2607.19306_figure.png|800]]

- **arXiv**: [2607.19306](https://arxiv.org/abs/2607.19306)
- **PDF**: https://arxiv.org/pdf/2607.19306
- **详细分析**: [[20_Research/Papers/机器人/From_Distances_to_Trajectories_Real-Time_Signed_Distance_Function_Mapping_and_Distance-Accelerated_Motion_Planning_for_UAVs|From Distances to Trajectories: Real-Time Signed Distance Function Mapping and Distance-Accelerated Motion Planning for UAVs]]
- **作者**: Jason Stanley, Zhirui Dai, Qihao Qian, Tzu-Chin Ho, Tianxing Fan, Siddharth Saha, Christopher Barngrover, Ki Myung Brian Lee, Nikolay Atanasov
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《From Distances to Trajectories: Real-Time Signed Distance Function Mapping and Distance-Accelerated Motion Planning for UAVs》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous flight in cluttered environments requires a robot to build a geometric map of its surroundings and plan safe, dynamically feasible trajectories, all onboard and in real time. Conventional approaches treat mapping and planning as separate stages and often rely on binary occupancy for collision checking. We argue that these two stages should be co-designed around a single representation: a signed distance function (SDF). By encoding distance to the nearest obstacle, an SDF provides richer information for planning and trajectory optimization than occupancy alone. We develop an Octree REsidual Network (OREN) that pairs an explicit octree prior with an implicit neural residual to reconstruct SDFs online from point cloud observations with the efficiency of volumetric methods and the accuracy and differentiability of neural methods. In tandem, we develop Bubble$^\star$, a search-based planner that exploits the distance information to grow maximal collision-free balls, which we call bubbles, with formal guarantees of termination, completeness, and failure detection. Planning over a graph of bubbles significantly reduces collision checks compared to a grid-based A$^\star$ search and returns a bubble sequence that forms a safe corridor for trajectory optimization. We demonstrate the integrated OREN-Bubble$^\star$ approach onboard a quadrotor, navigating unseen indoor environments in real time under tight compute constraints. OREN improves SDF estimation by $22$% compared to baselines, while Bubble$^\star$ finds trajectories spanning $\approx 90$ m through a cluttered environment in $1$-$3$ sec., whereas baselines take up to $10$ sec. in the same environment.

</details>

---

### [[20_Research/Papers/强化学习/The_Price_of_Reasoning_Cost-Quality_Tradeoffs_in_Reinforcement_Learning_for_Neural_Machine_Translation|The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation]]

![[assets/2607.19226_first_page.png|800]]

- **arXiv**: [2607.19226](https://arxiv.org/abs/2607.19226)
- **PDF**: https://arxiv.org/pdf/2607.19226
- **详细分析**: [[20_Research/Papers/强化学习/The_Price_of_Reasoning_Cost-Quality_Tradeoffs_in_Reinforcement_Learning_for_Neural_Machine_Translation|The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation]]
- **作者**: Michael Jungo, Aixiu An
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《The Price of Reasoning: Cost-Quality Tradeoffs in Reinforcement Learning for Neural Machine Translation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has been established as a viable paradigm for the post-training of Large Language Models (LLMs), including downstream tasks, such as Neural Machine Translation (NMT). With the latest research indicating that RLVR could be the preferred training method for translating legal documents due to the induced reasoning capabilities, it raises the question whether it is really attributed to the reasoning or more generally to the training paradigm. We investigate the importance of including the model's reasoning trace in the generated responses during both training and inference by systematically omitting it from one of the phases. Our experiments show that including the reasoning, specifically during inference, has a positive effect on the overall translation quality. Furthermore, we recognise that the reasoning leads to an increase in output tokens, hence we study the cost-quality tradeoff between the increased computational demands and the improved translation quality.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Score_Prediction_LLM-Based_Essay_Scoring_and_Feedback_Generation_via_Reinforcement_Learning_with_Rubric_Rewards|Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards]]

![[assets/2607.19219_figure.png|800]]

- **arXiv**: [2607.19219](https://arxiv.org/abs/2607.19219)
- **PDF**: https://arxiv.org/pdf/2607.19219
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Score_Prediction_LLM-Based_Essay_Scoring_and_Feedback_Generation_via_Reinforcement_Learning_with_Rubric_Rewards|Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards]]
- **作者**: Xuefeng Jin, Jiashuo Zhang, Teng Cao, Bin Yang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.55，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have been widely applied to automated essay scoring (AES) and automated feedback generation (AFG). However, existing studies rely primarily on prompt engineering or supervised fine-tuning, while systematic research on reinforcement learning (RL) post-training and automated evaluation of feedback quality remains limited. We propose RLAES, a unified LLM framework that jointly optimizes essay scoring and feedback generation through RL. To make feedback quality measurable, interpretable, and usable for training, we introduce Rubric-based Feedback Evaluation (RFE), an essay-grounded feedback evaluation framework comprising 166 fine-grained binary rubric items and an LLM-as-judge. Building on RFE, we propose Adaptive Gated Feedback Optimization (AGFO), which activates rubric-based feedback rewards on demand during RL, reducing evaluation overhead while improving feedback quality. We also propose Adjacent Contrastive Reasoning (ACR) to improve ordinal score calibration by explicitly contrasting adjacent score levels. Experimental results show that the RFE framework captures essay-feedback consistency, exhibits strong pairwise discriminative power, and closely aligns with expert preferences. On the ASAP benchmark, RLAES-AGFO achieves the best scoring performance among LLM-based methods (QWK = 0.803), while maintaining feedback quality comparable to GPT-5.5 and avoiding the feedback degradation observed under score-only RL. Code and datasets are publicly available at https://github.com/hellomuyi/RLAES.

</details>

---

### [[20_Research/Papers/机器人/Computing_on_the_Fly_Navigating_a_Vision_for_the_Future_of_Drone_Computing|Computing on the Fly: Navigating a Vision for the Future of Drone Computing]]

![[assets/2607.19213_first_page.png|800]]

- **arXiv**: [2607.19213](https://arxiv.org/abs/2607.19213)
- **PDF**: https://arxiv.org/pdf/2607.19213
- **详细分析**: [[20_Research/Papers/机器人/Computing_on_the_Fly_Navigating_a_Vision_for_the_Future_of_Drone_Computing|Computing on the Fly: Navigating a Vision for the Future of Drone Computing]]
- **作者**: Kevin Butler, Christopher Stewart, Nils Aschenbruck, Alina Gerall, Weisong Shi, Deborah Silver, Ufuk Topcu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, ComputerVision, Security

#### 研究背景与动机

《Computing on the Fly: Navigating a Vision for the Future of Drone Computing》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The report envisions a decade in which drones move goods, medical supplies, and information at a scale comparable to national infrastructure investments like highways and the electric grid. Potential applications include natural disaster detection drones that spot wildfire sources within minutes, medical supply chains that bypass ground congestion to reach rural hospitals, and nationwide fleets that continuously inspect bridges and power lines. Realizing this future, however, requires closing what report authors call a "capability gap," where hardware and aspirations are outpacing the software and systems needed to operate safely at scale. The report identifies twelve technical challenges that must be addressed to realize the transformative potential of drone technology: Scaling to millions of drones; AI intelligence and assurance; Edge-cloud continuum and real-time coordination; AI autonomy and agentic systems; Data, training, and validation infrastructure; Critical infrastructure protection; Building reliable fleets from non-deterministic agents; Trust, security, and distributed authentication; Next-generation drone networks; Human-AI partnership and scalable insight; Standards, certification, and regulation; and Workforce development and education. These twelve challenges and proposed approaches to them form the basis of the report, laying out a multifaceted path forward for the evolution of done technology.

</details>

---

### [[20_Research/Papers/世界模型/ABot-World-0_Infinite_Interactive_World_Rollout_on_a_Single_Desktop_GPU|ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU]]

![[assets/2607.19191_figure.png|800]]

- **arXiv**: [2607.19191](https://arxiv.org/abs/2607.19191)
- **PDF**: https://arxiv.org/pdf/2607.19191
- **详细分析**: [[20_Research/Papers/世界模型/ABot-World-0_Infinite_Interactive_World_Rollout_on_a_Single_Desktop_GPU|ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU]]
- **作者**: Fan Jiang, Zhaoxu Sun, Mengchao Wang, Ziyu Zhu, Chiyu Wang, Yunpeng Zhang, Wenlin Liu, Yun Wang, Xue Zheng, Rui Sun, Junfeng Ni, Hongyu Pan...
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.16，世界模型 0.36）
- **关联关键词**: Multimodal, Agent, WorldModel

#### 研究背景与动机

《ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ABot-World, U-Net, WorldRoamBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet videos to learn controllable world dynamics. WorldExplorer performs agent-driven collection guided by training feedback, while a unified pipeline applies 14 deterministic quality checks, VLM-based assessment, and synchronized action and text annotation. We progressively distill a bidirectional action-conditioned teacher into a causal student through teacher forcing and ODE distillation, and introduce LongForcing to align long student self-rollouts with an extended-horizon teacher, mitigating accumulated distribution shift and autoregressive drift. Raw keyboard actions provide a unified control interface for scene roaming and third-person character interaction, while reference-character memory provides persistent appearance cues for identity consistency during third-person rollouts. For deployment, we co-design a streaming inference stack with a lightweight VAE decoder, efficient attention, memory-aware scheduling, and low-bit DiT inference. Across optimized low-bit configurations, ABot-World-0 streams 720P video at up to 16 FPS on a single NVIDIA RTX 5090 desktop GPU, with 1.2s action-to-first-frame latency and approximately 19GiB peak VRAM. Experiments on WorldRoamBench and extended interactive rollouts demonstrate competitive controllability and coherent long-horizon world evolution.

</details>

---

### [[20_Research/Papers/强化学习/Agentic_Real2Sim_Physics-based_World_Modeling_with_Vision-Language_Agents|Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents]]

![[assets/2607.19190_first_page.png|800]]

- **arXiv**: [2607.19190](https://arxiv.org/abs/2607.19190)
- **PDF**: https://arxiv.org/pdf/2607.19190
- **详细分析**: [[20_Research/Papers/强化学习/Agentic_Real2Sim_Physics-based_World_Modeling_with_Vision-Language_Agents|Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents]]
- **作者**: Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LychSim, PointWorld, Real2Sim, SimWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-to-sim conversion for robotic interaction with objects remains labor-intensive because it requires more than visual reconstruction: a streamlined real2sim process must recover scene geometries and object states, infer physical parameters, and assemble actors, objects, cameras, poses, and trajectories into a runnable physical simulation. Today this process still depends on manual tuning of visual foundation models, mesh cleanup, coordinate-frame alignment, and brittle workflow glue across visual perception tools and simulators. We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states. We evaluate Agentic Real2Sim on rigid-object manipulation, deformable-object interaction, and humanoid motion scenes, spanning domains that are usually handled by separate Real2Sim pipelines, marking a first step toward scalable conversion. The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate. We aim to use the resulting real-world-aligned twins for downstream robotics tasks, specifically policy learning and evaluation. The project site is available at https://ericchen321.github.io/agentic_real2sim.github.io/.

</details>

---

### [[20_Research/Papers/强化学习/Comparative_Study_of_Multi-Agent_Actor-Critic_Algorithms_in_Parameterized_Action_Reinforcement_Learning|Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning]]

![[assets/2607.19117_figure.png|800]]

- **arXiv**: [2607.19117](https://arxiv.org/abs/2607.19117)
- **PDF**: https://arxiv.org/pdf/2607.19117
- **详细分析**: [[20_Research/Papers/强化学习/Comparative_Study_of_Multi-Agent_Actor-Critic_Algorithms_in_Parameterized_Action_Reinforcement_Learning|Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning]]
- **作者**: Ubayd Ali Bapoo, Clement N Nyirenda
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.1（加权：大模型 0.5，强化学习 1.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Comparative Study of Multi-Agent Actor-Critic Algorithms in Parameterized Action Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Parameterized action reinforcement learning has shown strong performance in environments requiring both discrete action selection and continuous parameterization. Prior work established the effectiveness of single-agent actor-critic algorithms - Greedy Actor-Critic (GAC), Soft Actor-Critic (SAC), and Truncated Quantile Critics (TQC) - on benchmark parameterized action tasks, but their extension to multi-agent settings remains largely unexplored. This paper presents a comparative study of shared-experience multi-agent extensions of these algorithms: Multi-Agent Greedy Actor-Critic (MAGAC), Multi-Agent Soft Actor-Critic (MASAC), and Multi-Agent Truncated Quantile Critics (MATQC). Rather than following the centralized training, decentralized execution (CTDE) paradigm, the proposed framework uses multiple independent actor-critic agents that share a replay buffer while maintaining separate policy and value networks. We evaluate the algorithms on the Platform-v0 and Goal-v0 benchmarks against their single-agent counterparts, using three-, five-, and ten-agent configurations to assess scalability. Performance is measured by average evaluation return and training time across ten independent runs, with one-way ANOVA and Tukey HSD post-hoc tests used to assess statistical significance. Results show that the multi-agent framework consistently improves Greedy Actor-Critic performance, while MASAC and MATQC show comparatively modest gains over their single-agent versions. Increasing the number of agents beyond five yields limited additional performance while substantially raising computational cost, particularly for MAGAC. These results highlight a trade-off between learning performance and computational efficiency, offering insight into the scalability of shared-experience multi-agent actor-critic methods for parameterized action reinforcement learning.

</details>

---

### [[20_Research/Papers/大模型/Supra_Cognitive_Modes_A_Routed_Architecture_for_Agent_Memory|Supra Cognitive Modes: A Routed Architecture for Agent Memory]]

![[assets/2607.19096_first_page.png|800]]

- **arXiv**: [2607.19096](https://arxiv.org/abs/2607.19096)
- **PDF**: https://arxiv.org/pdf/2607.19096
- **详细分析**: [[20_Research/Papers/大模型/Supra_Cognitive_Modes_A_Routed_Architecture_for_Agent_Memory|Supra Cognitive Modes: A Routed Architecture for Agent Memory]]
- **作者**: Joshua Tobkin, David Yang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《Supra Cognitive Modes: A Routed Architecture for Agent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent-memory workloads mix direct factual lookup, relation-chain and current-state reasoning, and broad synthesis over long histories. We describe Supra Cognitive Modes (SCM), an architecture that maps explicit or automatically selected per-query modes to retrieval and synthesis payloads over one shared ingest substrate. A frozen semantic classifier and runtime gates dispatch queries among fused lexical and dense lookup, graph or iterative multi-hop handling, and stratified long-form synthesis. The substrate combines multi-granularity embeddings, extracted triples, fact-version metadata, and optional asynchronous enrichments. We characterize the deployed configuration on three benchmarks: Long-term Conversational Memory (LoCoMo; n = 1,986), MemoryAgentBench (MAB; n = 3,671), and LongMemEval (n = 500). The reference run records 84.87% on LoCoMo factoid categories and 68.61% on adversarial abstention, 61.49% on MAB across two repetitions, and 86.00% on LongMemEval. A repository-backed reproduction produces similar aggregate scores and supports task- and mode-conditioned failure analysis. Raw baseline outputs, aligned end-to-end timing for LoCoMo and LongMemEval, and complete token ledgers are unavailable; stored rows also omit some final runtime decisions. The results characterize one implemented routed configuration and its diagnostic failure patterns, while source inspection verifies the per-query control interface and shared-substrate design. Causal routing effects, efficiency gains, and statistical significance remain outside the available evidence.

</details>

---

### [[20_Research/Papers/大模型/Quality_Action_Assurance_Multimodal_Verification_of_Examiner_Claims_in_VR_OSCEs|Quality Action Assurance: Multimodal Verification of Examiner Claims in VR OSCEs]]

![[assets/2607.19063_figure.png|800]]

- **arXiv**: [2607.19063](https://arxiv.org/abs/2607.19063)
- **PDF**: https://arxiv.org/pdf/2607.19063
- **详细分析**: [[20_Research/Papers/大模型/Quality_Action_Assurance_Multimodal_Verification_of_Examiner_Claims_in_VR_OSCEs|Quality Action Assurance: Multimodal Verification of Examiner Claims in VR OSCEs]]
- **作者**: Harry Rogers, Sally Shiels, Ashley Tomlinson, James Thomas, James Aylward, Nathan Gauge, Helen Higham, Alison Noble
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Quality Action Assurance: Multimodal Verification of Examiner Claims in VR OSCEs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Objective Structured Clinical Examinations (OSCEs) are the gold standard for assessing clinical competence, yet scoring remains vulnerable to examiner subjectivity, fatigue, and cognitive bias. Standard examiner validation via inter-rater statistics lacks explanatory power regarding the source of errors, as it neither analyzes examiner reasoning nor verifies examiner claims against actual events. Thus, we introduce Quality Action Assurance (QAA), a multimodal framework that verifies examiner claims in Virtual Reality (VR) pediatric OSCEs by comparing actions claimed by examiners against the true sequence of events, constructed from video, VR logs, and actor data. QAA combines a constrained temporal action alignment model, which performs action localization and actor source attribution, with a large language model that extracts examiner claims and checks them against the record. Across a 5-fold cross-validation, QAA achieves 99.2% $\pm$ 0.7% Actor F1 and 93.4% $\pm$ 1.9% W@16 for temporal alignment. Overall, QAA detects examiner errors with 70.0% precision and 76.7% recall, improving factual correctness from 39.2% to 79.2%, enabling fairer OSCE assessment.

</details>

---

### [[20_Research/Papers/大模型/Computational_Humor_with_Multimodal_LLMs_Methods,_Datasets,_Evaluation,_and_Challenges|Computational Humor with Multimodal LLMs: Methods, Datasets, Evaluation, and Challenges]]

![[assets/2607.19011_figure.png|800]]

- **arXiv**: [2607.19011](https://arxiv.org/abs/2607.19011)
- **PDF**: https://arxiv.org/pdf/2607.19011
- **详细分析**: [[20_Research/Papers/大模型/Computational_Humor_with_Multimodal_LLMs_Methods,_Datasets,_Evaluation,_and_Challenges|Computational Humor with Multimodal LLMs: Methods, Datasets, Evaluation, and Challenges]]
- **作者**: Tuo Liang, Zhe Hu, Disheng Liu, Jing Li, Yu Yin
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Computational Humor with Multimodal LLMs: Methods, Datasets, Evaluation, and Challenges》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal humor in memes, cartoons, and comics remains difficult for AI systems because intended meaning depends on non-literal mechanisms, shared cultural knowledge, and communicative intent rather than literal scene description. This survey focuses on visual humor understanding in single-image and multi-panel artifacts, while treating humor generation as an emerging downstream frontier. We position the literature against prior humor, sarcasm, and general MLLM surveys and organize it using a capability-centric hierarchy spanning recognition, interpretation and reasoning, and generation. Under this lens, we synthesize benchmark design, evaluation protocols, and modeling paradigms, tracing the field's shift from task-specific fusion models to large-model approaches based on multimodal alignment, evidence-grounded reasoning, and controlled generation. We conclude by highlighting the main barriers to progress: shortcut-prone evaluation, limited cultural and narrative coverage, weak evidence grounding, and unresolved safety and ownership concerns.

</details>

---

### [[20_Research/Papers/强化学习/MedDDC-Eval_Diagnosis-Decoupled_Evaluation_of_Multi-Turn_Medical_Consultation_Agents|MedDDC-Eval: Diagnosis-Decoupled Evaluation of Multi-Turn Medical Consultation Agents]]

![[assets/2607.18999_figure.png|800]]

- **arXiv**: [2607.18999](https://arxiv.org/abs/2607.18999)
- **PDF**: https://arxiv.org/pdf/2607.18999
- **详细分析**: [[20_Research/Papers/强化学习/MedDDC-Eval_Diagnosis-Decoupled_Evaluation_of_Multi-Turn_Medical_Consultation_Agents|MedDDC-Eval: Diagnosis-Decoupled Evaluation of Multi-Turn Medical Consultation Agents]]
- **作者**: Guofeng Zhang, Yizeng Quan, Huaiyi Fang, Jianwei Lv, Jinyao Liu, Xunxu Duan, Lening An, Yu Ouyang, Junfeng Wang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MedDDC-Eval: Diagnosis-Decoupled Evaluation of Multi-Turn Medical Consultation Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HealthBench, MedConsultBench, MedDDC-Eval, ThReadMed-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-turn medical consultation agents must decide what to ask, adapt to patient responses, and determine when the collected evidence is sufficient. However, coupled evaluation conflates the quality of the policy-elicited history with policy-specific terminal diagnosis generation: strong generation can compensate for a thin history, while weaker generation can obscure a rich one. We introduce MedDDC-Eval, a diagnosis-decoupled testbed that treats elicited history as the comparison object and holds the history-to-diagnosis mapping constant through a shared frozen reader. Across two held-out sources, a grounded interface and an auditable diagnosis-trajectory-efficiency (D/T/E) harness measure diagnostic usefulness, information acquisition, and efficiency. Directional semantic coverage followed by deterministic one-to-one assignment yields coherent precision-recall counts for open-ended items, with at most one credited match per prediction or reference. Holding histories fixed, changing only the diagnostic reader shifts diagnosis F1 by 2.2-19.0 points and reverses 18% and 36% of pairwise policy orderings on the Record and Dialogue splits. We further apply standard Group Relative Policy Optimization (GRPO) over interactive multi-turn rollouts to post-train Qwen3-32B using diagnosis-result and trajectory feedback. On the 100-case Record and 70-case Dialogue splits, the trained policy improves over its initialization by 9.7 and 4.6 total-score points; removing either primary signal lowers held-out joint performance. These results show that MedDDC-Eval supports controlled attribution, interpretable elicited-history measurement, and evaluation-guided evidence-acquisition policy development.

</details>

---

### [[20_Research/Papers/具身智能/Athena-Brain_Technical_Report_An_Efficient_Robot_Brain_for_General_Intelligence_and_Embodied_Interactio|Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interactio]]

![[assets/2607.18985_figure.png|800]]

- **arXiv**: [2607.18985](https://arxiv.org/abs/2607.18985)
- **PDF**: https://arxiv.org/pdf/2607.18985
- **详细分析**: [[20_Research/Papers/具身智能/Athena-Brain_Technical_Report_An_Efficient_Robot_Brain_for_General_Intelligence_and_Embodied_Interactio|Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interactio]]
- **作者**: Jialian Li, Junhong Liu, Yuchen Cao, Weiran Guo, Jiaming Song, Xutao Wang, Yi Zhao, Jiangpin Liu, Jie Chen
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.2，强化学习 0.2，机器人 0.6）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Athena-Brain Technical Report: An Efficient Robot Brain for General Intelligence and Embodied Interactio》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have demonstrated remarkable capabilities in language understanding, reasoning, and world knowledge. As embodied agents become increasingly capable, there is a growing demand for compact models that can serve as an on-device brain, preserving the broad general intelligence of LLMs while enabling effective high-level interaction with embodied environments. Existing approaches, however, often prioritize either general-purpose intelligence or specialized embodied capabilities, making it challenging to satisfy both requirements within a single model. We present \textbf{Athena-Brain-8B}, an 8B LLM designed to serve as an on-device brain for embodied intelligence for embodied intelligence. Through a multi-stage post-training pipeline consisting of General Supervised Fine-Tuning, General Reinforcement Learning, Embodied Expert training, and Model Merge, Athena-Brain-8B maintains strong general capabilities while acquiring strong high-level embodied interaction capabilities and generating concise responses for efficient embodied interaction. Experimental results demonstrate the effectiveness of Athena across both general and embodied evaluations. Compared with the corresponding Qwen3-8B thinking model, Athena-Brain-8B achieves comparable performance on general language and reasoning benchmarks while generating substantially shorter responses. On in-domain embodied benchmarks, Athena-Brain-8B consistently outperforms models of similar scale and surpasses several substantially larger frontier models evaluated zero-shot, demonstrating that compact language models can effectively integrate strong general intelligence with embodied capabilities.

</details>

---

### [[20_Research/Papers/强化学习/Fishing_Out_Free_Riders_Shapley-Based_Reward_Attribution_for_Parallel_Reasoning_via_Reinforcement_Learning|Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning]]

![[assets/2607.18979_figure.png|800]]

- **arXiv**: [2607.18979](https://arxiv.org/abs/2607.18979)
- **PDF**: https://arxiv.org/pdf/2607.18979
- **详细分析**: [[20_Research/Papers/强化学习/Fishing_Out_Free_Riders_Shapley-Based_Reward_Attribution_for_Parallel_Reasoning_via_Reinforcement_Learning|Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning]]
- **作者**: Wentao Zhang, Haoyu Zhang, Xinke Jiang, Yuxuan Cheng, Yuhan Pan, Miao Li, Zhipeng Qiao, Tao Feng, Zhen Tao, Dengji Zhao
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Fishing Out Free Riders: Shapley-Based Reward Attribution for Parallel Reasoning via Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) excel at multi-step reasoning, yet current parallel reasoning approaches often fail to distinguish the contributions of individual reasoning paths. Many paths may be redundant, misleading, or even detrimental, but outcome-level rewards assign uniform reward, leading to ambiguous learning signals and unstable training. We propose Parallel Shapley, a reinforcement learning framework that attributes fine-grained, path-level contributions in multi-path reasoning. Treating each path as a player in a cooperative game, we leverage Shapley values to quantify marginal contributions, using a generative reward model to evaluate path utilities and Monte Carlo sampling for efficient approximation. Experiments on mathematical reasoning benchmarks show that Parallel Shapley outperforms existing baselines while providing more stable and interpretable training. Our framework effectively "fishes out the free riders," assigning reward proportionally and improving multi-path reasoning in LLMs.

</details>

---

### [[20_Research/Papers/强化学习/From_Trajectories_to_Instructions_Language-Conditioned_Meta-Reinforcement_Learning|From Trajectories to Instructions: Language-Conditioned Meta-Reinforcement Learning]]

![[assets/2607.18830_figure.png|800]]

- **arXiv**: [2607.18830](https://arxiv.org/abs/2607.18830)
- **PDF**: https://arxiv.org/pdf/2607.18830
- **详细分析**: [[20_Research/Papers/强化学习/From_Trajectories_to_Instructions_Language-Conditioned_Meta-Reinforcement_Learning|From Trajectories to Instructions: Language-Conditioned Meta-Reinforcement Learning]]
- **作者**: Garvit Singla, Uma Maheswari Natarajan, Raghuram Bharadwaj Diddigi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《From Trajectories to Instructions: Language-Conditioned Meta-Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-Agnostic Meta-Learning (MAML) is a widely used framework for reinforcement learning (RL) that enables efficient transfer by learning global policy parameters that can be rapidly adapted to new tasks. MAML training proceeds in two loops: an inner loop where the global parameters are adapted to task-specific parameters, and an outer loop where these task-specific parameters are evaluated and losses are back-propagated to improve the global parameters. Traditionally, the inner loop adaptation is performed by collecting trajectories from the task environment and applying gradient updates on the empirical expected return, which can be a costly operation. We note that it is the outer loop that drives the actual learning of global parameters, and therefore the inner loop adaptation mechanism need not be restricted to be gradient-based. This observation leads us to ask: Can we replace the inner loop trajectory collection and gradient update with a simpler, task-specific signal? In many practical settings, tasks are naturally accompanied by language instructions. Leveraging these instructions as a direct task-specific signal, we propose LA-MAML (Language Adapted MAML), which modifies the inner loop by adapting the global policy parameters in a single step through a learned embedding of the task instruction, replacing the inner loop trajectory collection and gradient-based updates. Experiments on the BabyAI benchmark demonstrate that LA-MAML achieves competitive or improved performance compared to baselines at a significantly lower per-iteration wall-clock training time. These results demonstrate that language instructions are an effective and efficient substitute for trajectory-based inner loop adaptation in meta RL.

</details>

---

### [[20_Research/Papers/大模型/Cross-Agent_Campaign_Attribution_Linking_Asynchronous_Attacks_Across_LLM_Agents|Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents]]

![[assets/2607.18826_figure.png|800]]

- **arXiv**: [2607.18826](https://arxiv.org/abs/2607.18826)
- **PDF**: https://arxiv.org/pdf/2607.18826
- **详细分析**: [[20_Research/Papers/大模型/Cross-Agent_Campaign_Attribution_Linking_Asynchronous_Attacks_Across_LLM_Agents|Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents]]
- **作者**: SangJin Park, Myungsub Choi, Jineok Kim, Minseung Kang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-agent defenses are typically evaluated one session at a time. In deployment, however, attacks can be distributed across independent agents, teams, and runtimes, leaving each local guardrail with only a sparse fragment. We formalize cross-agent asynchronous campaign attribution: linking sessions from the same latent adversarial campaign without shared runtime state, test-time campaign labels, or attacker identity oracles. We introduce Asynchronous Attribution Fingerprint Vectors ($A^2FV$), a lightweight proxy-side reference protocol for scoring pairwise campaign similarity from proxy-observable tool-use, timing, and prompt residue. We also construct SCD-v1, a controlled persona-matched benchmark with benign traffic, isolated attacks, multi-session campaigns, matched non-oracle evasion, and leakage audits. On SCD-v1, $A^2FV$ achieves 0.82 pairwise AUC for campaign linking, while score-only adaptations of per-session detectors and chunked LLM judges remain near chance under the same task. The strongest fixed signal is carried by structural and stylometric residue, while timing is retained as a diagnostic channel for richer proxy traces. Crossed-style controls show that the signal is partly style-sensitive but not reducible to style alone. Static and dimension-aware non-oracle stress tests further show that pairwise separability persists under controlled evasion. These results establish cross-agent campaign attribution as a distinct evaluation layer for securing LLM agents in the wild.

</details>

---

### [[20_Research/Papers/大模型/AI_Tour_Meeting_Group_Travel_Planning_by_LLM_Agents|AI Tour Meeting: Group Travel Planning by LLM Agents]]

![[assets/2607.18806_figure.png|800]]

- **arXiv**: [2607.18806](https://arxiv.org/abs/2607.18806)
- **PDF**: https://arxiv.org/pdf/2607.18806
- **详细分析**: [[20_Research/Papers/大模型/AI_Tour_Meeting_Group_Travel_Planning_by_LLM_Agents|AI Tour Meeting: Group Travel Planning by LLM Agents]]
- **作者**: Daisuke Kikuta
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AI Tour Meeting: Group Travel Planning by LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes AI Tour Meeting, a group travel planning framework powered by multiple Large Language Model (LLM)-based agents. The agents are instantiated with distinct personas and collaboratively seek an itinerary that satisfies their constraints and preferences through natural language discussion. The framework enables easy and flexible orchestration of such discussions by providing interfaces for configuring agent personas, discussion workflows, monitoring, and LLM deployment. Its primary use case is a simulation tool for analyzing the behavior of multiple LLM agents during tour planning discussions. This paper demonstrates the utility of the framework by presenting system validation and several analytical results obtained by the framework.

</details>

---

### [[20_Research/Papers/大模型/Bounding_Boxes_to_Improve_Small_Language_Model_Performance_on_Vision-Based_Grading_Tasks|Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks]]

![[assets/2607.18767_figure.png|800]]

- **arXiv**: [2607.18767](https://arxiv.org/abs/2607.18767)
- **PDF**: https://arxiv.org/pdf/2607.18767
- **详细分析**: [[20_Research/Papers/大模型/Bounding_Boxes_to_Improve_Small_Language_Model_Performance_on_Vision-Based_Grading_Tasks|Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks]]
- **作者**: Lachlan McGinness
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

《Bounding Boxes to Improve Small Language Model Performance on Vision-Based Grading Tasks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The deployment of Small Language Models (SLMs) in educational settings offers significant advantages in terms of privacy, cost, and scalability. However, SLMs often struggle with complex vision-based tasks, such as grading handwritten student exams, due to the high computational cost of processing large images and the visual distractions present on a full page. In this paper, we investigate whether cropping student responses using bounding boxes can improve the accuracy and computational efficiency of SLMs on a short-answer grading task. Using a dataset of scanned handwritten responses from the 2025 Australian Physics Olympiad, we evaluate the performance of several models ranging from 4B to 72B parameters under varying conditions of Chain of Thought (CoT) prompting and image cropping. Our results demonstrate that using bounding boxes significantly improves grading accuracy and reduces computational cost (FLOPs) across models. We conclude that bounding boxes are a crucial pre-processing step for deploying SLMs in large-scale, vision-based educational assessments.

</details>

---

### [[20_Research/Papers/大模型/AgentDebugX_An_Open-Source_Toolkit_for_Failure_Observability,_Attribution,_and_Recovery_in_LLM_Agents|AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents]]

![[assets/2607.18754_figure.png|800]]

- **arXiv**: [2607.18754](https://arxiv.org/abs/2607.18754)
- **PDF**: https://arxiv.org/pdf/2607.18754
- **详细分析**: [[20_Research/Papers/大模型/AgentDebugX_An_Open-Source_Toolkit_for_Failure_Observability,_Attribution,_and_Recovery_in_LLM_Agents|AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents]]
- **作者**: Kunlun Zhu, Xuyan Ye, Zhiguang Han, Yuchen Zhao, Bingxuan Li, Weijia Zhang, Muxin Tian, Xiangru Tang, Pan Lu, James Zou, Jiaxuan You, Heng Ji
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agent failures are difficult to debug because the step where an error surfaces is often not the one that caused it. Existing observability tools replay execution traces but provide little support for identifying the root cause or translating diagnosis into recovery. We present AgentDebugX, an open-source debugging framework that organizes debugging as a closed loop of Detect, Attribute, Recover, and Rerun. At its core, DeepDebug performs multi-turn root-cause diagnosis through global trajectory understanding, structure-guided investigation, and cross-examination. On the Who and When benchmark, DeepDebug achieves the best strict attribution accuracy among the evaluated methods on both tested open-weight backbones, reaching 28.8 percent exact agent-and-step accuracy on qwen3.5-9b versus 21.7 percent for the strongest single-pass baseline. On GAIA, DeepDebug repairs 13 of 73 failed tasks in a single rerun, compared with 4 to 6 for three decoupled self-correction baselines, improving overall accuracy from 55.8 percent to 63.6 percent. AgentDebugX exposes this workflow through a Python library, CLI, web console, and installable agentic skill, and provides an opt-in Error Hub for sharing scrubbed failure-diagnosis-repair bundles and reusing them as debugging memory.

</details>

---

### [[20_Research/Papers/强化学习/Strategy-Following_Multi-Agent_Deep_Reinforcement_Learning_Considering_Control_Strategies_Provided_to_Other_Agents|Strategy-Following Multi-Agent Deep Reinforcement Learning Considering Control Strategies Provided to Other Agents]]

![[assets/2607.18719_figure.png|800]]

- **arXiv**: [2607.18719](https://arxiv.org/abs/2607.18719)
- **PDF**: https://arxiv.org/pdf/2607.18719
- **详细分析**: [[20_Research/Papers/强化学习/Strategy-Following_Multi-Agent_Deep_Reinforcement_Learning_Considering_Control_Strategies_Provided_to_Other_Agents|Strategy-Following Multi-Agent Deep Reinforcement Learning Considering Control Strategies Provided to Other Agents]]
- **作者**: Yamato Takahagi, Gentoku Nakasone, Yoshinari Motokawa, Toshiharu Sugawara
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.4（加权：大模型 0.8，强化学习 1.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Strategy-Following Multi-Agent Deep Reinforcement Learning Considering Control Strategies Provided to Other Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CIRL, DRL, MADRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study proposes a learning method for multi-agent systems that allows agents to be controlled through human manager instructions after learning and enables uninstructed agents to implicitly complement the overall work based on the actions of other agents. Multi-agent applications using deep learning have shown potential; thus, to achieve extensive social applications, humans should be able to control learned agents using simple methods to respond to environmental and social changes. Even without such changes, learned coordination often does not match the expectations of human managers, making it preferable to control coordination structures to match human intentions. Some studies have aimed to control agent behavior using simple instructions. However, they assumed that instructions are provided to all agents, which is time-consuming and not evident when designing a better cooperation regime. Ideally, specific agents should receive key action instructions, while others should automatically complete the remaining tasks. The proposed method, which extends previous work on controllability in multi-agent deep reinforcement learning, enables uninstructed agents to adaptively complement overlooked tasks and areas. The experimental results show that agents using the proposed method can shift to another cooperative structure and achieve better performance than those using conventional methods.

</details>

---

### [[20_Research/Papers/世界模型/DWM_Separating_World_Effects_from_Actions_in_Latent_World_Models|DWM: Separating World Effects from Actions in Latent World Models]]

![[assets/2607.18715_figure.png|800]]

- **arXiv**: [2607.18715](https://arxiv.org/abs/2607.18715)
- **PDF**: https://arxiv.org/pdf/2607.18715
- **详细分析**: [[20_Research/Papers/世界模型/DWM_Separating_World_Effects_from_Actions_in_Latent_World_Models|DWM: Separating World Effects from Actions in Latent World Models]]
- **作者**: Yi-Ge Zhang, Tianqi Du, Qi Zhang, Yisen Wang
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《DWM: Separating World Effects from Actions in Latent World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models underpin much of modern model-based control, yet current action-conditioned formulations supervise the next-latent transition with a single, undifferentiated target, forcing a monolithic learning signal to absorb every source of state change. In real world, however, transitions arise from two heterogeneous sources: an action-driven component induced by the agent, and an action-invariant world effect -- the change that would still occur under a null action, dictated by the environment's intrinsic dynamics (e.g., gravity-driven sliding, inertia, contact rebound, and persistent drift). Fusing them into a single target entangles the two inside the latent transition, prevents the model from attributing observed changes to their underlying causes, and undermines the transferability of the learned dynamics. We introduce DWM (Decomposed World Model), a supervision-level framework that operationalizes this decomposition. DWM augments the predictor of a latent world model with an auxiliary world head, regularized by a normalized world-contrastive objective to be action-invariant, while the original pred head is coupled to it via an orthogonality constraint; together, the two signals induce an explicit additive decomposition of the predicted transition into an action-invariant and a complementary action-driven component, without altering the underlying architecture or inference pipeline. To evaluate DWM under persistent world effects, we construct W-variants of three standard control benchmarks -- PushT-W, Reacher-W, and TwoRoom-W -- each instantiating a distinct action-invariant dynamic. DWM matches strong baselines on the flat counterparts and delivers a mean absolute improvement of 13.1% in CEM planning success across the W-variants.

</details>

---

### [[20_Research/Papers/世界模型/Do_AI-Native_Biotechs_Need_Departments_Benchmarking_Company_World_Models_for_AI-Driven_Drug_Development|Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development]]

![[assets/2607.18696_figure.png|800]]

- **arXiv**: [2607.18696](https://arxiv.org/abs/2607.18696)
- **PDF**: https://arxiv.org/pdf/2607.18696
- **详细分析**: [[20_Research/Papers/世界模型/Do_AI-Native_Biotechs_Need_Departments_Benchmarking_Company_World_Models_for_AI-Driven_Drug_Development|Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development]]
- **作者**: Yinan Wang
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, WorldModel, Systems

#### 研究背景与动机

《Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgentBench, Company-World, G-Eval, MT-Bench, MedQA, PubMedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI-native biotechnology companies are often designed by copying human biotech org charts into agent roles. We argue for a different abstraction: a Company World Model, defined as a persistent asset-to-value state representation with transition models, explicit value functions, planning, and updating across scientific, regulatory, BD, commercial, financial, and execution constraints. We introduce a dry-lab benchmark for testing whether AI-agent organizations should mimic departments or operate around such a world model. The benchmark contains 45 retrospective public-information decision cases with strict time cutoffs, hidden outcomes, common schemas, automatic scoring, and blinded pairwise judging. We compare human-org-mimic, stronger human-org-mimic-plus, AI-native asset-centric, and AI-native value-conversion architectures. The value-conversion architecture is a prompt-level approximation of a Company World Model: a Live Asset Value Record updated by Deal, Approval, Revenue, and Investment Arbiter loops. Under a success function defined by external BD, regulatory approval and launch, and revenue discipline, it achieved the highest automatic value-conversion score and was strongly preferred over the original baselines by value-specific blinded judges. Stress tests narrowed the claim: a stronger human baseline remained competitive, and a neutral judge did not show robust value-conversion dominance. Codex-only mechanistic ablations suggest that Revenue Room, Deal Room, and Approval Room carry useful work under the target objective. The central finding is objective-sensitive: departments may remain useful governance views, but the core AI-native operating primitive should be a shared, predictive asset-to-value state rather than a static human org chart. The study is dry-lab only and does not establish real-world drug success, clinical benefit, or revenue prediction accuracy.

</details>

---

### [[20_Research/Papers/大模型/Broken_Gates_Re-evaluating_Web_Bot_Defenses_in_the_Age_of_LLM_Agents|Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents]]

![[assets/2607.18659_figure.png|800]]

- **arXiv**: [2607.18659](https://arxiv.org/abs/2607.18659)
- **PDF**: https://arxiv.org/pdf/2607.18659
- **详细分析**: [[20_Research/Papers/大模型/Broken_Gates_Re-evaluating_Web_Bot_Defenses_in_the_Age_of_LLM_Agents|Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents]]
- **作者**: Behzad Ousat, Nikita Turkmen, Lalchandra Rampersaud, Dillan Bailey, Amin Kharraz
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based browser agents are rapidly changing the threat landscape for web security. Unlike traditional automation frameworks that execute predefined scripts, these agents can autonomously navigate websites, reason about page content, and interact with web interfaces using natural-language instructions. This evolution raises fundamental questions about the effectiveness of bot management systems, widely deployed to defend against automated web abuse. In this paper, we present a systematic measurement study evaluating the resilience of both interactive challenge-based defenses and non-interactive trust-based defenses against two attacker classes: commercial Captcha-solving services and LLM-based browser agents. Our evaluation spans seven solver services and six agents, including cloud-hosted, self-hosted, AI-assisted, and browser-extension configurations, tested against hCaptcha, reCaptcha v2, reCaptcha v3, and Cloudflare Turnstile. Our results show that challenge-based defenses are broadly ineffective against commercial solvers, which achieve near-perfect bypass at negligible cost. The challenges can similarly be defeated by LLM-based agents when a dedicated solver module is available. Non-interactive defenses such as reCaptcha v3 exhibit stronger resistance, but our analysis reveals that this resilience does not reflect a fundamental security property. Through fine-grained interaction trace analysis, we find that two agents with nearly indistinguishable behavioral footprints yield divergent outcomes, one bypassing the defense and one failing, isolating execution-environment authenticity, rather than agent behavior, as the determining factor. These findings suggest that the security boundary of non-interactive defenses lies at the environment layer, with significant implications for how bot management systems are designed and evaluated.

</details>

---

### [[20_Research/Papers/具身智能/Intelligent_Multi-UAV_Navigation_in_ITNTNs_A_Hierarchical_LLM_Approach|Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach]]

![[assets/2607.18604_figure.png|800]]

- **arXiv**: [2607.18604](https://arxiv.org/abs/2607.18604)
- **PDF**: https://arxiv.org/pdf/2607.18604
- **详细分析**: [[20_Research/Papers/具身智能/Intelligent_Multi-UAV_Navigation_in_ITNTNs_A_Hierarchical_LLM_Approach|Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach]]
- **作者**: Zijiang Yan, Hao Zhou, Wael Jaafar, Jianhua Pei, Ping Wang, Halim Yanikomeroglu, Hina Tabassum
- **cs 子类**: cs.AI, cs.LG, cs.NI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 大模型, 具身智能, 世界模型
- **相关性评分**: 2.32（加权：具身智能 0.3，大模型 0.4，强化学习 0.56，世界模型 0.16，机器人 0.9）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《Intelligent Multi-UAV Navigation in ITNTNs: A Hierarchical LLM Approach》归入 机器人、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The deployment of high-speed Uncrewed Aerial Vehicles (UAVs) in 3D aerial highways necessitates robust coordination of physical flight kinematics and multi-tier network handovers. While Deep Reinforcement Learning (DRL) offers rapid tactical control, it lacks the zero-shot strategic reasoning required to quickly adapt to dynamic Integrated Terrestrial and Non-Terrestrial Networks (ITNTNs). Conversely, Large Language Models (LLMs) excel at semantic reasoning but suffer from high inference latency, rendering them unsuitable for real-time aerodynamic control. To bridge this gap, we propose a novel Hierarchical LLM-driven control framework. A massive cloud-based LLM deployed on a High-Altitude Platform Station (HAPS) manages slow-timescale global load balancing, while lightweight edge-LLMs on individual UAVs translate local observations into tactical sub-goals. These sub-goals guide a fast-timescale physical DRL controller to execute collision-free, handover-aware trajectories. Simulation results demonstrate that our agentic architecture significantly reduces collision rates and improves aggregate system throughput compared to existing baselines.

</details>

---

### [[20_Research/Papers/强化学习/Planning_as_Emergent_Behavior_in_Reinforcement_Learning_with_Relational_Hidden_States|Planning as Emergent Behavior in Reinforcement Learning with Relational Hidden States]]

![[assets/2607.18589_figure.png|800]]

- **arXiv**: [2607.18589](https://arxiv.org/abs/2607.18589)
- **PDF**: https://arxiv.org/pdf/2607.18589
- **详细分析**: [[20_Research/Papers/强化学习/Planning_as_Emergent_Behavior_in_Reinforcement_Learning_with_Relational_Hidden_States|Planning as Emergent Behavior in Reinforcement Learning with Relational Hidden States]]
- **作者**: Armin Sommer
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.96，世界模型 0.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Planning as Emergent Behavior in Reinforcement Learning with Relational Hidden States》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning is conventionally divided into model-based and model-free methods. In this taxonomy, model-based methods perform lookahead planning over a learned world model, whereas model-free methods learn a reactive state-action mapping. Recent work, however, has shown that planning can emerge from model-free reinforcement learning alone. The conditions under which this behavior emerges from a pure reward-maximization objective have so far remained unclear. In this paper, we present evidence that, in the observed cases, the hidden-state structure of the neural architecture is the deciding factor. We find that a network of relational hidden states, each anchored to an environment state and exchanging messages along learned relations, acquires a planning mechanism. These hidden states recover the environment's transition structure in their learned relations, and improve the policy at decision time by planning over the learned graph. In a matched control agent that must additionally discover which cells represent which states, no such binding arises, and no planning follows from it. We argue that this explains the observed phenomenon of emergent planning in model-free reinforcement learning and raises the question of how common such emergent planning might be more generally. Finally, we hypothesize that the discovered mechanism could describe how planning emerges from pure reward maximization in the human brain through a neural architectural prior.

</details>

---

### [[20_Research/Papers/大模型/The_Story_Shapes_the_Agent_Narrative_Priors_in_LLM_Behavior|The Story Shapes the Agent: Narrative Priors in LLM Behavior]]

![[assets/2607.18566_figure.png|800]]

- **arXiv**: [2607.18566](https://arxiv.org/abs/2607.18566)
- **PDF**: https://arxiv.org/pdf/2607.18566
- **详细分析**: [[20_Research/Papers/大模型/The_Story_Shapes_the_Agent_Narrative_Priors_in_LLM_Behavior|The Story Shapes the Agent: Narrative Priors in LLM Behavior]]
- **作者**: Yixuan Wang, James Lester, Shashank Srivastava
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Story Shapes the Agent: Narrative Priors in LLM Behavior》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persona prompting is widely used to steer LLM agent behavior, yet the narrative framing of a task can matter more than the assigned persona. We isolate this effect through structural isomorphism, constructing three text-based investigation games that share the same action space, stage progression, and resource constraints while varying only task narrative: disease investigation, IT troubleshooting, and murder mystery. Across 1,890 sessions spanning 3 models and 10 personas, we identify narrative priors: systematic action tendencies activated by a task's story framing, independent of its decision structure. Narrative priors explain 5-31x more behavioral variance than persona, are consistent across model architectures, and in two of three domains are negatively associated with task success. Persona effects that do transfer across narratives arise from behavioral anchors, persona descriptions whose language maps directly onto shared actions. Causal interventions confirm this: removing anchor words from a high-transfer persona reduces cross-narrative consistency by 95%. Our framework also generalizes to a held-out fourth narrative and yields a persona-selection method that improves cross-narrative transfer. These results suggest that LLM behavior that survives narrative changes should be grounded in concrete actions rather than abstract descriptions.

</details>

---

### [[20_Research/Papers/大模型/EduPanel_A_Three-Agent_LLM_Judge_for_Teaching_Videos_--_Reliability,_Complementarity,_and_Human_Trust_Calibration|EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration]]

![[assets/2607.18529_figure.png|800]]

- **arXiv**: [2607.18529](https://arxiv.org/abs/2607.18529)
- **PDF**: https://arxiv.org/pdf/2607.18529
- **详细分析**: [[20_Research/Papers/大模型/EduPanel_A_Three-Agent_LLM_Judge_for_Teaching_Videos_--_Reliability,_Complementarity,_and_Human_Trust_Calibration|EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration]]
- **作者**: Jia-Kai Dong, Yi-Cheng Lin, Hung-yi Lee
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teaching videos are becoming a major medium for education, creating a growing need for scalable evaluation of their pedagogical quality. Existing automatic judges do not fully address this setting because teaching quality depends on multimodal evidence and should be evaluated with respect to the intended learner rather than as a universal property. We present EduPanel, a rubric-grounded, learner-conditioned LLM judge that decomposes evaluation across specialized agents to produce interpretable assessments for different aspects of teaching quality. Across expert studies, architecture ablations, and learner-persona analyses, EduPanel achieves reliability comparable to a median human expert. In expert evaluation, its feedback improves scoring accuracy (MAE 0.87 to 0.73), while experts remain able to detect unreliable outputs (AUC = 0.77) instead of accepting them blindly. These results suggest that EduPanel can serve as effective assistants for educational evaluation rather than replacements for human experts.

</details>

---

### [[20_Research/Papers/强化学习/The_Open_Ant_A_Robot_Platform_for_Reinforcement_Learning_Research|The Open Ant: A Robot Platform for Reinforcement Learning Research]]

![[assets/2607.18488_figure.png|800]]

- **arXiv**: [2607.18488](https://arxiv.org/abs/2607.18488)
- **PDF**: https://arxiv.org/pdf/2607.18488
- **详细分析**: [[20_Research/Papers/强化学习/The_Open_Ant_A_Robot_Platform_for_Reinforcement_Learning_Research|The Open Ant: A Robot Platform for Reinforcement Learning Research]]
- **作者**: Elena Sorina Lupu, Patrick Spieler, Khurram Javed, Kris De Asis, John D. Martin, Martha Steenstrup, Joseph Modayil
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，强化学习 1，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《The Open Ant: A Robot Platform for Reinforcement Learning Research》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) research has demonstrated success in both physical and simulated domains; however, the predominant methodology remains rooted in simulations. The predominance of simulations makes translating research to physical reality uncertain for both algorithms and researchers. We propose a physical platform that is designed to simplify the transition. In this paper, we present the Open Ant: a physical variant of the commonly used Gymnasium Ant environment, along with a simulation. We demonstrate that competent walking policies can be learned from scratch in approximately one hour directly from the physical robot's experience for two substantially different RL algorithms: SARSA($λ$) and Soft Actor-Critic (SAC). Separately, we show policies that were learned in simulation transfer to reality. We also examine how well the platform supports a nimble experimental ecosystem. Specifically, we observe the speed with which new users from diverse backgrounds achieve their first success with the platform, and how easily the platform can be repaired and updated when hardware issues arise. Both the hardware design and software are available as open-source on GitHub for ease of customization. In summary, we advocate for the use of the Open Ant for RL researchers who frequently use simulated environments, so they can more easily include robot experiments in their evaluations.

</details>

---

### [[20_Research/Papers/大模型/Trusted_Credentials,_Untrusted_Behavior_Benchmarking_LLM-Agent_Security_in_High-Performance_Computing|Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing]]

![[assets/2607.18485_first_page.png|800]]

- **arXiv**: [2607.18485](https://arxiv.org/abs/2607.18485)
- **PDF**: https://arxiv.org/pdf/2607.18485
- **详细分析**: [[20_Research/Papers/大模型/Trusted_Credentials,_Untrusted_Behavior_Benchmarking_LLM-Agent_Security_in_High-Performance_Computing|Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing]]
- **作者**: Jie Li
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Trusted Credentials, Untrusted Behavior: Benchmarking LLM-Agent Security in High-Performance Computing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are starting to take on routine work in high-performance computing (HPC), including monitoring Slurm jobs, diagnosing failed builds, inspecting simulation output, and coordinating scientific workflows. To do this work, an agent commonly acts under its user's credentials and inherits the user's access to files and the scheduler. This arrangement creates a failure mode that ordinary account-level controls do not capture. Adversarial instructions in a log, tool description, shared file, or peer-agent message may redirect the agent beyond the task the user assigned, even though every resulting command is authenticated and permitted for that account. We refer to this as the hijacked authorized agent problem. Existing agent-security studies explain relevant mechanisms, such as indirect prompt injection and tool misuse, but generally evaluate them in web, enterprise, or personal-assistant settings. HPC security, by contrast, has mature controls for identity and isolation but does not ordinarily represent the intent of a particular task. This paper defines the threat model in the HPC setting, identifies attack surfaces created by schedulers, shared storage, multi-project accounts, and scientific workflows, and examines where current controls fall short. It concludes with a research agenda and a plan for an empirical benchmark, TaskBound.

</details>

---

### [[20_Research/Papers/强化学习/RRPO_Reference-Relative_Policy_Optimization_with_Stratified_Conditional_Rollouts|RRPO: Reference-Relative Policy Optimization with Stratified Conditional Rollouts]]

![[assets/2607.18470_figure.png|800]]

- **arXiv**: [2607.18470](https://arxiv.org/abs/2607.18470)
- **PDF**: https://arxiv.org/pdf/2607.18470
- **详细分析**: [[20_Research/Papers/强化学习/RRPO_Reference-Relative_Policy_Optimization_with_Stratified_Conditional_Rollouts|RRPO: Reference-Relative Policy Optimization with Stratified Conditional Rollouts]]
- **作者**: Yuxin Xiong, Xunyi Jiang, Rohan Surana, Xintong Li, Sheldon Yu, Nikki Lijing Kuang, Ryan A. Rossi, Jingbo Shang, Tong Yu, Julian McAuley, Junda Wu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《RRPO: Reference-Relative Policy Optimization with Stratified Conditional Rollouts》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group Relative Policy Optimization (GRPO) has shown strong effectiveness in reinforcement learning from verifiable feedback, where sampled rollouts can be compared within a group using task-provided correctness signals. However, extending group-relative optimization beyond verifiable settings is challenging because success in many tasks is not captured by a single correctness criterion. We propose \textbf{Reference-Relative Policy Optimization (RRPO)}, which generalizes GRPO by replacing direct correctness-based advantage construction with reference-relative contrastive comparisons. RRPO first uses \emph{stratified conditional rollouts} to construct positive and negative anchor sets, and then trains a metric projection head with a set-contrastive objective to compare candidate rollouts against these anchors. The resulting alignment scores directly define contrastive advantages: during policy optimization, the projection head is frozen, and the scores are centered within each rollout group in a standard group-relative objective. We evaluate RRPO using anchor-based contrastive advantages throughout policy optimization, without relying on task ground-truth verifiers. Across verifiable reasoning, open-ended generation, and post-SFT settings, RRPO remains competitive with verifier-based optimization, improves over weakly supervised baselines, and provides additional gains after supervised fine-tuning.

</details>

---

### [[20_Research/Papers/大模型/Operational_Hallucination_and_Safety_Drift_in_AI_Agents|Operational Hallucination and Safety Drift in AI Agents]]

![[assets/2607.18366_first_page.png|800]]

- **arXiv**: [2607.18366](https://arxiv.org/abs/2607.18366)
- **PDF**: https://arxiv.org/pdf/2607.18366
- **详细分析**: [[20_Research/Papers/大模型/Operational_Hallucination_and_Safety_Drift_in_AI_Agents|Operational Hallucination and Safety Drift in AI Agents]]
- **作者**: Shasha Yu, Fiona Carroll, Barry L. Bentley
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Operational Hallucination and Safety Drift in AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) serving as planners in tool-using autonomous agents introduce dynamic reliability risks in multi-turn execution. While single-turn safety mechanisms are relatively mature, extended interactions reveal structural vulnerabilities where initial alignment degrades over time. This paper empirically characterizes two observed failure modes across multiple state-of-the-art LLMs: Safety Drift, the gradual erosion of declared safety intent leading to constraint-violating actions (e.g., textual refusal followed by reconnaissance and unsafe execution), and Operational Hallucination, persistent repetitive tool calls indicative of flawed state perception (e.g., livelocks even in legitimate tasks). Through controlled multi-turn evaluation on high-stakes ethical dilemmas, malicious requests, and benign controls, we quantify these phenomena using declaration-action gap and livelock metrics, demonstrating their cross-model prevalence under direct execution protocols. Root-cause analysis attributes the instabilities to the decoupling of reasoning context from execution state in current agent loops. We propose an Action-Aware Supervision Layer - a lightweight, plug-and-play architectural blueprint incorporating intent-action consistency checks, runtime state tracking, and forced termination primitives. Post-hoc simulation on captured failure trajectories shows the layer can intercept observed violations without false positives on benign cases. This work advances agent reliability by shifting focus from linguistic safeguards to enforceable architectural mechanisms for responsible agentic AI.

</details>

---

### [[20_Research/Papers/机器人/Hazard_or_Anomaly_Evaluating_VLMs_for_Understanding_Dangers_and_Discrepancies|Hazard or Anomaly? Evaluating VLMs for Understanding Dangers and Discrepancies]]

![[assets/2607.18325_figure.png|800]]

- **arXiv**: [2607.18325](https://arxiv.org/abs/2607.18325)
- **PDF**: https://arxiv.org/pdf/2607.18325
- **详细分析**: [[20_Research/Papers/机器人/Hazard_or_Anomaly_Evaluating_VLMs_for_Understanding_Dangers_and_Discrepancies|Hazard or Anomaly? Evaluating VLMs for Understanding Dangers and Discrepancies]]
- **作者**: Murali Indukuri, Mohammad Eskandari, Sree Nitya Kollu, Stephanie Lukin, Cynthia Matuszek
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Hazard or Anomaly? Evaluating VLMs for Understanding Dangers and Discrepancies》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern safety-critical systems increasingly rely on human-robot interaction to reduce disaster risk and support decision-making during emergencies. Vision-Language Models (VLMs) are promising for these settings because they can interpret complex scenes and communicate safety-relevant information, but they still require careful evaluation to ensure reliable safety reasoning. In particular, current evaluations often frame danger recognition as a binary decision (Safe/Unsafe), making it unclear whether a model is identifying true physical hazards or merely reacting to unusual scene elements. We address this limitation by introducing an explicit distinction between hazard and anomaly, and by separately recognizing hazardous and anomalous states. We evaluate several state-of-the-art VLMs across two datasets and multiple prompting strategies to test whether this distinction changes model behavior. Our results show that VLMs frequently misinterpret anomalousness as hazardousness, revealing an over-reliance on contextual irregularity as a proxy for danger. We further show that explicitly separating anomaly from hazard provides a more informative evaluation of VLM safety reasoning and exposes failure modes that binary safety judgments can obscure. Our public dataset is available on Roboflow https://app.roboflow.com/vlm-in-context-anomaly-and-hazard-detection/camera-ready-roman-ds.

</details>

---

### [[20_Research/Papers/大模型/Binding_Drift_in_Multi-Step_Tool-Augmented_Agents|Binding Drift in Multi-Step Tool-Augmented Agents]]

![[assets/2607.18316_first_page.png|800]]

- **arXiv**: [2607.18316](https://arxiv.org/abs/2607.18316)
- **PDF**: https://arxiv.org/pdf/2607.18316
- **详细分析**: [[20_Research/Papers/大模型/Binding_Drift_in_Multi-Step_Tool-Augmented_Agents|Binding Drift in Multi-Step Tool-Augmented Agents]]
- **作者**: Rahul Suresh Babu, Shashank Indukuri
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Binding Drift in Multi-Step Tool-Augmented Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-augmented language-model agents execute multi-step workflows over external systems, resolving an entity once and then acting on it across subsequent steps. Prior work shows that in single-step actions, agents select the correct tool but bind it to the wrong entity 24-26% of the time. We study what happens to entity bindings over time: do they stay correct, silently drift to a different entity, or, if wrong from the start, propagate and compound? We formalize binding drift (correct at step 1, wrong later) as distinct from error propagation (wrong at step 1, carried forward), and score them on disjoint workflow sets so the two cannot be conflated. In a controlled multi-step testbed (200 workflows, 580 entity-binding-scored steps, four enterprise domains, eight model backends spanning small to frontier), we find: (1) under controlled error injection, an entity lock (the intuitive "persist the first binding" fix) amplifies wrong actions from 907 to 2,746 (3.0x; bootstrap 95% CI [2.8, 3.3]), because it faithfully carries the seeded wrong entity into every later step; (2) the amplification reaches 8.5x on the most affected model (Claude Opus 4.5); (3) a practical LLM-based re-verifier (a single cheap second model call re-reading the original instruction) reduces wrong actions by 79% (0.21x; CI [0.18, 0.25]), closing the gap to within 1 percentage point of an oracle upper-bound (0.20x); and (4) in the natural (non-injected) setting, baseline agents drift on 18% of eligible workflows, with the per-step error rate rising across steps. Persistence and re-verification are not interchangeable: a defense that eliminates drift can worsen propagation, and a practical re-verifier nearly matches oracle recovery.

</details>

---

### [[20_Research/Papers/大模型/Distribution-First_Population_Simulation_Collapse,_Calibration,_and_Recall_in_Non-WEIRD_LLM_Persona_Modeling|Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling]]

![[assets/2607.18310_figure.png|800]]

- **arXiv**: [2607.18310](https://arxiv.org/abs/2607.18310)
- **PDF**: https://arxiv.org/pdf/2607.18310
- **详细分析**: [[20_Research/Papers/大模型/Distribution-First_Population_Simulation_Collapse,_Calibration,_and_Recall_in_Non-WEIRD_LLM_Persona_Modeling|Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling]]
- **作者**: Gurkan Ozkan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Distribution-First Population Simulation: Collapse, Calibration, and Recall in Non-WEIRD LLM Persona Modeling》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PersonaBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Synthetic-population tools increasingly run every individual as an independent large language model (LLM) agent. Using real survey microdata, we show that this paradigm has a basic failure mode, and we set a distribution-first corrective against it, all measured with a deterministic, construct-validated verifier on non-WEIRD (Turkey-first) data. First, N independent LLM agents grounded on 2,414 real World Values Survey respondents fail to reproduce the population's response distribution: they pile onto a modal default (four scenarios x five seeds: concentration 0.36-&gt;0.69, entropy 1.46-&gt;0.77, 85% collapse, TVD=0.44), and the collapse is a predictable function of scenario structure (r=0.55 with a single-answer structure). Second, Verbalized Sampling (VS) fixes the field's chronic under-dispersion without training in three model families (fidelity +7 to +10; significant on Qwen, p=0.002, d=6.2), yet the same move universally overshoots into over-dispersion (SD-ratio 0.4-0.56 -&gt; 1.26-1.37), a structural property of VS. Third, survey fidelity transfers only weakly to agentic behavior: in a single-model, single-domain booking task, a persona is dominated by a cheapest-default (~80%) that income modulates but does not override (comfort choice 0%-&gt;7%-&gt;32% across income bands). Fourth, a placebo-controlled memorization attack and an election backtest show VS keeps aggregate strength while subgroup and individual claims are contaminated by recall and underdetermination. We close with the corrective: model the distribution once (VS) and assign it to grounded characters at O(1) cost, with a budget-aware router whose honest AUC is 0.805, not the tautological 1.0 of a code-derived oracle. The central contribution needs no realism claim: it measures the internal inconsistency of the independent-agent route and the conditions under which the distribution-first route calibrates.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_to_Master_the_Asymmetric_Strategy_of_Baghchal|Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal]]

![[assets/2607.18296_first_page.png|800]]

- **arXiv**: [2607.18296](https://arxiv.org/abs/2607.18296)
- **PDF**: https://arxiv.org/pdf/2607.18296
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_to_Master_the_Asymmetric_Strategy_of_Baghchal|Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal]]
- **作者**: Ranjit Raut, Aarav Subedi, Sagun Rai, Aaryan Shakya, Manoj Shakya
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.8（加权：强化学习 1.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Deep Reinforcement Learning to Master the Asymmetric Strategy of Baghchal》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Baghchal is a two-player asymmetric board game with Nepali origins where four tigers are to capture goats and twenty goats desire to keep tigers in immobility. Although Baghchal has a complex structure which is strategic, has perfect information structure, and has cultural meaning, it has not been adequately covered in deep reinforcement learning (RL) literature. This paper gives a systematic exploration of four deep RL solutions Deep Q-Network (DQN), REINFORCE, Proximal Policy Optimization (PPO) and MuZero that are trained on one side of the asymmetric gameplay of Baghchal and then evaluated on the other side. The algorithms are rated based on win rate, draw rate, average captures, training convergence and computational cost. It is experimentally found that MuZero generates the best performance in both tasks, achieving 86 percent win over these Tiger and 62 percent win over these Goat and the ability to do so is due to the model-based planning machine through the Monte Carlo Tree Search. PPO is the most realistic algorithm and is provided to be competitive over both asymmetric tasks with significantly reduced computational costs compared to MuZero. Emergent strategic behavior analysis shows that model-based strategies are optimal over long-horizon planning, whereas value-based counterparts like DQN are more biased up towards the Tiger role owing to the more substantial reward signal.

</details>

---

### [[20_Research/Papers/强化学习/Preference-Conditioned_Multi-Objective_Reinforcement_Learning_for_Runtime-Tunable_Transit_Signal_Priority|Preference-Conditioned Multi-Objective Reinforcement Learning for Runtime-Tunable Transit Signal Priority]]

![[assets/2607.18286_figure.png|800]]

- **arXiv**: [2607.18286](https://arxiv.org/abs/2607.18286)
- **PDF**: https://arxiv.org/pdf/2607.18286
- **详细分析**: [[20_Research/Papers/强化学习/Preference-Conditioned_Multi-Objective_Reinforcement_Learning_for_Runtime-Tunable_Transit_Signal_Priority|Preference-Conditioned Multi-Objective Reinforcement Learning for Runtime-Tunable Transit Signal Priority]]
- **作者**: Philip-Roman Adam, Stefanie Schmidtner
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Preference-Conditioned Multi-Objective Reinforcement Learning for Runtime-Tunable Transit Signal Priority》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MORL, SUMO-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transit signal priority (TSP) requires balancing competing objectives: reducing bus delay while limiting adverse impacts on non-bus traffic and avoiding extreme waits for a subset of vehicles. Existing reinforcement-learning (RL) approaches to TSP typically encode transit-aware features (e.g., occupancy and schedule deviation) but optimize a fixed reward or fixed scalarization, which limits operational flexibility when agency priorities change across time-of-day or disruption conditions. We present a preference-conditioned TSP controller, $π(a \mid s,w)$, that selects the next signal phase under minimum/maximum green and transition-feasibility constraints and can be tuned at runtime via a preference parameter $w$ to trade off bus-priority emphasis against overall traffic delay without retraining. We implement this on top of IntersectionZoo by introducing a constrained signal-control/TSP wrapper, and we extend scenario generation with bus-prevalence augmentation and timetable-based bus insertion to address sparse transit-priority events during training. Experiments against fixed-time control, a rule-based TSP overlay, and fixed-weight PPO specialists show that a single learned conditioned policy spans a smooth empirical trade-off frontier across runtime preferences, outperforms fixed-time and rule-based baselines, and maintains constraint feasibility, while tail-delay diagnostics reveal that non-bus externalities remain limited for moderate preference settings but can increase substantially under high bus-priority weights. The source code of this work is available at https://github.com/urbanAIthi/morl-tsp.

</details>

---

### [[20_Research/Papers/大模型/Wisdom_of_LLM_Crowds_Aggregation_and_Contamination_in_Language_Model_Ensembles|Wisdom of LLM Crowds: Aggregation and Contamination in Language Model Ensembles]]

![[assets/2607.18269_figure.png|800]]

- **arXiv**: [2607.18269](https://arxiv.org/abs/2607.18269)
- **PDF**: https://arxiv.org/pdf/2607.18269
- **详细分析**: [[20_Research/Papers/大模型/Wisdom_of_LLM_Crowds_Aggregation_and_Contamination_in_Language_Model_Ensembles|Wisdom of LLM Crowds: Aggregation and Contamination in Language Model Ensembles]]
- **作者**: Igor Douven
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Wisdom of LLM Crowds: Aggregation and Contamination in Language Model Ensembles》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The wisdom of crowds -- the finding that aggregating judgments across individuals often outperforms the best individual -- has been extensively studied with human forecasters. Whether the same phenomenon emerges when the ``crowd'' consists of large language models (LLMs) is an open question with both theoretical and practical implications. We elicited probability estimates from 15 LLMs on 254 binary prediction market questions and evaluated classical and learned aggregation methods. Learned aggregators -- a multilayer perceptron and a logistic regression -- outperformed all individual models and classical methods. The logistic regression was found to match the neural network, suggesting that the benefit of learned aggregation derives from learning a linear combination of diverse model outputs rather than from nonlinear interactions. Symbolic regression applied to the neural network's learned mapping recovered a pure model-disagreement signal as the lowest-complexity useful formula on the Pareto frontier, further supporting this interpretation. Training cutoff contamination proved a pervasive confound: the apparent capability gap between frontier cloud models and smaller local models collapsed from 35.8% to 8.9% on a clean subset of questions resolving after all models' training cutoffs, and individual model rankings showed only moderate stability. Even when the prediction market is evaluated at each model's training cutoff, LLMs remained substantially less accurate, indicating a genuine gap in collective information aggregation. These findings suggest that LLM crowds can exhibit wisdom-of-crowds effects, but that contamination-free evaluation is essential for reliable assessment.

</details>

---

### [[20_Research/Papers/大模型/State_Compression_in_Two-Agent_LLM_Relays_A_Closed-World_Study_of_Constraint_Preservation|State Compression in Two-Agent LLM Relays: A Closed-World Study of Constraint Preservation]]

![[assets/2607.18265_figure.png|800]]

- **arXiv**: [2607.18265](https://arxiv.org/abs/2607.18265)
- **PDF**: https://arxiv.org/pdf/2607.18265
- **详细分析**: [[20_Research/Papers/大模型/State_Compression_in_Two-Agent_LLM_Relays_A_Closed-World_Study_of_Constraint_Preservation|State Compression in Two-Agent LLM Relays: A Closed-World Study of Constraint Preservation]]
- **作者**: Anantha Sharma, Sheeba Elizabeth John, Kaarthik Senthil Kumar, Saratsuhas Vijayababu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《State Compression in Two-Agent LLM Relays: A Closed-World Study of Constraint Preservation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Closed-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-running Large Language Model (LLM)-based agents often accumulate large intermediate traces containing audits, eliminations, and numeric calculations. In practice, this state is compressed before handing it to a downstream decision step, creating an information bottleneck in which small omissions can break strict numeric or categorical constraints. This paper evaluates hand-off compression in a closed-world travel-planning relay with two LLM agents. A Researcher audits a fixed inventory of hotels and flights for 50 goal instances, and a Booker selects a hotel--flight pair using only the goal and the hand-off payload, with the inventory withheld. We compare four hand-off conditions: no compression, narrative summarization, schema-constrained JSON extraction, and embedding-based pruning. Exhaustive enumeration over the fixed inventory provides exact feasible and optimal labels. Results show that hand-off representation strongly affects downstream feasibility under a small decision model. JSON extraction achieves the highest feasibility accuracy at 0.96, while narrative summarization, despite producing the smallest compressed hand-off payload, degrades feasibility to 0.48. Embedding-based pruning matches the uncompressed control on feasibility at 0.88 without an additional generative compression call. These findings indicate that constraint checking benefits from structured and auditable hand-off representations rather than relying on brevity alone.

</details>

---

### [[20_Research/Papers/大模型/When_JSON_Is_Not_Enough_Semantic_Reliability_of_Schema-Constrained_LLM_Ordering_Agents|When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents]]

![[assets/2607.18261_first_page.png|800]]

- **arXiv**: [2607.18261](https://arxiv.org/abs/2607.18261)
- **PDF**: https://arxiv.org/pdf/2607.18261
- **详细分析**: [[20_Research/Papers/大模型/When_JSON_Is_Not_Enough_Semantic_Reliability_of_Schema-Constrained_LLM_Ordering_Agents|When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents]]
- **作者**: Yin Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：APIBench, JSONSchemaBench, OrderBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly used as transaction compilers: a user states an intent in natural language, and the model emits a structured object that an API can execute. JSON Schema and provider-level structured-output modes are useful because they remove a large class of parse failures, but they do not by themselves decide whether the object is a safe, faithful transaction. We introduce OrderBench, a deterministic benchmark for restaurant ordering agents that separates syntactic validity, schema validity, status decisions, exact item semantics, constraint preservation, and unsafe acceptances. Across 2,400 Nebius Token Factory calls to four open models in prompt-only and JSON-schema modes, we find that schema-valid output can still have large semantic error rates. In the strongest model, both modes achieve 100% schema validity, yet semantic success remains near 80%; in weaker models, schema-valid unsafe acceptances occur in double digits. The result is a concrete engineering warning: structured output is a necessary interface layer, not a substitute for domain verification and fail-closed execution.

</details>

---

### [[20_Research/Papers/大模型/Semantic_Cooperative_Games_for_Contribution_Attribution_in_LLM-Based_Multi-Agent_Systems|Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems]]

![[assets/2607.18255_figure.png|800]]

- **arXiv**: [2607.18255](https://arxiv.org/abs/2607.18255)
- **PDF**: https://arxiv.org/pdf/2607.18255
- **详细分析**: [[20_Research/Papers/大模型/Semantic_Cooperative_Games_for_Contribution_Attribution_in_LLM-Based_Multi-Agent_Systems|Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems]]
- **作者**: Pengyi Jiang, Xiaoguang Zhu, Quanyan Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contribution attribution has become a central problem in LLM-based multi-agent systems, where final outputs are produced through multiple agents, message exchanges, and ordered workflow dependencies. Existing attribution methods often rely on counterfactual valuation, such as removing agents or comparing score changes across altered agent subsets. In language-mediated workflows, these methods require repeated model calls, introduce high variance, and do not explicitly capture the intermediate semantic states through which agents produce, preserve, and transform task-relevant information. We propose Semantic Cooperative Games (SCG), a framework that represents a realized language flow as a semantic generation hypergraph and induces an agent-level semantic value function on this structure. We define the Semantic Shapley Value (SSV) to allocate contribution over semantic support logic, and introduce SLIC, a single-trajectory algorithm that constructs the semantic hypergraph, recovers minimal semantic supports, applies Boolean absorption, and computes SSV without rerunning agent subsets. We prove that SSV reduces to the classical Shapley value under standard set-based, fully observable, and no-order-dependence conditions. On a medical benchmark satisfying these conditions, SLIC reduces computation cost by 93.3% while remaining highly consistent with a Monte Carlo Shapley baseline. In more general multi-role workflows, SSV aligns with perturbation-induced score-drop profiles and exposes cases where semantic contribution and failure impact diverge. Overall, SLIC provides a fast, counterfactual-free, and interpretable attribution method for complex LLM-based multi-agent systems.

</details>

---

### [[20_Research/Papers/大模型/Integro-differential_equations_in_angular_stabilization_of_drone_motion_by_distributed_feedback_control|Integro-differential equations in angular stabilization of drone motion by distributed feedback control]]

![[assets/2607.18251_figure.jpg|800]]

- **arXiv**: [2607.18251](https://arxiv.org/abs/2607.18251)
- **PDF**: https://arxiv.org/pdf/2607.18251
- **详细分析**: [[20_Research/Papers/大模型/Integro-differential_equations_in_angular_stabilization_of_drone_motion_by_distributed_feedback_control|Integro-differential equations in angular stabilization of drone motion by distributed feedback control]]
- **作者**: Alexander Domoshnitsky, Oleg Kupervasser, Anatoly Polonsky
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Systems

#### 研究背景与动机

《Integro-differential equations in angular stabilization of drone motion by distributed feedback control》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose angular stabilization of drone motion using distributed feedback control in the form of an integral operator. It should be stressed that the memory of this integral operator could be unbounded. It is intuitively clear that large length of the observation time open new possibilities to construct better control based on previous states of the control object. Unbounded memory in control requires the creation of a certain approach different from standard ones to the study of integro-differential equations. One of the goals of this article is to propose a certain universal approach that allows us to study the stability of integro-differential equations in the case of unbounded memory in the integral operator specifying the feedback control in stabilization. The approach we propose allows us to reduce the study of integro-differential equations to the analysis of systems of ordinary differential equations. In general, such systems can consist of an infinite number of equations. In relation to the so-called linear approximation in the problem of angle stabilization manages to limit itself to relatively simple exponential kernels in the integral control and arrive at a system with a finite number of equations. The examples explain that more complex kernels, for example, linear combinations of the exponential kernels, can enhance the stabilization capabilities. We obtain new unexpectable results on the exponential stability of integro-differential equations. Then we apply them to stabilization of drone flight.

</details>

---

### [[20_Research/Papers/大模型/MechAInistic_An_LLM-guided_Multi-Agent_System_for_Reasoning_over_Genome-Scale_Constraint-Based_Metabolic_Models|MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models]]

![[assets/2607.18249_first_page.png|800]]

- **arXiv**: [2607.18249](https://arxiv.org/abs/2607.18249)
- **PDF**: https://arxiv.org/pdf/2607.18249
- **详细分析**: [[20_Research/Papers/大模型/MechAInistic_An_LLM-guided_Multi-Agent_System_for_Reasoning_over_Genome-Scale_Constraint-Based_Metabolic_Models|MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models]]
- **作者**: Josh Loecker, Narayna Puraja, William Bryan, Bhanwar Lal Puniya, Ahmed Abdeen Hamed, Tomáš Helikar
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MechAInistic: An LLM-guided Multi-Agent System for Reasoning over Genome-Scale Constraint-Based Metabolic Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Constraint-based metabolic modeling is a powerful way to study the mechanistic basis of cellular states and disease, but its effective use demands substantial computational expertise and careful coordination of multi-step analyses. We developed MechAInistic to lower this barrier and enable researchers to ask complex biological questions in natural language. Harnessing large language models, MechAInistic is a multi-agent system organized around an Architect-Reviewer pattern that transforms a natural-language question into an executable, model-grounded workflow and generates a structured report. The system supports a variety of tasks, including pathway comparison, perturbation analysis, drug-target exploration, and literature-grounded interpretation across paired metabolic model states. We developed and evaluated MechAInistic using two paired immune-cell metabolic-model use cases for therapeutic hypothesis generation. For Naive B cells from rheumatoid arthritis (RA) paired with healthy controls, MechAInistic identified mitochondrial metabolic rewiring and nominated Devimistat/CPI-613 as an investigational OGDH-centered hypothesis. In a paired CD4+ Th17 cell study from multiple sclerosis (MS) and healthy controls, the same workflow identified NADP-dependent isocitrate dehydrogenase as the optimal single target and proposed ivosidenib as an FDA-approved repurposing candidate. Together, these results show that MechAInistic converts natural-language biological questions into executable, model-grounded workflows for traceable therapeutic hypothesis generation.

</details>

---

### [[20_Research/Papers/具身智能/From_Agent_Failure_Paths_to_Quantified_Residual_Risk_A_Compositional_Framework_for_Resilient_Agentic_AI|From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI]]

![[assets/2607.18243_figure.png|800]]

- **arXiv**: [2607.18243](https://arxiv.org/abs/2607.18243)
- **PDF**: https://arxiv.org/pdf/2607.18243
- **详细分析**: [[20_Research/Papers/具身智能/From_Agent_Failure_Paths_to_Quantified_Residual_Risk_A_Compositional_Framework_for_Resilient_Agentic_AI|From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI]]
- **作者**: Hassan Karim, Sai Sitharaman, Deepti Gupta, Danda B. Rawat
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.4，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic AI is crossing trust boundaries faster than current risk models can represent. Existing approaches provide one of two partial views. They either describe failure mechanisms without producing a transferable residual-risk estimate, or they produce a risk estimate while treating the internal failure path as a black box. We couple those two views by proposing CPSAINT, a seven-layer integrity decomposition over Physical state, Sensors, Data, Compute, Actuators, Environment, and Time, paired with FRIESA-K, a residual-risk functional that maps each failure path to a quantified risk instance. FRIESA-K grounds the resistance term K in a controlled absorbing Markov model so that control effectiveness is derived from state dynamics rather than assigned as an informal score. The result is a concise mechanism-to magnitude pipeline for resilient agentic and embodied AI. We report governance observability through a separate additive penalty instead of inserting governance as a new variable in the resistance functional. We formalize structural composability linking valid failure paths to well-defined risk instances and show the framework on two contrasting scenarios a hard real-time warehouse robot and a governance-instrumented financial-services agent. Across both cases, the same layer grammar, variable semantics, and dynamic-resistance construction remain intact. Thus, we obtain a compact kernel that supports cross-domain reasoning, explicit assumptions, and quantitatively grounded formalism of composable trust.

</details>

---
